"""
Platform rules, limits, formats and configurations.
Centralized and easily customizable.
"""

PLATFORM_CONFIG = {
    "instagram": {
        "name": "Instagram",
        "icon": "Instagram",
        "color": "from-pink-500 via-rose-500 to-purple-600",
        "description": "Engaging visual captions, Reel video scripts, carousel slides, hooks & trending hashtags",
        "supported_content_types": [
            "Caption",
            "Reel Script",
            "Carousel Slides",
            "Story",
            "Hook and Hashtags"
        ],
        "character_limit": 2200,
        "recommended_length": {
            "Short": {"min_words": 20, "max_words": 60, "max_chars": 400},
            "Medium": {"min_words": 60, "max_words": 150, "max_chars": 1000},
            "Long": {"min_words": 150, "max_words": 350, "max_chars": 2200}
        },
        "hashtag_limit": 30,
        "hashtag_recommended": 8,
        "required_sections": ["main_content", "hashtags", "call_to_action"]
    },
    "youtube": {
        "name": "YouTube",
        "icon": "Youtube",
        "color": "from-red-600 to-red-700",
        "description": "High-CTR click-worthy titles, SEO descriptions, full video scripts with timestamps & scene breakdowns",
        "supported_content_types": [
            "Video Script",
            "Title and Description",
            "Full Production Script",
            "Scene Breakdown"
        ],
        "character_limit": 5000,
        "title_limit": 100,
        "recommended_length": {
            "Short": {"min_words": 100, "max_words": 250, "max_chars": 1500},
            "Medium": {"min_words": 250, "max_words": 600, "max_chars": 3500},
            "Long": {"min_words": 600, "max_words": 1200, "max_chars": 5000}
        },
        "hashtag_limit": 15,
        "hashtag_recommended": 5,
        "required_sections": ["title", "main_content", "call_to_action"]
    },
    "youtube_shorts": {
        "name": "YouTube Shorts",
        "icon": "Video",
        "color": "from-red-500 via-orange-500 to-amber-600",
        "description": "Fast-paced vertical video scripts with a 3-second hook, fast cuts, audio cues & engagement loop",
        "supported_content_types": [
            "Short Script",
            "Dialogue",
            "Viral Hook"
        ],
        "character_limit": 1000,
        "title_limit": 100,
        "recommended_length": {
            "Short": {"min_words": 40, "max_words": 90, "max_chars": 600},
            "Medium": {"min_words": 90, "max_words": 160, "max_chars": 950},
            "Long": {"min_words": 160, "max_words": 220, "max_chars": 1000}
        },
        "hashtag_limit": 10,
        "hashtag_recommended": 4,
        "required_sections": ["title", "hook", "main_content", "call_to_action"]
    },
    "facebook": {
        "name": "Facebook",
        "icon": "Facebook",
        "color": "from-blue-600 to-indigo-700",
        "description": "Community-focused storytelling, interactive promotional posts, conversation starters & questions",
        "supported_content_types": [
            "Post",
            "Storytelling",
            "Advertisement",
            "Community Discussion"
        ],
        "character_limit": 5000,
        "recommended_length": {
            "Short": {"min_words": 30, "max_words": 80, "max_chars": 500},
            "Medium": {"min_words": 80, "max_words": 200, "max_chars": 1400},
            "Long": {"min_words": 200, "max_words": 500, "max_chars": 3500}
        },
        "hashtag_limit": 10,
        "hashtag_recommended": 3,
        "required_sections": ["main_content", "call_to_action"]
    },
    "x": {
        "name": "X (Twitter)",
        "icon": "Twitter",
        "color": "from-slate-800 to-slate-950",
        "description": "Punchy standalone posts and multi-tweet threads formatted with numbered tweets within the 280-char limit",
        "supported_content_types": [
            "Post",
            "Thread",
            "Hot Take",
            "Announcement"
        ],
        "character_limit": 280,
        "thread_max_tweets": 7,
        "recommended_length": {
            "Short": {"min_words": 10, "max_words": 35, "max_chars": 240},
            "Medium": {"min_words": 35, "max_words": 80, "max_chars": 280},
            "Long": {"min_words": 80, "max_words": 250, "max_chars": 1500} # Threads
        },
        "hashtag_limit": 5,
        "hashtag_recommended": 2,
        "required_sections": ["main_content"]
    },
    "linkedin": {
        "name": "LinkedIn",
        "icon": "Linkedin",
        "color": "from-sky-700 to-blue-800",
        "description": "Professional thought leadership, career/industry insights, structured takeaways & workplace storytelling",
        "supported_content_types": [
            "Post",
            "Storytelling",
            "Thought Leadership",
            "Industry Insight",
            "Career Advice"
        ],
        "character_limit": 3000,
        "recommended_length": {
            "Short": {"min_words": 50, "max_words": 120, "max_chars": 800},
            "Medium": {"min_words": 120, "max_words": 300, "max_chars": 1800},
            "Long": {"min_words": 300, "max_words": 600, "max_chars": 3000}
        },
        "hashtag_limit": 10,
        "hashtag_recommended": 4,
        "required_sections": ["headline", "main_content", "call_to_action"]
    }
}

VALID_TONES = [
    "Funny",
    "Emotional",
    "Suspense",
    "Motivational",
    "Professional",
    "Casual",
    "Educational",
    "Storytelling",
    "Dramatic"
]

VALID_LANGUAGES = ["English", "Hindi", "Hinglish"]

VALID_LENGTHS = ["Short", "Medium", "Long"]

