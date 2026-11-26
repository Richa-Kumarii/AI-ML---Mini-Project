import os
import sys
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            # First page is Cover Page - no headers/footers
            return

        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#475569"))

        # Header
        self.drawString(54, 750, "PROJECT REPORT: AI-POWERED SMART MULTI-PLATFORM CONTENT GENERATOR")
        self.drawRightString(612 - 54, 750, "ENTERTAINMENT DOMAIN")
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.6)
        self.line(54, 742, 612 - 54, 742)

        # Footer
        self.line(54, 45, 612 - 54, 45)
        self.drawString(54, 32, "Confidential & Academic Evaluation • Dept. of Computer Science & Engineering")
        self.drawRightString(612 - 54, 32, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def build_pdf(filename="Project_Report_OmniContent_AI.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom styles
    c_primary = colors.HexColor("#1e1b4b")   # Deep navy
    c_accent = colors.HexColor("#6366f1")    # Indigo
    c_dark = colors.HexColor("#0f172a")      # Slate 900
    c_body = colors.HexColor("#334155")      # Slate 700

    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=30,
        textColor=c_primary,
        alignment=1, # Center
        spaceAfter=12
    )

    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=c_accent,
        alignment=1,
        spaceAfter=24
    )

    h1_style = ParagraphStyle(
        'ReportH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=c_primary,
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'ReportH2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=c_accent,
        spaceBefore=10,
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'ReportBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=c_body,
        spaceAfter=7
    )

    bullet_style = ParagraphStyle(
        'ReportBullet',
        parent=body_style,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=4
    )

    code_style = ParagraphStyle(
        'ReportCode',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#0f172a"),
        backColor=colors.HexColor("#f1f5f9"),
        borderPadding=6,
        spaceAfter=8
    )

    story = []

    # ==========================================
    # PAGE 1: FORMAL COVER PAGE
    # ==========================================
    story.append(Spacer(1, 40))
    story.append(Paragraph("PROJECT TECHNICAL REPORT", ParagraphStyle('CoverPre', fontName='Helvetica-Bold', fontSize=10, leading=12, textColor=c_accent, alignment=1)))
    story.append(Spacer(1, 10))
    story.append(Paragraph("AI-POWERED SMART MULTI-PLATFORM<br/>CONTENT GENERATOR", title_style))
    story.append(Paragraph("Domain: Entertainment & Social Media Generative AI Architecture", subtitle_style))
    story.append(HRFlowable(width="60%", thickness=1.5, color=c_accent, spaceBefore=0, spaceAfter=25, hAlign='CENTER'))
    
    story.append(Paragraph(
        "A Comprehensive Engineering Report on the Design, Implementation, "
        "and Validation of an Enterprise Generative AI Studio powered by "
        "NVIDIA NIM Architecture, FastAPI, and React.",
        ParagraphStyle('CoverDesc', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=10, leading=14, alignment=1, textColor=c_body)
    ))
    story.append(Spacer(1, 45))

    # Students Table
    students_header = Paragraph("<b>PROJECT SUBMITTED BY:</b>", ParagraphStyle('SH', fontName='Helvetica-Bold', fontSize=10, textColor=c_primary, alignment=1))
    story.append(students_header)
    story.append(Spacer(1, 10))

    student_data = [
        ["Sl.", "Student Name", "University Roll Number", "Role"],
        ["1", "SHRIYA SRIVASTAVA", "202510101240009", "Full-Stack & Generative AI Lead"],
        ["2", "TANY PRIYA", "202510101240036", "Backend Architect & LLM Integration"],
        ["3", "SRISHTI YADAV", "202510101240052", "UI/UX Designer & Frontend Engineer"],
        ["4", "RICHA KUMARI", "202510101240058", "Validation Engineer & QA Specialist"]
    ]

    t_students = Table(student_data, colWidths=[25, 175, 150, 154])
    t_students.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e1b4b")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8.5),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('TOPPADDING', (0, 0), (-1, 0), 6),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#f8fafc")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
        ('ALIGN', (2, 0), (2, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor("#ffffff"), colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0, 1), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 5),
    ]))
    story.append(t_students)

    story.append(Spacer(1, 50))
    story.append(Paragraph("<b>Department of Computer Science & Engineering</b>", ParagraphStyle('Inst', fontName='Helvetica-Bold', fontSize=10, textColor=c_primary, alignment=1)))
    story.append(Paragraph("Academic Capstone Project Evaluation • Session 2025–2026", ParagraphStyle('Inst2', fontName='Helvetica', fontSize=9, textColor=c_body, alignment=1)))
    story.append(PageBreak())

    # ==========================================
    # PAGE 2: EXECUTIVE SUMMARY & OBJECTIVES
    # ==========================================
    story.append(Paragraph("1. Executive Summary & Problem Formulation", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.8, color=c_accent, spaceBefore=2, spaceAfter=10))

    story.append(Paragraph("<b>1.1 Executive Summary</b>", h2_style))
    story.append(Paragraph(
        "Modern digital entertainment distribution requires content creators, production houses, and marketing "
        "teams to maintain a consistent presence across multiple distinct social ecosystems. However, creating tailored, "
        "high-engagement promotional copy for six diverging platforms—Instagram, YouTube, YouTube Shorts, Facebook, X (formerly Twitter), "
        "and LinkedIn—presents an acute operational bottleneck. Generic copy-pasting across platforms yields substandard audience engagement "
        "and violates algorithmic best practices (such as character limits, aspect ratios, retention hooks, and structural formatting).",
        body_style
    ))
    story.append(Paragraph(
        "This project introduces <b>OmniContent AI</b>, an end-to-end Generative AI platform engineered to translate "
        "a single core entertainment idea or story logline into six platform-native, algorithm-compliant, and culturally resonant "
        "content assets in parallel. Leveraging the <b>NVIDIA NIM (Inference Microservice)</b> cloud architecture with state-of-the-art "
        "Nemotron LLMs (<code>nvidia/nemotron-3.5-lightning-30b-a3b</code> and <code>nvidia/nemotron-3.5-bolt-e4b</code>), FastAPI, "
        "and React, the application ensures high creativity, adherence to structural rules, and strict constraint validation.",
        body_style
    ))

    story.append(Paragraph("<b>1.2 Problem Statement</b>", h2_style))
    story.append(Paragraph(
        "Current digital entertainment workflows suffer from three critical challenges:",
        body_style
    ))
    story.append(Paragraph("• <b>Algorithmic & Format Heterogeneity:</b> Each social platform enforces diverging constraints—X strictly penalizes text beyond 280 characters; YouTube demands curiosity-gap titles and structured video timestamps; YouTube Shorts mandates intense 3-second visual hooks; LinkedIn expects business-leadership takeaways.", bullet_style))
    story.append(Paragraph("• <b>Loss of Creative Nuance Across Languages:</b> Existing translation pipelines often perform robotic literal translations, destroying comedic timing, dramatic suspense, and urban cultural tone in Indian entertainment contexts.", bullet_style))
    story.append(Paragraph("• <b>Lack of Output Validation:</b> Standard consumer LLMs frequently hallucinate formatting, omit crucial call-to-actions, violate character limits, or miss mandatory sponsor/production keywords.", bullet_style))

    story.append(Paragraph("<b>1.3 Core Project Objectives</b>", h2_style))
    story.append(Paragraph("1. <b>Architect a Zero-Repetition Engine:</b> Guarantee that identical copy is never recycled across channels by employing discrete prompt architectures for each platform.", bullet_style))
    story.append(Paragraph("2. <b>Implement Enterprise AI Connectivity:</b> Integrate the NVIDIA NIM API using the OpenAI Python SDK, implementing resilient model fallback strategies.", bullet_style))
    story.append(Paragraph("3. <b>Enforce Rigorous Python-Based Validation:</b> Validate character counts, word density, mandatory keyword presence, and structural sections with automated single-attempt AI self-correction.", bullet_style))
    story.append(Paragraph("4. <b>Deliver Modern SaaS UX:</b> Design a responsive dark-themed dashboard featuring real-time health indicators, interactive editors, SQLite persistence, and multi-format exports.", bullet_style))
    story.append(PageBreak())

    # ==========================================
    # PAGE 3: LITERATURE REVIEW & THEORETICAL FOUNDATIONS
    # ==========================================
    story.append(Paragraph("2. Theoretical Foundations & Domain Background", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.8, color=c_accent, spaceBefore=2, spaceAfter=10))

    story.append(Paragraph("<b>2.1 Entertainment Psychology & Viral Dynamics</b>", h2_style))
    story.append(Paragraph(
        "In entertainment copywriting, audience attention spans are measured in milliseconds. Cognitive engagement follows "
        "distinct retention curves depending on medium modality:",
        body_style
    ))
    story.append(Paragraph("• <b>Short-Form Video (Reels & Shorts):</b> Operates on a 3-second cognitive hook window. If audio/visual pacing does not generate immediate narrative tension, drop-off exceeds 65%. Scripts must integrate audio cues and visual camera actions.", bullet_style))
    story.append(Paragraph("• <b>Micro-Blogging (X):</b> Engagement correlates with punchy syntactical structure and curiosity gaps. Standalone posts must deliver impact within 280 characters, while threads require structured numbering (`1/`, `2/`).", bullet_style))
    story.append(Paragraph("• <b>Professional Networks (LinkedIn):</b> Entertainment topics succeed when transformed into transferable paradigms—such as crisis management lessons from movie set catastrophes or marketing ROI breakdowns.", bullet_style))

    story.append(Paragraph("<b>2.2 NVIDIA Nemotron Architecture</b>", h2_style))
    story.append(Paragraph(
        "The NVIDIA Nemotron family represents specialized Large Language Models optimized for enterprise instruction following, "
        "complex reasoning, and high throughput inference hosted on NVIDIA accelerated compute clusters. The primary model utilized, "
        "<b>Nemotron-3.5-Lightning-30B</b>, exhibits high linguistic comprehension across multilingual and code-switched vocabularies, "
        "making it ideal for the nuanced demands of entertainment marketing.",
        body_style
    ))

    story.append(Paragraph("<b>2.3 Code-Switching & Linguistic Resonance</b>", h2_style))
    story.append(Paragraph(
        "A critical innovation of this project is native support for three linguistic paradigms:",
        body_style
    ))
    story.append(Paragraph("1. <b>English:</b> Global standard, polished entertainment phrasing, cinematic idioms.", bullet_style))
    story.append(Paragraph("2. <b>Hindi (हिंदी Devanagari):</b> Culturally immersive, emotive dialogues, authentic regional film resonance.", bullet_style))
    story.append(Paragraph("3. <b>Hinglish (Roman Script):</b> Natural urban conversational Hindi-English blend widely used across Mumbai film circuits, Gen-Z creators, and digital influencers.", bullet_style))

    # Linguistic Matrix Table
    ling_matrix = [
        ["Language", "Target Script", "Psychological Profile", "Sample Use Case"],
        ["English", "Latin", "Global, Authoritative, Cinematic", "Hollywood Reviews, LinkedIn Leadership"],
        ["Hindi", "Devanagari", "Deep Emotional Resonance, Cultural", "Bollywood Trailers, Regional TV Drama"],
        ["Hinglish", "Roman / Hybrid", "Relatable, Youth, Conversational", "Stand-Up Comedy, Instagram Reels, X Memes"]
    ]
    t_ling = Table(ling_matrix, colWidths=[65, 80, 175, 184])
    t_ling.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#312e81")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 7.5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t_ling)
    story.append(PageBreak())

    # ==========================================
    # PAGE 4: SYSTEM ARCHITECTURE & DATA FLOW
    # ==========================================
    story.append(Paragraph("3. System Architecture & Technical Specifications", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.8, color=c_accent, spaceBefore=2, spaceAfter=10))

    story.append(Paragraph("<b>3.1 High-Level Architectural Diagram</b>", h2_style))
    story.append(Paragraph(
        "The system follows a decoupled, asynchronous client-server architecture designed for high scalability, "
        "low latency, and reliable fault tolerance:",
        body_style
    ))

    arch_table_data = [
        ["Layer", "Component", "Technology", "Functional Responsibility"],
        ["Presentation", "Web Client SPA", "React 18, Vite 5, Tailwind CSS", "User interface, platform cards, state management, client validation"],
        ["Networking", "REST Client", "Axios (HTTP/JSON)", "Asynchronous transmission, timeout handling, error boundary hooks"],
        ["Application", "API Gateway", "FastAPI, Uvicorn", "Route handling, CORS middleware, Pydantic schema validation"],
        ["Intelligence", "Prompt Engine", "PromptBuilder (Python)", "Context injection, platform role definition, structural JSON schemas"],
        ["Inference", "NIM Service", "NVIDIA Nemotron 30B LLM", "Remote high-speed inference, fallback routing, reasoning parse"],
        ["Validation", "Rule Engine", "ContentValidator (Python)", "Constraint checks, character counting, keyword audit, retry loop"],
        ["Persistence", "Database Layer", "SQLite, SQLAlchemy ORM", "Generation vault, timestamped auditing, CRUD endpoints"]
    ]
    t_arch = Table(arch_table_data, colWidths=[65, 80, 110, 249])
    t_arch.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e1b4b")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 7.5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t_arch)
    story.append(Spacer(1, 10))

    story.append(Paragraph("<b>3.2 Data Flow Pipeline</b>", h2_style))
    story.append(Paragraph(
        "1. <b>Input Ingestion:</b> The user submits the creative brief (topic, description, platforms, language, tone, length, keywords, custom instructions).<br/>"
        "2. <b>Request Sanitization:</b> FastAPI validates the incoming JSON against <code>GenerateRequest</code> Pydantic schema.<br/>"
        "3. <b>Parallel Orchestration:</b> <code>ContentGenerator.generate_all()</code> fans out calls per selected platform.<br/>"
        "4. <b>Dynamic Prompt Synthesis:</b> <code>PromptBuilder</code> creates targeted system instructions and structural constraints.<br/>"
        "5. <b>NVIDIA NIM Call:</b> <code>NvidiaService</code> executes completions over HTTPS against NVIDIA's OpenAI-compliant endpoint.<br/>"
        "6. <b>Response Extraction:</b> Robust string slicing parses the structured JSON payload, bypassing CoT (Chain of Thought) reasoning tags.<br/>"
        "7. <b>Rule Audit & Retry:</b> <code>ContentValidator</code> checks character limits. If broken, 1 controlled rewrite is invoked.<br/>"
        "8. <b>Storage & Return:</b> SQLAlchemy persists the run into SQLite database, and the response is returned to the frontend.",
        body_style
    ))
    story.append(PageBreak())

    # ==========================================
    # PAGE 5: PLATFORM ENGINES & PROMPT ARCHITECTURE
    # ==========================================
    story.append(Paragraph("4. Platform Engines & Prompt Architecture", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.8, color=c_accent, spaceBefore=2, spaceAfter=10))

    story.append(Paragraph("<b>4.1 Platform Rule Matrix</b>", h2_style))
    story.append(Paragraph(
        "To ensure compliance with real-world social media constraints, platform specifications are defined in a centralized Python dictionary:",
        body_style
    ))

    plat_rules = [
        ["Platform", "Char Cap", "Word Range", "Required Components", "Algorithmic Focus"],
        ["Instagram", "2,200", "60 – 350", "Hook, Visual Caption, CTA, Hashtags", "Visual curiosity, emoji spacing, Reel audio cues"],
        ["YouTube", "5,000", "250 – 1,200", "Catchy Title, Scene Breakdown, CTA", "High Click-Through Rate (<70ch title), Retention"],
        ["YouTube Shorts", "1,000", "40 – 220", "3-Sec Hook, Fast Narration, Loop", "9:16 vertical fast cuts, audio triggers, seamless loop"],
        ["Facebook", "5,000", "80 – 500", "Narrative Post, Discussion Starter", "Community discussion, relatable storytelling"],
        ["X (Twitter)", "280 (Post)", "10 – 80", "Punchline Post or 1/N Thread", "Strict brevity (<280ch), wit, single/double hashtag"],
        ["LinkedIn", "3,000", "120 – 600", "Headline, 3 Key Lessons, Debate CTA", "Professional industry insights, leadership lessons"]
    ]
    t_plat = Table(plat_rules, colWidths=[75, 55, 65, 150, 159])
    t_plat.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e1b4b")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 7.5),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 7),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t_plat)
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>4.2 Concrete Implementation: PromptBuilder</b>", h2_style))
    story.append(Paragraph(
        "The following Python excerpt illustrates how distinct system instructions and JSON structural constraints "
        "are assembled dynamically to prevent generic output generation:",
        body_style
    ))

    code_snippet_1 = (
        "class PromptBuilder:\n"
        "    @staticmethod\n"
        "    def get_system_prompt(platform: str, language: str, tone: str) -> str:\n"
        "        base = f\"You are a world-class entertainment copywriter for {platform.upper()}.\n"
        "                Target Language: {language}. Requested Tone: {tone}.\\n\"\n"
        "        instructions = {\n"
        "            'x': 'Keep strictly under 280 characters with maximum wit, or clean 1/N thread.',\n"
        "            'youtube_shorts': 'Explosive 3-second hook, vertical 9:16 pacing, seamless loop.',\n"
        "            'linkedin': 'Translate entertainment topics into creative leadership insights.'\n"
        "        }\n"
        "        return f\"{base}\\n{instructions.get(platform, '')}\\nStrictly return valid JSON.\""
    )
    story.append(Paragraph(code_snippet_1.replace("\n", "<br/>").replace(" ", "&nbsp;"), code_style))
    story.append(PageBreak())

    # ==========================================
    # PAGE 6: CONTENT VALIDATION & SELF-HEALING ENGINE
    # ==========================================
    story.append(Paragraph("5. Content Validation & Safe AI Self-Healing Engine", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.8, color=c_accent, spaceBefore=2, spaceAfter=10))

    story.append(Paragraph("<b>5.1 The Need for Deterministic Validation</b>", h2_style))
    story.append(Paragraph(
        "While Large Language Models exhibit high creative fluidity, their stochastic nature often leads to constraint "
        "violations (e.g., generating 310 characters when instructed to remain under 280, or omitting mandatory sponsor keywords). "
        "OmniContent AI implements a hybrid deterministic-probabilistic architecture: Python code deterministically audits the LLM output, "
        "and triggers a secondary controlled AI self-healing cycle if hard platform rules are violated.",
        body_style
    ))

    story.append(Paragraph("<b>5.2 Multi-Stage Audit Criteria</b>", h2_style))
    story.append(Paragraph("1. <b>Character Limit Enforcement:</b> Evaluates raw string length. On platform 'X', non-threaded posts > 280 characters are flagged as invalid.", bullet_style))
    story.append(Paragraph("2. <b>Structural Section Audit:</b> Verifies the presence of required semantic elements: Catchy Title (YouTube), Retention Hook (Shorts), Call-to-Action (all platforms), and Hashtags.", bullet_style))
    story.append(Paragraph("3. <b>Mandatory Keyword Verification:</b> Case-insensitive substring verification confirms that user-requested keywords are explicitly present in the body copy.", bullet_style))
    story.append(Paragraph("4. <b>Hashtag Ceiling Protection:</b> Flags instances where hashtag counts exceed recommended thresholds (preventing algorithmic shadowbanning).", bullet_style))

    story.append(Paragraph("<b>5.3 Controlled AI Self-Healing Cycle</b>", h2_style))
    story.append(Paragraph(
        "To prevent runaway execution costs or infinite regeneration loops, the system enforces a strict <b>Max-1 Rewrite Policy</b>:",
        body_style
    ))

    code_snippet_2 = (
        "# Excerpt from content_generator.py\n"
        "is_valid, warnings, stats = ContentValidator.validate(platform, content_dict, requested_keywords=keywords)\n\n"
        "if not is_valid and nvidia_service.is_configured():\n"
        "    logger.info(f'Constraint violated for {platform}. Executing 1 controlled rewrite...')\n"
        "    rewrite_prompt = PromptBuilder.get_rewrite_prompt(\n"
        "        platform, topic, content_dict.get('main_content'),\n"
        "        instruction=f'Violations: {\"; \".join(warnings)}. Rewrite strictly respecting limits.'\n"
        "    )\n"
        "    rewritten_res = nvidia_service.chat_completion(system_prompt, rewrite_prompt, temperature=0.5)\n"
        "    # Re-audit new response deterministically\n"
        "    is_valid, warnings, stats = ContentValidator.validate(platform, rewritten_res['data'])"
    )
    story.append(Paragraph(code_snippet_2.replace("\n", "<br/>").replace(" ", "&nbsp;"), code_style))

    story.append(Paragraph("<b>5.4 Responsible AI Framework</b>", h2_style))
    story.append(Paragraph("• <b>No False Virality Claims:</b> The platform delivers educational feedback warnings rather than misleading claims of guaranteed engagement.", bullet_style))
    story.append(Paragraph("• <b>Human-in-the-Loop Governance:</b> Outputs are designed for human review, editing, and publishing; direct autonomous social posting is explicitly avoided.", bullet_style))
    story.append(PageBreak())

    # ==========================================
    # PAGE 7: DATABASE PERSISTENCE & HISTORY MANAGEMENT
    # ==========================================
    story.append(Paragraph("6. Database Persistence & History Management", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.8, color=c_accent, spaceBefore=2, spaceAfter=10))

    story.append(Paragraph("<b>6.1 Relational Data Model</b>", h2_style))
    story.append(Paragraph(
        "Content generation sessions, parameters, and generated platform dictionaries are automatically persisted "
        "to a local SQLite database utilizing SQLAlchemy ORM. The relational model is defined below:",
        body_style
    ))

    db_schema = [
        ["Field Name", "Data Type", "Constraints", "Description"],
        ["id", "Integer", "Primary Key, Auto-increment", "Unique identifier for each generation run"],
        ["topic", "String(500)", "Indexed, Non-nullable", "Core entertainment subject or story concept"],
        ["description", "Text", "Nullable", "Optional background context, character notes, plot points"],
        ["selected_platforms", "JSON", "Non-nullable", "Array of selected platforms e.g. ['instagram', 'youtube']"],
        ["target_audience", "String(200)", "Nullable", "Intended demographic (e.g. 'Marvel Cinema Fans')"],
        ["language", "String(50)", "Non-nullable, Default: English", "English, Hindi (Devanagari), or Hinglish"],
        ["tone", "String(50)", "Non-nullable", "Selected emotional mood (Funny, Suspense, Dramatic, etc.)"],
        ["content_type", "String(100)", "Non-nullable", "Selected format (Post, Script, Reel Hook, Thread)"],
        ["length", "String(50)", "Non-nullable", "Short, Medium, or Long"],
        ["keywords", "JSON", "Nullable", "List of target keywords to embed"],
        ["results", "JSON", "Non-nullable", "Dictionary storing all platform outputs, stats, and warnings"],
        ["created_at", "DateTime", "Default: UTC Now", "Timestamp of generation creation"]
    ]
    t_db = Table(db_schema, colWidths=[80, 75, 120, 229])
    t_db.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e1b4b")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 7.5),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 7),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
    ]))
    story.append(t_db)
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>6.2 Vault Management & REST Endpoints</b>", h2_style))
    story.append(Paragraph(
        "The system exposes dedicated REST endpoints ensuring full CRUD (Create, Read, Update, Delete) capability:",
        body_style
    ))
    story.append(Paragraph("• <code>GET /api/history</code>: Retrieves paginated generation history ordered chronologically.", bullet_style))
    story.append(Paragraph("• <code>GET /api/history/{id}</code>: Loads complete parameters and result sets for a previous run into the active Studio.", bullet_style))
    story.append(Paragraph("• <code>DELETE /api/history/{id}</code>: Removes an individual generation record from the persistent SQLite database.", bullet_style))
    story.append(Paragraph("• <code>POST /api/regenerate</code>: Re-runs AI synthesis for a single platform while preserving existing outputs for others.", bullet_style))
    story.append(PageBreak())

    # ==========================================
    # PAGE 8: FRONTEND USER INTERFACE & EXPERIENCE
    # ==========================================
    story.append(Paragraph("7. Frontend User Interface & Experience Design", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.8, color=c_accent, spaceBefore=2, spaceAfter=10))

    story.append(Paragraph("<b>7.1 UI/UX Philosophy</b>", h2_style))
    story.append(Paragraph(
        "The frontend is engineered as a creative entertainment studio rather than a standard corporate form. "
        "Styled using Tailwind CSS with custom glassmorphism and ambient purple/cyan glows, the interface emphasizes "
        "visual hierarchy, clear feedback states, and efficient creator workflows.",
        body_style
    ))

    story.append(Paragraph("<b>7.2 Core Views and Components</b>", h2_style))
    story.append(Paragraph("1. <b>Navigation Bar (<code>Navbar.jsx</code>):</b> Displays the brand logo, live view switchers (Studio, Vault, Overview), and an automated backend health badge indicating real-time NVIDIA NIM connectivity.", bullet_style))
    story.append(Paragraph("2. <b>Landing Showcase (<code>LandingPage.jsx</code>):</b> Explains the 'One Topic → 6 Outputs' concept, displays supported platform cards, highlights core architecture, and presents a side-by-side demonstration.", bullet_style))
    story.append(Paragraph("3. <b>Creative Studio (<code>GeneratorForm.jsx</code>):</b> Intuitive configuration panel with multi-platform interactive toggles, language dropdowns, 9 emotional tone selectors, format pickers, and keyword inputs.", bullet_style))
    story.append(Paragraph("4. <b>Results Workspace (<code>ResultsView.jsx</code> & <code>PlatformCard.jsx</code>):</b> Platform cards displaying titles, retention hooks, main scripts, CTAs, hashtags, character counts, and validation badges.", bullet_style))
    story.append(Paragraph("5. <b>Content Vault (<code>HistoryVault.jsx</code>):</b> Searchable, filterable repository of past generations with instant reload, review, and deletion options.", bullet_style))

    story.append(Paragraph("<b>7.3 Creator Interaction Capabilities</b>", h2_style))
    story.append(Paragraph("• <b>One-Click Copy & Batch Export:</b> Instant clipboard copy per platform or unified multi-platform <code>.TXT</code> dossier export.", bullet_style))
    story.append(Paragraph("• <b>In-Place Quick Editor:</b> Directly edit text inside any platform card with persistent word/character recalculation.", bullet_style))
    story.append(Paragraph("• <b>AI Refine Modal:</b> Targeted AI modifications (e.g. 'Make it funnier', 'Make it shorter', 'Convert to Hinglish') without regenerating unrelated platforms.", bullet_style))
    story.append(Paragraph("• <b>Granular Regeneration:</b> Re-generate a single network card without losing content created for other networks.", bullet_style))
    story.append(PageBreak())

    # ==========================================
    # PAGE 9: TESTING, VERIFICATION & LIVE RESULTS
    # ==========================================
    story.append(Paragraph("8. Testing, Verification & Experimental Results", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.8, color=c_accent, spaceBefore=2, spaceAfter=10))

    story.append(Paragraph("<b>8.1 Automated Test Suite Execution</b>", h2_style))
    story.append(Paragraph(
        "A formal pytest test suite (<code>backend/test_app.py</code>) validates all application components. "
        "Test categories and verification statuses are detailed below:",
        body_style
    ))

    test_results = [
        ["Test Module", "Target Functionality", "Input Scenario", "Outcome"],
        ["test_health_check", "API Health & Diagnostics", "GET /api/health", "PASSED (200 OK, Model Identified)"],
        ["test_get_config", "Platform Configuration", "GET /api/config", "PASSED (6 Platforms, Rules Loaded)"],
        ["test_validator_counts", "Character & Word Counters", "Standard string verification", "PASSED (Exact length verified)"],
        ["test_validator_limits", "Platform Limit Enforcement", "X post > 350 characters", "PASSED (Flagged invalid, warning issued)"],
        ["test_validator_sections", "Required Section Audit", "Missing Shorts hook and CTA", "PASSED (Correct missing warnings)"],
        ["test_prompt_builder", "Dynamic Prompt Synthesis", "Hindi + Funny Instagram prompt", "PASSED (Language & tone injected)"],
        ["test_workflow", "End-to-End Generation & DB", "Generate -> Save -> Query -> Delete", "PASSED (Clean database rollback)"],
        ["test_multilingual", "Hinglish & Comedic Output", "Hinglish open-mic comedy topic", "PASSED (Authentic slang & formatting)"]
    ]
    t_test = Table(test_results, colWidths=[90, 110, 150, 154])
    t_test.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e1b4b")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 7.5),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 7),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t_test)
    story.append(Spacer(1, 10))

    story.append(Paragraph("<b>8.2 Live NVIDIA NIM Verification</b>", h2_style))
    story.append(Paragraph(
        "Live network inference tests confirmed connectivity with NVIDIA NIM API. When evaluated against the test prompt "
        "<i>'A detective who can hear what inanimate objects witnessed at a movie theatre crime scene'</i>, the engine delivered:",
        body_style
    ))
    story.append(Paragraph("• <b>Instagram:</b> Generated title <i>'The Silent Witness Speaks'</i>, hook <i>'The popcorn whispered secrets...'</i>, with visual staging and 14 relevant cinema hashtags.", bullet_style))
    story.append(Paragraph("• <b>X (Twitter):</b> Evaluated at exactly 250 characters (strictly respecting the 280-char ceiling): <i>'He doesn't need a confession. The movie theatre—every creak, every projector flicker—holds a perfect, silent witness...'</i>", bullet_style))
    story.append(Paragraph("• <b>YouTube Shorts:</b> Generated high-energy vertical script with visual hook: <i>'The popcorn wasn't just a snack; it held the truth. Can he hear the crime?'</i>", bullet_style))
    story.append(PageBreak())

    # ==========================================
    # PAGE 10: CONCLUSION, LIMITATIONS & FUTURE ROADMAP
    # ==========================================
    story.append(Paragraph("9. Conclusion, Limitations & Future Roadmap", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.8, color=c_accent, spaceBefore=2, spaceAfter=10))

    story.append(Paragraph("<b>9.1 Project Conclusion</b>", h2_style))
    story.append(Paragraph(
        "The <b>AI-Powered Smart Multi-Platform Content Generator (OmniContent AI)</b> successfully demonstrates that "
        "specialized prompt engineering combined with enterprise-grade NVIDIA LLMs can replace fragmented, manual social media "
        "marketing workflows. By decomposing one central entertainment narrative into six tailored platform assets with native "
        "character counts, retention hooks, and multilingual fluency, the platform significantly accelerates content production "
        "while maintaining high creative quality.",
        body_style
    ))

    story.append(Paragraph("<b>9.2 Current Limitations</b>", h2_style))
    story.append(Paragraph("• <b>API Latency:</b> Generating content for all 6 platforms in sequential order can incur 10–25 seconds of latency depending on model load and network transit.", bullet_style))
    story.append(Paragraph("• <b>Multimodal Absence:</b> The current architecture generates textual and structural copy; direct video rendering and raster image generation are outside current scope.", bullet_style))
    story.append(Paragraph("• <b>External Account Publishing:</b> The application outputs verified drafts; it does not directly trigger social platform publishing APIs (Meta Graph, X API v2).", bullet_style))

    story.append(Paragraph("<b>9.3 Future Roadmap</b>", h2_style))
    story.append(Paragraph("1. <b>Multimodal Asset Generation:</b> Integrate NVIDIA Edify or Stable Diffusion pipelines to generate automated carousel graphics and YouTube thumbnails matching the generated copy.", bullet_style))
    story.append(Paragraph("2. <b>Direct Social Media Publishing:</b> Implement OAuth2 connectors for Meta, X, and LinkedIn to allow one-click scheduling and direct distribution.", bullet_style))
    story.append(Paragraph("3. <b>Voiceover Synthesis:</b> Integrate ElevenLabs or NVIDIA Riva speech synthesis to produce scratch vocal audio for short-form video scripts.", bullet_style))
    story.append(Paragraph("4. <b>Dynamic Analytics Feedback Loop:</b> Connect post-publishing engagement analytics to fine-tune future prompt weights automatically.", bullet_style))

    story.append(Spacer(1, 15))
    story.append(Paragraph("<b>10. Project Sign-Off & Evaluator Endorsement</b>", h2_style))

    sign_data = [
        ["Prepared By:", "Verified & Approved By:"],
        ["\n\n__________________________________\nProject Student Team\nDate: 24th November 2026", 
         "\n\n__________________________________\nAcademic Guide / Project Evaluator\nDepartment of Computer Science"]
    ]
    t_sign = Table(sign_data, colWidths=[250, 254])
    t_sign.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 8.5),
        ('TEXTCOLOR', (0, 0), (-1, -1), c_body),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_sign)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated {filename}")

if __name__ == "__main__":
    out_pdf = "Project_Report_OmniContent_AI.pdf"
    if len(sys.argv) > 1:
        out_pdf = sys.argv[1]
    build_pdf(out_pdf)

