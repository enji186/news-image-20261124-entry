#!/usr/bin/env python3
"""Draw entry.png for make.fun news-image-20261124.

Own work: a 1024x1024 infographic drawn with PIL from verified news
reported on Tuesday 24 November 2026 (see SOURCES in README.md).
Run: python3 draw_entry.py  ->  writes entry.png next to this file.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
NAVY = (15, 27, 45)
NAVY2 = (24, 42, 68)
GOLD = (232, 184, 75)
CARD = (247, 245, 239)
INK = (18, 28, 44)
GREY = (74, 85, 104)
WHITE = (255, 255, 255)
MUTED = (168, 182, 200)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_TITLE = font("DejaVuSans-Bold.ttf", 66)
F_SUB = font("DejaVuSans.ttf", 34)
F_TAG = font("DejaVuSans-Bold.ttf", 19)
F_HEAD = font("DejaVuSans-Bold.ttf", 27)
F_SUM = font("DejaVuSans.ttf", 21)
F_FOOT = font("DejaVuSans.ttf", 19)
F_NUM = font("DejaVuSans-Bold.ttf", 26)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines that fit max_w."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# (tag, accent colour, headline, summary)
STORIES = [
    ("NORTH KOREA", (198, 60, 60),
     "Pyongyang threatens to shut Swiss office",
     "Kim Yo Jong hits back at Swiss sanctions over a children's camp; "
     "a decision is due within days."),
    ("MARKETS", (46, 134, 193),
     "Asian shares leap on Nvidia's return",
     "MSCI Asia-Pacific ex-Japan up 4.6% on Tuesday as the AI trade "
     "revives after Nvidia's 31% surge on Monday."),
    ("MEXICO", (34, 139, 92),
     "\u201cEl Chapo Isidro\u201d to be tried in Mexico",
     "Attorney general says the FBI most-wanted cartel boss will face "
     "trial at home, not extradition."),
    ("UNITED STATES", (122, 90, 180),
     "FBI deputy director to retire in December",
     "Christopher Raia's planned exit is the latest senior departure "
     "from the bureau, the Washington Post reports."),
    ("MARKETS", (176, 141, 28),
     "Gold steadies after hitting a 14-month low",
     "Spot gold near $3,645 an ounce as traders await US inflation "
     "data due on Wednesday."),
    ("SOUTH KOREA", (214, 96, 44),
     "Bank of Korea tipped to raise rates Thursday",
     "Reuters poll: base rate seen up 25 basis points to 3.25% on "
     "chip-led export growth."),
]


def main():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)

    # subtle header band
    d.rectangle([0, 0, W, 168], fill=NAVY2)
    d.rectangle([0, 168, W, 172], fill=GOLD)

    d.text((36, 26), "24 NOVEMBER 2026", font=F_TITLE, fill=WHITE)
    d.text((36, 104), "World News in One Image", font=F_SUB, fill=GOLD)

    # small globe glyph top-right: circle + meridians
    cx, cy, r = 940, 84, 52
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=GOLD, width=4)
    d.ellipse([cx - r // 2, cy - r, cx + r // 2, cy + r], outline=GOLD, width=2)
    d.line([cx - r, cy, cx + r, cy], fill=GOLD, width=2)
    d.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], 0, 360, fill=GOLD, width=2)

    # grid of story cards: 2 cols x 3 rows
    mx, my = 36, 188
    cw, ch, gap = 464, 250, 16
    for i, (tag, accent, head, summ) in enumerate(STORIES):
        x = mx + (i % 2) * (cw + gap)
        y = my + (i // 2) * (ch + gap)
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=14, fill=CARD)
        d.rounded_rectangle([x, y, x + 12, y + ch], radius=6, fill=accent)
        # number chip
        nx, ny = x + 30, y + 22
        d.ellipse([nx, ny, nx + 44, ny + 44], fill=accent)
        num = str(i + 1)
        tw = d.textlength(num, font=F_NUM)
        d.text((nx + (44 - tw) / 2, ny + 6), num, font=F_NUM, fill=WHITE)
        # tag
        d.text((nx + 58, ny + 10), tag, font=F_TAG, fill=accent)
        # headline, up to 2 lines
        tx = x + 30
        tw_max = cw - 60
        lines = wrap(d, head, F_HEAD, tw_max)[:2]
        ly = y + 78
        for ln in lines:
            d.text((tx, ly), ln, font=F_HEAD, fill=INK)
            ly += 34
        # summary, up to 3 lines
        slines = wrap(d, summ, F_SUM, tw_max)[:3]
        sy = y + 150
        for ln in slines:
            d.text((tx, sy), ln, font=F_SUM, fill=GREY)
            sy += 27

    d.text((36, 984), "Sources: Reuters, Korea JoongAng Daily  |  Early edition, 24 Nov 2026",
           font=F_FOOT, fill=MUTED)

    img.save(OUT, "PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
