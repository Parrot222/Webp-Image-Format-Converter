import streamlit as st
from PIL import Image
import io
import os
import random

# Define a function to perform WebP image format conversion
def convert_webp_to_jpg_or_png(input_image, fname="", output_format='JPEG', output_path=""):
    try:
        # Open the WebP image
        with Image.open(input_image) as img:
            #str = ''
            #fname = str.join(random.choice("0123456789abcde") for i in range(20))
            name = fname.replace(".webp", "")
            # Convert to RGB mode
            if output_format == "PNG":
                img.save((output_path + "/" + name + "-out.png"), "PNG")
            elif output_format == "JPEG":
                img.save((output_path + "/" + name + "-out.jpg"), "JPEG")
            st.write("Successfully converted")
            return
    except Exception as e:
        st.error(f'Conversion failed: {e}')
        return None

# Streamlit application
st.title("WebP Image Format Converter")

# Support multiple file uploads
uploaded_files = st.file_uploader("Upload WebP image files", type=["webp"], accept_multiple_files=True)
output_path = st.text_input("Enter the output path:", "/path/to/output")
# Display the user-specified output path
#st.write(f"Output Path: {output_path.replace(os.sep, '/')}")

if uploaded_files and output_path:
    output_format = st.selectbox("Select output format", ["JPEG", "PNG"])
    path = output_path.replace(os.sep, '/')

    if st.button("Convert"):
        for uploaded_file in uploaded_files:
            output_image = convert_webp_to_jpg_or_png(uploaded_file, uploaded_file.name, output_format, output_path=path)
            if output_image:
                st.image(output_image, use_column_width=True, caption=f"Out: {uploaded_file.name}")
            
