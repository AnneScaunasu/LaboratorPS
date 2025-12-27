import numpy as np
import matplotlib.pylab as plt
from scipy import datasets, ndimage
from scipy.fft import dctn, idctn


X = datasets.ascent()
plt.imshow(X, cmap='grey')
plt.show()

y = dctn(X)
freq_db = 20 * np.log10(abs(y))
plt.imshow(freq_db)
plt.show()

k = 120
y_ziped = y.copy()
y_ziped[k:] = 0
x_ziped = idctn(y_ziped)

plt.imshow(x_ziped, cmap='gray')
plt.show()

q_down = 10
x_jpeg = X.copy()
x_jpeg = q_down * np.round(x_jpeg / q_down)

plt.subplot(121).imshow(X, cmap='gray')
plt.title('Original')
plt.subplot(122).imshow(x_jpeg, cmap='gray')
plt.title('Down-sampled')
plt.show()

q_jpeg = [[16, 11, 10, 16, 24, 40, 51, 61],
          [12, 12, 14, 19, 26, 28, 60, 55],
          [14, 13, 16, 24, 40, 57, 69, 56],
          [14, 17, 22, 29, 51, 87, 80, 62],
          [18, 22, 37, 56, 68, 109, 103, 77],
          [24, 35, 55, 64, 81, 104, 113, 92],
          [49, 64, 78, 87, 103, 121, 120, 101],
          [72, 92, 95, 98, 112, 100, 103, 99]]

# encoding
x = X[:8,:8]
y = dctn(x)
y_jpeg = q_jpeg * np.round(y / q_jpeg)

# decoding
x_jpeg = idctn(y_jpeg)

# results
y_nnz = np.count_nonzero(y)
y_jpeg_nnz = np.count_nonzero(y_jpeg)

plt.subplot(121).imshow(x, cmap='gray')
plt.title('Original')
plt.subplot(122).imshow(x_jpeg, cmap='gray')
plt.title('JPEG')
plt.show()

print('Componente in frecventa:' + str(y_nnz) +
      '\nComponente in frecventa dupa cuantizare: ' + str(y_jpeg_nnz))
