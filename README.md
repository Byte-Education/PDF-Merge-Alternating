# PDF Merger

A simple PDF merger written in Python that merges two pdfs together, where the pdfs contain the even and odd pages of a complete pdf. This idea came up as I was using a scanner that couldn't scan two sided papers, so scanning all the odd pages then the even pages was the easiest way of scanning a larger document. This code was written to simplify the process of merging those PDFs together. While pypdf contains a PdfMerger class, it doesn't merge in alternating order with two documents.

## Installation Instructions

Clone the project from through github with `git clone git@github.com:Byte-Education/PDF-Merge-Alternating.git`.

Navigate to the project and run the code.

The python code will check if pypdf is installed. If it isn't, it should install it itself. Additionally, the python code will check if pip3 is installed. If it isn't, it will tell the user to install python3 and pip3. If there are no dependency issues, it will continue as expected.

## Instructions to Use

```python3
python3 merge_pdf.py <odd pages pdf file path> <even pages pdf file path> <output file name>
```

## Dependencies

pypdf-3.9.1
