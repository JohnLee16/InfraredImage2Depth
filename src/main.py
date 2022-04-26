import cv2
from cv2 import waitKey
import numpy as np

def image_read(path):
    imgs = cv2.imread(path)
    return imgs

image = image_read('./inputs/test_images/1646652789610919952.jpg')
cv2.imshow('image', image)
waitKey(0)
