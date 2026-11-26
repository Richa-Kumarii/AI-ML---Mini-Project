import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck(filename="OmniContent_AI_Presentation.pptx"):
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Formal Color Palette
    c_bg = RGBColor(11, 15, 25)          # Deep Navy/Dark Slate (#0b0f19)
    c_card = RGBColor(17, 24, 39)        # Slate 900 (#111827)
    c_card_border = RGBColor(51, 65, 85) # Slate 700 (#334155)
    c_primary = RGBColor(255, 255, 255)  # Pure White
    c_accent = RGBColor(168, 85, 247)    # Vibrant Purple (#a855f7)
    c_cyan = RGBColor(6, 182, 212)       # Tech Cyan (#06b6d4)
    c_body = RGBColor(203, 213, 225)     # Slate 300 (#cbd5e1)
    c_muted = RGBColor(148, 163, 184)    # Slate 400 (#94a3b8)

    blank_layout = prs.slide_layouts[6]

    def set_slide_background(slide):
        bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg_shape.fill.solid()
        bg_shape.fill.fore_color.rgb = c_bg
        bg_shape.line.color.rgb = c_bg
        return bg_shape

    def add_header(slide, title_text, category_text="CAPSTONE PROJECT PRESENTATION"):
        # Category / Running Header
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.4))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.name = "Arial"
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = c_accent

        # Title
        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.8))
        tf_t = t_box.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.name = "Arial"
        p_t.font.size = Pt(22)
        p_t.font.bold = True
        p_t.font.color.rgb = c_primary

        # Subtle Accent Divider
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(0.03))
        line.fill.solid()
        line.fill.fore_color.rgb = c_card_border
        line.line.color.rgb = c_card_border

    def add_footer(slide, current_slide, total_slides=13):
        f_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(11.7), Inches(0.4))
        tf_f = f_box.text_frame
        p_f = tf_f.paragraphs[0]
        p_f.text = f"OmniContent AI • Entertainment Domain Generative AI Studio   |   Slide {current_slide} of {total_slides}"
        p_f.font.name = "Arial"
        p_f.font.size = Pt(9)
        p_f.font.color.rgb = c_muted

    def add_card(slide, left, top, width, height, title="", items=[]):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = c_card
        card.line.color.rgb = c_card_border
        card.line.width = Pt(1)

        tx_box = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), width - Inches(0.4), height - Inches(0.4))
        tf = tx_box.text_frame
        tf.word_wrap = True

        if title:
            p_head = tf.paragraphs[0]
            p_head.text = title
            p_head.font.name = "Arial"
            p_head.font.size = Pt(14)
            p_head.font.bold = True
            p_head.font.color.rgb = c_cyan
            p_head.space_after = Pt(10)

        first = True if not title else False
        for item in items:
            p = tf.add_paragraph() if not first else tf.paragraphs[0]
            first = False
            p.text = f"• {item}"
            p.font.name = "Arial"
            p.font.size = Pt(11)
            p.font.color.rgb = c_body
            p.space_after = Pt(6)

        return card

    # ==========================================
    # SLIDE 1: FORMAL TITLE SLIDE
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    # Title Card Accent
    t_box = s1.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(11.7), Inches(2.2))
    tf1 = t_box.text_frame
    tf1.word_wrap = True

    p_badge = tf1.paragraphs[0]
    p_badge.text = "ACADEMIC CAPSTONE PRESENTATION • ENTERTAINMENT DOMAIN"
    p_badge.font.name = "Arial"
    p_badge.font.size = Pt(11)
    p_badge.font.bold = True
    p_badge.font.color.rgb = c_cyan
    p_badge.space_after = Pt(8)

    p_main = tf1.add_paragraph()
    p_main.text = "AI-Powered Smart Multi-Platform Content Generator"
    p_main.font.name = "Arial"
    p_main.font.size = Pt(28)
    p_main.font.bold = True
    p_main.font.color.rgb = c_primary
    p_main.space_after = Pt(6)

    p_sub = tf1.add_paragraph()
    p_sub.text = "OmniContent AI Studio: One Topic → Platform-Specific Prompt Architecture → NVIDIA Nemotron 30B LLM"
    p_sub.font.name = "Arial"
    p_sub.font.size = Pt(13)
    p_sub.font.color.rgb = c_accent

    # Student Details Table Card
    team_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.2), Inches(11.733), Inches(3.4))
    team_card.fill.solid()
    team_card.fill.fore_color.rgb = c_card
    team_card.line.color.rgb = c_card_border

    # Inside Team Card
    tc_box = s1.shapes.add_textbox(Inches(1.2), Inches(3.4), Inches(11.0), Inches(3.0))
    tf_tc = tc_box.text_frame
    tf_tc.word_wrap = True

    p_th = tf_tc.paragraphs[0]
    p_th.text = "PROJECT SUBMITTED BY:"
    p_th.font.name = "Arial"
    p_th.font.size = Pt(12)
    p_th.font.bold = True
    p_th.font.color.rgb = c_cyan
    p_th.space_after = Pt(14)

    students = [
        ("SHRIYA SRIVASTAVA", "202510101240009", "Full-Stack Lead & Generative AI Architect"),
        ("TANY PRIYA", "202510101240036", "Backend Architect & LLM Prompt Engineer"),
        ("SRISHTI YADAV", "202510101240052", "UI/UX Designer & Frontend Developer"),
        ("RICHA KUMARI", "202510101240058", "Validation Engineer & Quality Assurance Lead")
    ]

    for name, roll, role in students:
        p_st = tf_tc.add_paragraph()
        p_st.text = f"{name.ljust(22)}   |   Roll No: {roll}   |   {role}"
        p_st.font.name = "Courier New"
        p_st.font.size = Pt(11)
        p_st.font.bold = True
        p_st.font.color.rgb = c_primary
        p_st.space_after = Pt(8)

    p_dept = tf_tc.add_paragraph()
    p_dept.text = "\nDepartment of Computer Science & Engineering • Academic Session 2025-2026"
    p_dept.font.name = "Arial"
    p_dept.font.size = Pt(10)
    p_dept.font.color.rgb = c_muted

    # ==========================================
    # SLIDE 2: EXECUTIVE SUMMARY & BACKGROUND
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "Executive Summary & Entertainment Domain Context")
    add_footer(s2, 2)

    add_card(s2, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "The Entertainment Industry Problem", [
        "Modern creators & film marketing teams must maintain active distribution across 6 heterogeneous networks.",
        "Traditional workflow forces manual, tedious rewriting or disastrous generic copy-pasting.",
        "Generic identical text fails social algorithms, destroys audience engagement, and violates strict character ceilings.",
        "Linguistic barrier: Literal English-to-Hindi translations sound robotic and lose comedic/dramatic timing."
    ])

    add_card(s2, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), "The OmniContent AI Solution", [
        "Takes 1 creative entertainment logline or topic as single input.",
        "Synthesizes 6 divergent, platform-native outputs in parallel (Instagram, YouTube, Shorts, Facebook, X, LinkedIn).",
        "Deep platform psychology: 3-second retention hooks for Shorts, 280-char wit on X, thought leadership on LinkedIn.",
        "Multilingual fluency: English, Devanagari Hindi (हिंदी), and conversational urban Hinglish."
    ])

    # ==========================================
    # SLIDE 3: CORE PROBLEM STATEMENT & OBJECTIVES
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "Problem Formulation & Project Objectives")
    add_footer(s3, 3)

    add_card(s3, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8), "Algorithmic Heterogeneity", [
        "X (Twitter) strictly limits posts to 280 characters.",
        "YouTube mandates high-CTR titles and timestamped scene breakdowns.",
        "Shorts demands rapid 9:16 vertical pacing with audio sound effect triggers."
    ])

    add_card(s3, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.8), "Stochastic LLM Failures", [
        "Standard LLMs hallucinate, omit call-to-actions, and violate character constraints.",
        "Lack of verification leads to truncated posts or missing mandatory sponsor keywords.",
        "Need deterministic Python validation with controlled self-healing."
    ])

    add_card(s3, Inches(8.8), Inches(1.8), Inches(3.7), Inches(4.8), "Core Project Objectives", [
        "1. Build a Zero-Repetition Engine ensuring distinct prompt logic per platform.",
        "2. Integrate NVIDIA NIM Nemotron LLMs via OpenAI Python SDK.",
        "3. Implement deterministic Python validation & Max-1 AI rewrite loops.",
        "4. Develop interactive dark-mode studio with SQLite persistence."
    ])

    # ==========================================
    # SLIDE 4: SYSTEM ARCHITECTURE & DATA PIPELINE
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "Full-Stack System Architecture & Pipeline")
    add_footer(s4, 4)

    add_card(s4, Inches(0.8), Inches(1.8), Inches(11.7), Inches(4.8), "End-to-End Generative AI Pipeline Flow", [
        "1. Client Brief Ingestion: React SPA collects topic, audience, language, tone, format, length, and keywords.",
        "2. Gateway Sanitization: FastAPI server validates incoming JSON using Pydantic v2 schemas.",
        "3. Prompt Orchestration: PromptBuilder dynamically generates customized system instructions & JSON output schemas.",
        "4. NVIDIA NIM Inference: NvidiaService connects to 'integrate.api.nvidia.com' targeting Nemotron-30B.",
        "5. Output Extraction: Clean parsing extracts structured JSON, seamlessly bypassing Chain-of-Thought (CoT) reasoning.",
        "6. Validation & Self-Healing: ContentValidator audits character caps & keywords; executes 1 AI rewrite if constraints fail.",
        "7. Vault Storage & Response: SQLAlchemy commits record to SQLite database and returns verified payload to frontend."
    ])

    # ==========================================
    # SLIDE 5: COMPLETE TECHNOLOGY STACK
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "Technology Stack & Enterprise Frameworks")
    add_footer(s5, 5)

    add_card(s5, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8), "Frontend Layer", [
        "React 18: Component-based SPA architecture.",
        "Vite 5: High-speed bundling & HMR.",
        "Tailwind CSS: Dark entertainment studio theme.",
        "Lucide React: Clean vector iconography.",
        "Axios: Promise-based HTTP client."
    ])

    add_card(s5, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.8), "Backend Layer", [
        "Python 3.14: Async runtime environment.",
        "FastAPI: High-performance ASGI REST API.",
        "Uvicorn: Lightning-fast ASGI web server.",
        "Pydantic v2: Strict schema validation.",
        "SQLAlchemy: Robust ORM database abstraction."
    ])

    add_card(s5, Inches(8.8), Inches(1.8), Inches(3.7), Inches(4.8), "AI & Database Layer", [
        "NVIDIA NIM API: Hosted enterprise LLM microservice.",
        "Nemotron-3.5-Lightning-30B: Primary high-creativity LLM.",
        "Nemotron-3.5-Bolt-E4B: High-speed fallback model.",
        "OpenAI Python SDK: Configured for NVIDIA Base URL.",
        "SQLite 3: Local zero-configuration relational vault."
    ])

    # ==========================================
    # SLIDE 6: 6 DIVERGENT PLATFORM ENGINES
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, "Platform-Specific Generation Engines")
    add_footer(s6, 6)

    add_card(s6, Inches(0.8), Inches(1.8), Inches(3.6), Inches(2.2), "Instagram Engine", [
        "Visual curiosity hooks (<5 words).",
        "Aesthetic emoji spacing & Reel scripts.",
        "5 to 15 targeted hashtags."
    ])

    add_card(s6, Inches(4.8), Inches(1.8), Inches(3.6), Inches(2.2), "YouTube Engine", [
        "High-CTR curiosity-gap titles (<70 chars).",
        "Timestamped scene breakdowns [00:00].",
        "SEO-rich search descriptions & CTAs."
    ])

    add_card(s6, Inches(8.8), Inches(1.8), Inches(3.7), Inches(2.2), "YouTube Shorts Engine", [
        "Explosive 3-second retention hooks.",
        "Dynamic vertical 9:16 dialogue pacing.",
        "Audio cues [Bass Drop] & seamless loop."
    ])

    add_card(s6, Inches(0.8), Inches(4.4), Inches(3.6), Inches(2.2), "Facebook Engine", [
        "Relatable community storytelling.",
        "Emotional paragraph development.",
        "Audience conversation catalysts."
    ])

    add_card(s6, Inches(4.8), Inches(4.4), Inches(3.6), Inches(2.2), "X (Twitter) Engine", [
        "Strict compliance with 280-char ceiling.",
        "Clean numbered multi-tweet threads (1/, 2/).",
        "Maximum punchline impact & sharp wit."
    ])

    add_card(s6, Inches(8.8), Inches(4.4), Inches(3.7), Inches(2.2), "LinkedIn Engine", [
        "Translates cinematic crises to leadership.",
        "Whitespace formatting with 3 takeaways.",
        "Professional peer debate invitation."
    ])

    # ==========================================
    # SLIDE 7: LIVE CASE STUDY (DIVERGENT OUTPUTS)
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7, "Case Study: 1 Topic → Divergent Creative Assets")
    add_footer(s7, 7)

    add_card(s7, Inches(0.8), Inches(1.8), Inches(11.7), Inches(1.0), "Central Test Topic", [
        "Topic: 'A detective who can hear what inanimate objects witnessed at a movie theatre crime scene' (Tone: Suspense)"
    ])

    add_card(s7, Inches(0.8), Inches(3.1), Inches(3.6), Inches(3.5), "Instagram Reel Output", [
        "Title: 'The Silent Witness Speaks'",
        "Hook: 'The popcorn whispered secrets...'",
        "Content: Visual camera breakdown with glowing projector beams.",
        "Hashtags: #MysteryCinema #FilmLovers"
    ])

    add_card(s7, Inches(4.8), Inches(3.1), Inches(3.6), Inches(3.5), "X (Twitter) Output", [
        "Length: Exactly 250 characters (<280 cap).",
        "Copy: 'He doesn\\'t need a confession. The movie theatre—every creak, every projector flicker—holds a perfect, silent witness. What did the stale popcorn absorb?'"
    ])

    add_card(s7, Inches(8.8), Inches(3.1), Inches(3.7), Inches(3.5), "YouTube Shorts Output", [
        "Hook: 'The popcorn wasn\\'t just a snack; it held the truth. Can he hear the crime?'",
        "Format: [00:00 - Zoom on popcorn box] with bass drop audio cues and seamless loop."
    ])

    # ==========================================
    # SLIDE 8: MULTILINGUAL & TONE PSYCHOLOGY
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header(s8, "Multilingual Engineering & Tone Psychology")
    add_footer(s8, 8)

    add_card(s8, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "Tri-Lingual Generation Engine", [
        "English: Polished cinematic vocabulary, global marketing standard.",
        "Hindi (हिंदी Devanagari): Rich cultural phrasing, dramatic Bollywood dialogues, authentic Hindi syntax.",
        "Hinglish: Urban Roman-script Hindi-English blend widely used by Indian youth, standup comics, and creators.",
        "Preserves core story meaning without robotic literal machine translation artifacts."
    ])

    add_card(s8, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), "9 Entertainment Emotional Tones", [
        "Funny: Sharp comedic punchlines, self-deprecating irony, witty observational humor.",
        "Suspense: Ominous curiosity gaps, cliffhanger line breaks, psychological tension.",
        "Dramatic: High-stakes emotional conflicts, cinematic gravity, powerful character quotes.",
        "Motivational, Casual, Educational, Storytelling, Professional, Dialogue."
    ])

    # ==========================================
    # SLIDE 9: VALIDATION & CONTROLLED SELF-HEALING
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_header(s9, "Validation Engine & Controlled AI Self-Healing")
    add_footer(s9, 9)

    add_card(s9, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "Deterministic Python Validation", [
        "Character Ceiling Audit: Enforces 280-char hard cap on X; 2200 on Instagram; 100 on YouTube titles.",
        "Section Completeness: Verifies presence of Hooks, Scene Timestamps, and Calls-to-Action.",
        "Mandatory Keyword Audit: Scans text for required sponsor or plot keywords.",
        "Hashtag Spam Guard: Caps tags to prevent algorithmic shadowbanning."
    ])

    add_card(s9, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), "Controlled AI Self-Healing Loop", [
        "Hybrid Architecture: Combines deterministic Python checks with probabilistic LLM generation.",
        "Single Rewrite Policy: If a hard constraint is broken, exactly 1 targeted AI rewrite is executed.",
        "Zero Infinite Loops: Max-1 rewrite guarantee prevents unbounded API credit consumption.",
        "Responsible Guardrails: Issues actionable warnings without making false virality claims."
    ])

    # ==========================================
    # SLIDE 10: DATABASE & VAULT ARCHITECTURE
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10)
    add_header(s10, "SQLite Database & Vault Persistence")
    add_footer(s10, 10)

    add_card(s10, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "Relational Data Model (SQLAlchemy)", [
        "ContentGeneration Table: Automatically initialized on startup.",
        "Captures topic, context, audience, language, tone, length, and keywords.",
        "Results Column: Stores complete serialized JSON of all 6 platform outputs.",
        "Timestamp Tracking: Audit-ready created_at and updated_at fields.",
        "Zero Credential Leakage: API keys are strictly loaded from environment variables."
    ])

    add_card(s10, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), "Vault CRUD Operations", [
        "GET /api/history: Paginated generation retrieval.",
        "GET /api/history/{id}: Instant reload of past campaigns into active studio.",
        "DELETE /api/history/{id}: Permanent removal of archived records.",
        "POST /api/regenerate: Granular single-platform regeneration updating the active record."
    ])

    # ==========================================
    # SLIDE 11: USER EXPERIENCE & DASHBOARD CAPABILITIES
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11)
    add_header(s11, "UI/UX & Creator Studio Dashboard")
    add_footer(s11, 11)

    add_card(s11, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8), "Interactive Studio", [
        "Platform multi-select buttons with live active states.",
        "Dynamic length toggles (Short, Medium, Long).",
        "Target audience and keyword inputs.",
        "Live backend health badge for NVIDIA NIM."
    ])

    add_card(s11, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.8), "Results Workspace", [
        "Platform result cards with validation badges.",
        "Real-time word and character count indicators.",
        "Warning banners for limit excursions.",
        "Single-platform regenerate & AI refine modals."
    ])

    add_card(s11, Inches(8.8), Inches(1.8), Inches(3.7), Inches(4.8), "Export & Editing", [
        "In-place text editing with instant character recount.",
        "One-click copy to clipboard per card.",
        "Full dossier download (.TXT) containing all 6 assets.",
        "Content Vault search & reload panel."
    ])

    # ==========================================
    # SLIDE 12: TESTING, VERIFICATION & METRICS
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12)
    add_header(s12, "Testing, Verification & Quality Assurance")
    add_footer(s12, 12)

    add_card(s12, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "Automated Test Suite (pytest)", [
        "test_health_check: Verifies API health and NVIDIA model registration (200 OK).",
        "test_get_config: Validates platform metadata and rules.",
        "test_validator_limits: Confirms X character limits (>280 chars flagged).",
        "test_workflow: Tests multi-platform generation, SQLite saving, query, and deletion."
    ])

    add_card(s12, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), "Production Verification Results", [
        "Live NVIDIA NIM Calls: Confirmed HTTP 200 OK with Nemotron 30B inference.",
        "Reasoning Parsing: Successfully strips Chain-of-Thought tags for pure JSON.",
        "Fast Build: Production frontend bundle built with Vite & Tailwind.",
        "Zero Failure Graceful Degradation: Informative notices if credentials are missing."
    ])

    # ==========================================
    # SLIDE 13: CONCLUSION & FUTURE ROADMAP
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    set_slide_background(s13)
    add_header(s13, "Conclusion, Limitations & Future Roadmap")
    add_footer(s13, 13)

    add_card(s13, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "Project Impact & Limitations", [
        "Impact: Eliminates manual cross-platform rewriting bottlenecks in entertainment marketing.",
        "Algorithmic Alignment: Delivers native format compliance across 6 major networks.",
        "Current Limitation: Text and script focused; lacks direct raster rendering.",
        "Publishing Scope: Outputs drafts for creator review; avoids unapproved auto-posting."
    ])

    add_card(s13, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), "Future Engineering Roadmap", [
        "Multimodal Asset Generation: Integrate NVIDIA Edify/Stable Diffusion for automated thumbnails.",
        "Voiceover Synthesis: Integrate NVIDIA Riva or ElevenLabs for short-form audio previews.",
        "Social API Scheduling: OAuth2 integration with Meta Graph and X API for direct scheduling.",
        "Analytics Feedback Loop: Auto-tune prompt weights based on real-world post engagement."
    ])

    prs.save(filename)
    print(f"Successfully generated {filename}")

if __name__ == "__main__":
    out_file = "OmniContent_AI_Presentation.pptx"
    if len(sys.argv) > 1:
        out_file = sys.argv[1]
    create_deck(out_file)

