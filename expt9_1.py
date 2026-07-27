import cv2, numpy as np, matplotlib.pyplot as plt

img = np.zeros((20,20),np.uint8)
img[8:12,2:18]=img[2:18,8:12]=255
k = np.ones((3,3),np.uint8)
e = cv2.erode(img,k)

imgs = {
    "Original": img,
    "Dilated": cv2.dilate(img,k),
    "Eroded": e,
    "Opened": cv2.morphologyEx(img,cv2.MORPH_OPEN,k),
    "Closed": cv2.morphologyEx(img,cv2.MORPH_CLOSE,k),
    "Boundary": cv2.subtract(img,e),
    "Gradient": cv2.morphologyEx(img,cv2.MORPH_GRADIENT,k)
}

plt.figure(figsize=(12,8))
for i,(t,im) in enumerate(imgs.items(),1):
    plt.subplot(2,4,i)
    plt.imshow(im,cmap='gray')
    plt.title(t)
    plt.axis('off')

plt.tight_layout()
plt.show()