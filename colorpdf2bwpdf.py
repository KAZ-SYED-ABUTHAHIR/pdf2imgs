import os
from pdf2image import convert_from_path
from PIL import Image

def convert_pdf_to_bw(input_path, output_path):
    # Convert PDF to JPG images
    pages = convert_from_path(input_path)
    
    # Convert JPG images to black and white and save them as PNG images
    for i, page in enumerate(pages):
        image_path = os.path.join(output_path, f'page_{i+1}.png')
        page = page.convert('L') # Convert to grayscale
        page.save(image_path)
    
    # Convert PNG images to PDF
    images = [Image.open(os.path.join(output_path, f)) for f in os.listdir(output_path) if f.endswith('.png')]
    images[0].save(f'{output_path}/output.pdf', save_all=True, append_images=images[1:])

