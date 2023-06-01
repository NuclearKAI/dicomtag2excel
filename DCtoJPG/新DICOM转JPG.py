import pydicom # 用来解析dicom格式图像的像素值
import numpy as np
import cv2 # 用于保存图片
import os
import re
# 定义dicom to jpg转换函数
def convert_from_dicom_to_jpg(img, low_window, high_window, save_path):
    """

    :param img: dicom图像的像素值信息
    :param low_window: dicom图像像素值的最低值
    :param high_window: dicom图像像素值的最高值
    :param save_path: 新生成的jpg图片的保存路径
    :return:
    """
    lungwin = np.array([low_window * 1., high_window * 1.]) # 将pydicom解析的像素值转换为array
    newimg = (img - lungwin[0]) / (lungwin[1] - lungwin[0]) # 将像素值归一化0-1
    newimg = (newimg * 255).astype('uint8') # 再转换至0-255，且将编码方式由原来的unit16转换为unit8
    # 用cv2写入图像指令，保存jpg即可
    cv2.imwrite(save_path, newimg, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

count = 1 # 设置了一个变量用来作为保存后jpg图像的名称的，可自行修改其他的
path = r'/Users/kai/NCAC/example/zfk-example-ac-nc/230505503314' # dicom文件夹路径
filename = os.listdir(path) # 打开文件夹中的图像的文件名，作为列表返回
filenamelist = os.listdir(path)
rules = re.compile(r'(.*?).dcm')

# print(filename) # 可查看一下文件夹下有哪些文件

# 开始遍历文件夹下的每张dicom图像
# for i in filename:
for filename in filenamelist:
    print(filename)
    newFilename = re.findall(rules, str(filename))[0]
    print(newFilename)
    # document = os.path.join(path, i)
    document = os.path.join(path, filename)
    outputpath = r'/Users/kai/NCAC/example/zfk-example-ac-nc' # 保存jpg图像的路径
    countfullname =  newFilename + '.jpg' # 后缀.jpg
    output_jpg_path = os.path.join(outputpath, countfullname) # 设置保存每张图片的路径

    ds = pydicom.dcmread(document) # 解析一张dicom图片
    img_array = ds.pixel_array # 将像素值信息提取
    # img_array = sitk.GetArrayFromImage(ds_array)
    # shape = img_array.shape  # name.shape
    # img_array = np.reshape(img_array, (shape[1], shape[2]))
    high = np.max(img_array) # 找到最大的
    low = np.min(img_array)# 找到最小的
    # 调用函数，开始转换
    convert_from_dicom_to_jpg(img_array, low, high, output_jpg_path)
    # count += 1 # 为下一张图像的名称作准备，加1变成2

