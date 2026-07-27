import cv2, numpy as np, matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\Students\Downloads\cameraman.png", 0)

plt.figure(figsize=(15,5))
for i in range(8):
    plt.subplot(2,4,i+1)
    plt.imshow(((img>>i)&1)*255, cmap='gray')
    plt.title(f"Bit {i}")
    plt.axis('off')

bits = [7,6,5]
rec = sum(((img>>i)&1)<<i for i in bits).astype(np.uint8)

plt.figure(figsize=(8,4))
for i, im in enumerate([img, rec], 1):
    plt.subplot(1,2,i)
    plt.imshow(im, cmap='gray')
    plt.title("Original" if i==1 else f"Bits {bits}")
    plt.axis('off')

plt.tight_layout()
plt.show()