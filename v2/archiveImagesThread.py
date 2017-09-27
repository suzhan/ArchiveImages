import os
from cmath import e

import exifread
import re, shutil
import hachoir
import hashlib
import time
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal


class GetPostThread(QThread):
    # 在QThread类中定义信号
    postSignal = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)
        self.subreddits_src = []
        self.subreddits_dst = []
        self.myCheckBox_del = []
        self.myCheckBox_rename = []
        self.mylineEdit_rename = []

        self.myRadioButton_date = []
        self.myRadioButton_cameraType = []
        self.myRadioButton_lensType = []
        self.myRadioButton_GPS = []

        self.mylabel_1 = []
        self.mylabel_2 = []
        self.mylabel_3 = []
        self.mylabel_4 = []
        self.mylabel_5 = []
        self.mylabel_6 = []
        self.mylabel_7 = []
        self.mylabel_8 = []
        self.mylabel_9 = []


        self.filelist = []

    def setSubReddit_src(self, lineEdit_src):
        """源目录"""
        self.subreddits_src = lineEdit_src

    def setSubReddit_dst(self, lineEdit_dst):
        """存储目录"""
        self.subreddits_dst = lineEdit_dst

    def setCheckBox_del(self, checkBox_del):
        """是否选择删除"""
        self.myCheckBox_del = checkBox_del

    def setCheckBox_rename(self, checkBox_rename):
        """是否选择重命名"""
        self.myCheckBox_rename = checkBox_rename

    def setLineEdit_rename(self, lineEdit_rename):
        """重命名格式框"""
        self.mylineEdit_rename = lineEdit_rename

    def setRadioButton_date(self, radioButton_date):
        """按拍摄日期选择"""
        self.myRadioButton_date = radioButton_date

    def setRadioButton_cameraType(self, radioButton_cameraType):
        """按相机类型选择"""
        self.myRadioButton_cameraType = radioButton_cameraType

    def setRadioButton_lensType(self, radioButton_lensType):
        """按镜头类型选择"""
        self.myRadioButton_lensType = radioButton_lensType

    def setRadioButton_GPS(self, radioButton_GPS):
        """按GPS选择"""
        self.myRadioButton_GPS = radioButton_GPS


    def setlabel_1(self, label_1):
        """重命名参数1"""
        self.mylabel_1 = label_1
    def setlabel_2(self, label_2):
        """重命名参数2"""
        self.mylabel_2 = label_2
    def setlabel_3(self, label_3):
        """重命名参数3"""
        self.mylabel_3 = label_3
    def setlabel_4(self, label_4):
        """重命名参数4"""
        self.mylabel_4 = label_4
    def setlabel_5(self, label_5):
        """重命名参数5"""
        self.mylabel_5 = label_5
    def setlabel_6(self, label_6):
        """重命名参数6"""
        self.mylabel_6 = label_6
    def setlabel_7(self, label_7):
        """重命名参数7"""
        self.mylabel_7 = label_7
    def setlabel_8(self, label_8):
        """重命名参数7"""
        self.mylabel_8 = label_8
    def setlabel_9(self, label_9):
        """重命名参数7"""
        self.mylabel_9 = label_9


    def setArchFilename(self, archFilename):
        """需整理目录"""
        self.myfilenames = archFilename

    def get_top_post(self, archFilename):
        """对源目录中的文件进行处理"""
        # 取得exif中的拍摄日期时间
        #print(archFilename)


        if  os.path.splitext(archFilename)[1] == '.MOV':
            t = self.getOriginalDateMOV(archFilename)
        else:
            t = self.getOriginalDate(archFilename)

        # 建立存储目标目录名
        dst = f'{self.subreddits_dst}/{t[0:4]}/{t}'
        if not os.path.exists(dst):
            os.makedirs(dst)

        # 如果存储目录存在同名文件，检测hashe值及文件大小， 如果一样，不作处理, 如只是同命，更命后再复制
        dubfilelist = self.find_dub_filename(os.path.split(archFilename)[1])

        info = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " " +  os.path.split(archFilename)[1] + " " + "拍摄时间:" + t + " "


        if len(dubfilelist) == 0:
            #如果没有重复的
            #如果选择重命名

            #print(self.myCheckBox_rename.isChecked())
            #
            if self.myCheckBox_rename.isChecked() == True:
                print("选择了重命令及方式不为空")
                print("^^^^^^^^^^^^^^^^")
                print(self.mylabel_1.text())
                print(self.mylabel_2.text())
                print(self.mylabel_3.text())
                print(self.mylabel_4.text())
                print(self.mylabel_5.text())
                print(self.mylabel_6.text())
                print(self.mylabel_7.text())
                print(self.mylabel_8.text())
                print(self.mylabel_9.text())
                print("^^^^^^^^^^^^^^^^")
                if self.mylabel_1.text() == "<原名称>":
                    dst_name1 = os.path.split(dst)[1]
                elif self.mylabel_1.text() == "无":
                    dst_name1 = ''
                else:
                    dst_name1 = self.mylabel_1.text()

                if self.mylabel_3.text() == "20171130-0000":
                    dst_name3 = os.path.split(dst)[1]
                elif self.mylabel_3.text() == "无":
                    dst_name3 = ''
                else:
                    dst_name3 = self.mylabel_3.text()

                if self.mylabel_5.text() == "<原名称>":
                    dst_name5 = os.path.split(dst)[1]
                elif self.mylabel_5.text() == "无":
                    dst_name5 = ''
                else:
                    dst_name5 = self.mylabel_5.text()



                #print(self.rename.newname1)

            #shutil.copy2(archFilename, dst)


            #如果选择删除文件
            if self.myCheckBox_del == True:
                os.remove(archFilename)
            top_post = info + "移动到:" + os.path.split(dst)[1]
        else:
            if self.calculate_hashes(archFilename) in dubfilelist:
                #有重复的
                top_post = info + "已存在，不作复制"
            else:
                #只是文件名重复，修改为文件名再复制
                newfilename = f'{os.path.splitext(archFilename)[0]}{"_"}{t}{os.path.splitext(archFilename)[1]}'
                shutil.move(archFilename, newfilename)
                shutil.copy2(newfilename, dst)
                # 如果选择删除文件
                if self.myCheckBox_del == True:
                   os.remove(archFilename)
                top_post = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " " + os.path.split(archFilename)[1] + " "  + "文件名已存在, 变更文件名为" + newfilename + "复制"
        return top_post

    def getOriginalDate(self, filename):
        """
        处理'.jpg', '.png', '.mp4', '.nef', '.3gp', '.flv', '.mkv'文件.读出建立日期
        """
        #with open(filename,'rb') as f:
        #    exif = exifread.process_file(f)
        #    if exif is not None:
        #        t= exif['EXIF DateTimeOriginal']
        #        return str(t).replace(":", ".")[:10]
        #state = os.stat(filename)
        #return time.strftime("%Y.%m.%d", time.localtime(state[-2]))
        try:
            fd=open(filename, 'rb')
        except:
            raise ReadFailException("unopen file[%s]\n" % filename)

        data=exifread.process_file(fd)

        if data:
            try:
                t=data['EXIF DateTimeOriginal']
                return str(t).replace(":", ".")[:10]
            except:
                pass

        state=os.stat(filename)
        return time.strftime("%Y.%m.%d", time.localtime(state[-2]))

    def getOriginalDateMOV(self, filename):
        """单独处理mov视频文件,读出建立日期"""
        with createParser(filename) as parser:
            metadata = extractMetadata(parser)
            t = metadata.exportPlaintext(line_prefix="")[4][15:25]  # 截取建立日期
            return str(t).replace("-", ".")

    def calculate_hashes(self, filename):
        """得出文件的MD5,sha1码，文件大小,用于对比文件"""
        hash_md5 = hashlib.md5()
        hash_sha1 = hashlib.sha1()
        with open(filename, "rb") as f:
            data = f.read()
            md5_returned = hashlib.md5(data).hexdigest()
            sha1_returned = hashlib.sha1(data).hexdigest()
            filesize_returned = os.path.getsize(filename)
        return md5_returned, sha1_returned, filesize_returned

    def find_dub_filename(self, filename):
        """检测存储目录是否存在同名文件,并得出md5sha1码存在结果"""
        result = []
        for root, dirs, files in os.walk(self.subreddits_dst):
            for filename2 in files:
                if filename == filename2:
                    result.append(self.calculate_hashes(os.path.join(root, filename)))
        return result

    def run(self):
        for archFilename in self.myfilenames:  # 需处理的图像列表传到线程类中
            top_post = self.get_top_post(archFilename)  # 进行归档处理
            self.postSignal.emit(top_post)  # run方法中处理并获得数据，然后通过信号将其发出
