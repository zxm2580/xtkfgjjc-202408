#py5
import cv2
import matplotlib.pyplot as plt

# 读取图像ori1
img = cv2.imread('ori1.jpg')

# 查看ori1直方图并保存
plt.figure(figsize=(10, 5))
plt.title('1_1')
plt.ylabel('Number of Pixels')
plt.xlabel('Pixel Intensity')
plt.hist(img.ravel(), 256, [0, 256])
plt.xlim([0, 256])
plt.savefig('exp1_1_ori1原始直方图.jpg')
plt.show()
plt.close()

# ori1取反，再查看直方图并保存
inverted_img = 255 - img
plt.figure(figsize=(10, 5))
plt.title('1_2')
plt.ylabel('Number of Pixels')
plt.xlabel('Pixel Intensity')
plt.hist(inverted_img.ravel(), 256, [0, 256])
plt.xlim([0, 256])
plt.savefig('exp1_2_ori1取反直方图.jpg')
plt.show()
plt.close()

# ori1使用直方图均衡，再查看直方图
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #转为灰度图
equalized_img = cv2.equalizeHist(gray_img)
plt.figure(figsize=(10, 5))
plt.title('1_3')
plt.ylabel('Number of Pixels')
plt.xlabel('Pixel Intensity')
plt.hist(equalized_img.ravel(), 256, [0, 256])
plt.xlim([0, 256])
plt.savefig('exp1_3_ori1直方图均衡.jpg')
plt.show()
plt.close()

# 定义磨皮函数
def smooth_skin(image, kernel_size):
    # 使用高斯模糊进行磨皮
    blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    return blurred

# 读取图片ori2
image = cv2.imread('ori2.jpg', cv2.IMREAD_COLOR)

# 磨皮处理并保存
smoothed_image = smooth_skin(image, kernel_size=5)
cv2.imwrite('exp2_1_ori2smoothed.jpg', smoothed_image)

# 磨皮前后直方图数据
hist_before = cv2.calcHist([image], [0], None, [256], [0, 256])
hist_after = cv2.calcHist([smoothed_image], [0], None, [256], [0, 256])

# 直方图保存
plt.figure(figsize=(10, 5))
plt.plot(hist_before, color='b', label='Original')
plt.plot(hist_after, color='r', label='Smoothed')
plt.title('2_1')
plt.legend()
plt.savefig('exp2_1_ori2磨皮前后直方图对比.jpg')
plt.show()
plt.close()
