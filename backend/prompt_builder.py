"""
Platform-Specific Prompt Engineering Engine.
Provides distinct system instructions, structural output formats, and stylistic parameters
for Instagram, YouTube, YouTube Shorts, Facebook, X (Twitter), and LinkedIn.
"""

from typing import Dict, Any, List, Optional
from platform_config import PLATFORM_CONFIG

class PromptBuilder:
    @staticmethod
    def get_system_prompt(platform: str, language: str, tone: str) -> str:
        base_instruction = (
            f"You are a world-class entertainment industry copywriter, viral content creator, and social media strategist. "
            f"You generate unique, native content specifically crafted for {platform.upper()}. "
            f"Target Language: {language}. Requested Tone: {tone}. "
            f"CRITICAL RULES:\n"
            f"1. Language authenticity: If language is Hindi, use natural Devanagari Hindi or conversational tone. "
            f"If Hinglish, use natural modern urban Hindi-English blend (Roman script). If English, use compelling modern English.\n"
            f"2. Never produce generic copy-paste text. Emphasize the distinct entertainment and psychological dynamics of {platform}.\n"
            f"3. Strictly return a valid JSON object matching the requested schema. No conversational filler before or after the JSON."
        )

        platform_specific_instructions = {
            "instagram": (
                "Format: Instagram post/Reel. Optimize for visual curiosity, strong scroll-stopping first 5 words, "
                "aesthetic pacing, relatable entertainment hooks, spacing with emojis, and a focused Call To Action. "
                "Include 5 to 15 relevant trending entertainment hashtags without spamming."
            ),
            "youtube": (
                "Format: Long-form YouTube Video. Optimize for High Click-Through Rate (CTR) and High Audience Retention (AVD). "
                "Generate an irresistible, curiosity-gap YouTube title (< 70 chars recommended), a high-retention video script "
                "with an intense 0-30s opening hook, structured timestamps/scenes [00:00 - Hook, 01:00 - The Conflict, etc.], "
                "an SEO-optimized description with key search phrases, and a subscribe/comment Call To Action."
            ),
            "youtube_shorts": (
                "Format: YouTube Shorts (Vertical 9:16). Fast-paced, high adrenaline or intense curiosity. "
                "The first 3 seconds are make-or-break: script an explosive visual and verbal hook. "
                "Include rapid-fire dialogue/narration, concise beat drops/audio cues in brackets like [Dramatic sound fx], "
                "and an engaging seamless loop ending that makes viewers rewatch."
            ),
            "facebook": (
                "Format: Facebook Post. Focus on emotional connection, relatable community storytelling, "
                "and shareable discussion starters. Facebook audiences love narrative paragraphs, relatable questions, "
                "humor or heart-touching angles, and a prompt that urges people to tag friends or comment their opinion."
            ),
            "x": (
                "Format: X (formerly Twitter). Ultra-concise, high-impact phrasing. "
                "If it's a single post, keep it strictly under 280 characters with maximum wit, punchline, or insight. "
                "If it's a thread, format each tweet cleanly as '1/', '2/', '3/', with the opening hook being irresistible. "
                "Use at most 1-2 sharp hashtags."
            ),
            "linkedin": (
                "Format: LinkedIn Post. Transform entertainment and cultural topics into lessons, industry perspectives, "
                "creative insights, leadership takeaways, or storytelling with a clear moral/business angle. "
                "Use clean whitespace, one-sentence paragraphs, a compelling opening line that forces '...see more' clicks, "
                "and professional, thoughtful discussion questions."
            )
        }

        specific = platform_specific_instructions.get(platform, "Produce engaging, native platform content.")
        return f"{base_instruction}\n\nPlatform Focus:\n{specific}"

    @staticmethod
    def get_user_prompt(
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
    ) -> str:
        kw_str = ", ".join(keywords) if keywords else "None specified"
        custom_str = custom_instructions.strip() if custom_instructions else "None"
        desc_str = description.strip() if description else "None provided"
        audience = target_audience.strip() if target_audience else "General Public / Entertainment Fans"

        # Define JSON output requirements per platform
        json_schema_req = (
            "Return a strictly valid JSON object with the following keys:\n"
            "{\n"
            '  "title": "A catchy title or hook line (required for YouTube, YouTube Shorts, LinkedIn, optional for others)",\n'
            '  "hook": "The opening 1-2 sentence hook designed to grab attention immediately",\n'
            '  "main_content": "The full formatted content (script with scenes/timestamps, caption, thread, or article)",\n'
            '  "call_to_action": "Clear Call to Action inviting comments, shares, likes, or subscriptions",\n'
            '  "hashtags": ["list", "of", "relevant", "hashtags"],\n'
            '  "metadata": {"format_type": "' + content_type + '", "estimated_read_time": "1 min"}\n'
            "}"
        )

        prompt = (
            f"Generate entertainment content based on the following creative specifications:\n\n"
            f"TOPIC: {topic}\n"
            f"BACKGROUND CONTEXT: {desc_str}\n"
            f"PLATFORM: {platform.upper()}\n"
            f"TARGET AUDIENCE: {audience}\n"
            f"DESIRED LANGUAGE: {language}\n"
            f"TONE: {tone}\n"
            f"CONTENT FORMAT: {content_type}\n"
            f"DESIRED LENGTH: {length}\n"
            f"MANDATORY/TARGET KEYWORDS: {kw_str}\n"
            f"SPECIAL INSTRUCTIONS: {custom_str}\n\n"
            f"Strict Output Format:\n{json_schema_req}"
        )

        return prompt

    @staticmethod
    def get_rewrite_prompt(
        platform: str,
        topic: str,
        current_content: str,
        instruction: str,
        language: Optional[str] = None,
        tone: Optional[str] = None,
        length: Optional[str] = None
    ) -> str:
        mods = []
        if language:
            mods.append(f"Switch language to: {language}")
        if tone:
            mods.append(f"Adjust tone to: {tone}")
        if length:
            mods.append(f"Adjust length to: {length}")
        mods.append(f"User instruction: {instruction}")

        mods_str = "\n- ".join(mods)

        return (
            f"You are refining content for {platform.upper()} on the topic '{topic}'.\n\n"
            f"CURRENT CONTENT:\n{current_content}\n\n"
            f"REQUESTED MODIFICATIONS:\n- {mods_str}\n\n"
            f"CRITICAL: Always generate non-empty, detailed text for 'main_content'.\n"
            f"Preserve the core entertainment message and platform-native formatting.\n"
            f"Return a strictly valid JSON object with keys: title, hook, main_content, call_to_action, hashtags, metadata."
        )

