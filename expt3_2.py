import cv2, matplotlib.pyplot as plt
from skimage.exposure import match_histograms

src = cv2.imread(r"C:\Users\Students\Downloads\cameraman.png", 0)
ref = cv2.imread(r"C:\Users\Students\Downloads\Lena.png", 0)

imgs = {
    "Source": src,
    "Equalized": cv2.equalizeHist(src),
    "Reference": ref,
    "Matched": match_histograms(src, ref, channel_axis=None)
}

plt.figure(figsize=(12,8))
for i, (t, im) in enumerate(imgs.items(), 1):
    plt.subplot(2,3,i)
    plt.imshow(im, cmap='gray')
    plt.title(t)
    plt.axis('off')

for i, (t, im) in enumerate([("Source Hist", src), ("Matched Hist", imgs["Matched"])], 5):
    plt.subplot(2,3,i)
    plt.hist(im.ravel(), 256)
    plt.title(t)

plt.tight_layout()
plt.show()