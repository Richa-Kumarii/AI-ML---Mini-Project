"""
Create Two_Projects_Professional_Presentation.pptx
20 slides: Slides 1-10 = GlitchLab, Slides 11-20 = Style Avenue (Myntra Clone)
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import copy

prs = Presentation()
prs.slide_width  = Inches(13.33)
prs.slide_height = Inches(7.5)

# ─── COLOUR PALETTES ───────────────────────────────────────────────────────────
# Section A – GlitchLab  (deep purple / neon accent)
GA_BG      = RGBColor(0x0D, 0x09, 0x18)   # very dark purple
GA_HDR     = RGBColor(0x17, 0x10, 0x27)   # dark purple header
GA_ACCENT  = RGBColor(0xC7, 0x7D, 0xFF)   # lavender / violet
GA_ACCENT2 = RGBColor(0xFF, 0xD1, 0x66)   # gold
GA_WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
GA_LIGHT   = RGBColor(0xE0, 0xAA, 0xFF)   # soft purple text
GA_CARD    = RGBColor(0x21, 0x18, 0x2F)   # card bg

# Section B – Style Avenue (clean fashion / white & rose)
SB_BG      = RGBColor(0xFF, 0xFF, 0xFF)   # white
SB_HDR     = RGBColor(0x1A, 0x1A, 0x2E)   # very dark navy
SB_ACCENT  = RGBColor(0xE9, 0x4F, 0x78)   # rose / magenta
SB_ACCENT2 = RGBColor(0xF5, 0xF0, 0xE8)   # cream
SB_TEXT    = RGBColor(0x1A, 0x1A, 0x2E)   # dark navy text
SB_CARD    = RGBColor(0xF9, 0xF5, 0xF0)   # card bg
SB_GRAY    = RGBColor(0x55, 0x55, 0x66)   # secondary text

# ─── HELPERS ───────────────────────────────────────────────────────────────────

def add_rect(slide, l, t, w, h, fill, alpha=None):
    shape = slide.shapes.add_shape(1, Inches(l), Inches(t), Inches(w), Inches(h))
    shape.line.fill.background()
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    return shape

def add_text(slide, text, l, t, w, h,
             size=18, bold=False, color=RGBColor(0xFF,0xFF,0xFF),
             align=PP_ALIGN.LEFT, italic=False, font_name="Calibri"):
    txBox = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    run.font.name = font_name
    return txBox

def add_text_multiline(slide, lines, l, t, w, h,
                        size=16, color=RGBColor(0xFF,0xFF,0xFF),
                        align=PP_ALIGN.LEFT, font_name="Calibri",
                        bold=False, line_spacing=None):
    """lines: list of (text, bold, size, color) or just str"""
    txBox = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = txBox.text_frame
    tf.word_wrap = True
    first = True
    for line in lines:
        if isinstance(line, str):
            txt, b, s, c = line, bold, size, color
        else:
            txt, b, s, c = line
        if first:
            p = tf.paragraphs[0]
            first = False
        else:
            p = tf.add_paragraph()
        p.alignment = align
        if line_spacing:
            p.space_before = Pt(line_spacing)
        run = p.add_run()
        run.text = txt
        run.font.size = Pt(s)
        run.font.bold = b
        run.font.color.rgb = c
        run.font.name = font_name
    return txBox

def slide_header_A(slide, slide_num):
    """GlitchLab dark header bar"""
    add_rect(slide, 0, 0, 13.33, 7.5, GA_BG)            # full bg
    add_rect(slide, 0, 0, 13.33, 1.1, GA_HDR)            # header strip
    add_rect(slide, 0, 0, 0.35, 1.1, GA_ACCENT)          # left accent bar
    add_text(slide, "GLITCHLAB®", 0.5, 0.2, 3, 0.65,
             size=22, bold=True, color=GA_WHITE, font_name="Georgia")
    add_text(slide, f"Slide {slide_num}  |  PROJECT 1 — GlitchLab",
             4.5, 0.25, 8.5, 0.6, size=11,
             color=GA_ACCENT2, align=PP_ALIGN.RIGHT)

def slide_header_B(slide, slide_num):
    """Style Avenue light header bar"""
    add_rect(slide, 0, 0, 13.33, 7.5, SB_BG)
    add_rect(slide, 0, 0, 13.33, 1.1, SB_HDR)
    add_rect(slide, 0, 0, 0.35, 1.1, SB_ACCENT)
    add_text(slide, "STYLE AVENUE", 0.5, 0.2, 4, 0.65,
             size=22, bold=True, color=RGBColor(0xFF,0xFF,0xFF), font_name="Calibri")
    add_text(slide, f"Slide {slide_num}  |  PROJECT 2 — Style Avenue",
             4.5, 0.25, 8.5, 0.6, size=11,
             color=SB_ACCENT, align=PP_ALIGN.RIGHT)

def footer_A(slide):
    add_rect(slide, 0, 7.15, 13.33, 0.35, GA_HDR)
    add_text(slide, "GlitchLab — A Multi-Theme Creative Web Experiment  |  HTML · CSS · JavaScript",
             0.3, 7.17, 13, 0.3, size=9, color=GA_ACCENT2, align=PP_ALIGN.CENTER)

def footer_B(slide):
    add_rect(slide, 0, 7.15, 13.33, 0.35, SB_HDR)
    add_text(slide, "Style Avenue — Myntra-Inspired Fashion Store  |  HTML · CSS · Bootstrap · JavaScript",
             0.3, 7.17, 13, 0.3, size=9, color=SB_ACCENT, align=PP_ALIGN.CENTER)

def divider_A(slide, t=1.15):
    add_rect(slide, 0.5, t, 12.33, 0.04, GA_ACCENT)

def divider_B(slide, t=1.15):
    add_rect(slide, 0.5, t, 12.33, 0.04, SB_ACCENT)

def card_A(slide, l, t, w, h, title, body_lines):
    add_rect(slide, l, t, w, h, GA_CARD)
    # accent top bar
    add_rect(slide, l, t, w, 0.06, GA_ACCENT)
    add_text(slide, title, l+0.15, t+0.1, w-0.3, 0.45,
             size=14, bold=True, color=GA_ACCENT)
    add_text_multiline(slide, body_lines, l+0.15, t+0.55, w-0.3, h-0.7,
                        size=12, color=GA_LIGHT)

def card_B(slide, l, t, w, h, title, body_lines):
    add_rect(slide, l, t, w, h, SB_CARD)
    add_rect(slide, l, t, w, 0.06, SB_ACCENT)
    add_text(slide, title, l+0.15, t+0.1, w-0.3, 0.45,
             size=14, bold=True, color=SB_ACCENT)
    add_text_multiline(slide, body_lines, l+0.15, t+0.55, w-0.3, h-0.7,
                        size=12, color=SB_TEXT)

def add_bullet_A(slide, bullets, l, t, w, h, size=14):
    lines = []
    for b in bullets:
        if isinstance(b, tuple):
            lines.append(("▸  " + b[0], b[1] if len(b)>1 else False, b[2] if len(b)>2 else size, b[3] if len(b)>3 else GA_WHITE))
        else:
            lines.append(("▸  " + b, False, size, GA_WHITE))
    add_text_multiline(slide, lines, l, t, w, h, size=size, color=GA_WHITE, line_spacing=4)

def add_bullet_B(slide, bullets, l, t, w, h, size=14):
    lines = []
    for b in bullets:
        if isinstance(b, tuple):
            lines.append(("▸  " + b[0], b[1] if len(b)>1 else False, b[2] if len(b)>2 else size, b[3] if len(b)>3 else SB_TEXT))
        else:
            lines.append(("▸  " + b, False, size, SB_TEXT))
    add_text_multiline(slide, lines, l, t, w, h, size=size, color=SB_TEXT, line_spacing=4)

def add_notes(slide, text):
    notes_slide = slide.notes_slide
    tf = notes_slide.notes_text_frame
    tf.text = text

def new_slide(prs):
    blank_layout = prs.slide_layouts[6]  # completely blank
    return prs.slides.add_slide(blank_layout)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION A — GlitchLab  (Slides 1–10)
# ═══════════════════════════════════════════════════════════════════════════════

# ─── SLIDE 1 ── Project Title & Introduction ──────────────────────────────────
sl = new_slide(prs)
slide_header_A(sl, 1)
divider_A(sl)

# Hero title area
add_rect(sl, 0.5, 1.3, 7.8, 4.5, GA_CARD)
add_rect(sl, 0.5, 1.3, 0.1, 4.5, GA_ACCENT)

add_text(sl, "PROJECT 1", 0.75, 1.4, 5, 0.5, size=11, color=GA_ACCENT2, bold=True)
add_text(sl, "GlitchLab®", 0.75, 1.9, 7, 1.0, size=52, bold=True, color=GA_WHITE, font_name="Georgia")
add_text(sl, "Explore Your Style", 0.75, 2.95, 7, 0.6, size=24, italic=True, color=GA_LIGHT, font_name="Georgia")

add_text_multiline(sl, [
    ("A Creative Multi-Theme Web Experiment", False, 15, GA_ACCENT2),
    ("", False, 8, GA_WHITE),
    ("GlitchLab is a front-end web project that lets users", False, 13, GA_WHITE),
    ("explore three completely different visual design themes:", False, 13, GA_WHITE),
    ("Minimal, Retro, and Glitch — each with its own", False, 13, GA_WHITE),
    ("personality, colour palette, and layout style.", False, 13, GA_WHITE),
    ("", False, 8, GA_WHITE),
    ("Built using:  HTML  ·  CSS  ·  JavaScript", False, 13, GA_ACCENT),
    ("Total Files:  4 HTML  ·  1 CSS  ·  1 JavaScript", False, 13, GA_ACCENT),
], 0.75, 3.6, 7.3, 2.1)

# Right panel — theme cards
add_rect(sl, 8.6, 1.3, 4.3, 1.4, RGBColor(0xE9, 0xE8, 0xDD))
add_rect(sl, 8.6, 1.3, 0.08, 1.4, RGBColor(0x34, 0x4E, 0x41))
add_text(sl, "01 / MINIMAL", 8.75, 1.35, 4, 0.3, size=10, color=RGBColor(0x34,0x4E,0x41), bold=True)
add_text(sl, "Less noise. More meaning.", 8.75, 1.65, 4, 0.5, size=13, color=RGBColor(0x34,0x4E,0x41))

add_rect(sl, 8.6, 2.85, 4.3, 1.4, RGBColor(0xFF, 0xD4, 0xB2))
add_rect(sl, 8.6, 2.85, 0.08, 1.4, RGBColor(0x54, 0x23, 0x44))
add_text(sl, "02 / RETRO", 8.75, 2.9, 4, 0.3, size=10, color=RGBColor(0x54,0x23,0x44), bold=True)
add_text(sl, "Old-school soul. Bold energy.", 8.75, 3.2, 4, 0.5, size=13, color=RGBColor(0x54,0x23,0x44))

add_rect(sl, 8.6, 4.4, 4.3, 1.4, GA_CARD)
add_rect(sl, 8.6, 4.4, 0.08, 1.4, GA_ACCENT)
add_text(sl, "03 / GLITCH", 8.75, 4.45, 4, 0.3, size=10, color=GA_ACCENT, bold=True)
add_text(sl, "Break patterns. Make waves.", 8.75, 4.75, 4, 0.5, size=13, color=GA_WHITE)

footer_A(sl)
add_notes(sl, """SLIDE 1 — What to say:
"Good morning / afternoon sir/ma'am. I will be presenting two web development projects today. The first project is called GlitchLab."

What is GlitchLab?
- It is a creative website that has four pages in total.
- The home page (index.html) lets you choose between three design themes.
- The three themes are: Minimal (calm green design), Retro (warm vintage colours), and Glitch (neon cyber look).
- Each theme is a separate HTML page with its own look and feel.
- All themes share one CSS file (style.css) and one JavaScript file (script.js).

Technologies used: HTML, CSS, JavaScript — no frameworks or backend.

Possible teacher questions:
Q: What is the purpose of GlitchLab?
A: It is a creative front-end website that shows how the same website can look completely different using different themes and CSS styles.

Q: How many pages does GlitchLab have?
A: It has 4 main pages — index.html (Home), minimal.html, retro.html, and glitch.html. There are also older draft files in the folder.""")

# ─── SLIDE 2 ── Problem Statement & Objectives ───────────────────────────────
sl = new_slide(prs)
slide_header_A(sl, 2)
divider_A(sl)

add_text(sl, "Problem Statement & Project Objectives", 0.5, 1.25, 12.5, 0.6,
         size=26, bold=True, color=GA_WHITE)

# Left column
add_rect(sl, 0.5, 2.0, 5.9, 4.8, GA_CARD)
add_rect(sl, 0.5, 2.0, 5.9, 0.45, RGBColor(0x62, 0x42, 0x9B))
add_text(sl, "THE PROBLEM", 0.65, 2.05, 5.6, 0.35, size=13, bold=True, color=GA_ACCENT2)
add_bullet_A(sl, [
    "Beginners learning web development often build only plain, single-style websites",
    "They do not practise applying multiple CSS themes to the same project",
    "There is no hands-on way to understand how CSS classes control visual appearance",
    "Students miss the experience of connecting multiple HTML pages into one project",
    "Interactive JavaScript features are rarely explored in beginner projects",
], 0.65, 2.5, 5.6, 4.0, size=13)

# Right column
add_rect(sl, 6.7, 2.0, 6.0, 4.8, GA_CARD)
add_rect(sl, 6.7, 2.0, 6.0, 0.45, RGBColor(0x62, 0x42, 0x9B))
add_text(sl, "PROJECT OBJECTIVES", 6.85, 2.05, 5.7, 0.35, size=13, bold=True, color=GA_ACCENT2)
add_bullet_A(sl, [
    "Demonstrate how one CSS file can produce three completely different visual themes",
    "Build a multi-page website where all pages are linked and share the same CSS/JS",
    "Implement real JavaScript interactivity (theme toggle, colour palette, feedback form)",
    "Learn and apply CSS class-based theming using body class names",
    "Targeted at beginners and B.Tech students exploring front-end web development",
], 6.85, 2.5, 5.7, 4.0, size=13)

footer_A(sl)
add_notes(sl, """SLIDE 2 — What to say:
"The main idea behind GlitchLab was to solve a common beginner problem: most students only learn how to make one type of website. GlitchLab was built to show that by simply changing CSS classes, you can completely change how a website looks."

