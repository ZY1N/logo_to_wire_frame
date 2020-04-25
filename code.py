import sys
import numpy as np
from PIL import Image

def extract(data, img, volume):
    width, height = img.size
    mesh = ""
    county = 0
    for row in data:
        if(county % 15 == 0):
            countx = 0
            for pixel in row:
                if(countx % 15 == 0):
                    flag = 0
                    for pixelvalue in pixel:
                        if(pixelvalue > 0):
                            flag = 1
                    if(flag == 1):
                        mesh = mesh + volume + " "
                    else:
                        mesh = mesh + "0 "
                countx += 1
            mesh = mesh + "\n"
        county += 1
    return(mesh)


def main():
    # check to see if the arguments is 1
    # then import the image
    if(len(sys.argv) != 2):
        return
    else :
        img = Image.open(sys.argv[1])
        data = np.asarray(img)
        volume = input("What height do you want?")
        mesh = extract(data, img, volume)
        text_file = open("map", "w")
        text_file.write(mesh)
        text_file.close()

if __name__ == "__main__":
    main()