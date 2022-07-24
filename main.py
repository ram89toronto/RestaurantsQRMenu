# Importing Required Libraries

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pdf2image import convert_from_path
import glob, sys, fitz
import gdown
import numpy as np
import pdfqrgen
#from fpdf import FPDF
#import base64

# Displaying Required information on Site
st.write("# Restaurants QR Menu in 3 Simple Steps")
st.image('hands-1167612_1280.jpg')
st.write("## Step 1: Paste your Restaurant's PDF Menu that is uploaded on Google Drive below")

st.write("""##### Having trouble creating a shared google drive link ? No problem: Watch this youtube video :- https://www.youtube.com/watch?v=E1ntG7XexAM&t=85s """)
# Taking input and chaning it to downloadable googl drive link
link1 = st.text_input("Paste your Google Drive Link below and press enter ",value="hhttps://drive.google.com/file/d/1jeu_EmYoP4WEtphbQwqtJXyJbmJX5-Dc/view?usp=sharing")
st.write("###### Example : (https://drive.google.com/file/d/1zaprpJvswUHuTABFvvFwqA5CnsCDaml9/view?usp=sharing)")
link2 = link1.replace('/file/d/','/uc?id=')
link =  link2.replace('/view?usp=sharing','&export?format=pdf')

# Sample Links
sample_link = "https://drive.google.com/file/d/1zaprpJvswUHuTABFvvFwqA5CnsCDaml9/view?usp=sharing"
#sample_link1 ="https://drive.google.com/uc?export=download&id=1zaprpJvswUHuTABFvvFwqA5CnsCDaml9"
message = "Thanks for pasting the link :) "

# Downloading the pdf from google drive
pdfqrgen.main1(link)
# Downloading from google Drive
output="Menu4.pdf"
output1="output.pdf"
def gdownload(url):
    gdown.download(url=url, output=output, quiet=False, fuzzy=True)

gdownload(link)


# To get better resolution
zoom_x = 2.0  # horizontal zoom
zoom_y = 2.0  # vertical zoom
mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension

st.write("## Step 2: Check if this is the same menu")
#all_files = glob.glob(uploaded_file.name)
def displaypdf(output):

    if output != None:
        all_files = glob.glob(output)
        for filename in all_files:
            doc = fitz.open(filename)  # open document
            for page in doc:  # iterate through the pages
                pix = page.get_pixmap(matrix=mat)  # render page to an image
                pix.save("page-%i.png" % page.number)  # store image as a PNG
                st.image("page-%i.png" %page.number)

displaypdf(output)

st.write("## Step 3: Click below button to download your Print version of QR Menu")
pdfqrgen.main1(link)

with open("output.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="Download your QR Food Menu",
                    data=PDFbyte,
                    file_name="QRMenu.pdf",
                    mime='application/octet-stream')
displaypdf(output1)
st.snow()