Key points to remember:
- The problem: Students don't explore multiple CSS themes in one project.
- The solution: GlitchLab uses a single style.css file with separate CSS sections for each theme.
- When a user opens minimal.html, the body has the class "minimal-theme" — this triggers the green/cream styling.
- When they open glitch.html, the body has class "glitch-theme" — which shows neon colours.

Intended users: B.Tech / engineering students learning HTML, CSS, and JavaScript.

Possible teacher questions:
Q: Why did you use multiple HTML files instead of one page with switching?
A: To keep the code simple and beginner-friendly. Each theme is a separate page with its own structure, which makes it easier to learn how theming works.

Q: Who is the target user of this project?
A: Students and beginners who want to explore different web design styles and CSS concepts.""")

# ─── SLIDE 3 ── Project Overview & Architecture ───────────────────────────────
sl = new_slide(prs)
slide_header_A(sl, 3)
divider_A(sl)

add_text(sl, "Project Overview & Architecture", 0.5, 1.25, 12.5, 0.6,
         size=26, bold=True, color=GA_WHITE)

# Architecture diagram
# Centre box — index.html
add_rect(sl, 5.2, 2.0, 2.9, 0.75, GA_ACCENT)
add_text(sl, "index.html (Home)", 5.25, 2.1, 2.8, 0.55, size=13, bold=True,
         color=GA_BG, align=PP_ALIGN.CENTER)

# Three theme boxes
theme_boxes = [
    (0.6,  3.4, RGBColor(0xE9,0xE8,0xDD), RGBColor(0x34,0x4E,0x41), "minimal.html\nMinimal Theme"),
    (5.2,  3.4, RGBColor(0xFF,0xD4,0xB2), RGBColor(0x54,0x23,0x44), "retro.html\nRetro Theme"),
    (9.9,  3.4, GA_CARD,                   GA_ACCENT,                 "glitch.html\nGlitch Theme"),
]
for lx, ty, bg, tc, label in theme_boxes:
    add_rect(sl, lx, ty, 2.9, 0.9, bg)
    add_text(sl, label, lx+0.1, ty+0.07, 2.7, 0.75, size=12, bold=True, color=tc, align=PP_ALIGN.CENTER)

# Shared resources box
add_rect(sl, 2.5, 5.0, 8.3, 0.75, RGBColor(0x17,0x10,0x27))
add_rect(sl, 2.5, 5.0, 8.3, 0.06, GA_ACCENT2)
add_text(sl, "SHARED RESOURCES:   style.css  (all themes)   +   script.js  (all interactions)",
         2.6, 5.1, 8.1, 0.55, size=13, color=GA_ACCENT2, align=PP_ALIGN.CENTER)

# Connecting arrows (vertical rectangles)
for x in [1.95, 6.6, 11.3]:
    add_rect(sl, x, 2.75, 0.07, 0.65, GA_ACCENT)
    add_rect(sl, x, 4.3, 0.07, 0.7, GA_ACCENT)

# Horizontal connector
add_rect(sl, 1.95, 2.75, 9.4, 0.07, GA_ACCENT)
add_rect(sl, 1.95, 4.3, 9.4, 0.07, GA_ACCENT)

# Labels
add_text(sl, "User clicks navigation link", 5.5, 3.1, 2.5, 0.3, size=10, color=GA_LIGHT, align=PP_ALIGN.CENTER)
add_text(sl, "Arrow = navigation links between pages", 4.5, 4.9, 4, 0.3, size=9, color=GA_LIGHT, align=PP_ALIGN.CENTER)

# Right-side explanation
add_rect(sl, 0.5, 2.0, 4.5, 1.1, GA_CARD)
add_text(sl, "How it works:", 0.65, 2.05, 4.2, 0.35, size=12, bold=True, color=GA_ACCENT)
add_text(sl, "Home page has 3 cards linking to each theme page. Each theme page applies a different CSS class to its body tag.", 0.65, 2.4, 4.2, 0.65, size=11, color=GA_WHITE)

add_rect(sl, 8.8, 2.0, 4.5, 1.1, GA_CARD)
add_text(sl, "CSS Theme System:", 8.95, 2.05, 4.2, 0.35, size=12, bold=True, color=GA_ACCENT)
add_text(sl, 'body class="minimal-theme" → green design\nbody class="retro-theme" → warm vintage\nbody class="glitch-theme" → neon dark', 8.95, 2.4, 4.2, 0.65, size=11, color=GA_LIGHT)

footer_A(sl)
add_notes(sl, """SLIDE 3 — What to say:
"Let me explain how GlitchLab is structured. The home page (index.html) is like the entry point. It shows three cards — Minimal, Retro, and Glitch. When a user clicks a card, it takes them to a separate HTML page for that theme."

Architecture explanation:
- index.html = main hub page
- minimal.html, retro.html, glitch.html = three separate theme pages
- ALL four pages use the SAME style.css and script.js file
- The theme difference comes from the CSS class on the body tag
  - body class="minimal-theme" → activates minimal green colours
  - body class="retro-theme" → activates vintage warm colours
  - body class="glitch-theme" → activates neon dark colours

Navigation: Each page has links to the other pages in the navbar.

Possible teacher questions:
Q: How does the same CSS file produce three different looks?
A: The CSS file has separate sections for each theme. The body class name controls which section is active. For example, .minimal-theme sets background to cream colour, while .glitch-theme sets it to dark navy.

Q: Can a user switch themes without reloading?
A: There is a theme toggle button on the home page that switches between light and dark mode using JavaScript. For the three big themes, the user navigates to a different HTML page.""")

# ─── SLIDE 4 ── Technologies & Tools Used ────────────────────────────────────
sl = new_slide(prs)
slide_header_A(sl, 4)
divider_A(sl)

add_text(sl, "Technologies & Tools Used", 0.5, 1.25, 12.5, 0.6,
         size=26, bold=True, color=GA_WHITE)

tech_data = [
    ("HTML5", GA_ACCENT, [
        "Provides the skeleton/structure of every page",
        "Uses semantic tags: <header>, <main>, <section>, <footer>, <nav>",
        "Links all pages together using <a href='...'>",
        "Contains the button and form elements for JS features",
        "4 HTML files: index, minimal, retro, glitch",
    ]),
    ("CSS3", RGBColor(0xFF,0xD1,0x66), [
        "Provides ALL styling — colours, fonts, layout, spacing",
        "Single shared file: style.css (701 lines)",
        "Uses CSS class selectors to control each theme",
        "Implements Flexbox layout for card grids",
        "Uses CSS transitions for smooth theme colour change",
        "Fonts: Arial (body), Georgia (headings), Courier New (labels)",
    ]),
    ("JavaScript", RGBColor(0x00,0xF5,0xFF), [
        "Makes the website interactive (script.js — 86 lines)",
        "Theme Toggle: switches dark-mode class on body",
        "Read More / Read Less button for extra text",
        "Colour Palette Generator: picks 3 random hex colours",
        "Feedback Form: validates name & message, shows alert",
        "No libraries or frameworks used",
    ]),
]

for i, (tech, clr, pts) in enumerate(tech_data):
    lx = 0.5 + i * 4.3
    add_rect(sl, lx, 2.0, 4.1, 4.9, GA_CARD)
    add_rect(sl, lx, 2.0, 4.1, 0.55, clr)
    add_text(sl, tech, lx+0.15, 2.05, 3.8, 0.45, size=18, bold=True, color=GA_BG, align=PP_ALIGN.CENTER)
    for j, pt in enumerate(pts):
        add_text(sl, f"▸  {pt}", lx+0.15, 2.65 + j*0.72, 3.8, 0.65, size=12, color=GA_WHITE)

# bottom
add_rect(sl, 0.5, 7.0, 12.33, 0.08, GA_ACCENT)
add_text(sl, "Development Environment:  Any text editor (e.g. VS Code)  |  Browser to open HTML files  |  No server or installation required",
         0.5, 7.08, 12.33, 0.3, size=10, color=GA_ACCENT2, align=PP_ALIGN.CENTER)

footer_A(sl)
add_notes(sl, """SLIDE 4 — What to say:
"GlitchLab uses only three core web technologies: HTML, CSS, and JavaScript. There are no extra frameworks or libraries. This makes it a great beginner project."

HTML explanation:
- HTML creates the structure. It tells the browser where the header, navigation, sections, and footer are.
- Semantic tags like <header>, <section>, <footer> make the code readable and professional.

CSS explanation:
- CSS controls 100% of the visual appearance — colours, fonts, spacing, card layout.
- One CSS file (style.css) serves all four pages. The theme is controlled by which class is on the body tag.

JavaScript explanation:
- script.js handles three interactive features:
  1. Dark/Light theme toggle
  2. Random colour palette generator
  3. Feedback form validation

No backend: This is a pure front-end project. There is no database, server, or API.

Possible teacher questions:
Q: Why did you use only HTML, CSS, and JavaScript without any framework?
A: This is a learning project for beginners. Using plain HTML/CSS/JS helps understand fundamentals before moving to frameworks like React.

Q: What is the role of CSS transitions in this project?
A: The CSS file has 'transition: background-color 0.3s, color 0.3s' on the body, which makes the dark mode toggle look smooth instead of an abrupt colour change.""")

# ─── SLIDE 5 ── Project Structure & File Organization ─────────────────────────
sl = new_slide(prs)
slide_header_A(sl, 5)
divider_A(sl)

add_text(sl, "Project Structure & File Organization", 0.5, 1.25, 12.5, 0.6,
         size=26, bold=True, color=GA_WHITE)

# Left: folder tree visual
add_rect(sl, 0.5, 2.0, 5.5, 4.9, GA_CARD)
add_rect(sl, 0.5, 2.0, 5.5, 0.45, GA_ACCENT)
add_text(sl, "FOLDER STRUCTURE", 0.65, 2.05, 5.2, 0.35, size=13, bold=True, color=GA_BG)

folder_tree = [
    ("📁  GlitchLab/", True, 14, GA_ACCENT2),
    ("", False, 6, GA_WHITE),
    ("   📄  index.html", True, 13, GA_WHITE),
    ("         → Home page  |  entry point", False, 11, GA_LIGHT),
    ("   📄  minimal.html", True, 13, GA_WHITE),
    ("         → Minimal green theme page", False, 11, GA_LIGHT),
    ("   📄  retro.html", True, 13, GA_WHITE),
    ("         → Retro vintage theme page", False, 11, GA_LIGHT),
    ("   📄  glitch.html", True, 13, GA_WHITE),
    ("         → Neon dark theme page", False, 11, GA_LIGHT),
    ("   🎨  style.css", True, 13, GA_ACCENT2),
    ("         → ALL styling for ALL pages", False, 11, GA_LIGHT),
    ("   ⚙️  script.js", True, 13, GA_ACCENT2),
    ("         → ALL JavaScript interactions", False, 11, GA_LIGHT),
    ("   📁  dir_name/", True, 13, RGBColor(0x88,0x88,0x99)),
    ("         → Empty placeholder folder", False, 11, RGBColor(0x88,0x88,0x99)),
]
add_text_multiline(sl, folder_tree, 0.65, 2.5, 5.2, 4.3, size=13, color=GA_WHITE)

# Right: file descriptions
right_cards = [
    ("index.html  (4,515 bytes)", "The main landing page. Contains the hero section with the tagline, three world cards (Minimal / Retro / Glitch), interactive tools section with theme toggle, colour palette generator, and feedback form in the footer."),
    ("minimal.html / retro.html / glitch.html", "Three theme pages. Each has a hero section with an Unsplash image, three feature boxes explaining the theme philosophy, and a colour palette swatch section. Navigation links connect all pages."),
    ("style.css  (12,129 bytes  —  701 lines)", "One master stylesheet split into labelled sections: Universal, Common classes, Home theme, Minimal theme, Retro theme, Glitch theme, Common page content, Dark mode, Buttons, Forms, and Transitions."),
    ("script.js  (2,521 bytes  —  86 lines)", "Three JavaScript features: (1) Dark/light toggle, (2) Read More / Read Less button, (3) Random colour palette generator, (4) Feedback form validation with alert messages."),
]
for i, (title, body) in enumerate(right_cards):
    ty = 2.0 + i * 1.22
    add_rect(sl, 6.3, ty, 6.7, 1.1, GA_CARD)
    add_rect(sl, 6.3, ty, 0.07, 1.1, GA_ACCENT)
    add_text(sl, title, 6.5, ty+0.05, 6.4, 0.35, size=12, bold=True, color=GA_ACCENT)
    add_text(sl, body, 6.5, ty+0.4, 6.4, 0.65, size=11, color=GA_WHITE)

footer_A(sl)
add_notes(sl, """SLIDE 5 — What to say:
"GlitchLab has a very simple file structure. Everything is inside one folder called GlitchLab."

File descriptions:
- index.html: The home page. Users first see this page. It shows the logo, navigation, and three big cards to choose a theme.
- minimal.html, retro.html, glitch.html: The three theme pages. Each applies a CSS class to the body tag that changes the whole visual appearance.
- style.css: One single CSS file for ALL four pages. It is 701 lines long and organised into labelled sections for each theme.
- script.js: One JavaScript file, 86 lines, shared by all pages. It has four features: dark mode toggle, read more/less, colour palette, and form validation.
- dir_name: This is an empty folder, likely a leftover from development. It has no content.

