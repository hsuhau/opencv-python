import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('messi5.png', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # 隐藏 x 轴和 y 轴上的刻度值
plt.show()
