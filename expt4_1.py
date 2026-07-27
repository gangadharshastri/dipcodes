import cv2, numpy as np, matplotlib.pyplot as plt

img = np.zeros((200,200), np.uint8)
for i,v in zip(range(20,100,20), [100,150,190,255]):
    img[i:200-i, i:200-i] = v

r,c = img.shape
p1 = np.float32([[50,50],[150,50],[50,150],[150,150]])
p2 = np.float32([[30,70],[170,20],[50,180],[160,170]])

imgs = {
    "Original": img,
    "Scale 1.5": cv2.warpAffine(img, np.float32([[1.5,0,0],[0,1.5,0]]), (c,r)),
    "Scale 0.5": cv2.warpAffine(img, np.float32([[0.5,0,0],[0,0.5,0]]), (c,r)),
    "Translate": cv2.warpAffine(img, np.float32([[1,0,50],[0,1,50]]), (c,r)),
    "Shear H": cv2.warpAffine(img, np.float32([[1,1,0],[0,1,0]]), (c,r)),
    "Shear V": cv2.warpAffine(img, np.float32([[1,0,0],[1,1,0]]), (c,r)),
    "Rotate": cv2.warpAffine(img, cv2.getRotationMatrix2D((c//2,r//2),45,1), (c,r)),
    "Warp": cv2.warpPerspective(img, cv2.getPerspectiveTransform(p1,p2), (c,r))
}

plt.figure(figsize=(15,10))
for i,(t,im) in enumerate(imgs.items(),1):
    plt.subplot(3,3,i)
    plt.imshow(im,cmap='gray')
    plt.title(t)
    plt.axis('off')

plt.tight_layout()
plt.show()