import cv2, numpy as np, matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\Students\Downloads\Barbara.jpg", 0)

r1,s1,r2,s2 = 70,0,140,255

stretch = np.uint8(np.piecewise(
    img,
    [img<r1, (img>=r1)&(img<=r2), img>r2],
    [lambda x:s1*x/r1,
     lambda x:(s2-s1)*(x-r1)/(r2-r1)+s1,
     lambda x:(255-s2)*(x-r2)/(255-r2)+s2]
))

low, high = 100, 200
mask = (stretch>=low) & (stretch<=high)

imgs = {
    "Original": img,
    "Stretched": stretch,
    "Slice + BG": np.where(mask,255,stretch),
    "Slice": np.where(mask,255,0)
}

plt.figure(figsize=(15,5))
for i,(t,im) in enumerate(imgs.items(),1):
    plt.subplot(1,4,i)
    plt.imshow(im,cmap='gray')
    plt.title(t)
    plt.axis('off')

plt.tight_layout()
plt.show()