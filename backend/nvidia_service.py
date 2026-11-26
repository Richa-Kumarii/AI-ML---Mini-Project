"""
NVIDIA NIM API Service.
Uses OpenAI client library configured with NVIDIA's base URL.
Supports primary and alternative fallback models with timeout, rate limit, and error handling.
"""

import os
import json
import logging
from typing import Dict, Any, Optional
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("nvidia_service")
logging.basicConfig(level=logging.INFO)

class NvidiaService:
    def __init__(self):
        self.api_key = os.getenv("NVIDIA_API_KEY", "").strip()
        self.base_url = os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1").strip()
        self.primary_model = os.getenv("NVIDIA_MODEL", "nvidia/nemotron-3.5-lightning-30b-a3b").strip()
        self.fallback_model = os.getenv("NVIDIA_FALLBACK_MODEL", "nvidia/nemotron-3.5-bolt-e4b").strip()
        
        self.client = None
        if self.api_key and self.api_key != "your_nvidia_api_key_here":
            self.client = OpenAI(
                base_url=self.base_url,
                api_key=self.api_key,
                timeout=60.0
            )

    def is_configured(self) -> bool:
        return bool(self.api_key and self.api_key != "your_nvidia_api_key_here")

    def chat_completion(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.7,
        top_p: float = 0.9,
        max_tokens: int = 1500,
        response_format_json: bool = True
    ) -> Dict[str, Any]:
        """
        Executes a completion request against NVIDIA NIM API.
        Falls back to alternative model if primary model experiences transient errors.
        """
        if not self.is_configured():
            raise ValueError(
                "NVIDIA API Key is not configured. Please set NVIDIA_API_KEY in backend/.env "
                "or obtain a free key at https://build.nvidia.com/"
            )

        models_to_try = [self.primary_model]
        if self.fallback_model and self.fallback_model != self.primary_model:
            models_to_try.append(self.fallback_model)

        last_error = None
        for model in models_to_try:
            try:
                logger.info(f"Invoking NVIDIA NIM model: {model}")
                messages = [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]

                kwargs = {
                    "model": model,
                    "messages": messages,
                    "temperature": temperature,
                    "top_p": top_p,
                    "max_tokens": max_tokens
                }

                # Note: We omit response_format={'type': 'json_object'} because some NIM models
                # return an empty main_content under strict json_object mode for non-English prompts.
                # Instead, our prompt enforces strict JSON formatting, which yields rich outputs.

                response = self.client.chat.completions.create(**kwargs)
                message_obj = response.choices[0].message
                
                # Check for content first; only fall back to reasoning if content is completely None/empty
                raw_content = message_obj.content
                if not raw_content and getattr(message_obj, "reasoning_content", None):
                    raw_content = message_obj.reasoning_content
                raw_content = str(raw_content or "").strip()
                
                # Parse JSON if requested
                if response_format_json and raw_content:
                    parsed_json = None
                    
                    # 1. Try direct json.loads
                    try:
                        parsed_json = json.loads(raw_content)
                    except Exception:
                        pass
                    
                    # 2. Try markdown code fence extraction
                    if not parsed_json:
                        if "```json" in raw_content:
                            candidate = raw_content.split("```json", 1)[1].split("```", 1)[0].strip()
                            try:
                                parsed_json = json.loads(candidate)
                            except Exception:
                                pass
                        elif "```" in raw_content:
                            candidate = raw_content.split("```", 1)[1].split("```", 1)[0].strip()
                            try:
                                parsed_json = json.loads(candidate)
                            except Exception:
                                pass
                                
                    # 3. Try finding candidate block with title or main_content
                    if not parsed_json or not parsed_json.get("main_content"):
                        last_open = raw_content.rfind('{\n  "title"')
                        if last_open == -1:
                            last_open = raw_content.rfind('{"title"')
                        if last_open == -1:
                            idx = raw_content.rfind('"main_content"')
                            if idx != -1:
                                last_open = raw_content.rfind("{", 0, idx)

                        last_close = raw_content.rfind("}")
                        if last_open != -1 and last_close != -1 and last_close > last_open:
                            candidate = raw_content[last_open:last_close + 1].strip()
                            try:
                                candidate_obj = json.loads(candidate)
                                if isinstance(candidate_obj, dict) and candidate_obj.get("main_content"):
                                    parsed_json = candidate_obj
                            except Exception:
                                pass

                    if parsed_json and isinstance(parsed_json, dict) and parsed_json.get("main_content"):
                        return {"success": True, "data": parsed_json, "model_used": model}

                    logger.warning("Could not parse valid JSON object from model output, returning raw text.")
                    return {
                        "success": True,
                        "data": {"main_content": raw_content},
                        "model_used": model
                    }

                return {"success": True, "data": {"main_content": raw_content}, "model_used": model}

            except Exception as e:
                logger.error(f"Error calling NVIDIA model {model}: {str(e)}")
                last_error = e
                # Continue loop to try fallback model if available

        # If all models failed
        raise RuntimeError(f"NVIDIA API failed across attempted models: {str(last_error)}")

# Global singleton instance
nvidia_service = NvidiaService()

