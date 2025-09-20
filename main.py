# Author: Scott Grivner
# Website: linktr.ee/scottgriv
# Abstract: Convert pdf files to audio files (text to voice)
    
# Import Modules
import os, pyttsx3, PyPDF2

# Get Current Directory
cwd = os.getcwd()

# Define Input and Output File Locations
input_file = 'pdf_Sample.pdf'
output_file = 'pdf_Sample.aiff'

# Read the PDF File
pdfreader = PyPDF2.PdfReader(open(os.path.join(cwd, input_file), 'rb'))

# Initiate the Engine
engine = pyttsx3.init()

# Loop through the PDF File
for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

# Say the PDF File
engine.say(clean_text)

# Output the PDF File to an Audio Formatted File
engine.save_to_file(clean_text, os.path.join(cwd, output_file))

# Run the Engine
engine.runAndWait()
