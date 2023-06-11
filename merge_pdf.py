from os import system, path
from sys import argv
try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    system("pip3 install pypdf")
    from pypdf import PdfReader, PdfWriter


def get_pages(odd_pages, even_pages):
    odd_pages = PdfReader(odd_pages)
    even_pages = PdfReader(even_pages)
    return odd_pages, even_pages

def merge_pages(odd_pages, even_pages):
    output = PdfWriter()
    for i in range(len(odd_pages.pages)):
        output.add_page(odd_pages.pages[i])
        output.add_page(even_pages.pages[i])
    return output

def write_pages(output, output_file):
    with open(output_file, "wb") as f:
        output.write(f)
    print(f"Written to {output_file}")

def cli():
    if len(argv) < 4:
        print(f"Invalid usage: python3 {argv[0]} <odd pages pdf> <even pages pdf> <output file pdf>")
        exit(1)
    odd_pages = argv[1]
    even_pages = argv[2]
    output_file = argv[3]
    if not path.exists(odd_pages):
        print(f"File \"{odd_pages}\" does not exist")
        exit(1)
    if not path.exists(even_pages):
        print(f"File \"{even_pages}\" does not exist")
        exit(1)
    if not output_file.endswith(".pdf"):
        output_file += ".pdf"

    odd_pages, even_pages = get_pages(odd_pages, even_pages)
    output = merge_pages(odd_pages, even_pages)
    write_pages(output, output_file)

if __name__ == "__main__":
    cli()