#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: [wx]
Created: 2023-08-16 12:41
Last Modified: 2023-08-31 10:15
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
    figsize=(10, 6),
    # dpi=100,
)
""" subplots()
:param figsize: 设置画布大小，(横向，纵向)，单位为英寸
:param dpi: 设置分辨率
            最好创建画布的时候不要设置，保存图片的时候再设置，否则可能导致图片比例及文字字号失衡等问题
"""

# fig.set_size_inches(5, 9)
# 设置画布大小，(横向，纵向)，单位为英寸，与 figsize 效果相同


# 设置背景色
axs.set_facecolor("#f0f0f0")


# 设置边框线
## "top","left","bottom","right" 分别指代上，左，下，右，四条边框线，可以使用列表，也可以使用分号 : 指代所有框线
axs.spines.top.set_visible(True)
# 设置是否可见，有时可见也绘制不出边框线，可能颜色被设置透明或宽度被设置0
axs.spines[["top", "left"]].set_color("blue")
# 设置颜色
axs.spines["top"].set_linewidth(2)
# 设置宽度
axs.spines[:].set_linestyle("--")
# 设置样式


# 设置标题
title = axs.set_title(
    "My Title",
    fontsize=16,
    loc="center",
    pad=10,
    # x=1,
    # y=1,
)
""" Axes.set_title()
:param label: 标题内容
:param fontsize: 标题字号
:param loc: 设置标题显示位置，可选值有：["left", "center":[默认], "right"]，一般不与 x 参数一起使用
:param pad: 设置标题与图像顶部的距离，不会下降到图像内部，最多会在图像上边缘，单位为点，一般为1/72英寸，一般不与 y 参数一起使用
:param x: 设置标题显示的横向位置，默认为0.5，相对于图像的横向位置，一般不与 loc 参数一起使用
:param y: 设置标题显示的纵向位置，默认为1，相对于图像的纵向位置，一般不与 pad 参数一起使用
"""


# 设置x轴标签
axs.set_xlabel(
    xlabel="X Axis",
    fontsize=16,
    loc="center",
    labelpad=0,
)
""" Axes.set_xlabel()
:param xlabel: X 轴标签内容
:param fontsize: 字号
:param loc: 设置显示位置，可选参数有：{"left", "center":[默认], "right"}，一般不与 .xaxis.set_label_coords 一起使用
:param labelpad: # 调整 x 轴标签与 x 轴距离，一般不与 .xaxis.set_label_coords 一起使用
"""
# axs.xaxis.set_label_coords(0.5, -0.12)
# # 设置 x 轴标签的位置，相对于图像，(横向，纵向)，一般不与 set_xlabel 中的 labelpad 参数一起使用
# axs.xaxis.set_ticks_position('top')
# # 设置 x 轴位于上方
# axs.xaxis.set_label_position('top')
# # 设置 x 轴标签位于上方


# 设置y轴标签
axs.set_ylabel(
    ylabel="Y Axis",
    fontsize=16,
    loc="center",
    labelpad=0,
)
""" Axes.set_ylabel()
:param ylabel: Y 轴标签内容
:param fontsize: 字号
:param loc: 设置显示位置，可选参数有：{"bottom", "center":[默认], "top"}，一般不与 .yaxis.set_label_coords 一起使用
:param labelpad: # 调整 y 轴标签与 y 轴距离，一般不与 .yaxis.set_label_coords 一起使用
"""
# axs.yaxis.set_label_coords(-0.12, 2)
# # 设置 y 轴标签的位置，相对于图像，(横向，纵向)，一般不与 set_ylabel 中的 labelpad 参数一起使用
# # 由于位置原因，第二个控制纵向的参数无法正常使用，推荐使用 set_ylabel 中的 labelpad 参数
# axs.yaxis.set_ticks_position('right')
# # 设置 y 轴位于右侧
# axs.yaxis.set_label_position('right')
# # 设置 y 轴标签位于右侧


