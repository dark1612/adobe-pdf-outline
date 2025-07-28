# Overview

This repository contains our solution for Round 1A of the Adobe "Connecting the Dots" Hackathon. The objective is to automatically extract structured outlines from PDF documents. These outlines include titles and hierarchical headings (H1, H2, H3) along with their corresponding page numbers.

## Problem Statement
Given a set of input PDFs, generate a structured JSON representation of each document’s outline. This includes:
•	Title of the document

•	Headings at various levels (H1, H2, H3)

•	Page numbers where each heading appears

The solution is expected to work for diverse document structures with minimal assumptions.

## Our Approach

We adopted a heuristic-based and font-style-aware method for outline extraction, utilizing the following key techniques:

•	PDF Parsing : Extracts text blocks with metadata such as font size, font name, and position.

•	Font-Based Hierarchy Detection: Larger or bold fonts signify higher-level headings. A dynamic threshold is computed per document to differentiate between H1, H2, and H3.

•	Page Association: Every detected heading is mapped to its originating page number.

•	Title Detection: The first largest text block on the first page is heuristically considered the document title.

This approach generalizes well across academic papers, manuals, and general-purpose documents.

 ## Libraries & Tools Used
 
•	PyMuPDF (fitz) – for parsing PDF content and extracting text with layout metadata.

•	Python 3.8+ – scripting language used for development.

•	json – built-in library to format the extracted outline as per the required schema.

 # Implementation and Execution of the Solution
 
 ## Prerequisites
 
**Ensure you have the following installed:**

•	Python 3.8 or above

•	pip (Python package installer)

 Install Dependencies
 
python -m venv venv

source venv/bin/activate       

pip install -r requirements.txt

 ## Folder Structure
 
adobe-round1a-outline/

│

├── input/  

├── output/        

├── main.py  

├── requirements.txt

└── README.md        

Run the Script

Place all input PDF files into the input/ folder. Then execute:

python main.py

The script processes each PDF in the input/ directory and generates a structured outline in JSON format. Each output file is saved in the output/ folder with the same base name as the PDF.

 **Output Format**
 
Each generated .json file follows the expected schema with fields such as:

{

  "title": "Document Title",

  "headings": [
  
    {
      "text": "Introduction",
      "level": 1,
      "page_number": 1
    },
    {
      "text": "Background",
      "level": 2,
      "page_number": 2
    }
    // ...
  ]
}
## Testing

•	Add test documents in input/ folder.

•	After running the script, check output/ for correctly structured outline JSONs.

•	Compare with any provided expected output to validate correctness.
![Round1A](https://github.com/user-attachments/assets/0c537962-a308-4b8f-9c74-5d5d33c632b1)






## Future Improvements

•	Smarter font clustering for documents with non-standard formatting.

•	NLP-based post-processing to verify headings contextually.

•	Better handling of multi-column layouts or embedded images.

