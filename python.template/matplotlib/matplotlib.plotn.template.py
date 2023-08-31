#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: [wx]
Created: 2023-08-31 10:17
Last Modified: 2023-08-31 10:17
Description: 作为使用 matplotlib 绘制组图的模板文件，这其中只设置通用属性，不涉及具体绘图类别
Filename: matplotlib.plotn.template.py
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# 设置全局字体
matplotlib.rcParams["font.family"] = "Microsoft YaHei"
matplotlib.rcParams["font.size"] = 14
matplotlib.rcParams["font.style"] = "italic"
matplotlib.rcParams["font.weight"] = "bold"


# 创建画布
fig, axs = plt.subplots(
    figsize=(10, 6),
    # dpi=100,
)
""" subplots()
:param figsize: 设置画布大小，(横向，纵向)，单位为英寸
:param dpi: 设置分辨率
            最好创建画布的时候不要设置，保存图片的时候再设置，否则可能导致图片比例及文字字号失衡等问题
"""


# 保存图片到本地
fig.savefig(
    fname="./matplotlib.plot1.template_test.jpg",
    dpi=300,
    bbox_inches='tight',
    pad_inches=0.2,
)
""" Figure.savefig()
:param fname: 保存路径，支持格式包括：jpg,png,pdf,svg 等
:param dpi: 保存图像分辨率，点/英寸，也可以传入一个图像对象，会调用它的分辨率
:param format: 设置保存图像格式，通常在 fname 参数中包含后缀，可以不用设置
:param metadata: 设置保存图像源数据，不同格式有不同的参数对
:param facecolor: 设置图像背景色，通常不设置，默认为白色，如果是png默认透明
:param bbox_inches: 设置边界，如果为 "tight" ，则尝试找出图像的紧边界，或者设置一个距离列表 (0.5, 0.2, 0.8, 0.8)，表示左下右上的距离
:param pad_inches: 接受一个浮点数，英寸，设置图像的填充（内边距），控制图像内容与图像边框之间的距离，从而在保存图像时添加一定的内边距
                   一般在 bbox_inches 参数为 "tight" 时使用
"""


# plt.show()
# # 显示图像
plt.close(fig)  
# # 关闭图像
