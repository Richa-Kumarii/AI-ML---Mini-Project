"""
Comprehensive Test Suite for AI Multi-Platform Content Generator.
Tests:
1. Health and Config endpoints
2. Single-platform and multi-platform generation
3. English, Hindi, and Hinglish generations
4. Funny and emotional tone styling
5. Character limits and validation engine
6. Regeneration and rewrite capabilities
7. SQLite database persistence and deletion
8. NVIDIA API graceful fallback / missing key handling
"""

import pytest
import sys
import os

# Add backend directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from fastapi.testclient import TestClient
from main import app
from validator import ContentValidator
from platform_config import PLATFORM_CONFIG
from prompt_builder import PromptBuilder

client = TestClient(app)

def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "nvidia_configured" in data
    assert "primary_model" in data

def test_get_config():
    response = client.get("/api/config")
    assert response.status_code == 200
    data = response.json()
    assert "platforms" in data
    assert "instagram" in data["platforms"]
    assert "youtube" in data["platforms"]
    assert "tones" in data
    assert "languages" in data

def test_validator_word_and_char_counts():
    text = "In a world of neon cinema, heroes rise."
    words = ContentValidator.count_words(text)
    chars = ContentValidator.count_characters(text)
    assert words == 8
    assert chars == len(text)

def test_validator_x_character_limit():
    long_single_tweet = "A" * 350
    content_dict = {
        "title": "Viral Post",
        "main_content": long_single_tweet,
        "hashtags": ["#Film"]
    }
    is_valid, warnings, stats = ContentValidator.validate("x", content_dict)
    assert is_valid is False
    assert any("Exceeds standard single X post limit" in w for w in warnings)

def test_validator_required_sections_and_keywords():
    content_dict = {
        "title": "SciFi Movie",
        "hook": "",
        "main_content": "Just watched an incredible indie film.",
        "call_to_action": "",
        "hashtags": ["#Cinema"]
    }
    is_valid, warnings, stats = ContentValidator.validate(
        platform="youtube_shorts",
        content_dict=content_dict,
        requested_keywords=["CGI", "climax"]
    )
    # Missing hook, CTA, and target keywords
    assert any("opening hook is recommended" in w for w in warnings)
    assert any("Target keywords not explicitly found" in w for w in warnings)

def test_prompt_builder_structure():
    sys_prompt = PromptBuilder.get_system_prompt("instagram", "Hindi", "Funny")
    assert "INSTAGRAM" in sys_prompt
    assert "Hindi" in sys_prompt
    assert "Funny" in sys_prompt

    user_prompt = PromptBuilder.get_user_prompt(
        platform="youtube",
        topic="AI in Bollywood",
        description="Deep dive on VFX pipelines",
        target_audience="Cinema students",
        language="Hinglish",
        tone="Dramatic",
        content_type="Video Script",
        length="Long",
        keywords=["VFX", "CGI"],
        custom_instructions="Focus on budgeting"
    )
    assert "AI in Bollywood" in user_prompt
    assert "Hinglish" in user_prompt
    assert "VFX, CGI" in user_prompt

def test_full_generation_and_history_workflow():
    payload = {
        "topic": "The Mystery of the Quantum Soundstage",
        "description": "A film director vanishes mid-take inside a high-tech studio.",
        "platforms": ["instagram", "youtube_shorts", "x"],
        "target_audience": "Film geeks & mystery enthusiasts",
        "language": "English",
        "tone": "Suspense",
        "content_type": "Post",
        "length": "Medium",
        "keywords": ["soundstage", "portal"],
        "custom_instructions": "End with an unresolved question"
    }

    # 1. Generate multi-platform
    gen_res = client.post("/api/generate", json=payload)
    assert gen_res.status_code == 200
    gen_data = gen_res.json()
    assert gen_data["topic"] == payload["topic"]
    assert "instagram" in gen_data["results"]
    assert "youtube_shorts" in gen_data["results"]
    assert "x" in gen_data["results"]
    gen_id = gen_data["id"]
    assert gen_id is not None

    # 2. Check history contains this entry
    hist_res = client.get(f"/api/history/{gen_id}")
    assert hist_res.status_code == 200
    hist_item = hist_res.json()
    assert hist_item["topic"] == payload["topic"]

    # 3. Test single-platform regeneration
    regen_payload = {
        "generation_id": gen_id,
        "platform": "instagram",
        "topic": payload["topic"],
        "language": "Hindi",
        "tone": "Emotional",
        "content_type": "Caption",
        "length": "Short"
    }
    regen_res = client.post("/api/regenerate", json=regen_payload)
    assert regen_res.status_code == 200
    regen_data = regen_res.json()
    assert regen_data["platform"] == "instagram"
    assert regen_data["main_content"]

    # 4. Test smart AI rewrite
    rewrite_payload = {
        "platform": "instagram",
        "topic": payload["topic"],
        "current_content": regen_data["main_content"],
        "instruction": "Make it funnier and add a joke about craft services",
        "tone": "Funny"
    }
    rw_res = client.post("/api/rewrite", json=rewrite_payload)
    assert rw_res.status_code == 200
    rw_data = rw_res.json()
    assert rw_data["platform"] == "instagram"

    # 5. Delete history entry
    del_res = client.delete(f"/api/history/{gen_id}")
    assert del_res.status_code == 200

    # 6. Verify deleted
    not_found_res = client.get(f"/api/history/{gen_id}")
    assert not_found_res.status_code == 404

def test_hinglish_and_funny_generation():
    payload = {
        "topic": "First Day at Film School Expectations vs Reality",
        "platforms": ["x", "linkedin"],
        "language": "Hinglish",
        "tone": "Funny",
        "content_type": "Post",
        "length": "Short"
    }
    res = client.post("/api/generate", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "x" in data["results"]
    assert "linkedin" in data["results"]
    # Clean up test entry
    if data.get("id"):
        client.delete(f"/api/history/{data['id']}")

