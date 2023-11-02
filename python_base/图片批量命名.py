import os


class BatchRename():

    def __init__(self):
        self.path = 'E:\\Python test\\图像处理\\Picture'  # 图片的路径 D:\Study Date\SSD\Train

    def rename(self):
        filelist = os.listdir(self.path)
        filelist.sort()
        total_num = len(filelist)  # 获取文件中有多少图片
        i = 0  # 文件命名从哪里开始（即命名从哪里开始）
        for item in filelist:
            if item.endswith('.JPG'):
                src = os.path.join(self.path, item)
                dst = os.path.join(os.path.abspath(self.path), str(i) + '.JPG')

                try:
                    os.rename(src, dst)
                    print('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except Exception as e:
                    print(e)
                    print('rename dir fail\r\n')
            elif item.endswith('.TIF'):
                src = os.path.join(self.path, item)
                dst = os.path.join(os.path.abspath(self.path), str(i) + '.TIF')

                try:
                    os.rename(src, dst)
                    print('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except Exception as e:
                    print(e)
                    print('rename dir fail\r\n')

        print('total %d to rename & converted %d jpgs' % (total_num, i))


if __name__ == '__main__':
    demo = BatchRename()  # 创建对象
    demo.rename()  # 调用对象的方法