# 设置刻度范围
# xmin, xmax, ymin, ymax = 0, 1, 0, 1
# axs.set_xlim(xmin, xmax)
# axs.set_ylim(ymin, ymax)


# 设置刻度线（坐标轴上那一小段线段）
axs.xaxis.set_tick_params(
    direction='inout',
    length=3,
    width=1,
    colors='red'
)
""" Axes.xaxis.set_tick_params()
:param direction: 指定方向，{"in":向内, "out":外向, "inout": 双向}
:param length: 设置刻度线长度
:param width: 设置刻度线宽度
:param colors: 设置刻度与刻度线颜色
"""
axs.yaxis.set_tick_params(direction='inout', length=3, width=1, colors='red')
""" Axes.yaxis.set_tick_params()
:param 同 Axes.xaxis.set_tick_params()
"""
axs.tick_params(
    axis="x",
    direction="inout", length=3, width=1, colors="red",
)
""" Axes.tick_params()
:param axis: 选择应用的轴，可选参数为 {"x", "y", "both"}
:param 同 Axes.xaxis.set_tick_params()
"""


# 设置网格线
axs.grid(
    visible=True,
    which="major",
    axis="both",
    color="gray",
    alpha=0.5,
    linestyle="--",
    linewidth=0.5,
)
""" Axes.grid()
:param visible: bool 值，是否显示网格线
:param which: 控制显示主要和/或次要刻度上的网格线，可选参数有：{"major", "minor", "both"}
:param axis: 控制显示刻度的轴，可选参数有：{"both":双轴[默认], "x", "y"}
:param color: 设置网格线颜色，可接收任意色彩格式与matplotlib全局色彩
:param alpha: 设置网格线透明度，也可以在 color 参数中使用 RGBa 格式设置
:param linestyle: 设置网格线样式
:param linewidth: 设置网格线宽度
"""


# # 关闭轴线，This affects the axis lines, ticks, ticklabels, grid and axis labels.
# axs.set_axis_off()
# # 开启轴线
# axs.set_axis_on()


# 自定义设置图例
## 如不需要自定义，直接在绘图时指定标签，最后使用 plt.legend() 或 fig.legend() 显示即可
import matplotlib.patches as mpatches
COLOR_DICT = {
    "label1": (1 / 255, 83 / 255, 102 / 255),
    "label2": (245 / 255, 152 / 255, 143 / 255),
    "label3": (190 / 255, 228 / 255, 237 / 255),
    "label4": (90 / 255, 195 / 255, 220 / 255),
    "label5": (1 / 255, 165 / 255, 204 / 255),
}
handles = [
    mpatches.Patch(color=COLOR_DICT[key], label=key) for key in ["label1", "label2", "label3", "label4", "label5"]
]
first_legend = fig.legend(
    handles=handles,
    # loc='upper right',
    bbox_to_anchor=(0.94, 0.9)
)
""" Figure.legend()
:param handles: 用于绘制图例的列表，每个元素是图例中的一个对
:param loc: 用于设置图例显示位置，
            {"best", "upper right", "upper left", "lower left", "lower right", "right", 
             "center left", "center right", "lower center", "upper center", "center"}
            会与 bbox_to_anchor 参数冲突
:param bbox_to_anchor: 设置图例显示位置，元组首元素表示横向距左侧，次元素表示纵向距下方
"""
## 将图例添加到画布，在绘制单一图像时下三句代码作用相同
# plt.gca().add_artist(first_legend)
# fig.gca().add_artist(first_legend)
axs.add_artist(first_legend)


# 设置图像边缘的位置
fig.subplots_adjust(
    left=0.1,
    bottom=0.1,
    right=0.9,
    top=0.9
)
""" Figure.subplots_adjust()
:param left: 图像左边缘的位置，需要 <= right 参数
:param bottom: 图像下边缘的位置，需要 <= top 参数
:param right: 图像右边缘的位置
:param top: 图像上边缘的位置
"""


# 绘制图像
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
axs.plot(x, y1, label='Sin')
axs.plot(x, y2, label='Cos')


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
