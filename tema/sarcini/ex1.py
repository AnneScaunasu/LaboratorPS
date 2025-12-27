import numpy as np
import matplotlib.pylab as plt
from scipy import datasets, ndimage
from scipy.fft import dctn, idctn


X = datasets.ascent()
q_jpeg = [[16, 11, 10, 16, 24, 40, 51, 61],
          [12, 12, 14, 19, 26, 28, 60, 55],
          [14, 13, 16, 24, 40, 57, 69, 56],
          [14, 17, 22, 29, 51, 87, 80, 62],
          [18, 22, 37, 56, 68, 109, 103, 77],
          [24, 35, 55, 64, 81, 104, 113, 92],
          [49, 64, 78, 87, 103, 121, 120, 101],
          [72, 92, 95, 98, 112, 100, 103, 99]]

x_jpeg_final = np.zeros(X.shape)
non_zeroes = []

for i in range(8, X.shape[0] + 1, 8):
    for j in range(8, X.shape[1] + 1, 8):
        # encoding
        x = X[i-8:i,j-8:j]
        y = dctn(x)
        y_jpeg = q_jpeg * np.round(y / q_jpeg)

        # decoding
        x_jpeg = idctn(y_jpeg)

        # results
        y_nnz = np.count_nonzero(y)
        y_jpeg_nnz = np.count_nonzero(y_jpeg)
        non_zeroes.append((y_nnz, y_jpeg_nnz))

        # appending
        x_jpeg_final[i-8:i, j-8:j] = x_jpeg

for pair in non_zeroes:
    print('Componente in frecventa:' + str(pair[0]) +
          '\nComponente in frecventa dupa cuantizare: ' + str(pair[1]))

plt.subplot(121).imshow(X, cmap='gray')
plt.title('Original')
plt.subplot(122).imshow(x_jpeg_final, cmap='gray')
plt.title('JPEG')

plt.savefig("ex1.pdf", format="pdf", bbox_inches="tight")
plt.show()
