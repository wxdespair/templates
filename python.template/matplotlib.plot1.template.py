#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: [wx]
Created: 2023-08-16 12:41
Last Modified: 2023-08-16 15:52
Description: 作为使用 matplotlib 绘制单一图像的模板文件，这其中只设置通用属性，不涉及具体绘图类别
Filename: matplotlib.plot1.template.py
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
    figsize=(10, 6),                            # 设置画布大小，(横向，纵向)，单位为英寸
    dpi=100,                                    # 设置分辨率
)

# 设置背景色
axs.set_facecolor("#f0f0f0")

# 设置边框线
## "top","left","bottom","right" 分别指代上，左，下，右，四条边框线，可以使用列表，也可以使用分号 : 指代所有框线
axs.spines.top.set_visible(True)                # 设置是否可见
axs.spines[["top", "left"]].set_color("blue")   # 设置颜色
axs.spines["top"].set_linewidth(2)              # 设置宽度
axs.spines[:].set_linestyle("--")               # 设置样式

# 设置标题
title = axs.set_title(
    "My Title",             # 标题内容
    fontsize=16,            # 标题字号
    loc="center",           # 设置标题显示位置，默认为居中，可选值有："left", "center", "right"，一般不与 x 参数一起使用
    pad=10,                 # 设置标题与图像顶部的距离，不会下降到图像内部，最多会在图像上边缘，单位为点，一般为1/72英寸，一般不与 y 参数一起使用
    # x=1,                    # 设置标题显示的横向位置，默认为0.5，相对于图像的横向位置，一般不与 loc 参数一起使用
    # y=1,                    # 设置标题显示的纵向位置，默认为1，相对于图像的纵向位置，一般不与 pad 参数一起使用
)

axs.set_xlabel(
    "X Axis",               # X 轴标签内容
    fontsize=16,            # 字号
    loc="center",           # 设置显示位置，默认居中，可选参数有："left", "center", "right"，一般不与 .xaxis.set_label_coords 一起使用
    labelpad=0,             # 调整 x 轴标签与 x 轴距离，一般不与 .xaxis.set_label_coords 一起使用
)
# axs.xaxis.set_label_coords(0.5, -0.12)      
                            # 设置 x 轴标签的位置，相对于图像，(横向，纵向)，一般不与 set_xlabel 中的 labelpad 参数一起使用


axs.set_ylabel(
    "Y Axis",               # Y 轴标签内容
    fontsize=16,            # 字号
    loc="center",           # 设置显示位置，默认居中，可选参数有："bottom", "center", "top"，一般不与 .yaxis.set_label_coords 一起使用
    labelpad=0,             # 调整 y 轴标签与 y 轴距离，一般不与 .yaxis.set_label_coords 一起使用，推荐使用该参数
)
# axs.yaxis.set_label_coords(-0.12, 2)
                            # 设置 y 轴标签的位置，相对于图像，(横向，纵向)，一般不与 set_ylabel 中的 labelpad 参数一起使用
                            # 由于位置原因，第二个控制纵向的参数无法正常使用，推荐使用 set_ylabel 中的 labelpad 参数


# 设置刻度与刻度线（坐标轴上那一小段线段）
axs.tick_params(
    # TODO 设置刻度
    axis="x",               # 指定坐标轴
    direction="inout",      # 指定方向，向内 in ，向外 out，双向 inout
    length=3,               # 设置刻度线长度
    width=1,                # 设置刻度线宽度
    colors="red",           # 设置刻度与刻度线颜色
)

axs.grid(
    True,                   # bool 值，是否显示网格线
    which="major",          # 控制显示主要和/或次要刻度上的网格线，可选参数有："major", "minor", "both"
    axis="both",            # 控制显示刻度的轴，可选参数有："both", "x", "y"
    color="gray",           # 设置网格线颜色，可接收任意色彩格式与matplotlib全局色彩
    alpha=0.5,              # 设置网格线透明度，也可以在 color 参数中使用 RGBa 格式设置
    linestyle="--",         # 设置网格线样式
    linewidth=0.5,          # 设置网格线宽度
)

# 绘制图像
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
axs.plot(x, y1, label='Sin')
axs.plot(x, y2, label='Cos')

# TODO 设置图像与边缘的距离
# TODO 设置图例

# 保存图片到本地
fig.savefig(
    "./images/test.jpg",    # 保持路径，支持格式包括：jpg,png,pdf,svg 等
    dpi=300,
    # bbox_inches= ,   # TODO
    # pad_inches= ,    # TODO
)
plt.show()                  # 显示图像
plt.close(fig)              # 关闭图像
