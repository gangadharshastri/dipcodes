import cv2, numpy as np, matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\deron\OneDrive\Desktop\Barbara.tif", 0)

k = {
    "Original": None,
    "Average": np.ones((3,3),np.float32)/9,
    "Gaussian": np.array([[1,2,1],[2,4,2],[1,2,1]],np.float32)/16,
    "Laplacian 4": [[0,-1,0],[-1,4,-1],[0,-1,0]],
    "Laplacian 8": [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]],
    "Unsharp": [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
}

plt.figure(figsize=(12,8))
for i,(t,f) in enumerate(k.items(),1):
    plt.subplot(2,3,i)
    plt.imshow(img if f is None else cv2.filter2D(img,-1,np.float32(f)), cmap='gray')
    plt.title(t)
    plt.axis('off')

plt.tight_layout()
plt.show()