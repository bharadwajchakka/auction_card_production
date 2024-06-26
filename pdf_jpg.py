from PIL import Image
import fitz  # PyMuPDF
import os

def pdf_to_image(pdf_path, output_image_path):
    try:
        pdf_document = fitz.open(pdf_path)
        first_page = pdf_document[0]  # Get the first page (adjust index if needed)
        image_matrix = fitz.Matrix(300 / 72, 300 / 72)  # Set resolution (300 DPI)
        image_pixmap = first_page.get_pixmap(matrix=image_matrix)
        
        # Convert the pixmap to a Pillow Image
        image = Image.frombytes("RGB", [image_pixmap.width, image_pixmap.height], image_pixmap.samples)
        image.save(output_image_path, "png")
        
        print(f"The first page of {pdf_path} was successfully converted to {output_image_path}.")
    except Exception as e:
        print(f"Error converting PDF to image: {e}")

def convert_multiple_pdfs(pdf_directory, output_directory):
    # Get a list of all PDF files in the directory
    pdf_files = [file for file in os.listdir(pdf_directory) if file.lower().endswith(".pdf")]
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    
    # Convert each PDF to an image
    for pdf_file in pdf_files:
        pdf_file_path = os.path.join(pdf_directory, pdf_file)
        output_image_path = os.path.join(output_directory, os.path.splitext(pdf_file)[0] + ".png")
        pdf_to_image(pdf_file_path, output_image_path)
    
    print(f"All PDF files have been converted to image files in the {output_directory} folder.")

if __name__ == "__main__":
    input_pdf_directory = "C:/Users/BHARADWAJ/Downloads/cricverse2024/pdf_png/pdf"
    output_image_directory = "C:/Users/BHARADWAJ/Downloads/cricverse2024/player_card"
    convert_multiple_pdfs(input_pdf_directory, output_image_directory)



