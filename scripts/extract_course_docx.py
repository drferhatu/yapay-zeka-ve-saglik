#!/usr/bin/env python
"""DOCX ders öneri formunu ayrıştırır; paragrafları ve tabloları belge sırasıyla
düz metin (ve isteğe bağlı JSON) olarak dışa aktarır.

Kullanım:
  /opt/miniconda3/envs/ferhat_ml/bin/python scripts/extract_course_docx.py "<dosya.docx>" [--json çıktı.json]
"""
import json
import sys
from pathlib import Path

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph


def iter_block_items(doc):
    body = doc.element.body
    for child in body.iterchildren():
        tag = child.tag.split('}')[-1]
        if tag == 'p':
            yield Paragraph(child, doc)
        elif tag == 'tbl':
            yield Table(child, doc)


def table_rows(table):
    rows = []
    for row in table.rows:
        cells = []
        prev = None
        for cell in row.cells:
            txt = cell.text.strip().replace('\n', ' / ')
            # birleştirilmiş hücreler tekrar eder; tekrarları at
            if cell._tc is prev:
                continue
            prev = cell._tc
            cells.append(txt)
        rows.append(cells)
    return rows


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    path = Path(sys.argv[1])
    doc = Document(str(path))
    blocks = []
    for item in iter_block_items(doc):
        if isinstance(item, Paragraph):
            t = item.text.strip()
            if t:
                blocks.append({"type": "p", "style": item.style.name, "text": t})
        else:
            blocks.append({"type": "table", "rows": table_rows(item)})

    for b in blocks:
        if b["type"] == "p":
            print(f"[{b['style']}] {b['text']}")
        else:
            print("=== TABLE ===")
            for r in b["rows"]:
                print(" | ".join(r))
            print("=== /TABLE ===")

    if "--json" in sys.argv:
        out = Path(sys.argv[sys.argv.index("--json") + 1])
        out.write_text(json.dumps(blocks, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\nJSON yazıldı: {out}")


if __name__ == "__main__":
    main()