Possible teacher questions:
Q: Why is there only one CSS file for all four pages?
A: This saves code. Instead of writing four separate CSS files, one file has all the styles organised by theme class names. Each page just uses a different body class name.

Q: What is the purpose of the dir_name folder?
A: It appears to be an empty placeholder folder left from development. It does not contain any files and does not affect the project.""")

# ─── SLIDE 6 ── Main Features & Functionalities ───────────────────────────────
sl = new_slide(prs)
slide_header_A(sl, 6)
divider_A(sl)

add_text(sl, "Main Features & Functionalities", 0.5, 1.25, 12.5, 0.6,
         size=26, bold=True, color=GA_WHITE)

features = [
    ("🎨  Three Distinct Visual Themes", [
        "Minimal — cream & forest green, Georgia serif font, calm aesthetic",
        "Retro — dark maroon bg, gold & pink accents, vintage energy",
        "Glitch — near-black bg (#080B16), neon cyan & electric purple",
        "Each theme is a separate HTML page with its own body class",
    ]),
    ("🔀  Dark / Light Mode Toggle", [
        "Button on the home page footer — 'Switch Theme'",
        "JavaScript toggles class 'dark-mode' on the body element",
        "CSS transitions make the colour change smooth (0.3s)",
        "Button label changes: 'Dark Mode' ↔ 'Light Mode'",
    ]),
    ("🎲  Colour Palette Generator", [
        "Button: 'Generate Colours' — creates 3 random colour boxes",
        "JS picks from a preset list of 6 hex colours",
        "Each box shows the hex code as text and fills with that colour",
        "Useful for design inspiration — a creative interactive feature",
    ]),
    ("📝  Feedback Form with Validation", [
        "Form with Name field and Textarea for feedback message",
        "JavaScript checks: both fields must be filled before submit",
        "If fields are empty → alert('Please fill in all fields.')",
        "On success → alert with personalised thank-you message",
        "Form resets after successful submission",
    ]),
    ("🧭  Multi-Page Navigation", [
        "Consistent nav bar on ALL four pages: Home / Minimal / Retro / Glitch",
        "Footer prev/next navigation on theme pages",
        "Home page world cards — each card is a clickable link",
        "Back to Top link in the footer scrolls to top of page",
    ]),
    ("🖼️  Hero Images & Colour Swatches", [
        "Each theme page has a full-width Unsplash hero image",
        "Background gradient overlay dims the image for text readability",
        "Colour swatch section on each theme page shows 3 key palette colours",
        "Feature boxes explain the design philosophy of each theme",
    ]),
]

cols = [(0.5, 2.0), (4.6, 2.0), (8.7, 2.0)]
for i, (title, pts) in enumerate(features):
    col_idx = i % 3
    row_idx = i // 3
    lx, ty = cols[col_idx]
    ty += row_idx * 2.9
    add_rect(sl, lx, ty, 3.8, 2.6, GA_CARD)
    add_rect(sl, lx, ty, 3.8, 0.42, RGBColor(0x17,0x10,0x27))
    add_text(sl, title, lx+0.12, ty+0.05, 3.6, 0.32, size=12, bold=True, color=GA_ACCENT)
    for j, pt in enumerate(pts[:4]):
        add_text(sl, f"▸  {pt}", lx+0.12, ty+0.52 + j*0.49, 3.6, 0.44, size=10.5, color=GA_WHITE)

footer_A(sl)
add_notes(sl, """SLIDE 6 — What to say:
"GlitchLab has six main features. Let me explain each one."

1. Three visual themes:
   - Each theme is a separate page. The body tag has a unique class name that triggers a different set of CSS styles.

2. Dark/Light Mode Toggle:
   - On the home page, there is a 'Switch Theme' button in the footer area.
   - When clicked, JavaScript adds or removes the class 'dark-mode' on the body tag.
   - CSS has styling for body.dark-mode that changes background to dark and text to white.

3. Colour Palette Generator:
   - There is a 'Generate Colours' button on the home page.
   - When clicked, JavaScript randomly picks 3 colours from a list of 6 preset hex values.
   - Three coloured boxes appear, each showing its hex code.

4. Feedback Form:
   - There is a form with a Name field and a Feedback textarea.
   - If either field is empty, an alert box appears saying to fill all fields.
   - If both are filled, a thank-you message appears with the user's name.

5. Multi-Page Navigation:
   - All pages have the same navigation bar linking to each other.

6. Hero Images and Colour Swatches:
   - Each theme page has a background image from Unsplash with a dark overlay.
   - Below, there are three feature boxes and three colour swatches.

Possible teacher questions:
Q: How does the colour palette generator work?
A: JavaScript has an array of 6 preset hex colour values. When the button is clicked, a loop runs 3 times. Each time it picks a random index from the array using Math.random() and creates a coloured div with that hex code as the text.

Q: Is the feedback form data stored anywhere?
A: No. This is a front-end only project. The form data is not sent to any server. It only validates the input and shows an alert message.""")

# ─── SLIDE 7 ── UI/UX & Design Implementation ─────────────────────────────────
sl = new_slide(prs)
slide_header_A(sl, 7)
divider_A(sl)

add_text(sl, "UI/UX & Design Implementation", 0.5, 1.25, 12.5, 0.6,
         size=26, bold=True, color=GA_WHITE)

# Left side — layout breakdown
add_rect(sl, 0.5, 2.0, 5.8, 4.9, GA_CARD)
add_rect(sl, 0.5, 2.0, 5.8, 0.42, RGBColor(0x17,0x10,0x27))
add_text(sl, "LAYOUT & NAVIGATION DESIGN", 0.65, 2.05, 5.5, 0.32, size=12, bold=True, color=GA_ACCENT2)

layout_pts = [
    ("HOME PAGE LAYOUT:", True, 13, GA_ACCENT),
    ("▸  Header: Logo + Navigation bar", False, 12, GA_WHITE),
    ("▸  Hero Section: Large headline + CTA button", False, 12, GA_WHITE),
    ("▸  World Grid: 3 clickable theme cards (inline-block)", False, 12, GA_WHITE),
    ("▸  Footer: Interactive tools + feedback form", False, 12, GA_WHITE),
    ("", False, 6, GA_WHITE),
    ("THEME PAGES LAYOUT:", True, 13, GA_ACCENT),
    ("▸  Sub-header: Logo + same navigation links", False, 12, GA_WHITE),
    ("▸  Hero section: Unsplash image + text overlay", False, 12, GA_WHITE),
    ("▸  Feature Grid: 3 boxes (inline-block, 300px each)", False, 12, GA_WHITE),
    ("▸  Palette section: 3 colour swatches", False, 12, GA_WHITE),
    ("▸  Footer: prev / next page navigation", False, 12, GA_WHITE),
    ("", False, 6, GA_WHITE),
    ("CSS LAYOUT TECHNIQUE:", True, 13, GA_ACCENT),
    ("▸  display: inline-block (cards, feature boxes)", False, 12, GA_WHITE),
    ("▸  display: flex (colour palette generator)", False, 12, GA_WHITE),
    ("▸  max-width containers to centre content", False, 12, GA_WHITE),
]
add_text_multiline(sl, layout_pts, 0.65, 2.48, 5.5, 4.35)

# Right side — theme design breakdown
add_rect(sl, 6.6, 2.0, 6.4, 1.3, RGBColor(0xE9,0xE8,0xDD))
add_rect(sl, 6.6, 2.0, 0.08, 1.3, RGBColor(0x34,0x4E,0x41))
add_text(sl, "MINIMAL THEME", 6.75, 2.05, 6, 0.3, size=12, bold=True, color=RGBColor(0x34,0x4E,0x41))
add_text(sl, "BG: #F5F0E8 (cream)  |  Text: #344E41 (forest green)\nFont: Georgia serif  |  Calm, clean, airy design", 6.75, 2.38, 6, 0.65, size=11, color=RGBColor(0x34,0x4E,0x41))

add_rect(sl, 6.6, 3.45, 6.4, 1.3, RGBColor(0x24,0x10,0x25))
add_rect(sl, 6.6, 3.45, 0.08, 1.3, RGBColor(0xFF,0xD1,0x66))
add_text(sl, "RETRO THEME", 6.75, 3.5, 6, 0.3, size=12, bold=True, color=RGBColor(0xFF,0xD1,0x66))
add_text(sl, "BG: #241025 (dark maroon)  |  Accent: #FFD166 (gold)\nFont: Georgia serif  |  Bold vintage warm energy", 6.75, 3.83, 6, 0.65, size=11, color=RGBColor(0xFF,0xE3,0xA3))

add_rect(sl, 6.6, 4.9, 6.4, 1.3, GA_CARD)
add_rect(sl, 6.6, 4.9, 0.08, 1.3, RGBColor(0x00,0xF5,0xFF))
add_text(sl, "GLITCH THEME", 6.75, 4.95, 6, 0.3, size=12, bold=True, color=RGBColor(0x00,0xF5,0xFF))
add_text(sl, "BG: #080B16 (near black)  |  Accents: Cyan #00F5FF + Purple #B026FF\nFont: Courier New monospace  |  Cyber neon futuristic", 6.75, 5.28, 6, 0.65, size=11, color=GA_WHITE)

add_rect(sl, 6.6, 6.35, 6.4, 0.6, GA_CARD)
add_text(sl, "No responsive/mobile media queries implemented in this project. All layouts use fixed px widths. Best viewed on a desktop browser.", 6.65, 6.37, 6.3, 0.55, size=11, italic=True, color=RGBColor(0xAA,0xAA,0xBB))

footer_A(sl)
add_notes(sl, """SLIDE 7 — What to say:
"Let me explain the visual design and layout of GlitchLab."

Layout:
- The home page has four sections stacked vertically: header, hero, world cards grid, and footer.
- CSS uses 'inline-block' display for the three world cards and feature boxes — this places them side by side.
- The colour palette generator uses Flexbox (display: flex) to lay the colour boxes in a row.

Typography:
- Minimal theme uses Georgia serif — gives a calm editorial feel.
- Glitch theme uses Courier New monospace — gives a hacker/code terminal feel.
- Retro theme also uses Georgia — gives a classic, old-book style.

IMPORTANT HONESTY NOTE:
- This project does NOT have responsive design / media queries.
- It is designed for desktop viewing only.
- Do not say it is responsive unless you have checked.

Possible teacher questions:
Q: Is the website responsive?
A: No, GlitchLab does not have responsive design. There are no media queries in the CSS. The layout is designed for desktop screens and may not look perfect on mobile devices.

Q: What font family does the Glitch theme use?
A: The Glitch theme uses Courier New, a monospace font. This was chosen because monospace fonts look like code or hacker terminals, which fits the neon cyber theme.""")

# ─── SLIDE 8 ── Technical Implementation ──────────────────────────────────────
sl = new_slide(prs)
slide_header_A(sl, 8)
divider_A(sl)

add_text(sl, "Technical Implementation & Working Methodology", 0.5, 1.25, 12.5, 0.6,
         size=26, bold=True, color=GA_WHITE)

# CSS Theme System explanation
add_rect(sl, 0.5, 2.0, 5.9, 2.3, GA_CARD)
add_rect(sl, 0.5, 2.0, 5.9, 0.4, RGBColor(0x17,0x10,0x27))
add_text(sl, "CSS Theme Class System", 0.65, 2.05, 5.6, 0.3, size=13, bold=True, color=GA_ACCENT2)
add_text(sl, '<!-- glitch.html -->\n<body class="glitch-theme">\n\n/* style.css */\n.glitch-theme {\n  background-color: #080B16;\n  color: #FFFFFF;\n  font-family: "Courier New";\n}',
         0.65, 2.45, 5.6, 1.78, size=12, color=RGBColor(0x00,0xF5,0xFF), font_name="Courier New")

# JS Dark Mode
add_rect(sl, 0.5, 4.5, 5.9, 2.4, GA_CARD)
add_rect(sl, 0.5, 4.5, 5.9, 0.4, RGBColor(0x17,0x10,0x27))
add_text(sl, "JavaScript — Dark Mode Toggle", 0.65, 4.55, 5.6, 0.3, size=13, bold=True, color=GA_ACCENT2)
add_text(sl, 'themeButton.addEventListener("click", function() {\n  document.body.classList.toggle("dark-mode");\n  if (document.body.classList.contains("dark-mode")) {\n    themeButton.textContent = "Light Mode";\n  } else {\n    themeButton.textContent = "Dark Mode";\n  }\n});',
         0.65, 4.95, 5.6, 1.85, size=11.5, color=RGBColor(0xC7,0x7D,0xFF), font_name="Courier New")

# JS Palette Generator
add_rect(sl, 6.7, 2.0, 6.0, 2.3, GA_CARD)
add_rect(sl, 6.7, 2.0, 6.0, 0.4, RGBColor(0x17,0x10,0x27))
add_text(sl, "JavaScript — Colour Palette Generator", 6.85, 2.05, 5.7, 0.3, size=13, bold=True, color=GA_ACCENT2)
add_text(sl, 'const colours = ["#B026FF","#00F5FF","#FF78A9","#A3B18A","#F5F0E8","#344E41"];\n\npaletteButton.addEventListener("click", function() {\n  paletteBox.innerHTML = "";\n  for (let i = 0; i < 3; i++) {\n    const index = Math.floor(Math.random() * colours.length);\n    const colour = colours[index];\n    const box = document.createElement("div");\n    box.style.backgroundColor = colour;\n    box.textContent = colour;\n    paletteBox.appendChild(box);\n  }\n});',
         6.85, 2.45, 5.7, 1.78, size=11, color=RGBColor(0xC7,0x7D,0xFF), font_name="Courier New")

# JS Form Validation
add_rect(sl, 6.7, 4.5, 6.0, 2.4, GA_CARD)
add_rect(sl, 6.7, 4.5, 6.0, 0.4, RGBColor(0x17,0x10,0x27))
add_text(sl, "JavaScript — Feedback Form Validation", 6.85, 4.55, 5.7, 0.3, size=13, bold=True, color=GA_ACCENT2)
add_text(sl, 'feedbackForm.addEventListener("submit", function(event) {\n  event.preventDefault(); // stop page reload\n  const name = document.getElementById("userName").value;\n  const msg  = document.getElementById("feedback").value;\n  if (name.trim() === "" || msg.trim() === "") {\n    alert("Please fill in all fields.");\n  } else {\n    alert("Thank you, " + name + "! Received.");\n    feedbackForm.reset();\n  }\n});',
         6.85, 4.95, 5.7, 1.85, size=11, color=RGBColor(0xC7,0x7D,0xFF), font_name="Courier New")

footer_A(sl)
add_notes(sl, """SLIDE 8 — What to say:
"Let me explain how the main JavaScript features actually work, step by step."

