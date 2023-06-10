import fitz

def extract_pdf_pages_as_images(pdf_path, output_dir):
    doc = fitz.open(pdf_path)
    
    for i in range(doc.page_count):
        page = doc.load_page(i)
        pix = page.get_pixmap()
        output_path = f'{output_dir}/page_{i+1}.png'  # Agregar el número de índice al nombre del archivo
        pix.save(output_path)

def main():
    pdf_path = './pdfs/logo.pdf'
    output_dir = './images'
    extract_pdf_pages_as_images(pdf_path, output_dir)

if __name__ == '__main__':
    main()
