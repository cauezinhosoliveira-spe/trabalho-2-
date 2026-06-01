import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar imagem em escala de cinza
img = cv2.imread("imagem.jpg", 0)

# Transformada de Fourier
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Espectro de magnitude
magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)

rows, cols = img.shape
crow, ccol = rows // 2, cols // 2

# ==========================
# FILTRO PASSA-BAIXA
# ==========================
mask_low = np.zeros((rows, cols), np.uint8)
r = 50

for i in range(rows):
    for j in range(cols):
        if (i - crow)**2 + (j - ccol)**2 <= r**2:
            mask_low[i, j] = 1

low_pass = fshift * mask_low

img_back_low = np.fft.ifft2(np.fft.ifftshift(low_pass))
img_back_low = np.abs(img_back_low)

# ==========================
# FILTRO PASSA-ALTA
# ==========================
mask_high = np.ones((rows, cols), np.uint8)

for i in range(rows):
    for j in range(cols):
        if (i - crow)**2 + (j - ccol)**2 <= r**2:
            mask_high[i, j] = 0

high_pass = fshift * mask_high

img_back_high = np.fft.ifft2(np.fft.ifftshift(high_pass))
img_back_high = np.abs(img_back_high)

# ==========================
# FILTRO PASSA-BANDA
# ==========================
mask_band = np.zeros((rows, cols), np.uint8)

r1 = 30
r2 = 80

for i in range(rows):
    for j in range(cols):
        dist = (i - crow)**2 + (j - ccol)**2

        if r1**2 <= dist <= r2**2:
            mask_band[i, j] = 1

band_pass = fshift * mask_band

img_back_band = np.fft.ifft2(np.fft.ifftshift(band_pass))
img_back_band = np.abs(img_back_band)

# ==========================
# EXIBIÇÃO
# ==========================

plt.figure(figsize=(15,8))

plt.subplot(231)
plt.imshow(img, cmap='gray')
plt.title("Imagem Original")
plt.axis("off")

plt.subplot(232)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title("Espectro de Fourier")
plt.axis("off")

plt.subplot(234)
plt.imshow(img_back_low, cmap='gray')
plt.title("Passa-Baixa")
plt.axis("off")

plt.subplot(235)
plt.imshow(img_back_high, cmap='gray')
plt.title("Passa-Alta")
plt.axis("off")

plt.subplot(236)
plt.imshow(img_back_band, cmap='gray')
plt.title("Passa-Banda")
plt.axis("off")

plt.tight_layout()
plt.show()