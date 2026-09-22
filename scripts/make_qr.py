#!/usr/bin/env python
"""course.json içindeki iletişim kanalları için public/qr/<id>.svg karekodlarını üretir.

Kullanım: /opt/miniconda3/envs/ferhat_ml/bin/python scripts/make_qr.py
"""
import json
from pathlib import Path

import qrcode
from qrcode.image.svg import SvgPathImage

ROOT = Path(__file__).resolve().parent.parent
course = json.loads((ROOT / "content" / "data" / "course.json").read_text(encoding="utf-8"))
out = ROOT / "public" / "qr"
out.mkdir(exist_ok=True)
for ch in course["channels"]:
    img = qrcode.make(ch["url"], image_factory=SvgPathImage, box_size=10, border=1)
    svg = img.to_string().decode().replace('fill="#000000"', 'fill="#10262e"')
    (out / f"{ch['id']}.svg").write_text(svg, encoding="utf-8")
    print("✓", ch["id"])
