import cv2, numpy as np, matplotlib.pyplot as plt

img = np.zeros((200,200), np.uint8)
cv2.putText(img,'R',(50,150),cv2.FONT_HERSHEY_SIMPLEX,4,255,8)

r,c = img.shape
sx = sy = 0.5

T = {
    "Original": None,
    "V Reflect": [[-1,0,c],[0,1,0]],
    "H Reflect": [[1,0,0],[0,-1,r]],
    "Both": [[-1,0,c],[0,-1,r]],
    "Shear X": [[1,.5,-.5*r//2],[0,1,0]],
    "Shear Y": [[1,0,0],[.5,1,-.5*c//2]],
    "Scale": [[sx,0,c*(1-sx)/2],[0,sy,r*(1-sy)/2]],
    "Translate": [[1,0,40],[0,1,30]]
}

plt.figure(figsize=(16,8))
for i,(t,m) in enumerate(T.items(),1):
    plt.subplot(2,4,i)
    plt.imshow(img if m is None else cv2.warpAffine(img,np.float32(m),(c,r)), cmap='gray')
    plt.title(t)
    plt.axis('off')

plt.tight_layout()
plt.show()