1. CSS Theme System (top left):
   - Each HTML file has a specific class on the body tag, like class="glitch-theme".
   - The CSS file has a section that starts with .glitch-theme { ... } which applies styles only to that body class.
   - This is how three different pages get three different looks from one CSS file.

2. Dark Mode Toggle (bottom left):
   - There is a button with the id 'themeButton'.
   - When clicked, JavaScript calls classList.toggle("dark-mode") on the body.
   - 'toggle' means: if the class is there, remove it. If it is not there, add it.
   - The CSS has styles for body.dark-mode that make background dark and text white.

3. Colour Palette Generator (top right):
   - JavaScript has an array of 6 hex colour values stored in a constant called 'colours'.
   - When the button is clicked, a 'for' loop runs 3 times.
   - Each iteration picks a random number using Math.floor(Math.random() * 6).
   - That number is used as an index to get a colour from the array.
   - A new div element is created, its background and text are set to that colour, and it is added to the page.

4. Feedback Form Validation (bottom right):
   - The form has an event listener for 'submit'.
   - event.preventDefault() stops the browser from reloading the page (default form behaviour).
   - Then it checks if the name or message fields are empty using .trim() === "".
   - If empty: shows an alert. If filled: shows a thank-you message and resets the form.

Possible teacher questions:
Q: What does event.preventDefault() do?
A: Normally when you submit an HTML form, the browser reloads the page or sends data to a server. event.preventDefault() cancels this default action so JavaScript can handle the submission instead.

Q: What does classList.toggle() do?
A: It is a JavaScript method that checks if a CSS class exists on an element. If it exists, it removes it. If it does not exist, it adds it. This is useful for toggle features like dark mode.""")

# ─── SLIDE 9 ── Project Workflow, Testing & Results ───────────────────────────
sl = new_slide(prs)
slide_header_A(sl, 9)
divider_A(sl)

add_text(sl, "Project Workflow, Testing & Results", 0.5, 1.25, 12.5, 0.6,
         size=26, bold=True, color=GA_WHITE)

# Left: user workflow
add_rect(sl, 0.5, 2.0, 5.5, 4.9, GA_CARD)
add_rect(sl, 0.5, 2.0, 5.5, 0.4, RGBColor(0x17,0x10,0x27))
add_text(sl, "USER EXPERIENCE FLOW", 0.65, 2.05, 5.2, 0.3, size=13, bold=True, color=GA_ACCENT2)

flow_steps = [
    ("STEP 1", GA_ACCENT, "Open index.html in browser"),
    ("STEP 2", GA_ACCENT, "See home hero — 'Design Beyond Ordinary'"),
    ("STEP 3", GA_ACCENT, "Scroll to 3 World Cards: Minimal / Retro / Glitch"),
    ("STEP 4", GA_ACCENT, "Click a card — navigate to that theme page"),
    ("STEP 5", GA_ACCENT, "Explore the theme hero, features, and colour swatches"),
    ("STEP 6", GA_ACCENT, "Use navbar to switch between themes"),
    ("STEP 7", GA_ACCENT, "Return to home page footer — try the interactive tools"),
    ("STEP 8", GA_ACCENT, "Click 'Switch Theme' — dark mode activates"),
    ("STEP 9", GA_ACCENT, "Click 'Generate Colours' — 3 colour boxes appear"),
    ("STEP 10", GA_ACCENT, "Fill feedback form — submit to see thank-you alert"),
]
for i, (label, lclr, desc) in enumerate(flow_steps):
    ty = 2.48 + i * 0.44
    add_rect(sl, 0.65, ty, 0.75, 0.33, lclr)
    add_text(sl, label, 0.67, ty+0.03, 0.72, 0.28, size=9, bold=True, color=GA_BG, align=PP_ALIGN.CENTER)
    add_text(sl, desc, 1.47, ty+0.03, 4.3, 0.33, size=11, color=GA_WHITE)

# Right: test results
add_rect(sl, 6.3, 2.0, 6.7, 2.2, GA_CARD)
add_rect(sl, 6.3, 2.0, 6.7, 0.4, RGBColor(0x17,0x10,0x27))
add_text(sl, "TESTING OBSERVATIONS", 6.45, 2.05, 6.4, 0.3, size=13, bold=True, color=GA_ACCENT2)
add_bullet_A(sl, [
    "All 4 pages open correctly in Chrome/Edge/Firefox",
    "Navigation links between pages work as expected",
    "Dark mode toggle works on the home page",
    "Colour palette generates 3 coloured boxes each click",
    "Form rejects empty submissions and thanks on success",
    "Theme styles load correctly for all three themes",
], 6.45, 2.45, 6.4, 1.65, size=12)

add_rect(sl, 6.3, 4.35, 6.7, 1.5, GA_CARD)
add_rect(sl, 6.3, 4.35, 6.7, 0.4, RGBColor(0x17,0x10,0x27))
add_text(sl, "KNOWN LIMITATIONS", 6.45, 4.4, 6.4, 0.3, size=13, bold=True, color=RGBColor(0xFF,0x78,0xA9))
add_bullet_A(sl, [
    "No responsive/mobile design — best viewed on desktop",
    "Colour palette picks from only 6 preset colours",
    "Feedback form data is not saved anywhere (front-end only)",
    "Draft files (glitchhh.html, minimall.html, etc.) present in folder — not part of the final project",
    "dir_name folder is empty — appears to be unused",
], 6.45, 4.8, 6.4, 1.0, size=11)

add_rect(sl, 6.3, 5.95, 6.7, 1.0, GA_CARD)
add_rect(sl, 6.3, 5.95, 0.07, 1.0, GA_ACCENT2)
add_text(sl, "ACTUAL RESULTS", 6.5, 5.97, 6.4, 0.32, size=12, bold=True, color=GA_ACCENT2)
add_text(sl, "Project successfully demonstrates a multi-theme website using HTML class-based CSS theming with real JavaScript interactivity. All stated features function as expected.", 6.5, 6.3, 6.4, 0.6, size=11, color=GA_WHITE)

footer_A(sl)
add_notes(sl, """SLIDE 9 — What to say:
"Let me walk you through how a user experiences GlitchLab from start to finish."

User flow explanation (say it naturally):
1. The user opens index.html in a browser. They see the dark purple home page with the headline 'Design Beyond Ordinary.'
2. Scrolling down shows three cards: Minimal, Retro, and Glitch.
3. Clicking a card navigates to the respective theme page.
4. Each theme page has its own colour scheme, font, hero image, feature boxes, and colour swatches.
5. The navigation bar on every page lets you switch between all themes without going back to home.
6. Back on the home page footer, there are three interactive features: dark mode toggle, colour palette generator, and feedback form.

Testing:
- The project was tested in Chrome, Edge, and Firefox.
- All features work correctly.

Limitations (be honest with the teacher):
- No mobile responsiveness — the layout may look off on phones.
- Feedback data is not saved — it only shows an alert.
- There are old draft files (glitchhh.html, minimall.html, etc.) in the folder. These are earlier versions. Only the final files are used.

Possible teacher questions:
Q: What happens if a user submits the form with an empty name?
A: JavaScript checks if the .trim() value of the name input equals an empty string. If it does, an alert pops up saying 'Please fill in all fields.' The form does not submit.

Q: Are the extra files (glitchhh.html, etc.) part of the project?
A: No. Those are earlier draft versions from development. Only index.html, minimal.html, retro.html, and glitch.html are the final project files.""")

# ─── SLIDE 10 ── Conclusion & Future Scope ────────────────────────────────────
sl = new_slide(prs)
slide_header_A(sl, 10)
divider_A(sl)

add_text(sl, "Conclusion & Future Scope", 0.5, 1.25, 12.5, 0.6,
         size=26, bold=True, color=GA_WHITE)

# Left
add_rect(sl, 0.5, 2.0, 5.9, 4.9, GA_CARD)
add_rect(sl, 0.5, 2.0, 5.9, 0.4, RGBColor(0x17,0x10,0x27))
add_text(sl, "KEY LEARNING OUTCOMES", 0.65, 2.05, 5.6, 0.3, size=13, bold=True, color=GA_ACCENT2)
add_bullet_A(sl, [
    "Understood how to build a multi-page website with linked HTML files",
    "Learned CSS class-based theming: how one stylesheet drives multiple looks",
    "Practised writing clean, organised CSS with labelled sections",
    "Applied JavaScript for real user interactions (toggle, generator, form)",
    "Understood DOM manipulation: classList.toggle, createElement, appendChild",
    "Learned how to use event listeners for buttons and forms",
    "Understood the importance of CSS transitions for smooth UX",
    "Practised file organisation and project structure",
], 0.65, 2.48, 5.6, 4.35, size=12)

# Right top
add_rect(sl, 6.7, 2.0, 6.3, 2.5, GA_CARD)
add_rect(sl, 6.7, 2.0, 6.3, 0.4, RGBColor(0x17,0x10,0x27))
add_text(sl, "WHAT THE PROJECT DEMONSTRATES", 6.85, 2.05, 6.0, 0.3, size=13, bold=True, color=GA_ACCENT2)
add_bullet_A(sl, [
    "CSS class-based theming — one file, multiple designs",
    "JavaScript DOM manipulation — adding classes, creating elements",
    "Multi-page navigation using HTML anchor links",
    "Form validation without any external library",
    "Design awareness: typography, colour, spacing for 3 styles",
], 6.85, 2.48, 6.0, 2.0, size=12)

# Right bottom
add_rect(sl, 6.7, 4.65, 6.3, 2.25, GA_CARD)
add_rect(sl, 6.7, 4.65, 6.3, 0.4, RGBColor(0x17,0x10,0x27))
add_text(sl, "FUTURE IMPROVEMENTS", 6.85, 4.7, 6.0, 0.3, size=13, bold=True, color=GA_ACCENT)
add_bullet_A(sl, [
    "Add CSS media queries for mobile / responsive design",
    "Allow theme switching without changing pages (single-page JS toggle)",
    "Save feedback using localStorage so data is not lost on refresh",
    "Add more colour options to the palette generator",
    "Add smooth CSS animations for page transitions",
    "Connect feedback form to a backend (e.g. Node.js / Firebase)",
], 6.85, 5.12, 6.0, 1.7, size=12)

footer_A(sl)
add_notes(sl, """SLIDE 10 — What to say:
"GlitchLab successfully meets all its learning objectives. Let me summarise what I learnt and what can be improved."

What to say about learning outcomes:
- The biggest thing I learnt is how CSS class names on the body tag can completely control the visual theme of a page.
- I also learnt how to write clean, organised CSS using labelled comment sections.
- JavaScript-wise, I learnt how classList.toggle adds or removes a class, how Math.random picks random values, and how event listeners handle user actions.

What to say about future scope:
- Currently the website only works properly on desktop. Adding media queries would make it mobile-friendly.
- The themes currently require navigating to a new page. A better approach would be to use JavaScript to switch themes on a single page without reloading.
- The feedback form only shows an alert. In a real project, the data would be saved to a database.
- The colour palette could have more colours or even let users generate any colour using an input.

Quick viva preparation points:
1. What is the purpose of GlitchLab? → A multi-theme creative website with 3 design styles.
2. How many files does it have? → 4 HTML, 1 CSS, 1 JS.
3. What JavaScript features are implemented? → Dark mode, colour palette, form validation.
4. How does the CSS theming work? → Body class name controls which CSS section is active.
5. What is a limitation? → No responsive design. Front-end only. No data storage.

Possible teacher questions:
Q: How would you make GlitchLab mobile-friendly?
A: I would add CSS media queries. For example, @media (max-width: 768px) { .world-card { width: 90%; display: block; } } to stack the cards vertically on small screens.

Q: What is localStorage and how could you use it here?
A: localStorage is a browser feature that lets you save small pieces of data in the user's browser. I could use it to save the feedback form submissions so they persist even after the page is refreshed.""")

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION B — Style Avenue  (Slides 11–20)
# ═══════════════════════════════════════════════════════════════════════════════

# ─── SLIDE 11 ── Project Title & Introduction ─────────────────────────────────
sl = new_slide(prs)
slide_header_B(sl, 11)
divider_B(sl)

# Hero area
add_rect(sl, 0.5, 1.3, 7.5, 5.6, SB_CARD)
add_rect(sl, 0.5, 1.3, 0.1, 5.6, SB_ACCENT)

add_text(sl, "PROJECT 2", 0.75, 1.4, 5, 0.4, size=11, color=SB_ACCENT, bold=True)
add_text(sl, "Style Avenue", 0.75, 1.82, 7, 0.95, size=48, bold=True, color=SB_TEXT, font_name="Calibri")
add_text(sl, "Fashion & Lifestyle", 0.75, 2.8, 7, 0.55, size=22, italic=True, color=SB_ACCENT, font_name="Calibri")

