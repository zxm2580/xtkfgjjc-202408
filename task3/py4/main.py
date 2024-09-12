# task4.py
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 图像列表
img_files = ['1.bmp', '2.bmp', '2.jpg', '3.bmp', '4.bmp']

for i, imgfile in enumerate(img_files, start=1):
    img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)
    # 傅立叶变换
    fft_image = np.fft.fftshift(np.fft.fft2(img))
    plt.imsave(f'exp{i}_傅里叶频谱图.jpg', fft_image.real, cmap='gray')
    # 离散余弦变换 (DCT)
    dct_image = cv2.dct(np.float32(img))
    plt.imsave(f'exp{i}_DCT频谱图.jpg', dct_image, cmap='gray')
    # 空间域图像增强,这里使用log变换
    fft_enhance = np.log(1 + np.abs(fft_image))
    plt.imsave(f'exp{i}_傅里叶频谱图增强.jpg', fft_enhance, cmap='gray')
    dct_enhance = np.log(1 + np.abs(dct_image))
    plt.imsave(f'exp{i}_DCT频谱图增强.jpg', dct_enhance, cmap='gray')
    # 滤波
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)    # 傅里叶变换
    fshift = np.fft.fftshift(dft)   # 低频移至中心
    # 设置掩膜
    rows, cols = img.shape
    crow, ccol = int(rows / 2), int(cols / 2)   # 中心位置
    for j, yuzhi in enumerate([15, 30, 45], start = 1):
        # 低通滤波
        mask = np.zeros((rows, cols, 2), np.uint8)
        mask[crow - yuzhi:crow + yuzhi, ccol - yuzhi:ccol + yuzhi] = 1
        f = fshift * mask   # 将掩模与傅里叶变化后的图像相乘，保留四周部分，即保留低频部分
        ishift = np.fft.ifftshift(f)    # 低频移回
        img_back = cv2.idft(ishift)     # 傅里叶逆变换
        img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])  # 频域转回空域
        plt.imsave(f'exp{i}_低通滤波{j}.jpg', img_back, cmap='gray')
        # 高通滤波
        mask = np.ones((rows, cols, 2), np.uint8)
        mask[crow - yuzhi:crow + yuzhi, ccol - yuzhi:ccol + yuzhi] = 0
        f = fshift * mask   # 将掩模与傅里叶变化后的图像相乘，保留四周部分，即保留高频部分
        ishift = np.fft.ifftshift(f)    # 低频移回
        img_back = cv2.idft(ishift)     # 傅里叶逆变换
        img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])  # 频域转回空域
        plt.imsave(f'exp{i}_高通滤波{j}.jpg', img_back, cmap='gray')