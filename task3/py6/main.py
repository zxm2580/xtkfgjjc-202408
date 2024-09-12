import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

#图像列表
img_files = ['1.tiff', '2.tiff', '3.tiff', '4.tiff','5.tiff','6.tiff','7.tiff','8.tiff','9.tiff','10.tiff','11.tiff']

# 遍历图像文件
for filename in img_files:
    # 读取图片
    image = cv2.imread(filename)
    # 转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 应用高斯模糊以减少图像噪声
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # 创建掩膜
    mask = cv2.inRange(blurred, 0, 95)
    ''' 
    # 也可以通过二值化区分轮廓
    # 应用阈值处理以二值化图像
    _, thresh = cv2.threshold(gray, 95, 255, cv2.THRESH_BINARY_INV)
    # 查找轮廓
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    '''
    # 进行形态学开操作，先腐蚀后膨胀，以消除噪声和恢复油滴边缘
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=1)
    # 找到掩膜中的轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 复制一个图片用于绘制结果
    colored_image = image.copy()
    # 遍历所有轮廓，并对其进行填色处理
    for contour in contours:
        cv2.drawContours(colored_image, [contour], -1, (255, 0, 0), -1)

    #展示填色结果图
    file_basename, _ = os.path.splitext(filename)
    result = cv2.cvtColor(colored_image, cv2.COLOR_RGB2BGR)
    plt.subplot(1, 2, 1), plt.imshow(image), plt.title(f'{filename}')
    plt.subplot(1, 2, 2), plt.imshow(result), plt.title(f'exp_{file_basename}.tiff')
    plt.show()
    plt.close()

    # 保存结果图片
    cv2.imwrite(f'exp_{file_basename}.tiff', colored_image)
