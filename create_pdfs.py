"""
Generate both PDF documents for the two projects:
1. Project_Explanation_Quick_Guide.pdf
2. Project_Comparison_Quick_Reference.pdf
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, HRFlowable, PageBreak, KeepTogether)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import ListFlowable, ListItem

# ─── COLOURS ───────────────────────────────────────────────────────────────────
COL_GA_BG     = colors.HexColor("#0D0918")
COL_GA_ACC    = colors.HexColor("#C77DFF")
COL_GA_GOLD   = colors.HexColor("#FFD166")
COL_GA_DARK   = colors.HexColor("#171027")
COL_GA_LIGHT  = colors.HexColor("#E0AAFF")

COL_SB_NAVY   = colors.HexColor("#1A1A2E")
COL_SB_ROSE   = colors.HexColor("#E94F78")
COL_SB_CREAM  = colors.HexColor("#F5F0E8")

COL_WHITE     = colors.white
COL_GRAY      = colors.HexColor("#555566")
COL_LGRAY     = colors.HexColor("#EEEEEE")

# ════════════════════════════════════════════════════════════════════════════════
#  PDF 1 — Project_Explanation_Quick_Guide.pdf
# ════════════════════════════════════════════════════════════════════════════════

out1 = r"C:\Users\shriy\OneDrive\Desktop\genAI mini project\Project_Explanation_Quick_Guide.pdf"
doc1 = SimpleDocTemplate(out1, pagesize=A4,
                          leftMargin=2*cm, rightMargin=2*cm,
                          topMargin=2*cm, bottomMargin=2*cm)

styles = getSampleStyleSheet()

def S(name, **kw):
    return ParagraphStyle(name, **kw)

# Custom styles
H1 = S("H1", fontSize=22, textColor=COL_GA_ACC, spaceAfter=6, fontName="Helvetica-Bold", alignment=TA_CENTER)
H1b = S("H1b", fontSize=22, textColor=COL_SB_ROSE, spaceAfter=6, fontName="Helvetica-Bold", alignment=TA_CENTER)
H2 = S("H2", fontSize=16, textColor=COL_GA_DARK, spaceAfter=4, fontName="Helvetica-Bold", backColor=COL_GA_ACC,
        leftIndent=0, rightIndent=0, leading=20, borderPad=4)
H2b = S("H2b", fontSize=16, textColor=COL_WHITE, spaceAfter=4, fontName="Helvetica-Bold", backColor=COL_SB_ROSE,
        leading=20, borderPad=4)
H3 = S("H3", fontSize=13, textColor=COL_GA_ACC, spaceAfter=2, fontName="Helvetica-Bold")
H3b = S("H3b", fontSize=13, textColor=COL_SB_ROSE, spaceAfter=2, fontName="Helvetica-Bold")
BODY = S("BODY", fontSize=10.5, textColor=colors.HexColor("#222233"), spaceAfter=4, leading=15, alignment=TA_JUSTIFY)
BULLET = S("BULLET", fontSize=10.5, textColor=colors.HexColor("#222233"), spaceAfter=3, leading=15,
           leftIndent=14, bulletIndent=0)
CODE = S("CODE", fontSize=9.5, textColor=colors.HexColor("#1A1A2E"), fontName="Courier",
         backColor=colors.HexColor("#F0F0F5"), borderPad=4, spaceAfter=4, leading=13)
NOTE = S("NOTE", fontSize=9.5, textColor=colors.HexColor("#555566"), spaceAfter=3, leading=14, leftIndent=10)
VIVA_Q = S("VIVA_Q", fontSize=10.5, textColor=COL_SB_ROSE, fontName="Helvetica-Bold", spaceAfter=1, leading=15)
VIVA_A = S("VIVA_A", fontSize=10.5, textColor=colors.HexColor("#222233"), spaceAfter=6, leading=15, leftIndent=12)

def p(text, style=None):
    return Paragraph(text, style or BODY)

def h2(text, is_b=False):
    st = H2b if is_b else H2
    color = COL_WHITE if is_b else COL_WHITE
    filled = f"<font color='white'>&nbsp;&nbsp;{text}&nbsp;</font>"
    return Paragraph(filled, st)

def hr(c=COL_GA_ACC, t=1.5):
    return HRFlowable(width="100%", thickness=t, color=c, spaceAfter=4, spaceBefore=4)

def bullet(items, is_b=False):
    color = "#1A1A2E" if is_b else "#1A1A2E"
    result = []
    for item in items:
        result.append(p(f"<font color='{('#E94F78' if is_b else '#C77DFF')}'>▸</font>&nbsp;&nbsp;{item}", BULLET))
    return result

def viva_qa(pairs, is_b=False):
    result = []
    for q, a in pairs:
        result.append(p(f"<b>Q: {q}</b>", VIVA_Q if is_b else S("VQ", fontSize=10.5, textColor=COL_GA_ACC, fontName="Helvetica-Bold", spaceAfter=1, leading=15)))
        result.append(p(f"A: {a}", VIVA_A))
    return result

def spacer(h=0.3):
    return Spacer(1, h*cm)

# ─── BUILD CONTENT ────────────────────────────────────────────────────────────
story1 = []

# Cover
story1.append(spacer(0.5))
story1.append(p("<b>PROJECT EXPLANATION QUICK GUIDE</b>",
                S("COVER", fontSize=24, textColor=COL_GA_ACC, alignment=TA_CENTER, fontName="Helvetica-Bold", spaceAfter=4)))
story1.append(p("Two Web Development Projects — B.Tech Presentation Reference",
                S("SUB", fontSize=13, textColor=COL_GRAY, alignment=TA_CENTER, spaceAfter=4)))
story1.append(hr(COL_GA_ACC, 2))
story1.append(p("This guide explains both projects in simple language to help you present confidently to your faculty.",
                S("INTRO", fontSize=11, textColor=colors.HexColor("#222233"), alignment=TA_CENTER, spaceAfter=8, leading=16)))
story1.append(hr(COL_GA_ACC, 0.5))
story1.append(spacer(0.3))

# ═══════════════════ PROJECT 1 — GLITCHLAB ═══════════════════════════════════
story1.append(p("<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>",
                S("SEP", fontSize=10, textColor=COL_GA_ACC, alignment=TA_CENTER, spaceAfter=2)))
story1.append(p("<b>PROJECT 1 — GLITCHLAB</b>",
                S("PROJ", fontSize=18, textColor=COL_GA_ACC, alignment=TA_CENTER, fontName="Helvetica-Bold", spaceAfter=4)))
story1.append(p("<b>A Multi-Theme Creative Web Experiment</b>",
                S("PROJSUB", fontSize=12, textColor=COL_GRAY, alignment=TA_CENTER, spaceAfter=6)))
story1.append(hr(COL_GA_ACC))

# 1.1 Overview
story1.append(h2("1.1  What Is GlitchLab?"))
story1.append(spacer(0.1))
story1.append(p("GlitchLab is a front-end only website that lets users explore three different visual design themes — Minimal, Retro, and Glitch. Each theme has its own look and feel. The home page (index.html) acts as a hub where users choose their theme by clicking a card. All four pages share one CSS file (style.css) and one JavaScript file (script.js)."))
story1.append(spacer(0.2))

# 1.2 Files
story1.append(h2("1.2  Project Files"))
story1.append(spacer(0.1))
file_data = [
    ["File", "Size", "Purpose"],
    ["index.html", "4,515 bytes", "Home page — hero, world cards, interactive tools in footer"],
    ["minimal.html", "~2,200 bytes", "Minimal green theme page"],
    ["retro.html", "~3,100 bytes", "Retro vintage warm theme page"],
    ["glitch.html", "~3,100 bytes", "Glitch neon dark theme page"],
    ["style.css", "12,129 bytes\n701 lines", "Master stylesheet for ALL pages — themed by body class"],
    ["script.js", "2,521 bytes\n86 lines", "JavaScript: dark mode, colour palette, form validation"],
]
t1 = Table(file_data, colWidths=[4*cm, 3.5*cm, 10*cm])
t1.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), COL_GA_ACC),
    ("TEXTCOLOR", (0,0), (-1,0), COL_WHITE),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,0), 10),
    ("ALIGN", (0,0), (-1,-1), "LEFT"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("FONTSIZE", (0,1), (-1,-1), 9.5),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [COL_LGRAY, COL_WHITE]),
    ("GRID", (0,0), (-1,-1), 0.5, COL_GRAY),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
story1.append(t1)
story1.append(spacer(0.2))

# 1.3 How themes work
story1.append(h2("1.3  How the CSS Theming System Works"))
story1.append(spacer(0.1))
story1.append(p("The secret is the class name on the &lt;body&gt; tag. Each HTML page has a different class:"))
story1.append(p('<font face="Courier" size="9">minimal.html → &lt;body class="minimal-theme"&gt;<br/>retro.html → &lt;body class="retro-theme"&gt;<br/>glitch.html → &lt;body class="glitch-theme"&gt;</font>', CODE))
story1.append(p("The CSS file has separate sections for each class. When a browser reads the class name, it applies only that section's styles — this is how the same file produces three completely different visual designs."))
story1.append(spacer(0.2))

# 1.4 Three themes explained
story1.append(h2("1.4  The Three Themes Explained"))
story1.append(spacer(0.1))
theme_table = [
    ["Theme", "Background", "Main Accent", "Font", "Mood"],
    ["Minimal", "#F5F0E8 (Cream)", "#344E41 (Forest Green)", "Georgia serif", "Calm, clean, airy"],
    ["Retro", "#241025 (Dark Maroon)", "#FFD166 (Gold)", "Georgia serif", "Vintage, warm, bold"],
    ["Glitch", "#080B16 (Near Black)", "#00F5FF (Neon Cyan)", "Courier New mono", "Futuristic, cyber, neon"],
]
tt = Table(theme_table, colWidths=[3*cm, 4*cm, 4*cm, 3.5*cm, 3*cm])
tt.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), COL_GA_DARK),
    ("TEXTCOLOR", (0,0), (-1,0), COL_GA_GOLD),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,0), 10),
    ("FONTSIZE", (0,1), (-1,-1), 9.5),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [COL_LGRAY, COL_WHITE]),
    ("GRID", (0,0), (-1,-1), 0.5, COL_GRAY),
    ("ALIGN", (0,0), (-1,-1), "LEFT"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
story1.append(tt)
story1.append(spacer(0.2))

# 1.5 JS Features
story1.append(h2("1.5  JavaScript Features (script.js)"))
story1.append(spacer(0.1))
js_features = [
    ("Dark / Light Mode Toggle",
     "The 'Switch Theme' button toggles the class 'dark-mode' on the body. If dark-mode class is added → dark background and white text. If removed → original colours return. The button text updates accordingly.",
     'themeButton.addEventListener("click", function() {\n  document.body.classList.toggle("dark-mode");\n});'),
    ("Colour Palette Generator",
     "The 'Generate Colours' button picks 3 random colours from an array of 6 preset hex values. For each colour, a div element is created using document.createElement, its background is set to that colour, and the hex code is shown as text. The div is added to the page using appendChild.",
     'for (let i = 0; i < 3; i++) {\n  const index = Math.floor(Math.random() * colours.length);\n  const box = document.createElement("div");\n  box.style.backgroundColor = colours[index];\n  paletteBox.appendChild(box);\n}'),
    ("Feedback Form Validation",
     "The form has an event listener for 'submit'. event.preventDefault() stops the page from reloading. JavaScript then checks if the name and feedback fields are empty using .trim() === ''. Empty: shows an alert. Filled: shows thank-you message and resets form.",
     'feedbackForm.addEventListener("submit", function(event) {\n  event.preventDefault();\n  if (name.trim() === "" || msg.trim() === "") {\n    alert("Please fill in all fields.");\n  } else {\n    alert("Thank you, " + userName + "!");\n    feedbackForm.reset();\n  }\n});'),
]
for title, desc, code in js_features:
    story1.append(p(f"<b>{title}</b>", H3))
    story1.append(p(desc))
    story1.append(p(code, CODE))
    story1.append(spacer(0.1))

# 1.6 Limitations
story1.append(h2("1.6  Known Limitations"))
story1.append(spacer(0.1))
story1 += bullet([
    "No responsive/mobile design — no CSS media queries. Best viewed on desktop.",
    "Colour palette picks from only 6 preset colours.",
    "Feedback form data is not saved (no backend or localStorage).",
    "Draft files are present in the folder (glitchhh.html, minimall.html, etc.) — these are old working files, not the final project.",
    "The dir_name folder inside GlitchLab is completely empty.",
])
story1.append(spacer(0.2))

# 1.7 Viva QA
story1.append(h2("1.7  Important Viva Questions & Answers"))
story1.append(spacer(0.1))
viva_1 = [
    ("What is GlitchLab?", "A front-end website with 4 pages that demonstrates three visual CSS themes: Minimal, Retro, and Glitch."),
    ("How many files does GlitchLab have?", "4 HTML files (index, minimal, retro, glitch), 1 CSS file (style.css), 1 JavaScript file (script.js)."),
    ("How does the CSS theming work?", "Each HTML page has a unique class on its body tag (e.g., 'glitch-theme'). The single CSS file has separate styling sections for each class name."),
    ("What are the JavaScript features?", "Dark/light mode toggle, random colour palette generator, and feedback form validation."),
    ("What does classList.toggle() do?", "If the class exists on the element, it removes it. If it does not exist, it adds it. This is used for the dark mode feature."),
    ("What does event.preventDefault() do?", "It stops the browser's default action — in a form, this prevents the page from reloading when the form is submitted."),
    ("Is the website responsive?", "No. GlitchLab does not have media queries. The layout is designed for desktop only."),
    ("What does Math.random() do in the palette?", "It generates a random decimal number between 0 and 1. Multiplied by 6 and floored, it gives a random index (0–5) to pick from the colour array."),
    ("What is a limitation of the feedback form?", "The form data is not stored anywhere. It only shows an alert message on the same page. No backend or database is used."),
    ("What would you improve in GlitchLab?", "Add CSS media queries for mobile, use localStorage to save feedback, expand the colour palette to include more colours, and implement single-page theme switching using JavaScript."),
]
story1 += viva_qa(viva_1)
story1.append(spacer(0.5))

# ═══════════════════ PROJECT 2 — STYLE AVENUE ════════════════════════════════
story1.append(PageBreak())
story1.append(p("<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>",
                S("SEP", fontSize=10, textColor=COL_SB_ROSE, alignment=TA_CENTER, spaceAfter=2)))
story1.append(p("<b>PROJECT 2 — STYLE AVENUE</b>",
                S("PROJ2", fontSize=18, textColor=COL_SB_ROSE, alignment=TA_CENTER, fontName="Helvetica-Bold", spaceAfter=4)))
story1.append(p("<b>Myntra-Inspired Fashion Store — Student Learning Project</b>",
                S("PROJSUB2", fontSize=12, textColor=COL_GRAY, alignment=TA_CENTER, spaceAfter=6)))
story1.append(hr(COL_SB_ROSE))

# 2.1 Overview
story1.append(h2("2.1  What Is Style Avenue?", is_b=True))
story1.append(spacer(0.1))
story1.append(p("Style Avenue is a 5-page front-end fashion e-commerce website inspired by Myntra. It includes a home page, and four category pages (Men, Women, Kids, Beauty). It demonstrates product search, category filtering, an add-to-bag cart, wishlist toggling, dark/light theme switching, and newsletter form validation — all built using HTML, CSS, Bootstrap 5, Font Awesome, and JavaScript (ES6+). There is no backend, database, or real payment system — this is a front-end learning project."))
story1.append(spacer(0.2))

# 2.2 Files
story1.append(h2("2.2  Project Files", is_b=True))
story1.append(spacer(0.1))
file_data_b = [
    ["File", "Size", "Purpose"],
    ["index.html", "8,750 bytes", "Home page — hero, ticker, category tiles, product section, editorial strip, newsletter"],
    ["men.html", "~5,000 bytes", "Men's collection hero + product grid + newsletter"],
    ["women.html", "~5,000 bytes", "Women's collection hero + product grid + newsletter"],
    ["kids.html", "~5,000 bytes", "Kids' collection hero + product grid + newsletter"],
    ["beauty.html", "~5,000 bytes", "Beauty collection hero + product grid + newsletter"],
    ["style.css", "15,473 bytes", "All custom CSS — Flexbox, Grid, responsive, dark theme, cart panel animation"],
    ["script.js", "9,663 bytes\n166 lines", "All JavaScript — products array, cart, wishlist, search, filters, theme, newsletter"],
    ["README.md", "2,523 bytes", "Project documentation — setup, features, technologies, credits"],
    [".gitignore", "65 bytes", "Git ignore list — standard development file"],
]
t2 = Table(file_data_b, colWidths=[4*cm, 3.5*cm, 10*cm])
t2.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), COL_SB_ROSE),
    ("TEXTCOLOR", (0,0), (-1,0), COL_WHITE),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,0), 10),
    ("FONTSIZE", (0,1), (-1,-1), 9.5),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [COL_LGRAY, COL_WHITE]),
    ("GRID", (0,0), (-1,-1), 0.5, COL_GRAY),
    ("ALIGN", (0,0), (-1,-1), "LEFT"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
story1.append(t2)
story1.append(spacer(0.2))

# 2.3 Technologies
story1.append(h2("2.3  Technologies Used", is_b=True))
story1.append(spacer(0.1))
tech_table_b = [
    ["Technology", "Role in Project"],
    ["HTML5", "5-page structure, semantic tags, data-page attribute, ARIA accessibility labels"],
    ["CSS3", "Custom styles, Flexbox, CSS Grid, hover effects, dark theme, responsive media queries, cart slide animation"],
    ["Bootstrap 5.3.3 (CDN)", "Responsive grid: col-6 (mobile 2/row) → col-md-4 (tablet 3/row) → col-lg-3 (desktop 4/row)"],
    ["Font Awesome 6.5.2 (CDN)", "Icons: shopping bag, heart (wishlist), moon/sun (theme), arrows, magnifying glass"],
    ["Google Fonts (CDN)", "DM Sans (body text, weights 400–800) + Playfair Display (headings, elegant serif)"],
    ["JavaScript (ES6+)", "Products array, filter/map/find/reduce/forEach, cart, wishlist, search, newsletter validation"],
]
tb = Table(tech_table_b, colWidths=[5*cm, 12.5*cm])
tb.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), COL_SB_NAVY),
    ("TEXTCOLOR", (0,0), (-1,0), COL_SB_ROSE),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,0), 10),
    ("FONTSIZE", (0,1), (-1,-1), 9.5),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [COL_LGRAY, COL_WHITE]),
    ("GRID", (0,0), (-1,-1), 0.5, COL_GRAY),
    ("ALIGN", (0,0), (-1,-1), "LEFT"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
story1.append(tb)
story1.append(spacer(0.2))

# 2.4 Features
story1.append(h2("2.4  Main Features Explained", is_b=True))
story1.append(spacer(0.1))

features_b_text = [
    ("Product Grid (Dynamically Rendered)",
     "10 products are stored as JavaScript objects in the 'products' array. The renderProducts() function filters the array and builds HTML card strings using template literals. These are injected into the product grid div using innerHTML. The product grid in HTML is EMPTY — JavaScript fills it completely.",
     'for (const item of visibleProducts) {\n  cards += `<article class="product-card">...</article>`;\n}\ngrid.innerHTML = cards;'),
    ("Search & Category Filter",
     "Every time the user types in the search box, renderProducts() runs. It filters using THREE combined conditions: (1) page match — the category must match the current page, (2) filter chip match — the selected filter button, (3) search text — the search term must appear in the name or description.",
     'let visible = products.filter((item) => {\n  const pageMatch = page==="home" ? true : item.category===page;\n  const filterMatch = activeFilter==="all" || item.category===activeFilter;\n  const searchMatch = (item.name + " " + item.description)\n                      .toLowerCase().includes(searchText);\n  return pageMatch && filterMatch && searchMatch;\n});'),
    ("Shopping Bag (Cart)",
     "The addToCart() function pushes the product object into the cart array. updateCart() refreshes the cart count badge and subtotal. The subtotal uses reduce() to sum all prices. The cart panel is a div off-screen to the right — clicking the bag button adds the .open class, which uses CSS transform: translateX(0) to slide it into view.",
     'function addToCart(productId) {\n  const item = getProductById(productId);\n  cart.push(item);\n  updateCart();\n  showToast(item.name + " added to your bag");\n}\nconst total = cart.reduce((sum,item)=>sum+item.price, 0);'),
    ("Wishlist Toggle",
     "The wishlist is a JavaScript array of product IDs. When the heart button is clicked, toggleWishlist() checks if the ID is already in the array using includes(). If yes, filter() removes it. If no, push() adds it. Then renderProducts() redraws all cards, switching the heart icon between solid (saved) and outline (not saved).",
     'if (wishlist.includes(id))\n  wishlist = wishlist.filter(x => x !== id);\nelse\n  wishlist.push(id);\nrenderProducts(); // redraw with updated heart state'),
    ("Dark/Light Theme Toggle",
     "The moon icon button toggles class 'dark-theme' on the body element. All CSS rules that start with body.dark-theme { ... } become active. The button icon switches between fa-regular fa-moon and fa-regular fa-sun using innerHTML.",
     'themeButton.addEventListener("click", function() {\n  document.body.classList.toggle("dark-theme");\n  const isDark = document.body.classList.contains("dark-theme");\n  themeButton.innerHTML = isDark ? "sun icon" : "moon icon";\n});'),
    ("Newsletter Form Validation",
     "event.preventDefault() stops the page from reloading. JavaScript checks if the email value includes both '@' and '.' characters. If valid: shows a success message. If not: shows an error message. The form is then reset.",
     'if (email.includes("@") && email.includes("."))\n  message.textContent = "Thank you! You are on the style list.";\nelse\n  message.textContent = "Please enter a valid email address.";'),
]

for title, desc, code in features_b_text:
    story1.append(p(f"<b>{title}</b>", H3b))
    story1.append(p(desc))
    story1.append(p(code, CODE))
    story1.append(spacer(0.15))

# 2.5 Data page system
story1.append(h2("2.5  The data-page System", is_b=True))
story1.append(spacer(0.1))
story1.append(p("Each HTML page sets a data-page attribute on its body tag. JavaScript reads this to automatically show the correct products for each page without changing the script.js code."))
dp_table = [
    ["HTML Page", "data-page Value", "Products Shown"],
    ["index.html", "home", "All 10 products (filtered by selected filter chip)"],
    ["men.html", "men", "Only products where category === 'men'"],
    ["women.html", "women", "Only products where category === 'women'"],
    ["kids.html", "kids", "Only products where category === 'kids'"],
    ["beauty.html", "beauty", "Only products where category === 'beauty'"],
]
dp = Table(dp_table, colWidths=[4.5*cm, 4*cm, 9*cm])
dp.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), COL_SB_ROSE),
    ("TEXTCOLOR", (0,0), (-1,0), COL_WHITE),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,0), 10),
    ("FONTSIZE", (0,1), (-1,-1), 9.5),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [COL_LGRAY, COL_WHITE]),
    ("GRID", (0,0), (-1,-1), 0.5, COL_GRAY),
    ("ALIGN", (0,0), (-1,-1), "LEFT"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
story1.append(dp)
story1.append(spacer(0.2))

# 2.6 Limitations
story1.append(h2("2.6  Known Limitations", is_b=True))
story1.append(spacer(0.1))
story1 += bullet([
    "No backend — cart, wishlist, search are front-end only. Data is not stored on any server.",
    "Cart data is lost on page refresh (not saved to localStorage).",
    "No real checkout or payment gateway implemented.",
    "Product images are hosted on Unsplash — requires an active internet connection.",
    "Only 10 sample products exist — not a real inventory system.",
    "Bootstrap CDN, Font Awesome CDN, and Google Fonts CDN require internet connection.",
], is_b=True)
story1.append(spacer(0.2))

# 2.7 Viva
story1.append(h2("2.7  Important Viva Questions & Answers", is_b=True))
story1.append(spacer(0.1))
viva_2 = [
    ("What is Style Avenue?", "A 5-page Myntra-inspired fashion e-commerce website built as a student project using HTML, CSS, Bootstrap 5, and JavaScript."),
    ("What is the data-page attribute?", "A custom HTML attribute on each page's body tag. JavaScript reads it to know which category page is active and filters the products array accordingly."),
    ("How are products created on the page?", "Products are stored as JavaScript objects in an array. renderProducts() loops through the filtered array, builds an HTML string using template literals, and injects it into the product grid using innerHTML."),
    ("What does filter() do?", "It is a JavaScript array method. It goes through every item in the array and returns a new array containing only the items where the condition is true. Used here to filter products by page, category, and search text."),
    ("What does reduce() do?", "It processes each item in an array and accumulates a single result. Here it is used to calculate the cart subtotal: cart.reduce((sum, item) => sum + item.price, 0)."),
    ("What is event delegation?", "Instead of adding a click listener to every ADD+ button, one listener is added to the product grid container. When any button inside is clicked, the event bubbles up. JavaScript checks event.target.closest('[data-add]') to identify which button was clicked."),
    ("Is the shopping bag real?", "No. The bag is a demo. Items are added to a JavaScript array in memory. There is no real inventory system, order processing, or payment gateway. The page footer says: 'Demo bag only'."),
    ("What is Bootstrap's grid system?", "Bootstrap provides CSS classes (col-6, col-md-4, col-lg-3) that automatically arrange elements in a responsive grid. col-6 means 2 items per row on mobile. col-md-4 means 3 items per row on tablet. col-lg-3 means 4 items per row on desktop."),
    ("What is a CDN?", "Content Delivery Network. An online server that hosts library files. Bootstrap, Font Awesome, and Google Fonts are loaded via CDN links in the HTML head — no installation or download is needed."),
    ("What would you improve?", "Add localStorage to save the cart between refreshes, add a backend with Node.js and MongoDB for real data, implement a real payment gateway like Razorpay, and add product quantity controls in the cart panel."),
]
story1 += viva_qa(viva_2, is_b=True)
story1.append(spacer(0.5))

doc1.build(story1)
print(f"Saved: {out1}")


# ════════════════════════════════════════════════════════════════════════════════
#  PDF 2 — Project_Comparison_Quick_Reference.pdf
# ════════════════════════════════════════════════════════════════════════════════

out2 = r"C:\Users\shriy\OneDrive\Desktop\genAI mini project\Project_Comparison_Quick_Reference.pdf"
doc2 = SimpleDocTemplate(out2, pagesize=A4,
                          leftMargin=1.5*cm, rightMargin=1.5*cm,
                          topMargin=2*cm, bottomMargin=2*cm)

story2 = []

# Cover
story2.append(p("<b>PROJECT COMPARISON QUICK REFERENCE</b>",
                S("C2COVER", fontSize=22, textColor=COL_GA_ACC, alignment=TA_CENTER, fontName="Helvetica-Bold", spaceAfter=4)))
story2.append(p("GlitchLab  vs  Style Avenue — Side-by-Side Comparison",
                S("C2SUB", fontSize=13, textColor=COL_SB_ROSE, alignment=TA_CENTER, spaceAfter=4)))
story2.append(hr(COL_GA_ACC, 2))
story2.append(spacer(0.3))

# ─── Main Comparison Table ─────────────────────────────────────────────────────
comp_data = [
    ["Attribute", "PROJECT 1 — GlitchLab", "PROJECT 2 — Style Avenue"],
    ["Full Name", "GlitchLab", "Style Avenue (Myntra-Clone-SRDT)"],
    ["Project Type", "Creative multi-theme web experiment", "Fashion e-commerce front-end"],
    ["Inspiration", "Original creative concept", "Inspired by Myntra (Indian fashion e-commerce)"],
    ["Purpose", "Demonstrate CSS class-based theming with 3 visual styles", "Build a realistic shopping website with cart, wishlist, search"],
    ["Number of Pages", "4 (index, minimal, retro, glitch)", "5 (index, men, women, kids, beauty)"],
    ["HTML", "Semantic structure, multi-page navigation", "Semantic structure + data-page attribute + ARIA accessibility"],
    ["CSS", "12,129 bytes, 701 lines. No media queries.\nBody class-based theming.", "15,473 bytes. Flexbox, Grid, hover effects,\nmedia queries, dark theme, cart slide animation."],
    ["JavaScript", "86 lines. Dark toggle, colour palette,\nform validation. Basic DOM.", "166 lines. Products array, filter/map/find/reduce/forEach,\ncart, wishlist, search, newsletter, event delegation."],
    ["Bootstrap", "Not used", "Bootstrap 5.3.3 — responsive grid (col-6, col-md-4, col-lg-3)"],
    ["Font Awesome", "Not used", "Font Awesome 6.5.2 — bag, heart, moon/sun icons"],
    ["Google Fonts", "Not used", "DM Sans (body) + Playfair Display (headings) via CDN"],
    ["External Libraries", "None — pure HTML/CSS/JS", "Bootstrap + Font Awesome + Google Fonts (all CDN)"],
    ["Responsive Design", "NO — desktop only. No media queries.", "YES — Bootstrap grid + custom CSS media queries."],
    ["Dark Mode", "YES — classList.toggle('dark-mode') on body", "YES — classList.toggle('dark-theme') on body"],
    ["Product Cards", "World cards (clickable links to theme pages)", "10 real product cards dynamically rendered by JavaScript"],
    ["Search Feature", "No search", "Live search box — filters products as you type"],
    ["Cart / Bag", "No cart", "Full shopping bag with item count, subtotal, slide-in panel"],
    ["Wishlist", "No wishlist", "Heart icon toggle — saves/unsaves product IDs in array"],
    ["Form", "Feedback form (name + textarea)", "Newsletter form (email validation)"],
    ["Data Storage", "No data storage", "No data storage (front-end only)"],
    ["Backend / Server", "None — pure front-end", "None — pure front-end"],
    ["Payment Gateway", "Not applicable", "Not implemented — demo only"],
    ["Colour Palette", "Minimal: Cream/Green\nRetro: Dark/Gold/Pink\nGlitch: Black/Neon Cyan/Purple\nHome: Dark Purple/Lavender", "Light: White + Rose Pink (#E94F78)\nDark: Navy (#1A1A2E) + Cream (#F5F0E8)"],
    ["Fonts Used", "Arial (body), Georgia (headings),\nCourier New (labels/glitch) — web-safe only", "DM Sans + Playfair Display (Google Fonts)\nFallback: sans-serif"],
    ["JavaScript Concepts", "classList.toggle, createElement, appendChild,\nMath.random, event listeners, array iteration", "Arrays, objects, filter, map, find, reduce, forEach,\nfor...of, for...in, do...while, event delegation,\ntemplate literals, arrow functions, switch"],
    ["CSS Concepts", "Class selectors, body class theming,\nFlexbox (paletteBox), inline-block grids,\nCSS transitions (0.3s)", "Flexbox (header, hero), CSS Grid (categories),\nHover effects, media queries, transform (cart panel),\nBootstrap classes, dark-theme class"],
    ["File Count", "6 files (+ draft files + empty dir_name)", "8 files (index, 4 category pages, style, script, README)"],
    ["Complexity Level", "Beginner", "Beginner-Intermediate"],
    ["Main Strength", "Shows CSS theming power — one file, three looks", "Shows full e-commerce workflow with real JavaScript logic"],
    ["Main Limitation", "No responsiveness, no data storage, no search", "No backend, cart lost on refresh, only 10 products"],
]

col_w = [4*cm, 7.5*cm, 7*cm]
ct = Table(comp_data, colWidths=col_w, repeatRows=1)
ct.setStyle(TableStyle([
    # Header row
    ("BACKGROUND", (0,0), (0,0), COL_GRAY),
    ("BACKGROUND", (1,0), (1,0), COL_GA_DARK),
    ("BACKGROUND", (2,0), (2,0), COL_SB_NAVY),
    ("TEXTCOLOR", (0,0), (-1,0), COL_WHITE),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,0), 10),
    # Attribute column
    ("BACKGROUND", (0,1), (0,-1), colors.HexColor("#F0EEF5")),
    ("FONTNAME", (0,1), (0,-1), "Helvetica-Bold"),
    ("TEXTCOLOR", (0,1), (0,-1), COL_SB_NAVY),
    # GlitchLab column
    ("TEXTCOLOR", (1,1), (1,-1), colors.HexColor("#222233")),
    # Style Avenue column
    ("TEXTCOLOR", (2,1), (2,-1), colors.HexColor("#222233")),
    # Alternating rows
    ("ROWBACKGROUNDS", (1,1), (2,-1), [COL_WHITE, colors.HexColor("#FFF8FB")]),
    # Grid
    ("GRID", (0,0), (-1,-1), 0.4, COL_GRAY),
    # Padding
    ("LEFTPADDING", (0,0), (-1,-1), 5),
    ("RIGHTPADDING", (0,0), (-1,-1), 5),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    # Font sizes
    ("FONTSIZE", (0,1), (-1,-1), 9),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
]))
story2.append(ct)
story2.append(spacer(0.4))

# Summary section
story2.append(hr(COL_SB_ROSE))
story2.append(p("<b>SUMMARY: KEY DIFFERENCES IN ONE LINE</b>",
                S("SUM", fontSize=12, textColor=COL_SB_ROSE, fontName="Helvetica-Bold", spaceAfter=4)))
summary_data = [
    ["Area", "GlitchLab", "Style Avenue"],
    ["Core Goal", "Show 3 visual CSS themes from one file", "Build a full shopping experience in pure JS"],
    ["JS Complexity", "Basic — 3 simple interactive features", "Advanced — arrays, objects, all array methods"],
    ["Responsive?", "No (desktop only)", "Yes (Bootstrap + media queries)"],
    ["External Libraries?", "None", "Bootstrap, Font Awesome, Google Fonts"],
    ["Cart / Shopping?", "No", "Yes (demo bag with subtotal)"],
    ["Best For Learning", "CSS theming, body classes, DOM basics", "Arrays, filter/map/reduce, event delegation, Bootstrap grid"],
]
st = Table(summary_data, colWidths=[4*cm, 7*cm, 7.5*cm])
st.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), COL_SB_ROSE),
    ("TEXTCOLOR", (0,0), (-1,0), COL_WHITE),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,0), 10),
    ("FONTSIZE", (0,1), (-1,-1), 9.5),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [COL_LGRAY, COL_WHITE]),
    ("GRID", (0,0), (-1,-1), 0.5, COL_GRAY),
    ("ALIGN", (0,0), (-1,-1), "LEFT"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("FONTNAME", (0,1), (0,-1), "Helvetica-Bold"),
    ("TEXTCOLOR", (0,1), (0,-1), COL_SB_NAVY),
]))
story2.append(st)
story2.append(spacer(0.3))

# Footer note
story2.append(hr(COL_GA_ACC, 0.5))
story2.append(p("Both projects are front-end only, built with HTML, CSS, and JavaScript. GlitchLab focuses on CSS design and theming. Style Avenue focuses on JavaScript logic and real-world e-commerce interaction patterns. Together they cover the complete beginner-to-intermediate front-end development learning path.",
                S("FOOTER_NOTE", fontSize=10, textColor=COL_GRAY, alignment=TA_JUSTIFY, leading=15)))

doc2.build(story2)
print(f"Saved: {out2}")
print("All files generated successfully!")
