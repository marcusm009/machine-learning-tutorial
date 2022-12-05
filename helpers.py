import cv2
import matplotlib.pyplot as plt

def show_digit(img):
    plt.imshow(img.reshape(8,8), cmap='gray')

def load_image(filename):
    img = cv2.imread(filename)
    img_resized = cv2.resize(img, dsize=(8, 8), interpolation=cv2.INTER_AREA)
    img_flattened = img_resized.reshape(64, 3).T[0]
    return img_flattened / 255