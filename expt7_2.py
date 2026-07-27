import cv2, numpy as np, matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\deron\OneDrive\Desktop\Cameraman.jpg",0)

F = np.fft.fftshift(np.fft.fft2(img))
r,c = img.shape
y,x = np.ogrid[:r,:c]
D0,n = 50,2

D = np.sqrt((x-c//2)**2 + (y-r//2)**2)
LP = 1/(1+(D/D0)**(2*n))
HP = 1-LP

ifft = lambda H: np.abs(np.fft.ifft2(np.fft.ifftshift(F*H)))

imgs = {
    "Original": img,
    "LPF": LP,
    "HPF": HP,
    "FFT": np.log1p(np.abs(F)),
    "Low Pass": ifft(LP),
    "High Pass": ifft(HP)
}

plt.figure(figsize=(12,6))
for i,(t,im) in enumerate(imgs.items(),1):
    plt.subplot(2,3,i)
    plt.imshow(im,cmap='gray')
    plt.title(t)
    plt.axis('off')

plt.tight_layout()
plt.show()