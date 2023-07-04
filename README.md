# MusicCrack
This is a list of programs that convert SVG files from Musescore and converts them to a single PDF. 
For it to work you need to supply the program with a specific set of files since I haven't found a way to extract them with code.

Step 1. Find the music sheet you need 

Step 2. Zoom to the minimum for me it was 25% of the viewing screen (this will load more files at once)

Step 3. Press Ctrl+S to save the HTML of the page as complete HTML (this will also download a folder with all the sources of the page)

Step 4. Move the folder and the HTML file to the src directory on the program file (you can also directly download it there)

Step 5. Run the runner.py 

TIPS!!!
If the music sheet you want has many pages the best way that I found was to directly download to the src folder and do the download 
process two or more times and each time make sure that I have labeled more pages.

Requirements!:
You need to have Visual Studio Code(it is free) and also download some libraries and programs.
(in the future if I figure out a way to extract the svgs using code I might just have an exe file)

The libraries: 
1.Python 3

2.svglib:(pip command)
  pip install svglib

3.reportlab:(pip command)
  pip install reportlab

4.PyPDF2:(pip command)
  pip install PyPDF2
