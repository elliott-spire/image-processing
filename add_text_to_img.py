# https://note.nkmk.me/en/python-opencv-hconcat-vconcat-np-tile/
import os
import sys
import cv2
import glob


def display_text(img, text, loc, scale, thick):
    # fonts:
    # FONT_HERSHEY_COMPLEX
    # FONT_HERSHEY_COMPLEX_SMALL
    # FONT_HERSHEY_DUPLEX
    # FONT_HERSHEY_PLAIN
    # FONT_HERSHEY_SCRIPT_COMPLEX
    # FONT_HERSHEY_SCRIPT_SIMPLEX
    # FONT_HERSHEY_SIMPLEX
    # FONT_HERSHEY_TRIPLEX
    # FONT_ITALIC
    font = cv2.FONT_HERSHEY_SIMPLEX
    # Black outline
    cv2.putText(
        img,
        text,
        loc,
        font,
        scale,
        (0, 0, 0),
        # Increase thickness from baseline
        # to create a backdrop/outline effect
        thick + 10,
    )
    # White text
    cv2.putText(img, text, loc, font, scale, (255, 255, 255), thick)


def parse_timestring(filename):
    time = filename.split("/")[1]
    time = time.replace("__", " ")
    time = time.replace("_UTC", " UTC")
    time = time.replace("_", ":")
    time = time.replace(".png", "")
    return time


def add_text(file, pos):
    # Parse time string from filename
    timestring = parse_timestring(file)
    # Load image
    out_img = cv2.imread(file)

    # Add the time string to the image
    display_text(out_img, timestring, pos, fontScale + 3, thickness + 7)
    # Display the image
    # cv2.imshow('out', out_img)

    # Save the image
    out_name = "output/{}.png".format(timestring)
    cv2.imwrite(out_name, out_img)
    cv2.waitKey(0)
    print("Writing image file:".format(out_name))


def read_png_files(folder):
    # Read all image files in the folder
    filepath = os.path.join(folder, "*.png")
    filenames = glob.glob(filepath)
    # Sort the filenames alphabetically
    filenames = sorted(filenames)
    return filenames


if __name__ == "__main__":
    # get folder from script argument
    folder = sys.argv[1]
    # read PNG files in specified folder
    files = read_png_files(folder)
    # coordinate for positioning text on image
    pos = (100, 300)
    # scale of text font size
    fontscale = 1
    # thickness of text font
    thickness = 10
    # add text to each image
    for x in range(0, len(files)):
        add_text(files[x], pos, fontscale, thickness)
