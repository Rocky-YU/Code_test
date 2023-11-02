# coding = utf-8
import cv2
from PIL import Image
from PIL import ImageEnhance
from numpy.ma import array
import numpy as np
import os
# 批量处理代码

rootdir = 'E://数据处理//A//0//' # 指明被遍历的文件夹

def operate(currentPath, filename, targetPath):
    # 读取图像
    image = Image.open(currentPath)
    image_cv = cv2.imread(currentPath)
    # image.show()
    # 增强亮度 bh_
    enh_bri = ImageEnhance.Brightness(image)
    brightness = 1.07
    image_brightened_h = enh_bri.enhance(brightness)
    # image_brightened_h.show()
    image_brightened_h.save(targetPath + 'bh_//images//bh_' + filename)  # 保存

    # 降低亮度 bl_
    enh_bri_low = ImageEnhance.Brightness(image)
    brightness = 0.87
    image_brightened_low = enh_bri_low.enhance(brightness)
    # image_brightened_low.show()
    image_brightened_low.save(targetPath + 'bl_//images//bl_' + filename)

    # 改变色度 co_
    enh_col = ImageEnhance.Color(image)
    color = 0.8
    image_colored = enh_col.enhance(color)
    # image_colored.show()
    image_colored.save(targetPath + 'co_//images//co_' + filename)

    # 改变对比度 cont_
    enh_con = ImageEnhance.Contrast(image)
    contrast = 0.8
    image_contrasted = enh_con.enhance(contrast)
    # image_contrasted.show()
    image_contrasted.save(targetPath + 'cont_//images//cont_' + filename)

    # 改变锐度 sha_
    enh_sha = ImageEnhance.Sharpness(image)
    sharpness = 3.0
    image_sharp = enh_sha.enhance(sharpness)
    # image_sharp.show()
    image_sharp.save(targetPath + 'sha_//images//sha_' + filename)

    # y方向上的缩放 yre_
    # image.show()
    w = image.width
    h = image.height
    print(w, h)
    out_ww = image.resize((w, h + 40))  # 拉伸成高为h的正方形
    # out_ww.show()
    out_ww_1 = np.array(out_ww)
    out_w_2 = out_ww_1[30:(h - 10), 0:w]  # 开始的纵坐标，开始的横坐标
    out_w_2 = Image.fromarray(out_w_2)
    # out_w_2.show()
    out_w_2.save(targetPath + 'yre_//images//yre_' + filename)

    # x方向上的缩放 xre_
    # image.show()
    out_hh = image.resize((w + 80, h))  # 拉伸成宽为w的正方形,width,height
    # out_hh.show()
    out_hh_1 = array(out_hh)
    out_h_2 = out_hh_1[0:h, 40:(w + 40)]
    out_h_2 = Image.fromarray(out_h_2)
    # out_h_2.show()
    out_h_2.save(targetPath + 'xre_//images//xre_' + filename)

    # x左方向的平移 xl_
    # 平移矩阵[[1,0,-10]，[0,1,-12]]
    # image.show()
    w = image.width
    h = image.height
    M = np.array([[1, 0, -80], [0, 1, 0]], dtype=np.float32)
    image_cv_change = cv2.warpAffine(image_cv, M, (w, h))
    image_cv_change_RGB = cv2.cvtColor(image_cv_change, cv2.COLOR_BGR2RGB)
    image_cv_change = Image.fromarray(image_cv_change_RGB)
    # image_cv_change.show()
    image_cv_change.save(targetPath + 'xl_//images//xl_' + filename)

    # x右方向的平移 xr_
    # image.show()
    w = image.width
    h = image.height
    M = np.array([[1, 0, 80], [0, 1, 0]], dtype=np.float32)
    image_cv_change = cv2.warpAffine(image_cv, M, (w, h))
    image_cv_change_RGB = cv2.cvtColor(image_cv_change, cv2.COLOR_BGR2RGB)
    image_cv_change = Image.fromarray(image_cv_change_RGB)
    # image_cv_change.show()
    image_cv_change.save(targetPath + 'xr_//images//xr_' + filename)


for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        # print('parent is:' + parent)
        print('filename is: ' + filename)
        # 把文件名添加到一起后输出
        currentPath = os.path.join(parent, filename)
        # print('the full name of file is :' + currentPath)
        # 保存处理后的图片的目标文件夹
        targetPath = 'D://data//data enhancement//surprise//'
        # 进行处理
        operate(currentPath, filename, targetPath)
