import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"/content/drive/MyDrive/sample_data_dip/Lenna.png", 0)

plt.figure(figsize=(12,8))

for i, f in enumerate([1, 2, 4, 8, 16, 32], 1):
    plt.subplot(2, 3, i)
    plt.imshow(img[::f, ::f], cmap='gray')
    plt.title("Original" if f == 1 else f"×{f}")
    plt.axis('off')
plt.tight_layout()
plt.show()