import cv2, numpy as np, matplotlib.pyplot as plt

img = np.zeros((20,20),np.uint8)
img[2:18,3:6]=img[2:18,14:17]=img[8:11,6:14]=255

kernels = {
    "Square": np.ones((3,3),np.uint8),
    "Cross": np.array([[0,1,0],[1,1,1],[0,1,0]],np.uint8)
}

imgs = {"Original": img}
for n,k in kernels.items():
    imgs[f"Dilate {n}"] = cv2.dilate(img,k)
    imgs[f"Erode {n}"] = cv2.erode(img,k)
    imgs[f"Open {n}"] = cv2.morphologyEx(img,cv2.MORPH_OPEN,k)
    imgs[f"Close {n}"] = cv2.morphologyEx(img,cv2.MORPH_CLOSE,k)

plt.figure(figsize=(12,8))
for i,(t,im) in enumerate(imgs.items(),1):
    plt.subplot(3,3,i)
    plt.imshow(im,cmap='gray')
    plt.title(t)
    plt.axis('off')

plt.tight_layout()
plt.show()