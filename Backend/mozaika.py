import base64
import os

import numpy
import requests
from PIL import Image
import cv2 as cv
from matplotlib import pyplot as plt

def mozaika(tab,nazwa):
    width = 1536
    height = 256
    mosaic = Image.new('RGB', (width, height))
    j = 0
    for i in range(len(tab)):
        image = Image.fromarray(tab[i])
        if len(tab) < 4:
            image = image.resize((int(width / len(tab)), height))
            mosaic.paste(image, ((int(width / len(tab))) * i, 0))
        elif len(tab) == 5:
            image = image.resize((int(width / 2), int(height / 3)))
            if i < 2:
                mosaic.paste(image, ((int(width / 2)) * i, 0))
            if i == 2:
                mosaic.paste(image, (int(1.33 * width / len(tab)), int(height / 3)))
            if i > 2:
                mosaic.paste(image, (int((width / 2)) * j, int(2*height / 3)))
                j += 1
        elif len(tab) == 7:
            image = image.resize((int(width / 3), int(height / 3)))
            if i < 2:
                mosaic.paste(image, (int((width / 3) * (i + 0.5)), 0))
            elif i < 5:
                mosaic.paste(image, (int(width / 3) * (i-2), int(height / 3)))
            elif i > 4:
                mosaic.paste(image, (int((width / 3) * (j+0.5)), int(2*height / 3)))
                j +=1
        else:
            image = image.resize((int(width / (len(tab) / 2)), int(height / 2)))
            if i < (len(tab) / 2):
                mosaic.paste(image, ((int(width / len(tab))) * i * 2, 0))
            else:
                mosaic.paste(image, (int((width / len(tab))) * j * 2, int(height / 2)))
                j += 1
    open_cv_image = numpy.array(mosaic.convert('RGB'))
    ret = open_cv_image[:, :, ::-1].copy()
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv.calcHist([ret], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.savefig(nazwa + ".png", format='png')
    f = open(nazwa + ".png", "rb")
    image_data = f.read()
    b64_image = base64.standard_b64encode(image_data)
    headers = {'Authorization': 'Client-ID ' + os.environ['IMGUR']}
    data = {'image': b64_image, 'title': nazwa}
    r = requests.post("https://api.imgur.com/3/upload", data=data,headers=headers)
    print(r.json()['data']['link'])
    link = r.json()['data']['link']
    return link

def histogram(data):
    name = data.vidID + ".mp4"
    vidcap = cv.VideoCapture(name)
    count = 0
    success = True
    fps = int(vidcap.get(cv.CAP_PROP_FPS))
    f = int(fps*data.vidDuration/11)
    i = 0
    images = []
    while success:
        success, image = vidcap.read()
        if count == i:
            print('Read a new frame: ', success)
            images.append(cv.cvtColor(image, cv.COLOR_BGR2RGB))
            i += f
        count += 1
    return mozaika(images,data.vidID)


