"""
Content Generation Orchestrator.
Orchestrates prompt generation, AI API calls, response parsing, validation,
and automated one-time AI retry if hard constraints are violated.
"""

from typing import Dict, Any, List, Optional
import logging
from nvidia_service import nvidia_service
from prompt_builder import PromptBuilder
from validator import ContentValidator
from schemas import GenerateRequest, PlatformResult, RegenerateRequest, RewriteRequest
from platform_config import PLATFORM_CONFIG

logger = logging.getLogger("content_generator")

class ContentGenerator:
    @staticmethod
    def _create_fallback_content(
        platform: str,
        topic: str,
        language: str,
        tone: str,
        content_type: str,
        length: str,
        notice: str
    ) -> Dict[str, Any]:
        """
        Creates clean, structured placeholder content ONLY when NVIDIA API key is missing or unreachable,
        clearly informing the user how to configure their credentials without leaving the UI broken.
        """
        cfg = PLATFORM_CONFIG.get(platform, {})
        p_name = cfg.get("name", platform)

        return {
            "title": f"[{p_name}] {topic.capitalize()} - {tone} {content_type}",
            "hook": f"Attention entertainment fans: here is what you need to know about {topic}.",
            "main_content": (
                f"Note: {notice}\n\n"
                f"Sample Generated Preview for {p_name} ({language} - {tone} tone):\n"
                f"Exploring '{topic}' through the lens of {tone.lower()} entertainment. "
                f"This platform-tailored narrative showcases {content_type.lower()} dynamics for {p_name}.\n\n"
                f"Configure your NVIDIA_API_KEY in backend/.env to unlock real-time Nemotron-powered outputs."
            ),
            "call_to_action": f"What's your take on {topic}? Drop your thoughts below!",
            "hashtags": [f"#{topic.replace(' ', '')}", f"#{platform}", "#Entertainment", "#ContentCreation"],
            "metadata": {"mode": "configuration_required", "format": content_type}
        }

    @classmethod
    def generate_for_platform(
        cls,
        platform: str,
        topic: str,
        description: Optional[str],
        target_audience: Optional[str],
        language: str,
        tone: str,
        content_type: str,
        length: str,
        keywords: Optional[List[str]] = None,
        custom_instructions: Optional[str] = None
    ) -> PlatformResult:
        """
        Generates content for a single platform with validation and 1 controlled AI rewrite if needed.
        """
        system_prompt = PromptBuilder.get_system_prompt(platform, language, tone)
        user_prompt = PromptBuilder.get_user_prompt(
            platform=platform,
            topic=topic,
            description=description,
            target_audience=target_audience,
            language=language,
            tone=tone,
            content_type=content_type,
            length=length,
            keywords=keywords,
            custom_instructions=custom_instructions
        )

        content_dict = None
        generation_error_msg = None

        if nvidia_service.is_configured():
            try:
                res = nvidia_service.chat_completion(
                    system_prompt=system_prompt,
                    user_prompt=user_prompt,
                    temperature=0.75,
                    response_format_json=True
                )
                content_dict = res.get("data", {})
            except Exception as e:
                logger.error(f"Generation error for {platform}: {str(e)}")
                generation_error_msg = str(e)
        else:
            generation_error_msg = (
                "NVIDIA_API_KEY is not configured in backend/.env. "
                "Get your key from https://build.nvidia.com/ and set it to generate live AI content."
            )

        if not content_dict:
            content_dict = cls._create_fallback_content(
                platform=platform,
                topic=topic,
                language=language,
                tone=tone,
                content_type=content_type,
                length=length,
                notice=generation_error_msg or "Failed to contact NVIDIA API."
            )

        # Validate initial content
        is_valid, warnings, stats = ContentValidator.validate(
            platform=platform,
            content_dict=content_dict,
            requested_keywords=keywords
        )

        # Controlled AI retry (Max 1 rewrite) if hard constraints violated and NVIDIA is configured
        if not is_valid and nvidia_service.is_configured() and generation_error_msg is None:
            logger.info(f"Platform constraint violated for {platform}. Attempting 1 controlled rewrite...")
            rewrite_instruction = (
                f"The generated content violated constraints: {'; '.join(warnings)}. "
                f"Please rewrite strictly respecting platform rules, character limits, and requested keywords."
            )
            rewrite_prompt = PromptBuilder.get_rewrite_prompt(
                platform=platform,
                topic=topic,
                current_content=content_dict.get("main_content", ""),
                instruction=rewrite_instruction,
                language=language,
                tone=tone,
                length=length
            )
            try:
                rewritten_res = nvidia_service.chat_completion(
                    system_prompt=system_prompt,
                    user_prompt=rewrite_prompt,
                    temperature=0.6,
                    response_format_json=True
                )
                rewritten_dict = rewritten_res.get("data", {})
                if rewritten_dict and rewritten_dict.get("main_content") and len(rewritten_dict.get("main_content", "").strip()) >= 10:
                    content_dict = rewritten_dict
                    is_valid, warnings, stats = ContentValidator.validate(
                        platform=platform,
                        content_dict=content_dict,
                        requested_keywords=keywords
                    )
            except Exception as re_err:
                logger.warning(f"Rewrite attempt failed: {re_err}")

        # Ensure hashtags is list
        raw_tags = content_dict.get("hashtags", [])
        if isinstance(raw_tags, str):
            raw_tags = [t.strip() for t in raw_tags.split() if t.startswith("#")]
        elif not isinstance(raw_tags, list):
            raw_tags = []

        return PlatformResult(
            platform=platform,
            title=content_dict.get("title"),
            hook=content_dict.get("hook"),
            main_content=content_dict.get("main_content", ""),
            call_to_action=content_dict.get("call_to_action"),
            hashtags=raw_tags,
            content_type=content_type,
            word_count=stats.get("word_count", 0),
            character_count=stats.get("character_count", 0),
            is_valid=is_valid,
            validation_warnings=warnings,
            metadata=content_dict.get("metadata", {})
        )

    @classmethod
    def generate_all(cls, req: GenerateRequest) -> Dict[str, PlatformResult]:
        results = {}
        for platform in req.platforms:
            result = cls.generate_for_platform(
                platform=platform,
                topic=req.topic,
                description=req.description,
                target_audience=req.target_audience,
                language=req.language,
                tone=req.tone,
                content_type=req.content_type,
                length=req.length,
                keywords=req.keywords,
                custom_instructions=req.custom_instructions
            )
            results[platform] = result
        return results

    @classmethod
    def rewrite_content(cls, req: RewriteRequest) -> PlatformResult:
        platform = req.platform.lower()
        system_prompt = PromptBuilder.get_system_prompt(platform, req.language or "English", req.tone or "Engaging")
        rewrite_prompt = PromptBuilder.get_rewrite_prompt(
            platform=platform,
            topic=req.topic,
            current_content=req.current_content,
            instruction=req.instruction,
            language=req.language,
            tone=req.tone,
            length=req.length
        )

        content_dict = None
        if nvidia_service.is_configured():
            try:
                res = nvidia_service.chat_completion(
                    system_prompt=system_prompt,
                    user_prompt=rewrite_prompt,
                    temperature=0.7,
                    response_format_json=True
                )
                content_dict = res.get("data", {})
            except Exception as e:
                logger.error(f"Error in rewrite: {e}")

        if not content_dict:
            content_dict = {
                "title": f"Refined {req.topic}",
                "hook": f"Updated hook for {platform}",
                "main_content": f"[Modified based on '{req.instruction}']:\n\n{req.current_content}",
                "call_to_action": "Let us know your thoughts!",
                "hashtags": [f"#{req.topic.replace(' ', '')}", f"#{platform}"]
            }

        is_valid, warnings, stats = ContentValidator.validate(
            platform=platform,
            content_dict=content_dict
        )

        raw_tags = content_dict.get("hashtags", [])
        if isinstance(raw_tags, str):
            raw_tags = [t.strip() for t in raw_tags.split() if t.startswith("#")]
        elif not isinstance(raw_tags, list):
            raw_tags = []

        return PlatformResult(
            platform=platform,
            title=content_dict.get("title"),
            hook=content_dict.get("hook"),
            main_content=content_dict.get("main_content", ""),
            call_to_action=content_dict.get("call_to_action"),
            hashtags=raw_tags,
            content_type="Refined Post",
            word_count=stats.get("word_count", 0),
            character_count=stats.get("character_count", 0),
            is_valid=is_valid,
            validation_warnings=warnings,
            metadata=content_dict.get("metadata", {})
        )

