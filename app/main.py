# app/main.py
import os
import fitz  # PyMuPDF
import json
from utils import detect_title_and_headings

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def process_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    title, outline = detect_title_and_headings(doc)
    return {
        "title": title,
        "outline": outline
    }

def main():
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(INPUT_DIR, filename)
            result = process_pdf(pdf_path)
            output_path = os.path.join(OUTPUT_DIR, filename.replace(".pdf", ".json"))
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
