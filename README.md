# PDF Merger

A simple PDF merger written in Python that merges two pdfs together, where the pdfs contain the even and odd pages of a complete pdf. This idea came up as I was using a scanner that couldn't scan two sided papers, so scanning all the odd pages then the even pages was the easiest way of scanning a larger document. This code was written to simplify the process of merging those PDFs together. While pypdf contains a PdfMerger class, it doesn't merge in alternating order with two documents.

## Instructions to Use

```python3
python3 merge_pdf.py <odd pages pdf file path> <even pages pdf file path> <output file name>
```

## Dependencies

pypdf-3.9.1
