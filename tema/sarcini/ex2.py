import numpy as np
import matplotlib.pylab as plt
from scipy import datasets, ndimage
from scipy.fft import dctn, idctn


X = datasets.face()
plt.imshow(X, cmap='grey')
plt.show()

y_cb_cr_transform = np.array([[0.299, 0.587, 0.114],
                     [-0.169, -0.331, 0.5],
                     [0.5, -0.419, -0.081]])
centralize_y_cb_cr = [0, 128, 128] # ca sa nu avem numere negative

y_cb_cr_X = X @ y_cb_cr_transform.T + centralize_y_cb_cr

q_jpeg = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
          [12, 12, 14, 19, 26, 28, 60, 55],
          [14, 13, 16, 24, 40, 57, 69, 56],
          [14, 17, 22, 29, 51, 87, 80, 62],
          [18, 22, 37, 56, 68, 109, 103, 77],
          [24, 35, 55, 64, 81, 104, 113, 92],
          [49, 64, 78, 87, 103, 121, 120, 101],
          [72, 92, 95, 98, 112, 100, 103, 99]])
q3 = q_jpeg[:, :, None] # 3 canale

x_jpeg_YCbCr = np.zeros(y_cb_cr_X.shape)
non_zeroes = []

for i in range(8, y_cb_cr_X.shape[0] + 1, 8):
    for j in range(8, y_cb_cr_X.shape[1] + 1, 8):
        # encoding
        x = y_cb_cr_X[i-8:i,j-8:j, :]
        y = dctn(x, axes=(0,1), norm="ortho")

        y_jpeg = q3 * np.round(y / q3)

        # decoding
        x_jpeg = idctn(y_jpeg, axes=(0,1), norm="ortho")

        # results
        y_nnz = np.count_nonzero(y)
        y_jpeg_nnz = np.count_nonzero(y_jpeg)
        non_zeroes.append((y_nnz, y_jpeg_nnz))

        # appending
        x_jpeg_YCbCr[i - 8:i, j - 8:j, :] = x_jpeg

for pair in non_zeroes:
    print('Componente in frecventa:' + str(pair[0]) +
          '\nComponente in frecventa dupa cuantizare: ' + str(pair[1]))

inv_transform = np.linalg.inv(y_cb_cr_transform)
x_jpeg_final = np.clip((x_jpeg_YCbCr - centralize_y_cb_cr) @ inv_transform.T, 0, 255).astype(np.uint8)

plt.subplot(121).imshow(X)
plt.title('Original')
plt.subplot(122).imshow(x_jpeg_final)
plt.title('JPEG')

plt.savefig("ex2.pdf", format="pdf", bbox_inches="tight")
plt.show()
