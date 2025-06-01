# Task Matcher

Task Matcher is a Django web application that matches tasks to employees based on skill extraction from PDF resumes. It uses natural language processing (NLP) to extract skills from resumes and task descriptions, then calculates match scores to recommend the best fit.

---

## Features

- Upload or input task descriptions to find the best matching employee.
- Extract skills automatically from PDF resumes.
- Calculate match scores based on skill overlap.
- Displays the best match and match score.
- Stylish UI with a custom background image and fancy fonts.

---

## Technologies Used

- Python 3.x
- Django 4.x
- spaCy (NLP for skill extraction)
- PyMuPDF (fitz) for PDF text extraction
- HTML/CSS for frontend styling
- FPDF (for generating sample resumes, if needed)

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/task-matcher.git
   cd task-matcher
