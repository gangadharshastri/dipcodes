import cv2, numpy as np, matplotlib.pyplot as plt

img = cv2.imread(r"/content/drive/MyDrive/sample_data_dip/Lenna.png", 0)

plt.figure(figsize=(12,8))
for i, l in enumerate([256, 128, 64, 32, 16, 8], 1):
    plt.subplot(2, 3, i)
    plt.imshow(np.floor(img/(256//l))*(256//l), cmap='gray')
    plt.title("Original" if l == 256 else f"{l} Levels")
    plt.axis('off')

plt.tight_layout()
plt.show()