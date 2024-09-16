import torch
import torch.nn as nn
from PIL import Image
import numpy as np
import torchvision.transforms as transforms
from torch.autograd import Variable

# 加载图像
image = Image.open('ori.jpg').convert('L')  # 转换为灰度图
transform = transforms.ToTensor()
image_tensor = transform(image)
image_tensor = image_tensor.unsqueeze(0)  # 添加batch维度

# 定义Sobel算子的水平和垂直核
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32)

# 创建PyTorch卷积层
sobel_x_conv = nn.Conv2d(1, 1, kernel_size=3, bias=False, padding=1)
sobel_y_conv = nn.Conv2d(1, 1, kernel_size=3, bias=False, padding=1)

# 设置卷积核权重
sobel_x_conv.weight.data = torch.from_numpy(sobel_x).view(1, 1, 3, 3)
sobel_y_conv.weight.data = torch.from_numpy(sobel_y).view(1, 1, 3, 3)

# 对图像应用水平和垂直Sobel滤波器
x_gradient = sobel_x_conv(Variable(image_tensor))
y_gradient = sobel_y_conv(Variable(image_tensor))

# 计算梯度幅值图像
gradient_magnitude = torch.sqrt(torch.pow(x_gradient, 2) + torch.pow(y_gradient, 2))

# 将结果裁剪到[0, 255]范围并转换为uint8类型，以便保存为图像文件
grad_x_img = (x_gradient.squeeze().detach().numpy() * 255).astype(np.uint8)
grad_y_img = (y_gradient.squeeze().detach().numpy() * 255).astype(np.uint8)
grad_magnitude_img = (gradient_magnitude.squeeze().detach().numpy() * 255).astype(np.uint8)

# 保存结果
Image.fromarray(grad_x_img).save('exp_1.jpg')
Image.fromarray(grad_y_img).save('exp_2.jpg')
Image.fromarray(grad_magnitude_img).save('exp_3.jpg')
