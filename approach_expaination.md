# Round 1A: Approach Explanation

## Overview

The objective of Round 1A in the Adobe "Connecting the Dots" Hackathon is to automatically extract structured outlines from a set of input PDF documents. These outlines must include the document title and all headings (H1, H2, H3) along with their respective page numbers. The solution is expected to work across a wide variety of PDFs with different formatting styles and structures.

## Methodology

We designed a lightweight yet powerful heuristic-based solution that utilizes font metadata and layout patterns to identify structural elements within PDF files. This approach is particularly effective for extracting outlines in documents where no explicit metadata or tags are available.

### 1. PDF Parsing

We use the **PyMuPDF (fitz)** library to read and extract text blocks from each PDF. For every block of text, we extract additional metadata:

* Font size
* Font type (bold/italic/plain)
* Bounding box (position on the page)
* Page number

This metadata is critical for detecting hierarchical patterns across documents.

### 2. Title Detection

We assume that the largest font size text block on the **first page** is most likely the document title. In cases where multiple candidates exist, we select the one nearest to the top center.

### 3. Heading Detection (H1, H2, H3)

To identify heading levels:

* We compute a dynamic threshold for font sizes across the document
* Cluster font sizes to determine distinct levels
* The largest cluster (excluding the title) is labeled H1, followed by H2 and H3

We also apply basic layout heuristics (e.g., alignment, text length) to reduce false positives.

### 4. Page Mapping

Once headings are detected, we associate each heading with its corresponding page number. This mapping enables structured outline creation per document.

### 5. Output Format

The extracted data is formatted as a structured JSON with the following fields:

* Title
* List of headings, each with text, level, and page number

This format provides a clean, machine-readable output suitable for downstream use.

## Tools and Libraries

* **Python 3.8+** – Development language
* **PyMuPDF (fitz)** – PDF parsing and metadata extraction
* **json** – For writing structured output

## Strengths of Our Approach

* **Font-size aware**: Uses document-specific thresholds
* **Heuristic and rule-based**: No external model dependency
* **Generalizable**: Works across academic, technical, and general-purpose documents
* **Lightweight**: Fast processing and minimal dependencies

## Limitations and Future Enhancements

* May miss headings that use unusual font sizes
* Limited support for multi-column or image-heavy layouts
* Could benefit from a font-clustering algorithm like KMeans
* Optional: Apply NLP techniques to validate heading context

## Conclusion

This solution provides a practical and robust way to extract structured outlines from diverse PDF files using font-style-driven heuristics. It is reliable, interpretable, and easily extendable, making it suitable for scalable document processing.

---

**Word Count**: \~480
