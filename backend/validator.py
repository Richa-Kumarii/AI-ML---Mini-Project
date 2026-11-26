"""
Validation Engine for Content Generations.
Validates word count, character limits, required structural sections,
presence of mandatory keywords, and platform constraints.
Provides educational warnings instead of false claims of virality.
"""

from typing import Dict, Any, List, Tuple
import re
from platform_config import PLATFORM_CONFIG

class ContentValidator:
    @staticmethod
    def count_words(text: str) -> int:
        if not text:
            return 0
        return len(re.findall(r'\b\w+\b', text))

    @staticmethod
    def count_characters(text: str) -> int:
        if not text:
            return 0
        return len(text)

    @classmethod
    def validate(
        cls,
        platform: str,
        content_dict: Dict[str, Any],
        requested_keywords: List[str] = None
    ) -> Tuple[bool, List[str], Dict[str, Any]]:
        """
        Validates content against platform limits and rules.
        Returns: (is_valid, warnings, stats)
        """
        cfg = PLATFORM_CONFIG.get(platform, {})
        warnings = []
        is_valid = True

        title = content_dict.get("title", "") or ""
        hook = content_dict.get("hook", "") or ""
        main_content = content_dict.get("main_content", "") or ""
        cta = content_dict.get("call_to_action", "") or ""
        hashtags = content_dict.get("hashtags", []) or []

        # Combined content for general length analysis
        full_text = f"{title}\n{hook}\n{main_content}\n{cta}".strip()
        word_count = cls.count_words(full_text)
        char_count = cls.count_characters(full_text)

        # 1. Check for empty or malformed main content
        if not main_content or len(main_content.strip()) < 10:
            warnings.append("Content appears incomplete or empty.")
            return False, warnings, {"word_count": word_count, "character_count": char_count}

        # 2. Check platform-specific character limits
        char_limit = cfg.get("character_limit")
        if char_limit:
            # Special check for X (Twitter): if not a thread, check tweet limit
            if platform == "x":
                # Check if it's formatted as a thread (e.g., 1/, 2/)
                is_thread = bool(re.search(r'^\s*1[/.)]', main_content, re.MULTILINE))
                if not is_thread and char_count > char_limit:
                    warnings.append(
                        f"Exceeds standard single X post limit of {char_limit} characters (current: {char_count}). "
                        f"Consider formatting as a multi-tweet thread or shortening."
                    )
                    is_valid = False
            elif char_count > char_limit:
                warnings.append(
                    f"Exceeds {cfg.get('name', platform)} character limit of {char_limit} (current: {char_count})."
                )
                is_valid = False

        # 3. Check YouTube / Shorts title limits
        title_limit = cfg.get("title_limit")
        if title_limit and title and len(title) > title_limit:
            warnings.append(f"Title exceeds recommended {title_limit} characters (current: {len(title)}).")

        # 4. Check required sections
        req_sections = cfg.get("required_sections", [])
        if "title" in req_sections and not title.strip():
            warnings.append(f"A catchy title is recommended for {cfg.get('name', platform)}.")
        if "hook" in req_sections and not hook.strip():
            warnings.append(f"A designated opening hook is recommended for {cfg.get('name', platform)}.")
        if "call_to_action" in req_sections and not cta.strip():
            warnings.append(f"A closing Call to Action is recommended to prompt audience response.")

        # 5. Hashtag limits
        hashtag_limit = cfg.get("hashtag_limit", 30)
        if len(hashtags) > hashtag_limit:
            warnings.append(
                f"Hashtag count ({len(hashtags)}) exceeds recommended platform maximum of {hashtag_limit}."
            )

        # 6. Check for requested keywords
        if requested_keywords:
            missing_keywords = []
            combined_lower = full_text.lower()
            for kw in requested_keywords:
                kw_clean = kw.strip().lower()
                if kw_clean and kw_clean not in combined_lower:
                    missing_keywords.append(kw.strip())
            if missing_keywords:
                warnings.append(f"Target keywords not explicitly found in copy: {', '.join(missing_keywords)}.")

        stats = {
            "word_count": word_count,
            "character_count": char_count,
            "hashtag_count": len(hashtags)
        }

        return is_valid, warnings, stats

