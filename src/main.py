# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import matplotlib.pyplot as plt

def canny_edge_detection(img_src):
    img = cv2.imread(img_src)

    edges = cv2.Canny(img, 100, 200, 3, L2gradient=True)
    plt.figure()
    plt.title('Dollhouse')
    plt.imsave('data/processed/doll-canny.png', edges, cmap='gray', format='png')
    plt.imshow(edges, cmap='gray')
    plt.show()


if __name__ == '__main__':
    canny_edge_detection('data/raw/doll-house.jpg')

