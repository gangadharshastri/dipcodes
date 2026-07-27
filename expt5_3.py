import cv2, numpy as np, matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\deron\OneDrive\Desktop\blurry_moon.tif",0)

k = np.array([[1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[4,16,24,16,4],[1,4,6,4,1]],np.float32)/256

def conv(img,k):
    p=k.shape[0]//2
    pad=np.pad(img,p)
    out=np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            out[i,j]=np.clip((pad[i:i+5,j:j+5]*k).sum(),0,255)
    return out.astype(np.uint8)

b = conv(img,k)
m = cv2.subtract(img,b)

imgs = {
    "Original": img,
    "Blurred": b,
    "Mask": m,
    "Unsharp": cv2.add(img,m),
    "HB 1.5": cv2.addWeighted(img,1.5,b,-1,0),
    "HB 2.5": cv2.addWeighted(img,2.5,b,-1,0)
}

plt.figure(figsize=(15,8))
for i,(t,im) in enumerate(imgs.items(),1):
    plt.subplot(2,3,i)
    plt.imshow(im,cmap='gray')
    plt.title(t)
    plt.axis('off')

plt.tight_layout()
plt.show()