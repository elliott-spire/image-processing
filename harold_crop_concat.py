# https://note.nkmk.me/en/python-opencv-hconcat-vconcat-np-tile/
import os
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
        (0,0,0),
        # Increase thickness from baseline
        # to create a backdrop/outline effect
        thick + 10
    )
    # White text
    cv2.putText(
        img,
        text,
        loc,
        font,
        scale,
        (255,255,255),
        thick
    )

def parse_timestring(filename):
    time = filename.split('/')[1]
    time = time.replace('__',' ')
    time = time.replace('_UTC',' UTC')
    time = time.replace('_',':')
    time = time.replace('.png','')
    # ugh
    time = time.replace('010','10')
    time = time.replace('011','11')
    return time

def combine_images(fileA, fileB, fileC, fileD, fileE, fileF):
    # Parse time string from filename
    timestring = parse_timestring(fileA)
    # Load images
    img1 = cv2.imread(fileA)
    img2 = cv2.imread(fileB)
    img3 = cv2.imread(fileC)
    img4 = cv2.imread(fileD)
    img5 = cv2.imread(fileE)
    img6 = cv2.imread(fileF)
    # Crop images [y,x]
    img1 = img1[:, 600:2980]
    img2 = img2[:, 600:2980]
    img3 = img3[:, 600:2980]
    img4 = img4[:, 600:2980]
    img5 = img5[:, 600:2980]
    img6 = img6[:, 600:2980]
    # Horizontally concatenate images
    top_img = cv2.hconcat([img1, img2, img3])
    bottom_img = cv2.hconcat([img4, img5, img6])
    # print(top_img.shape)
    # print(bottom_img.shape)
    # Vertically concatenate images
    out_img = cv2.vconcat([top_img, bottom_img])

    fontScale = 4
    thickness = 10
    # Display time string top center
    display_text(
        out_img,
        timestring,
        (2190,300),
        fontScale + 3,
        thickness + 7
    )
    # Display variable name 1
    display_text(
    	out_img,
    	'Precipitable Water',
        (600,2100),
        fontScale,
        thickness
    )
    # Display variable name 2
    display_text(
    	out_img,
    	'Significant Wave Height',
        (2800,2100),
        fontScale,
        thickness
    )
    # Display variable name 3
    display_text(
        out_img,
        'Convective Available Potential Energy',
        (5050,2100),
        fontScale - 1, # long text, make font smaller
        thickness
    )
    # Display variable name 4
    display_text(
        out_img,
        'Wind Gusts',
        (790,4300),
        fontScale,
        thickness
    )
    # Display variable name 5
    display_text(
        out_img,
        'Air Pressure at MSL',
        (2930,4300),
        fontScale,
        thickness
    )
    # Display variable name 6
    display_text(
        out_img,
        'Relative Humidity',
        (5420,4300),
        fontScale,
        thickness
    )

    # Display the image
    # cv2.imshow('out', out_img)

    # Save the image
    out_name = 'output/'+timestring+'.png'
    cv2.imwrite(out_name, out_img)
    cv2.waitKey(0)
    print(out_name)

def read_files(folder):
    # Read all image files in the folder
    filepath = os.path.join(folder, '*.png')
    filenames = glob.glob(filepath)
    # Sort the filenames alphabetically
    filenames = sorted(filenames)
    return filenames

if __name__ == '__main__':

    filesA = read_files('Precipitable Water')
    filesB = read_files('Significant Wave Height')
    filesC = read_files('Convective Available Potential Energy')
    filesD = read_files('Wind Gusts')
    filesE = read_files('Air Pressure at MSL')
    filesF = read_files('Relative Humidity')

    for x in range(0, len(filesA)):
        combine_images(
            filesA[x],
            filesB[x],
            filesC[x],
            filesD[x],
            filesE[x],
            filesF[x],
        )
