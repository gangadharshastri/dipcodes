import cv2, numpy as np, matplotlib.pyplot as plt

img = cv2.imread(r"/content/drive/MyDrive/sample_data_dip/cameraman.tiff", 0)
g = 0.4

imgs = {
    "Original": img,
    "Negative": 255 - img,
    "Log": np.uint8(np.log1p(img)*255/np.log1p(img).max()),
    f"Gamma={g}": np.uint8((img/255)**g*255)
}

plt.figure(figsize=(12,8))
for i, (t, im) in enumerate(imgs.items(), 1):
    plt.subplot(2,2,i)
    plt.imshow(im, cmap='gray')
    plt.title(t)
    plt.axis('off')

plt.figure(figsize=(12,8))
for i, (t, im) in enumerate(imgs.items(), 1):
    plt.subplot(2,2,i)
    plt.hist(im.ravel(), 256, (0,256))
    plt.title(t)

plt.tight_layout()
plt.show()