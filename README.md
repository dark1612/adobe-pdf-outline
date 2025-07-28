# Adobe India Hackathon - README Collection

This document includes **both** README files for Round 1A and Round 1B solutions of the Adobe "Connecting the Dots" Hackathon. These can be used directly in their respective project folders or in a combined GitHub repo.

---

## 🧠 Round 1A – PDF Outline Extractor

> **Track:** Connecting the Dots
> **Challenge:** Automatically extract structured outlines from unstructured PDFs

### 📌 Overview

This solution extracts structured outlines from input PDF documents. Each output contains:

* 🏷️ Title of the document
* 🧩 Headings (H1, H2, H3)
* 📄 Corresponding page numbers

### 💡 Approach

We implemented a **font-style-aware heuristic algorithm**:

* **Font Metadata Parsing**: Extracts size, font name, and position
* **Heading Detection**: Clusters font sizes to infer heading levels
* **Title Detection**: Picks the largest text on the first page

### 🛠️ Tools Used

* `Python 3.8+`
* `PyMuPDF (fitz)`
* `json` (built-in)

### 📁 Folder Structure

```
adobe-round1a-outline/
├── input/               ← Input PDFs
├── output/              ← Output JSONs
├── main.py              ← Main script
├── utils.py             ← Logic helpers
├── requirements.txt     ← Python dependencies
├── Dockerfile           ← (Optional) container setup
└── README.md            ← This file
```

### 🧪 How to Run

```bash
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### 📝 Sample Output Format

```json
{
  "title": "Document Title",
  "headings": [
    {
      "text": "Introduction",
      "level": 1,
      "page_number": 1
    }
  ]
}
```

### 🔮 Future Work

* KMeans clustering of font styles
* NLP-based heading validation
* Multi-column layout support

---

## 📊 Round 1B – Multi-Collection PDF Persona Analysis

> **Track:** Connecting the Dots
> **Challenge:** Analyze and extract semantically relevant sections from PDFs across multiple collections based on a persona’s need.

### 📌 Objective

Given multiple PDFs and a user persona + task, extract the most relevant sections and refined content, and return them ranked by importance.

### 🧠 Approach Summary

* Load JSON input and PDFs
* Extract headings (reuses Round 1A logic)
* Use `sentence-transformers` to embed headings, persona, and job
* Compute similarity scores → rank sections
* Extract best-matching pages/snippets

### 🛠️ Stack

| Task             | Tool                    |
| ---------------- | ----------------------- |
| PDF Parsing      | `PyMuPDF` (fitz)        |
| Text Embeddings  | `sentence-transformers` |
| Scoring          | `cosine_similarity`     |
| Containerization | Docker (offline mode)   |

### 📁 Structure

```
Round1B/
├── Collection_1/…     ← 3 collection folders
├── app/               ← logic scripts
├── model/             ← MiniLM model cache
├── main.py
├── requirements.txt
├── Dockerfile
├── README.md
└── approach_explanation.md
```

### 📤 Output JSON

```json
{
  "metadata": {
    "persona": "HR Professional",
    "job_to_be_done": "Design onboarding forms"
  },
  "extracted_sections": [
    {
      "document": "form_guide.pdf",
      "section_title": "Creating Fillable Forms",
      "importance_rank": 1,
      "page_number": 3
    }
  ],
  "subsection_analysis": [
    {
      "document": "form_guide.pdf",
      "refined_text": "You can create fillable text fields using...",
      "page_number": 3
    }
  ]
}
```

### 🐳 Docker Usage

```bash
# Build
docker build --platform linux/amd64 -t round1b-solution .

# Run
docker run --rm \
  -v ${PWD}/Collection_1:/app/Collection_1 \
  --network none \
  round1b-solution
```

---


