# -*- coding: utf-8 -*-
import os            # 导入os模块，用于文件和目录操作
import cv2           # 导入OpenCV库，用于图像处理操作
import time          # 导入time模块，用于添加延迟操作
import argparse      # 导入argparse模块，用于解析命令行参数
import itertools     # 导入itertools模块，用于创建高效的迭代器
import numpy as np   # 导入NumPy库，用于科学计算和多维数组处理

def draw_QR(img, left_top_points, size, data, row, col, reverse=False):
    """
    在给定的图像上绘制QR码样式的矩形块
    :param img: 要绘制QR码的图像 (空白图像)
    :param left_top_points: 矩形块左上角坐标的列表
    :param size: 每个矩形块的大小
    :param data: 要编码的二进制数据
    :param row: QR码的行数
    :param col: QR码的列数
    :param reverse: 是否反转颜色，默认为False
    :return: 绘制好的图像
    """
    for i, v in enumerate(data[:row*col]):  # 遍历二进制数据中的每一位
        # 计算当前矩形块的右下角坐标
        right_bottom_point = (left_top_points[i][0] + size, left_top_points[i][1] + size)
        
        if not reverse:  # 如果不反转颜色
            color = (255, 255, 255) if v == "0" else (0, 0, 0)  # "0" -> 白色, "1" -> 黑色
        else:  # 如果反转颜色
            color = (0, 0, 0) if v == "0" else (255, 255, 255)  # "0" -> 黑色, "1" -> 白色
        
        # 在图像上绘制一个填充的矩形块，颜色根据二进制数据决定
        cv2.rectangle(img, left_top_points[i], right_bottom_point, color=color, thickness=-1)
    
    return img  # 返回绘制完成的图像

if __name__ == '__main__':
    parser = argparse.ArgumentParser()  # 创建ArgumentParser对象，用于解析命令行参数
    # 添加-f参数，用于指定输入文件名，参数为必须提供
    parser.add_argument('-f', type=str, default=None, required=True, help='输入文件名称')
    # 添加-size参数，用于指定图片放大倍数，默认为5
    parser.add_argument('-size', type=int, default=5, help='图片放大倍数(默认5倍)')
    
    args = parser.parse_args()  # 解析命令行参数

    # 根据提供的文件名参数，获取完整的文件路径
    file_path = os.path.join(args.f)

    if not os.path.exists(file_path):  # 检查输入文件是否存在
        print(f"文件 {file_path} 不存在，请检查路径！")  # 如果文件不存在，打印错误信息
        exit(1)  # 退出程序

    if not os.path.exists("./out"):  # 检查是否存在输出目录，如果不存在则创建
        os.mkdir("./out")
    
    # 打开并读取输入文件中的二进制数据，去除首尾空白字符
    with open(file_path, "r", encoding='utf-8') as f:
        data = f.read().strip()

    size = args.size  # 获取放大倍数

    # 计算所有可能的行数和列数的组合，使得row * col == len(data)
    dic = {X: int(len(data) / X) for X in range(1, len(data)) if len(data) % X == 0}
    
    if not dic:  # 如果找不到合适的行列组合
        print("无法找到适合的宽高比例，请检查输入数据长度是否正确。")  # 打印错误信息
        exit(1)  # 退出程序

    # 遍历所有可能的行列组合
    for row, col in dic.items():
        # 创建两个空白图像，用于绘制QR码，大小为(row * size, col * size)
        img1 = np.zeros((row * size, col * size), dtype=np.uint8)
        img2 = np.zeros((row * size, col * size), dtype=np.uint8)

        # 生成左上角坐标列表，用于绘制矩形块
        left_top_points = [(j, i) for i, j in itertools.product(range(0, row * size, size), range(0, col * size, size))]

        # 在第一个图像上绘制正常的QR码，并保存到输出目录
        cv2.imwrite(f"./out/{col}_{row}.png", draw_QR(img1, left_top_points, size, data, row, col, reverse=False))
        # 在第二个图像上绘制颜色反转的QR码，并保存到输出目录
        cv2.imwrite(f"./out/{col}_{row}_reverse.png", draw_QR(img2, left_top_points, size, data, row, col, reverse=True))
        # 打印当前图像的宽度和高度信息
        print(f"[-] 宽度:{col:6} 高度:{row:6}, 已保存在运行目录out中...")

    # 打印所有行列组合遍历完成的提示信息
    print("[-] 已经遍历完所有情况, 即将自动关闭!")
    time.sleep(0.5)  # 延迟0.5秒后退出程序
