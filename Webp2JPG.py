#! python3
# Convert images to webp

from PIL import Image
import os

def convert_to_webp(filename, path="images/"):
    extension = filename.split('.')[-1]
    fname = filename.split('.')[0]
    img = Image.open(path + filename)

    if extension == "png":
        img.save((path+fname+".webp"), "webp", lossless=True)
    elif extension == "jpg" or extension == "jpeg":
        img.save((path+fname+".webp"), "webp", quality=85)

def convert_from_webp(filename, path="images/", new_extension="png", out_path="out/"):
    fname = filename.split('.')[0]
    img = Image.open(path + filename)

    if new_extension == "png":
        img.save((out_path + fname + "-out.png"), "PNG")
    elif new_extension == "jpg":
        img.save((out_path + fname + "-out.jpg"), "JPEG")

def convert_all(path="images/"):
    for root, dirs, files in os.walk(path):
        for imagefile in files:
            if imagefile.endswith(".webp"):
                convert_from_webp(imagefile, "images/")

if __name__ == "__main__":
    convert_all()