add_text_multiline(sl, [
    ("Myntra-Inspired Fashion Store — Student Learning Project", True, 14, SB_ACCENT),
    ("", False, 7, SB_TEXT),
    ("Style Avenue is a multi-page front-end fashion e-commerce website", False, 13, SB_TEXT),
    ("inspired by Myntra. It features product browsing, search, wishlist,", False, 13, SB_TEXT),
    ("add-to-bag functionality, dark/light theme toggle, and newsletter form.", False, 13, SB_TEXT),
    ("", False, 7, SB_TEXT),
    ("Technologies:  HTML · CSS · Bootstrap 5 · Font Awesome · JavaScript", False, 13, SB_ACCENT),
    ("Total Files:   5 HTML · 1 CSS · 1 JavaScript · 1 README.md", False, 13, SB_ACCENT),
    ("Pages: Home · Men · Women · Kids · Beauty", False, 13, SB_TEXT),
], 0.75, 3.4, 7.1, 2.9)

# Right side — category tiles
categories = [
    (SB_TEXT,                        RGBColor(0xFF,0xFF,0xFF), "FOR HIM",     "Men's Collection"),
    (SB_ACCENT,                      RGBColor(0xFF,0xFF,0xFF), "FOR HER",     "Women's Collection"),
    (RGBColor(0x2D,0x6A,0x4F),       RGBColor(0xFF,0xFF,0xFF), "FOR KIDS",    "Kids Collection"),
    (RGBColor(0x6D,0x28,0x4D),       RGBColor(0xFF,0xFF,0xFF), "BEAUTY",      "Beauty & Selfcare"),
]
for i, (bg, tc, lbl, sub) in enumerate(categories):
    lx = 8.3 + (i % 2) * 2.5
    ty = 1.4 + (i // 2) * 2.65
    add_rect(sl, lx, ty, 2.3, 2.4, bg)
    add_text(sl, lbl, lx+0.1, ty+0.1, 2.1, 0.45, size=16, bold=True, color=tc, align=PP_ALIGN.CENTER)
    add_text(sl, sub, lx+0.1, ty+1.75, 2.1, 0.5, size=11, color=tc, align=PP_ALIGN.CENTER)

footer_B(sl)
add_notes(sl, """SLIDE 11 — What to say:
"The second project is called Style Avenue. It is a Myntra-inspired fashion shopping website built as a student learning project using HTML, CSS, and JavaScript."

What is Style Avenue?
- It is a 5-page fashion e-commerce website.
- Pages: Home (index.html), Men (men.html), Women (women.html), Kids (kids.html), Beauty (beauty.html).
- It is inspired by Myntra — a popular Indian fashion e-commerce platform.
- It is a FRONT-END ONLY project. There is no real payment, login, or database.

Extra libraries used (compared to GlitchLab):
- Bootstrap 5: Provides a grid system for responsive layout.
- Font Awesome 6: Provides icons (shopping bag, heart, moon, magnifying glass, etc.)
- Google Fonts: DM Sans and Playfair Display for a premium fashion feel.

The project footer actually says: "© 2026 Style Avenue · Student learning project — Made with HTML, CSS & JavaScript."

Possible teacher questions:
Q: Is Style Avenue the same as Myntra?
A: No. Style Avenue is an independent student project inspired by Myntra's general e-commerce design. It is not affiliated with Myntra in any way. All product names, prices, and content are sample data created for learning purposes.

Q: How many pages does Style Avenue have?
A: Five pages — index.html (home), men.html, women.html, kids.html, and beauty.html. All share the same style.css and script.js.""")

# ─── SLIDE 12 ── Problem Statement & Objectives ───────────────────────────────
sl = new_slide(prs)
slide_header_B(sl, 12)
divider_B(sl)

add_text(sl, "Problem Statement & Project Objectives", 0.5, 1.25, 12.5, 0.6,
         size=26, bold=True, color=SB_TEXT)

add_rect(sl, 0.5, 2.0, 5.9, 4.8, SB_CARD)
add_rect(sl, 0.5, 2.0, 5.9, 0.42, SB_ACCENT)
add_text(sl, "THE PROBLEM", 0.65, 2.05, 5.6, 0.32, size=13, bold=True, color=RGBColor(0xFF,0xFF,0xFF))
add_bullet_B(sl, [
    "Beginners learn HTML/CSS/JS separately but rarely combine them in a real-world project",
    "E-commerce UI patterns (product cards, filters, carts) are not covered in beginner tutorials",
    "Students miss experience using external libraries like Bootstrap and Font Awesome",
    "Concepts like arrays, objects, filter(), map(), reduce() are not practised in real projects",
    "No example of how search, filters, wishlist, and cart work together in pure JavaScript",
], 0.65, 2.48, 5.6, 4.35, size=13)

add_rect(sl, 6.7, 2.0, 6.0, 4.8, SB_CARD)
add_rect(sl, 6.7, 2.0, 6.0, 0.42, SB_ACCENT)
add_text(sl, "PROJECT OBJECTIVES", 6.85, 2.05, 5.7, 0.32, size=13, bold=True, color=RGBColor(0xFF,0xFF,0xFF))
add_bullet_B(sl, [
    "Build a complete multi-page fashion e-commerce front-end using HTML, CSS, and JavaScript",
    "Use Bootstrap for responsive grid layout across all screen sizes",
    "Implement product search, category filters, and real-time product rendering via JavaScript",
    "Build a working shopping bag with item count, subtotal calculation, and slide-in panel",
    "Implement wishlist toggle using heart icon and JavaScript arrays",
    "Demonstrate advanced JavaScript concepts: arrays, objects, filter, map, reduce, for loops",
    "Add newsletter form with email validation and toast notification messages",
    "Implement dark / light theme toggle using CSS class switching",
], 6.85, 2.48, 5.7, 4.35, size=12)

footer_B(sl)
add_notes(sl, """SLIDE 12 — What to say:
"The main goal of Style Avenue was to solve a common beginner problem: students learn HTML, CSS, and JavaScript theory separately but never combine them in a realistic project."

Key problem statement:
- Real e-commerce websites have features like product cards, search, filters, cart, and wishlist.
- These require all three technologies working together.
- Beginners also miss out on using external libraries like Bootstrap.
- Advanced JS concepts like filter(), map(), reduce() are rarely practised.

Objectives:
- Build a fully functional front-end fashion store with 5 pages.
- Use Bootstrap's grid system (col-6, col-md-4, col-lg-3) for responsive product cards.
- Implement product search, category filter, wishlist, cart, and dark mode purely in JavaScript.
- Use Font Awesome icons for a professional look.
- Use Google Fonts for premium typography.

Target users: B.Tech/engineering students who have learnt the basics of HTML, CSS, and JavaScript and want a comprehensive project to showcase.

Possible teacher questions:
Q: Why did you use Bootstrap in this project?
A: Bootstrap provides a ready-made grid system (using classes like col-6, col-md-4) that makes the product cards automatically adjust to different screen sizes. Without Bootstrap, writing responsive CSS manually would take much more time.

Q: What is the main difference between GlitchLab and Style Avenue?
A: GlitchLab is a creative/artistic project focused on CSS theming. Style Avenue is a practical e-commerce project that uses more advanced JavaScript features like arrays, objects, filter, map, and reduce to build real shopping features.""")

# ─── SLIDE 13 ── Project Overview & Architecture ──────────────────────────────
sl = new_slide(prs)
slide_header_B(sl, 13)
divider_B(sl)

add_text(sl, "Project Overview & Architecture", 0.5, 1.25, 12.5, 0.6,
         size=26, bold=True, color=SB_TEXT)

# Top — shared resources
add_rect(sl, 0.5, 2.0, 12.33, 0.75, SB_HDR)
add_rect(sl, 0.5, 2.0, 0.07, 0.75, SB_ACCENT)
add_text(sl, "SHARED FILES (used by all pages):   script.js  —  All JavaScript logic, product data, cart, search, filters, wishlist, theme toggle, newsletter form",
         0.65, 2.1, 12.0, 0.55, size=12, color=RGBColor(0xFF,0xFF,0xFF))

add_rect(sl, 0.5, 2.85, 12.33, 0.75, SB_CARD)
add_rect(sl, 0.5, 2.85, 0.07, 0.75, SB_ACCENT)
add_text(sl, "SHARED FILES (used by all pages):   style.css  —  All custom CSS  |  Bootstrap 5 CDN  |  Font Awesome 6 CDN  |  Google Fonts CDN",
         0.65, 2.95, 12.0, 0.55, size=12, color=SB_TEXT)

# Five page boxes
pages = [
    ("index.html\n(Home)", SB_TEXT, RGBColor(0xFF,0xFF,0xFF), "Hero · Category tiles · Featured products · Search · Filter"),
    ("men.html\n(Men)", RGBColor(0x14,0x33,0x1E), RGBColor(0xFF,0xFF,0xFF), "Collection hero · Men's products · Search · Cart"),
    ("women.html\n(Women)", RGBColor(0x6D,0x17,0x40), RGBColor(0xFF,0xFF,0xFF), "Collection hero · Women's products · Search · Cart"),
    ("kids.html\n(Kids)", RGBColor(0x0E,0x34,0x5A), RGBColor(0xFF,0xFF,0xFF), "Collection hero · Kids' products · Search · Cart"),
    ("beauty.html\n(Beauty)", RGBColor(0x4A,0x1A,0x3A), RGBColor(0xFF,0xFF,0xFF), "Collection hero · Beauty products · Search · Cart"),
]
for i, (title, bg, tc, desc) in enumerate(pages):
    lx = 0.5 + i * 2.47
    add_rect(sl, lx, 3.75, 2.3, 1.1, bg)
    add_text(sl, title, lx+0.1, 3.8, 2.1, 0.55, size=12, bold=True, color=tc, align=PP_ALIGN.CENTER)
    add_text(sl, desc, lx+0.1, 4.35, 2.1, 0.45, size=9, color=tc, align=PP_ALIGN.CENTER)

# Connecting arrows (down from shared to pages)
add_rect(sl, 1.5, 3.6, 10.5, 0.07, SB_ACCENT)
for x in [1.5, 3.95, 6.4, 8.85, 11.3]:
    add_rect(sl, x, 3.6, 0.07, 0.15, SB_ACCENT)

# Bottom: Architecture notes
add_rect(sl, 0.5, 5.05, 5.9, 1.9, SB_CARD)
add_rect(sl, 0.5, 5.05, 0.07, 1.9, SB_ACCENT)
add_text(sl, "HOW PAGES ARE DIFFERENTIATED", 0.65, 5.1, 5.6, 0.32, size=12, bold=True, color=SB_ACCENT)
add_text(sl, 'Each HTML page has:\n<body data-page="women">\nscript.js reads data-page to filter products for that category automatically. Same JS file, different behaviour per page.', 0.65, 5.45, 5.6, 1.45, size=12, color=SB_TEXT)

add_rect(sl, 6.6, 5.05, 6.3, 1.9, SB_CARD)
add_rect(sl, 6.6, 5.05, 0.07, 1.9, SB_ACCENT)
add_text(sl, "EXTERNAL LIBRARIES (CDN — no install)", 6.75, 5.1, 6.0, 0.32, size=12, bold=True, color=SB_ACCENT)
add_bullet_B(sl, [
    "Bootstrap 5.3.3 — responsive grid layout (col-6, col-md-4, col-lg-3)",
    "Font Awesome 6.5.2 — icons (bag, heart, moon, arrow, star)",
    "Google Fonts — DM Sans (body) + Playfair Display (headings)",
], 6.75, 5.45, 6.0, 1.45, size=12)

footer_B(sl)
add_notes(sl, """SLIDE 13 — What to say:
"Let me explain how Style Avenue is structured. All five pages share the same style.css and script.js files. What makes each page different is the data-page attribute on the body tag."

data-page system:
- index.html has <body data-page="home">
- men.html has <body data-page="men">
- women.html has <body data-page="women">
- etc.
- In script.js, the renderProducts() function reads: const page = document.body.dataset.page;
- If page is "women", it only shows products where item.category === "women"
- This means one JavaScript function powers all five product pages.

External libraries:
- Bootstrap: Loaded via CDN (Content Delivery Network). No installation needed. Provides the col-6 col-md-4 col-lg-3 grid classes for responsive product cards.
- Font Awesome: CDN link. Provides vector icons — the shopping bag icon, heart icon, moon icon, search icon, etc.
- Google Fonts: CDN link. DM Sans is used for body text, Playfair Display for headings.

Possible teacher questions:
Q: What is a CDN and why is it used?
A: CDN stands for Content Delivery Network. It is an online server that hosts library files. Instead of downloading Bootstrap or Font Awesome and including them in the project folder, we can link directly to the CDN URL. This saves storage space and usually loads faster.

Q: How does the same script.js know which products to show on the Women page vs the Men page?
A: The body tag on each HTML page has a data-page attribute (e.g., data-page="women"). The JavaScript reads this value using document.body.dataset.page, and then filters the products array to show only items where category matches the page name.""")

# ─── SLIDE 14 ── Technologies & Tools Used ────────────────────────────────────
sl = new_slide(prs)
slide_header_B(sl, 14)
divider_B(sl)

add_text(sl, "Technologies & Tools Used", 0.5, 1.25, 12.5, 0.6,
         size=26, bold=True, color=SB_TEXT)

tech_b = [
    ("HTML5", SB_ACCENT, [
        "5-page multi-page structure",
        "Semantic tags: <header>, <main>, <section>, <article>, <footer>",
        "Bootstrap grid classes on HTML elements (col-6, col-md-4)",
        "data-page attribute to identify each page to JavaScript",
        "ARIA labels for accessibility (aria-label, aria-live)",
        "Internal CSS example on home page  |  Inline style example in product",
    ]),
    ("CSS3", RGBColor(0x2D,0x6A,0x4F), [
        "Custom stylesheet: style.css  (15,473 bytes)",
        "Flexbox for header, hero, footer layout",
        "CSS Grid for category tiles",
        "Hover effects on product cards and buttons",
        "Dark theme: body.dark-theme class changes colours",
        "Responsive media queries for mobile layout",
        "Smooth transitions for cart panel sliding in/out",
    ]),
    ("Bootstrap 5", RGBColor(0x6F,0x42,0xC1), [
        "Bootstrap grid: col-6 col-md-4 col-lg-3",
        "Products display 2 per row on mobile, 3 on tablet, 4 on desktop",
        "Bootstrap's container-fluid for the header layout",
        "Only CSS grid utilities are used (not JS components)",
        "Loaded via CDN — no local install needed",
    ]),
]

tech_b2 = [
    ("JavaScript (ES6+)", RGBColor(0xE9,0x4F,0x78), [
        "Products array: 10 objects with id, name, category, price, tag, image",
        "filter() — search and category filtering of products",
        "map() — create product name lists for console logging",
        "find() — look up a product by its ID number",
        "reduce() — calculate the cart subtotal total price",
        "forEach() — loop through filter buttons, attach event listeners",
        "for...of, for...in, do...while — multiple loop types demonstrated",
    ]),
    ("Font Awesome 6", RGBColor(0x0D,0xBF,0xFB), [
        "Shopping bag icon (fa-bag-shopping)",
        "Heart / wishlist icon (fa-heart solid/regular)",
        "Moon and sun icons for theme toggle",
        "Arrow icons for navigation and CTAs",
        "Star icons in the ticker / marquee strip",
    ]),
    ("Google Fonts", RGBColor(0xE5,0x57,0x22), [
        "DM Sans — primary body font (weights 400–800)",
        "Playfair Display — elegant serif for headings",
        "Loaded via Google Fonts CDN link in <head>",
        "Fallback: sans-serif (if internet is unavailable)",
    ]),
]

for i, (tech, clr, pts) in enumerate(tech_b):
    lx = 0.5 + i * 4.3
    add_rect(sl, lx, 2.0, 4.1, 2.5, SB_CARD)
    add_rect(sl, lx, 2.0, 4.1, 0.42, clr)
    add_text(sl, tech, lx+0.12, 2.05, 3.85, 0.32, size=14, bold=True, color=RGBColor(0xFF,0xFF,0xFF), align=PP_ALIGN.CENTER)
    for j, pt in enumerate(pts[:6]):
        add_text(sl, f"▸  {pt}", lx+0.12, 2.52 + j*0.33, 3.85, 0.3, size=11, color=SB_TEXT)

for i, (tech, clr, pts) in enumerate(tech_b2):
    lx = 0.5 + i * 4.3
    add_rect(sl, lx, 4.6, 4.1, 2.4, SB_CARD)
    add_rect(sl, lx, 4.6, 4.1, 0.42, clr)
    add_text(sl, tech, lx+0.12, 4.65, 3.85, 0.32, size=14, bold=True, color=RGBColor(0xFF,0xFF,0xFF), align=PP_ALIGN.CENTER)
    for j, pt in enumerate(pts[:6]):
        add_text(sl, f"▸  {pt}", lx+0.12, 5.12 + j*0.33, 3.85, 0.3, size=11, color=SB_TEXT)

footer_B(sl)
add_notes(sl, """SLIDE 14 — What to say:
"Style Avenue uses six technologies. Let me quickly explain each one."

HTML5:
- Provides the page structure with semantic tags.
- The key difference from GlitchLab is the data-page attribute on the body tag, which JavaScript uses to filter products per page.
- Also has an internal CSS example (a small <style> tag in the home page head) and an inline style example on a product element to demonstrate all three ways to write CSS.

CSS3:
- Custom style.css is 15,473 bytes — much larger than GlitchLab's CSS.
- Uses Flexbox for header layout, CSS Grid for category tiles, hover effects, and responsive media queries.
- Has a dark theme: when body gets class 'dark-theme', colours change throughout the site.

Bootstrap 5:
- Only the CSS part of Bootstrap is used — the grid system.
- col-6 on mobile = 2 columns | col-md-4 on tablet = 3 columns | col-lg-3 on desktop = 4 columns.
- This makes product cards automatically resize and rearrange based on screen size.

JavaScript:
- Uses modern ES6+ features: const, let, arrow functions, template literals.
- 10 products stored as an array of objects.
- Uses filter(), map(), find(), reduce(), forEach() — all array methods.
- Multiple loop types used: for...of, for...in, do...while.

Font Awesome and Google Fonts are loaded via CDN links in the HTML head — no installation needed.

Possible teacher questions:
Q: What is the difference between Flexbox and Grid in CSS?
A: Flexbox works in one direction — either a row or a column. It is used for the header (logo + nav + icons in a row). CSS Grid works in two dimensions — rows AND columns. It is used for the category tiles section which has a 2x2 layout.

Q: What does the reduce() method do in this project?
A: It is used to calculate the total price of all items in the cart array. It goes through each item, adds its price to a running sum, and returns the final total. For example: cart.reduce((sum, item) => sum + item.price, 0)""")

# ─── SLIDE 15 ── Project Structure & File Organization ─────────────────────────
sl = new_slide(prs)
slide_header_B(sl, 15)
divider_B(sl)

add_text(sl, "Project Structure & File Organization", 0.5, 1.25, 12.5, 0.6,
         size=26, bold=True, color=SB_TEXT)

add_rect(sl, 0.5, 2.0, 5.5, 4.9, SB_CARD)
add_rect(sl, 0.5, 2.0, 5.5, 0.42, SB_ACCENT)
add_text(sl, "FOLDER STRUCTURE", 0.65, 2.05, 5.2, 0.32, size=13, bold=True, color=RGBColor(0xFF,0xFF,0xFF))

folder_tree_b = [
    ("📁  Myntra-Clone-SRDT/", True, 14, SB_ACCENT),
    ("", False, 5, SB_TEXT),
    ("   📄  index.html", True, 13, SB_TEXT),
    ("         → Home, hero, categories, featured products", False, 11, SB_GRAY),
    ("   📄  men.html", True, 13, SB_TEXT),
    ("         → Men's collection page", False, 11, SB_GRAY),
    ("   📄  women.html", True, 13, SB_TEXT),
    ("         → Women's collection page", False, 11, SB_GRAY),
    ("   📄  kids.html", True, 13, SB_TEXT),
    ("         → Kids' collection page", False, 11, SB_GRAY),
    ("   📄  beauty.html", True, 13, SB_TEXT),
    ("         → Beauty & self-care collection page", False, 11, SB_GRAY),
    ("   🎨  style.css", True, 13, SB_ACCENT),
    ("         → ALL custom styling (15,473 bytes)", False, 11, SB_GRAY),
    ("   ⚙️  script.js", True, 13, SB_ACCENT),
    ("         → ALL JavaScript (9,663 bytes, 166 lines)", False, 11, SB_GRAY),
    ("   📄  README.md", True, 13, SB_GRAY),
    ("         → Project description and setup guide", False, 11, SB_GRAY),
    ("   📄  .gitignore", True, 13, SB_GRAY),
    ("         → Files excluded from Git (node_modules etc.)", False, 11, SB_GRAY),
    ("   📁  .git/", True, 13, SB_GRAY),
    ("         → Git version control history folder", False, 11, SB_GRAY),
]
add_text_multiline(sl, folder_tree_b, 0.65, 2.5, 5.2, 4.3)

right_cards_b = [
    ("index.html  (8,750 bytes)", "Largest HTML file. Contains the full home page: hero section with hero image and CTA buttons, an animated ticker strip, category grid (4 tiles), product section with search and filter buttons, editorial strip, and newsletter form in footer."),
    ("men/women/kids/beauty.html  (~5,000 bytes each)", "Collection pages. Each has a hero section styled for its category, a product section with search bar, and a collection note section. The body has data-page='men/women/kids/beauty' — this makes script.js show only the right products."),
    ("style.css  (15,473 bytes)", "Large custom CSS file. Uses Flexbox, CSS Grid, hover effects, dark theme (body.dark-theme), responsive media queries, cart panel slide-in animation (translateX), and smooth transitions."),
    ("script.js  (9,663 bytes  —  166 lines)", "Single JS file serving all pages. Contains: products array (10 items), functions (formatPrice, addToCart, toggleWishlist, updateCart, renderProducts, showToast), search, filter, cart panel, theme toggle, newsletter form."),
]
for i, (title, body) in enumerate(right_cards_b):
    ty = 2.0 + i * 1.22
    add_rect(sl, 6.3, ty, 6.7, 1.1, SB_CARD)
    add_rect(sl, 6.3, ty, 0.07, 1.1, SB_ACCENT)
    add_text(sl, title, 6.5, ty+0.05, 6.4, 0.32, size=12, bold=True, color=SB_ACCENT)
    add_text(sl, body, 6.5, ty+0.4, 6.4, 0.65, size=11, color=SB_TEXT)

footer_B(sl)
add_notes(sl, """SLIDE 15 — What to say:
"Style Avenue has a clean file structure. All files are in one folder called Myntra-Clone-SRDT."

File descriptions:
- index.html: The main home page. It is the largest HTML file at 8,750 bytes. It has a hero section, animated ticker strip, 4 category tiles, a product section with search and filter, an editorial strip, and a newsletter form.
- men.html, women.html, kids.html, beauty.html: Four collection pages. Each is about 5,000 bytes. They all have the same structure — collection hero, product grid, and collection note — but show different products based on the data-page attribute.
- style.css: The custom stylesheet. 15,473 bytes. Much larger than GlitchLab's CSS because it handles responsive design, cart panel animations, hover effects, dark theme, etc.
- script.js: 166 lines. Contains all JavaScript for the entire website — product data, cart, wishlist, search, filter, theme toggle, and newsletter validation.
- README.md: A markdown file (plain text documentation) that explains the project, how to run it, what technologies are used, and important notes.
- .gitignore: A file that tells Git which files to ignore when uploading to GitHub. This is a standard development practice.
- .git/: A hidden folder created by Git for version control. Not part of the actual website.

Possible teacher questions:
Q: What is a README.md file?
A: README.md is a documentation file written in Markdown format. It explains what the project does, how to run it, what technologies it uses, and any other important information. GitHub displays it automatically on the project page.

Q: What is the .gitignore file?
A: It is a configuration file that tells the Git version control system which files and folders to ignore and not upload. For example, node_modules/ is a common entry — it prevents large library folders from being uploaded unnecessarily.""")

# ─── SLIDE 16 ── Main Features & Functionalities ──────────────────────────────
sl = new_slide(prs)
slide_header_B(sl, 16)
divider_B(sl)

add_text(sl, "Main Features & Functionalities", 0.5, 1.25, 12.5, 0.6,
         size=26, bold=True, color=SB_TEXT)

features_b = [
    ("🛍️  Product Grid & Cards", [
        "10 products stored as JavaScript objects in an array",
        "Each card: product image, category label, name, description, price, tag",
        "Wishlist heart icon + 'ADD +' button on every card",
        "Bootstrap grid: 2 per row (mobile) → 3 (tablet) → 4 (desktop)",
        "Products rendered 100% by JavaScript (not hardcoded in HTML)",
    ]),
    ("🔍  Search & Category Filters", [
        "Live search box — results update instantly as you type",
        "Filter chips: All / Women / Men / Beauty (on home page)",
        "Filters are combined: search text AND category filter both apply",
        "No results message shown when no products match",
        "Result count label shows how many products are visible",
    ]),
    ("🛒  Shopping Bag (Cart)", [
        "Click 'ADD +' — item added to cart array in JavaScript",
        "Cart icon in header shows live item count badge",
        "Bag slide-in panel opens from the right side",
        "Lists all added items with their prices",
        "Subtotal calculated using reduce() method",
        "Note: Demo only — no checkout or payment processing",
    ]),
    ("❤️  Wishlist Toggle", [
        "Every product card has a heart (♡) icon button",
        "Click to save: heart becomes solid red (fa-solid fa-heart)",
        "Click again to unsave: heart returns to outline (fa-regular)",
        "Wishlist stored as an array of product IDs in JavaScript",
        "State is preserved while you stay on the page",
    ]),
    ("🌙  Dark / Light Theme", [
        "Moon icon button in the header — 'Theme'",
        "Toggles class 'dark-theme' on the body element",
        "All pages respond to dark theme through CSS",
        "Button icon switches: moon ↔ sun based on current mode",
        "Smooth colour transition using CSS transition property",
    ]),
    ("📧  Newsletter Form", [
        "Email input in the footer of every page",
        "JavaScript validates: must contain '@' and '.' symbols",
        "Valid email: 'Thank you! You are on the style list.' shown",
        "Invalid email: 'Please enter a valid email address.' shown",
        "Form resets after successful submission",
        "Toast notifications for cart actions (pop-up messages)",
    ]),
]

for i, (title, pts) in enumerate(features_b):
    col_idx = i % 3
    row_idx = i // 3
    lx = 0.5 + col_idx * 4.3
    ty = 2.0 + row_idx * 2.9
    add_rect(sl, lx, ty, 4.1, 2.6, SB_CARD)
    add_rect(sl, lx, ty, 4.1, 0.42, SB_HDR)
    add_text(sl, title, lx+0.12, ty+0.05, 3.85, 0.32, size=12, bold=True, color=SB_ACCENT)
    for j, pt in enumerate(pts[:5]):
        add_text(sl, f"▸  {pt}", lx+0.12, ty+0.52 + j*0.42, 3.85, 0.38, size=10.5, color=SB_TEXT)

footer_B(sl)
add_notes(sl, """SLIDE 16 — What to say:
"Style Avenue has six main features. These are all fully implemented and working in the browser."

1. Product Grid:
   - 10 products are stored as objects in a JavaScript array.
   - script.js dynamically creates HTML product cards using template literals and injects them into the page.
   - The HTML product grid is EMPTY in the HTML file — JavaScript fills it in.

2. Search & Filters:
   - There is a search box. When you type, the renderProducts() function runs again and filters the products array.
   - On the home page, there are also filter chips (All, Women, Men, Beauty).
   - Both search AND filter work together at the same time.

3. Shopping Bag:
   - Clicking 'ADD +' on a product card calls addToCart() in JavaScript.
   - The product object is pushed into the cart array.
   - The cart count badge on the bag icon updates.
   - Clicking the bag icon opens a slide-in panel on the right.
   - The subtotal is calculated using cart.reduce((sum, item) => sum + item.price, 0).
   - IMPORTANT: This is a DEMO bag. There is no real checkout or payment.

4. Wishlist:
   - Each product card has a heart button.
   - Clicking it toggles the product ID in a wishlist array.
   - If the ID is already in the array, it is removed (unsaved). If not, it is added.
   - The heart icon switches between solid (saved) and outline (not saved) using Font Awesome classes.

5. Dark/Light Theme:
   - The moon button toggles class 'dark-theme' on the body.
   - CSS has styles for body.dark-theme that change background, card colours, text, etc.

6. Newsletter Form:
   - JavaScript checks if the email contains '@' and '.'.
   - Shows a success or error message below the form.
   - Toast notifications pop up briefly when you add an item to the bag.

Possible teacher questions:
Q: How are product cards created?
A: The product data is stored as a JavaScript array of objects. The renderProducts() function loops through the filtered products using for...of, builds an HTML string using template literals, and sets the productGrid.innerHTML to that string.

Q: How does the cart calculate the total price?
A: JavaScript's reduce() method is used. It goes through each item in the cart array and adds its price to a running total, starting from 0. The result is formatted with the ₹ symbol using the formatPrice() function.""")

# ─── SLIDE 17 ── UI/UX & Design Implementation ────────────────────────────────
sl = new_slide(prs)
slide_header_B(sl, 17)
divider_B(sl)

add_text(sl, "UI/UX & Design Implementation", 0.5, 1.25, 12.5, 0.6,
         size=26, bold=True, color=SB_TEXT)

# Colour palette
add_rect(sl, 0.5, 2.0, 12.33, 1.1, SB_CARD)
add_rect(sl, 0.5, 2.0, 0.07, 1.1, SB_ACCENT)
add_text(sl, "COLOUR PALETTE", 0.65, 2.05, 3, 0.32, size=12, bold=True, color=SB_ACCENT)
swatches = [
    (SB_HDR,                            "#1A1A2E  Dark Navy — primary background"),
    (SB_ACCENT,                         "#E94F78  Rose Pink — primary accent"),
    (SB_ACCENT2,                        "#F5F0E8  Cream — card backgrounds"),
    (RGBColor(0xFF,0xFF,0xFF),          "#FFFFFF  White — main bg (light mode)"),
    (RGBColor(0x2D,0x6A,0x4F),         "#2D6A4F  Green — men category accent"),
]
for i, (clr, label) in enumerate(swatches):
    lx = 0.65 + i * 2.42
    add_rect(sl, lx, 2.4, 2.1, 0.5, clr)
    add_text(sl, label, lx, 2.92, 2.3, 0.2, size=8, color=SB_TEXT)

# Left — UI layout
add_rect(sl, 0.5, 3.2, 5.9, 3.7, SB_CARD)
add_rect(sl, 0.5, 3.2, 5.9, 0.4, SB_HDR)
add_text(sl, "LAYOUT & RESPONSIVE DESIGN", 0.65, 3.25, 5.6, 0.3, size=12, bold=True, color=SB_ACCENT)

layout_b = [
    ("HEADER (all pages):", True, 13, SB_ACCENT),
    ("▸  Brand logo left  |  Main nav centre  |  Theme + Bag icons right", False, 12, SB_TEXT),
    ("▸  Mobile nav bar below header for small screens", False, 12, SB_TEXT),
    ("", False, 5, SB_TEXT),
    ("HOME PAGE SECTIONS:", True, 13, SB_ACCENT),
    ("▸  Hero — split layout: left copy + right image", False, 12, SB_TEXT),
    ("▸  Animated Ticker strip — NEW SEASON · FRESH FINDS · etc.", False, 12, SB_TEXT),
    ("▸  Category grid — 2×2 image tiles (CSS Grid)", False, 12, SB_TEXT),
    ("▸  Home feature — editorial image + text side by side", False, 12, SB_TEXT),
    ("▸  Product section — search bar + filter chips + product grid", False, 12, SB_TEXT),
    ("", False, 5, SB_TEXT),
    ("BOOTSTRAP RESPONSIVE GRID:", True, 13, SB_ACCENT),
    ("▸  col-6 → 2 products per row on mobile", False, 12, SB_TEXT),
    ("▸  col-md-4 → 3 products per row on tablet", False, 12, SB_TEXT),
    ("▸  col-lg-3 → 4 products per row on desktop", False, 12, SB_TEXT),
    ("▸  CSS media queries for header, hero, and category tiles", False, 12, SB_TEXT),
]
add_text_multiline(sl, layout_b, 0.65, 3.65, 5.6, 3.1)

# Right — typography & components
add_rect(sl, 6.6, 3.2, 6.4, 3.7, SB_CARD)
add_rect(sl, 6.6, 3.2, 6.4, 0.4, SB_HDR)
add_text(sl, "TYPOGRAPHY & UI COMPONENTS", 6.75, 3.25, 6.1, 0.3, size=12, bold=True, color=SB_ACCENT)

ui_pts = [
    ("FONTS:", True, 13, SB_ACCENT),
    ("▸  DM Sans — body text, navigation, buttons, prices", False, 12, SB_TEXT),
    ("▸  Playfair Display — hero headings (elegant serif look)", False, 12, SB_TEXT),
    ("", False, 5, SB_TEXT),
    ("CART PANEL:", True, 13, SB_ACCENT),
    ("▸  Slides in from right using CSS transform: translateX()", False, 12, SB_TEXT),
    ("▸  .open class added/removed by JavaScript", False, 12, SB_TEXT),
    ("", False, 5, SB_TEXT),
    ("TOAST NOTIFICATION:", True, 13, SB_ACCENT),
    ("▸  Pops up at bottom of screen when item added to bag", False, 12, SB_TEXT),
    ("▸  Automatically disappears after 2.2 seconds (setTimeout)", False, 12, SB_TEXT),
    ("", False, 5, SB_TEXT),
    ("HOVER EFFECTS:", True, 13, SB_ACCENT),
    ("▸  Product cards lift on hover (CSS transform + box-shadow)", False, 12, SB_TEXT),
    ("▸  Category tiles have image zoom on hover (transform: scale)", False, 12, SB_TEXT),
    ("", False, 5, SB_TEXT),
    ("DARK MODE:", True, 13, SB_ACCENT),
    ("▸  body.dark-theme class → all dark background + light text", False, 12, SB_TEXT),
    ("▸  Card backgrounds, header, footer all respond to dark class", False, 12, SB_TEXT),
]
add_text_multiline(sl, ui_pts, 6.75, 3.65, 6.1, 3.1)

footer_B(sl)
add_notes(sl, """SLIDE 17 — What to say:
"Let me explain the visual design and user interface of Style Avenue."

Colour palette:
- The main colour is a deep navy (#1A1A2E) used for the header and footer.
- The accent colour is rose pink (#E94F78) used for buttons, links, and highlights.
- Product cards have a cream/off-white background (#F5F0E8) for a fashion editorial feel.
- DM Sans is used for all body text — it is a clean, modern sans-serif font.
- Playfair Display is used for the main hero headings — it is an elegant serif font that gives a high-fashion magazine feel.

Layout:
- The header has three parts: logo on the left, navigation in the centre, action buttons (Theme + Bag) on the right — using Flexbox.
- The home page has a split hero: left side has the headline and buttons, right side has the fashion image.
- The category grid uses CSS Grid to arrange 4 image tiles in a 2×2 layout.

Responsive design (this is implemented unlike GlitchLab):
- Bootstrap col-6 col-md-4 col-lg-3 grid classes are used on product cards.
- On a mobile phone: 2 products per row.
- On a tablet: 3 products per row.
- On desktop: 4 products per row.
- There are also custom CSS media queries for the header and hero section.

UI Components:
- Cart Panel: Slides in from the right side using CSS transform: translateX(). When the .open class is added by JavaScript, the panel moves into view.
- Toast: A small notification bar pops up at the bottom for 2.2 seconds when you add an item to the bag. It uses window.setTimeout() to auto-dismiss.

Possible teacher questions:
Q: How does the cart panel slide in?
A: The cart panel div is positioned off-screen to the right using CSS transform: translateX(100%). When the bag icon is clicked, JavaScript adds the .open class to the panel. The CSS for .cart-panel.open sets transform: translateX(0), bringing it into view. The transition property makes this smooth.

Q: What fonts are used and why?
A: DM Sans (from Google Fonts) is used for body text — it is a clean, modern font that works well for interface text. Playfair Display is used for headings — it is an elegant serif font that gives a premium fashion magazine look, appropriate for a fashion e-commerce website.""")

# ─── SLIDE 18 ── Technical Implementation ─────────────────────────────────────
sl = new_slide(prs)
slide_header_B(sl, 18)
divider_B(sl)

add_text(sl, "Technical Implementation & Working Methodology", 0.5, 1.25, 12.5, 0.6,
         size=26, bold=True, color=SB_TEXT)

# Products data
add_rect(sl, 0.5, 2.0, 5.9, 2.0, SB_CARD)
add_rect(sl, 0.5, 2.0, 5.9, 0.38, SB_HDR)
add_text(sl, "Product Data — JavaScript Array of Objects", 0.65, 2.05, 5.6, 0.28, size=12, bold=True, color=SB_ACCENT)
add_text(sl, 'const products = [\n  { id:1, name:"Relaxed Fit Shirt", category:"men",\n    price:1299, tag:"BESTSELLER",\n    description:"An easy layer for everyday plans.",\n    image: "https://images.unsplash.com/..." },\n  { id:3, name:"Modern Day Dress", category:"women",\n    price:1599, tag:"NEW", ... },\n  // ... 10 products total\n];',
         0.65, 2.42, 5.6, 1.5, size=11, color=RGBColor(0xE9,0x4F,0x78), font_name="Courier New")

# Render products
add_rect(sl, 0.5, 4.1, 5.9, 2.8, SB_CARD)
add_rect(sl, 0.5, 4.1, 5.9, 0.38, SB_HDR)
add_text(sl, "renderProducts() — Filter + Build Cards", 0.65, 4.15, 5.6, 0.28, size=12, bold=True, color=SB_ACCENT)
add_text(sl, 'function renderProducts() {\n  const page = document.body.dataset.page;\n  let visible = products.filter((item) => {\n    const pageMatch = page==="home" ? true\n                      : item.category === page;\n    const filterMatch = activeFilter==="all"\n                        || item.category===activeFilter;\n    const searchMatch = (item.name + " " + item.description)\n                        .toLowerCase().includes(searchText);\n    return pageMatch && filterMatch && searchMatch;\n  });\n  for (const item of visible) { /* build card HTML */ }\n  grid.innerHTML = cards;\n}',
         0.65, 4.52, 5.6, 2.3, size=10.5, color=RGBColor(0xE9,0x4F,0x78), font_name="Courier New")

# Cart add & total
add_rect(sl, 6.7, 2.0, 6.0, 2.0, SB_CARD)
add_rect(sl, 6.7, 2.0, 6.0, 0.38, SB_HDR)
add_text(sl, "addToCart() + Cart Subtotal (reduce)", 6.85, 2.05, 5.7, 0.28, size=12, bold=True, color=SB_ACCENT)
add_text(sl, 'function addToCart(productId) {\n  const item = getProductById(productId);\n  cart.push(item);\n  updateCart();\n  showToast(item.name + " added to your bag");\n}\n\n// reduce() calculates subtotal:\nconst total = cart.reduce(\n  (sum, item) => sum + item.price, 0\n);\ntotalArea.textContent = formatPrice(total);',
         6.85, 2.42, 5.7, 1.5, size=11, color=RGBColor(0xE9,0x4F,0x78), font_name="Courier New")

# Wishlist toggle
add_rect(sl, 6.7, 4.1, 6.0, 1.3, SB_CARD)
add_rect(sl, 6.7, 4.1, 6.0, 0.38, SB_HDR)
add_text(sl, "toggleWishlist() — Save & Unsave", 6.85, 4.15, 5.7, 0.28, size=12, bold=True, color=SB_ACCENT)
add_text(sl, 'function toggleWishlist(productId) {\n  const id = Number(productId);\n  if (wishlist.includes(id))\n    wishlist = wishlist.filter(x => x !== id);\n  else wishlist.push(id);\n  renderProducts(); // re-draw cards\n}',
         6.85, 4.52, 5.7, 0.84, size=11, color=RGBColor(0xE9,0x4F,0x78), font_name="Courier New")

# Newsletter
add_rect(sl, 6.7, 5.5, 6.0, 1.4, SB_CARD)
add_rect(sl, 6.7, 5.5, 6.0, 0.38, SB_HDR)
add_text(sl, "Newsletter Form Validation", 6.85, 5.55, 5.7, 0.28, size=12, bold=True, color=SB_ACCENT)
add_text(sl, 'newsletterForm.addEventListener("submit",function(e){\n  e.preventDefault();\n  const email = emailInput.value.trim();\n  if (email.includes("@") && email.includes("."))\n    message.textContent = "Thank you! You\'re on the list.";\n  else\n    message.textContent = "Please enter a valid email.";\n  newsletterForm.reset();\n});',
         6.85, 5.92, 5.7, 0.95, size=10.5, color=RGBColor(0xE9,0x4F,0x78), font_name="Courier New")

footer_B(sl)
add_notes(sl, """SLIDE 18 — What to say:
"Let me explain the most important JavaScript functions in Style Avenue."

1. Products Array (top left):
   - All 10 products are stored as JavaScript objects inside an array called 'products'.
   - Each object has: id, name, category, price, tag, description, and image URL.
   - This is the central data source for the entire website.

2. renderProducts() function (bottom left):
   - This is the most important function. It runs every time the page loads, when you search, or when you apply a filter.
   - It reads the data-page attribute from the body tag to know which page it is on.
   - It then filters the products array using THREE conditions: page match (category matches the page), filter match (the active filter chip), and search match (the search text).
   - All three conditions must be true for a product to be shown.
   - Then it loops through the filtered products using for...of, builds an HTML string for each card, and injects it into the product grid div.

3. addToCart() (top right):
   - When 'ADD +' is clicked, addToCart() is called with the product's ID.
   - It finds the product object using getProductById() (which uses the find() array method).
   - It pushes the product object into the cart array.
   - Then updateCart() is called to refresh the cart count and subtotal.
   - reduce() calculates the total by adding all item prices together starting from 0.

4. toggleWishlist() (middle right):
   - Checks if the product ID is already in the wishlist array using includes().
   - If yes: removes it using filter() to create a new array without that ID.
   - If no: pushes the ID into the wishlist array.
   - Then calls renderProducts() to redraw the cards with the updated heart icon state.

5. Newsletter Validation (bottom right):
   - Uses event.preventDefault() to stop page reload.
   - Checks if the email string includes both '@' and '.' characters.
   - Shows an appropriate message, then resets the form.

Possible teacher questions:
Q: What is event delegation and how is it used here?
A: Event delegation means putting one event listener on a parent element instead of many listeners on individual child elements. In this project, one click listener is added to the product grid div. When a user clicks ADD+ or the heart icon, the event bubbles up to the grid. JavaScript then checks event.target.closest('[data-add]') to find which button was actually clicked.

Q: What does includes() do in the wishlist check?
A: Array.includes(value) returns true if the value exists in the array, and false if it does not. It is used to check if a product's ID is already in the wishlist array before deciding to add or remove it.""")

# ─── SLIDE 19 ── Workflow, Testing & Results ───────────────────────────────────
sl = new_slide(prs)
slide_header_B(sl, 19)
divider_B(sl)

add_text(sl, "Project Workflow, Testing & Results", 0.5, 1.25, 12.5, 0.6,
         size=26, bold=True, color=SB_TEXT)

# Left workflow
add_rect(sl, 0.5, 2.0, 5.5, 4.9, SB_CARD)
add_rect(sl, 0.5, 2.0, 5.5, 0.4, SB_HDR)
add_text(sl, "USER EXPERIENCE FLOW", 0.65, 2.05, 5.2, 0.3, size=13, bold=True, color=SB_ACCENT)

flow_b = [
    ("01", "Open index.html — home page loads with hero section"),
    ("02", "Products render automatically in 'Popular Picks' section"),
    ("03", "Click a category tile (e.g. Women) → women.html loads"),
    ("04", "Women's products appear in a 4-column Bootstrap grid"),
    ("05", "Type in search box → products filter as you type"),
    ("06", "Click heart icon → product saved to wishlist (solid heart)"),
    ("07", "Click 'ADD +' → item added to bag, toast pops up"),
    ("08", "Click bag icon → cart panel slides in from right"),
    ("09", "See all added items and subtotal (₹) in cart panel"),
    ("10", "Click moon icon → dark theme activates across all elements"),
    ("11", "Scroll to footer → fill newsletter form, validation works"),
]
for i, (num, desc) in enumerate(flow_b):
    ty = 2.48 + i * 0.42
    add_rect(sl, 0.65, ty, 0.52, 0.32, SB_ACCENT)
    add_text(sl, num, 0.67, ty+0.03, 0.49, 0.26, size=11, bold=True, color=RGBColor(0xFF,0xFF,0xFF), align=PP_ALIGN.CENTER)
    add_text(sl, desc, 1.24, ty+0.03, 4.6, 0.33, size=11, color=SB_TEXT)

# Right
add_rect(sl, 6.3, 2.0, 6.7, 2.4, SB_CARD)
add_rect(sl, 6.3, 2.0, 6.7, 0.4, SB_HDR)
add_text(sl, "TESTING OBSERVATIONS", 6.45, 2.05, 6.4, 0.3, size=13, bold=True, color=SB_ACCENT)
add_bullet_B(sl, [
    "All 5 pages load correctly in Chrome, Edge, and Firefox",
    "Products render correctly on each category page",
    "Search box filters products correctly in real time",
    "Filter chips (All/Women/Men/Beauty) work on home page",
    "Wishlist heart toggle works — saves and unsaves correctly",
    "Cart badge count updates correctly with each add",
    "Cart panel slides in with correct items and subtotal",
    "Dark/light theme toggle works across all pages",
    "Newsletter form validates correct and incorrect emails",
    "Toast messages appear and disappear after 2.2 seconds",
    "Bootstrap grid: 4 → 3 → 2 columns on resize verified",
], 6.45, 2.45, 6.4, 1.9, size=11)

add_rect(sl, 6.3, 4.5, 6.7, 1.5, SB_CARD)
add_rect(sl, 6.3, 4.5, 6.7, 0.4, SB_HDR)
add_text(sl, "KNOWN LIMITATIONS", 6.45, 4.55, 6.4, 0.3, size=13, bold=True, color=RGBColor(0xE9,0x4F,0x78))
add_bullet_B(sl, [
    "No backend — cart, wishlist, and search are front-end only",
    "Cart data is lost when page is reloaded (not saved in localStorage)",
    "No real checkout or payment gateway implemented",
    "Product images are loaded from Unsplash — requires internet connection",
    "Only 10 sample products — not a real inventory",
], 6.45, 4.95, 6.4, 1.0, size=11)

add_rect(sl, 6.3, 6.1, 6.7, 0.85, SB_CARD)
add_rect(sl, 6.3, 6.1, 0.07, 0.85, SB_ACCENT)
add_text(sl, "ACTUAL RESULTS", 6.5, 6.12, 6.4, 0.3, size=12, bold=True, color=SB_ACCENT)
add_text(sl, "Style Avenue successfully demonstrates a fully interactive front-end fashion store. All features work as designed. This is a comprehensive demonstration of HTML, CSS, Bootstrap, and JavaScript working together.", 6.5, 6.44, 6.4, 0.5, size=10.5, color=SB_TEXT)

footer_B(sl)
add_notes(sl, """SLIDE 19 — What to say:
"Let me walk you through how a user would experience Style Avenue from start to finish."

User flow explanation:
1. User opens index.html. The home page loads with the hero section and products are automatically rendered by JavaScript in the 'Popular Picks' section.
2. Click on a category tile (e.g., Women) — navigates to women.html. Products are automatically filtered to show only women's items.
3. Type in the search box — products filter in real time as you type.
4. Click the heart icon on a product — it saves the product to the wishlist. The heart turns solid.
5. Click 'ADD +' on a product — a toast notification pops up at the bottom. The bag icon count increases.
6. Click the bag icon in the header — the cart panel slides in from the right, showing all added items and the subtotal.
7. Click the moon icon — dark theme activates. All backgrounds turn dark.
8. Scroll to footer — fill the email form. If a valid email is entered, a success message appears.

Testing:
- Tested in Chrome, Edge, Firefox — all features work.
- Bootstrap grid responsiveness verified — layout changes correctly at different screen widths.

Limitations (be honest):
- No backend: data is not saved to any server or database.
- Cart data is lost on page refresh because it is stored in a JavaScript array (RAM), not localStorage.
- Product images require internet — they load from Unsplash CDN.
- Only 10 sample products exist.

Possible teacher questions:
Q: What happens to the cart if the user refreshes the page?
A: The cart data is lost because it is stored in a JavaScript array in memory. When the page refreshes, the JavaScript restarts and the array is empty again. To fix this, localStorage could be used to save cart data in the browser.

Q: Does Style Avenue work offline?
A: The HTML, CSS, and JavaScript work offline, but product images, Bootstrap, Font Awesome, and Google Fonts are loaded from CDN servers on the internet. If there is no internet connection, images and icons would not appear.""")

# ─── SLIDE 20 ── Conclusion, Future Scope & Viva Prep ─────────────────────────
sl = new_slide(prs)
slide_header_B(sl, 20)
divider_B(sl)

add_text(sl, "Conclusion, Future Scope & Viva Preparation", 0.5, 1.25, 12.5, 0.6,
         size=26, bold=True, color=SB_TEXT)

# Left
add_rect(sl, 0.5, 2.0, 5.9, 4.9, SB_CARD)
add_rect(sl, 0.5, 2.0, 5.9, 0.4, SB_HDR)
add_text(sl, "KEY LEARNING OUTCOMES", 0.65, 2.05, 5.6, 0.3, size=13, bold=True, color=SB_ACCENT)
add_bullet_B(sl, [
    "Built a complete 5-page front-end e-commerce website",
    "Understood Bootstrap grid system (col-6, col-md-4, col-lg-3)",
    "Learned how to use external libraries via CDN links",
    "Practised all major JavaScript array methods: filter, map, find, reduce, forEach",
    "Applied multiple loop types: for...of, for...in, do...while",
    "Built real interactive features: cart, wishlist, search, filters",
    "Understood DOM manipulation: innerHTML, createElement, appendChild",
    "Learned event delegation to handle dynamically created buttons",
    "Implemented form validation without any external library",
    "Understood data-attribute pattern (data-page, data-filter, data-add)",
    "Practised clean code organisation and proper comment structure",
], 0.65, 2.45, 5.6, 4.35, size=11.5)

# Right top — future
add_rect(sl, 6.7, 2.0, 6.3, 2.5, SB_CARD)
add_rect(sl, 6.7, 2.0, 6.3, 0.4, SB_HDR)
add_text(sl, "FUTURE IMPROVEMENTS", 6.85, 2.05, 6.0, 0.3, size=13, bold=True, color=SB_ACCENT)
add_bullet_B(sl, [
    "Save cart and wishlist to localStorage so data persists on refresh",
    "Add a real product detail / individual item page",
    "Add quantity controls (+/-) in the cart panel",
    "Connect to a backend (Node.js + Express + MongoDB) for real data",
    "Add a user login/signup system",
    "Add a real payment gateway (e.g. Razorpay API for India)",
    "Add product sorting: price low-high, high-low, newest first",
    "Add more products and product categories",
], 6.85, 2.48, 6.0, 2.0, size=12)

# Right bottom — viva
add_rect(sl, 6.7, 4.6, 6.3, 2.3, SB_CARD)
add_rect(sl, 6.7, 4.6, 6.3, 0.4, SB_HDR)
add_text(sl, "QUICK VIVA PREPARATION", 6.85, 4.65, 6.0, 0.3, size=13, bold=True, color=SB_ACCENT)
viva = [
    ("What is Style Avenue?", "A 5-page Myntra-inspired fashion store built with HTML, CSS, Bootstrap, and JavaScript."),
    ("What does data-page do?", "Tells JavaScript which category page is active so it shows the right products."),
    ("How does search work?", "search.addEventListener('input') calls renderProducts() which filters the array."),
    ("What does reduce() do?", "Calculates cart total by adding each item's price: cart.reduce((sum,item)=>sum+item.price, 0)"),
    ("Is checkout real?", "No. The bag and wishlist are front-end demos. No payment gateway is implemented."),
]
for i, (q, a) in enumerate(viva):
    ty = 5.05 + i * 0.37
    add_text(sl, f"Q: {q}", 6.85, ty, 6.0, 0.18, size=10, bold=True, color=SB_ACCENT)
    add_text(sl, f"A: {a}", 6.85, ty+0.18, 6.0, 0.17, size=10, color=SB_TEXT)

footer_B(sl)
add_notes(sl, """SLIDE 20 — What to say:
"Let me summarise what Style Avenue demonstrates and what can be improved in the future."

What to say about learning outcomes:
- This project taught me how a real front-end e-commerce website works.
- I learnt how to store product data as JavaScript objects in an array.
- I learnt how to dynamically create HTML cards from JavaScript — this is how modern websites like Myntra actually work.
- I understood how filter(), map(), and reduce() make data operations easy.
- I learnt Bootstrap's grid system for responsive layouts without writing custom media queries for every element.
- I learnt event delegation — one listener handling many dynamic buttons.
- I understood the data-attribute pattern for communicating between HTML and JavaScript.

Future scope explanation:
- The biggest improvement would be adding a backend (server + database).
- Right now, refreshing the page loses the cart. localStorage would fix this easily.
- Adding real products, a login system, and a payment gateway would make it a real e-commerce site.

Viva quick answers:
1. What is Style Avenue? → A front-end fashion store with 5 pages, 10 products, cart, wishlist, search, filters, and dark mode.
2. What does data-page do? → HTML body attribute. JavaScript reads it to know which category page is active and filters products accordingly.
3. How does search work? → The search input has an event listener for 'input'. Every time you type, renderProducts() runs and filters the products array where the name or description includes the search text.
4. What does reduce() do in this project? → Calculates the cart total by looping through all cart items and summing their prices.
5. Is checkout real? → No. The bag is a demonstration. There is no real payment gateway, server, or database.

Final statement to teacher:
"Both GlitchLab and Style Avenue together cover all major HTML, CSS, and JavaScript concepts, from basic structure and styling to advanced DOM manipulation, array methods, and external library integration. I am happy to demonstrate any feature live."

Possible teacher questions:
Q: What is the most advanced JavaScript concept used in Style Avenue?
A: Event delegation — adding one click listener on the product grid to handle all ADD+ buttons and heart buttons that are dynamically created by JavaScript. This is better than adding individual listeners to each button.

Q: If you had to pick one improvement, what would it be?
A: I would add localStorage to save the cart and wishlist data. This would make the user experience much better because the cart would not be lost when the page refreshes. This requires just a few lines of JSON.stringify and JSON.parse to save and load from the browser's local storage.""")

# ─── SAVE ─────────────────────────────────────────────────────────────────────
out_path = r"C:\Users\shriy\OneDrive\Desktop\genAI mini project\Two_Projects_Professional_Presentation.pptx"
prs.save(out_path)
print(f"Saved: {out_path}")
print(f"Total slides: {len(prs.slides)}")
