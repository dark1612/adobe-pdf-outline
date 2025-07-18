from collections import defaultdict
import re

def detect_title_and_headings(doc):
    font_stats = defaultdict(int)
    text_blocks = []

    # Step 1: Collect all font sizes and spans
    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        text = span["text"].strip()
                        if not text:
                            continue
                        font_size = round(span["size"], 1)
                        font_stats[font_size] += 1
                        text_blocks.append({
                            "text": text,
                            "font": font_size,
                            "bold": "Bold" in span["font"],
                            "y": span["bbox"][1],
                            "page": page_num
                        })

    # Step 2: Sort font sizes (large & frequent = more important)
    sorted_fonts = sorted(font_stats.items(), key=lambda x: (-x[0], -x[1]))
    font_levels = [font for font, _ in sorted_fonts[:4]]

    title_font = font_levels[0]
    h1_font = font_levels[1] if len(font_levels) > 1 else title_font
    h2_font = font_levels[2] if len(font_levels) > 2 else h1_font
    h3_font = font_levels[3] if len(font_levels) > 3 else h2_font

    detected_title = ""
    outline = []

    # Step 3: Identify title and clean headings
    for block in text_blocks:
        text = block["text"]
        font = block["font"]
        page = block["page"]
        bold = block["bold"]
        y = block["y"]

        if font == title_font and y < 100 and not detected_title:
            detected_title = text

        elif font in [h1_font, h2_font, h3_font]:
            if is_valid_heading(text):
                level = get_heading_level(font, h1_font, h2_font, h3_font)
                outline.append({
                    "level": level,
                    "text": text,
                    "page": page
                })

    return detected_title, outline

# ---------------------------
# 🚫 Semantic Filter
# ---------------------------

def is_valid_heading(text):
    """Reject headings that are too short, generic, or meaningless."""
    if len(text.strip()) < 4:
        return False
    if text.lower() in {"table", "figure", "page", "image", "img", "eq"}:
        return False
    if re.fullmatch(r"[\d\.\(\)a-zA-Z]+", text) and len(text.split()) < 2:
        return False
    return True

def get_heading_level(font, h1, h2, h3):
    if font == h1:
        return "H1"
    elif font == h2:
        return "H2"
    elif font == h3:
        return "H3"
    return "H3"
