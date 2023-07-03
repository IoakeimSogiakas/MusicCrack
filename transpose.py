import os
import shutil
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from PyPDF2 import PdfMerger

def convert_svg_to_pdf(svg_file, pdf_file):
    drawing = svg2rlg(svg_file)
    renderPDF.drawToFile(drawing, pdf_file)

def combine_pdfs(input_directory):
    program_directory = os.path.dirname(os.path.abspath(__file__))
    scores_directory = os.path.join(program_directory, input_directory)

    # Create or empty the temporary folder in the "Scores" directory
    temp_folder_path = os.path.join(scores_directory, "temp_folder")
    if os.path.exists(temp_folder_path):
        shutil.rmtree(temp_folder_path)
    os.makedirs(temp_folder_path)

    for folder_name in os.listdir(scores_directory):
        folder_path = os.path.join(scores_directory, folder_name)
        if os.path.isdir(folder_path):
            pdf_merger = PdfMerger()


            # Create the pdf_output directory
            output_dir = os.path.join(temp_folder_path, "pdf_output")
            os.makedirs(output_dir, exist_ok=True)

            # Get the list of SVG files in the folder
            svg_files = [filename for filename in os.listdir(folder_path) if filename.endswith(".svg")]

            # Convert each SVG file to PDF and add it to the PDF merger
            for i, svg_file in enumerate(svg_files):
                svg_path = os.path.join(folder_path, svg_file)
                pdf_file = f"{i+1}.pdf"  # Use a numerical index for the PDF file name
                pdf_path = os.path.join(output_dir, pdf_file)
                convert_svg_to_pdf(svg_path, pdf_path)
                pdf_merger.append(pdf_path)

            # Write the combined PDF to the output file
            output_file = f"{folder_name}.pdf"  # Use the folder name for the PDF file name
            with open(os.path.join(output_dir, output_file), "wb") as output:
                pdf_merger.write(output)

            # Move the final merged PDF to the root directory where the program is located
            final_pdf_path = os.path.join(output_dir, output_file)
            final_destination = os.path.join(program_directory, output_file)
            os.replace(final_pdf_path, final_destination)

            # Copy the entire folder to the temporary folder
            folder_destination = os.path.join(temp_folder_path, folder_name)
            shutil.rmtree(folder_path)
            
    # Remove the temporary file
    temp_file_path = os.path.join(scores_directory, "temp.txt")
    if os.path.exists(temp_file_path):
        os.remove(temp_file_path)

# Specify the directory containing the folders with SVG files
input_directory = "Scores"

# Call the function to combine the SVG files into separate PDFs in each folder
combine_pdfs(input_directory)