import os
import shutil
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from PyPDF2 import PdfMerger
import uuid
import time
# Directory paths
directory = r'D:\user\Ioakeim Sogiakas\Music\MusicCrack\Scores'
temp_directory = os.path.join(directory, 'temp')
program_directory = r'D:\user\Ioakeim Sogiakas\Music\MusicCrack'

# Check if the 'temp' folder exists, empty it if it does
if os.path.exists(temp_directory):
    shutil.rmtree(temp_directory)
else :
    # Create the 'temp' folder
    os.mkdir(temp_directory)

# Get a list of folders in the directory (excluding 'temp')
folders = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name)) and name != 'temp']

# If there are no other folders (excluding 'temp'), stop
if len(folders) == 0:
    print("No other folders found. Exiting...")
    exit()

# Move the first folder found to the 'temp' folder
folder_to_move = os.path.join(directory, folders[0])
shutil.move(folder_to_move, temp_directory)

# Convert SVG files to PDF and merge them
folder_name = os.path.basename(folder_to_move)
pdf_output_path = os.path.join(program_directory, folder_name + '.pdf')
pdf_merger = PdfMerger()

for filename in os.listdir(temp_directory):
    if filename.endswith('.svg'):
        svg_path = os.path.join(temp_directory, filename)
        print(f"Converting SVG: {svg_path}")
        drawing = svg2rlg(svg_path)
        pdf_path = os.path.join(temp_directory, filename.replace('.svg', '.pdf'))
        try:
            renderPDF.drawToFile(drawing, pdf_path)
            pdf_merger.append(pdf_path)
        except Exception as e:
            print(f"Error converting SVG to PDF: {e}")

# Generate a unique filename for the merged PDF
unique_filename = folder_name + '_' + str(uuid.uuid4()) + '.pdf'
unique_pdf_output_path = os.path.join(program_directory, unique_filename)

pdf_merger.write(unique_pdf_output_path)
pdf_merger.close()

# Move the final PDF to the program directory
shutil.move(unique_pdf_output_path, os.path.join(program_directory, unique_filename))

print("Process completed successfully.")
