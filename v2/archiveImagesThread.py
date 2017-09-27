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

        self.mylabel_newname1 = []
        self.mylabel_hyphen1 = []
        self.mylabel_datetimesn1 = []
        self.mylabel_datetimesn2 = []
        self.mylabel_datetimesn3 = []
        self.mylabel_hyphen2 = []
        self.mylabel_newname2 = []
        self.mylabel_lineEdit_sn = []
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


    def setlabel_newname1(self, label_newname1):
        """前缀名称"""
        self.mylabel_newname1 = label_newname1

    def setlabel_hyphen1(self, label_hyphen1):
        """前缀连接符"""
        self.mylabel_hyphen1 = label_hyphen1

    def setlabel_datetimesn1(self, label_datetimesn1):
        """中缀日期类型"""
        self.mylabel_datetimesn1 = label_datetimesn1

    def setlabel_datetimesn2(self, label_datetimesn2):
        """中缀连接符"""
        self.mylabel_datetimesn2 = label_datetimesn2

    def setlabel_datetimesn3(self, label_datetimesn3):
        """中缀时间或序号位数"""
        self.mylabel_datetimesn3 = label_datetimesn3

    def setlabel_hyphen2(self, label_hyphen2):
        """后缀连接符"""
        self.mylabel_hyphen2 = label_hyphen2

    def setlabel_newname2(self, label_newname2):
        """后缀名称"""
        self.mylabel_newname2 = label_newname2

    def setlabel_lineEdit_sn(self, label_lineEdit_sn):
        """中缀序列号"""
        self.mylabel_lineEdit_sn = label_lineEdit_sn



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
            if self.myCheckBox_rename.isChecked() == True:
                print("选择了重命令及方式不为空")
                print("^^^^^^^^^^^^^^^^")
                print(self.mylabel_newname1.text())
                print(self.mylabel_hyphen1.text())
                print(self.mylabel_datetimesn1.text())
                print(self.mylabel_datetimesn2.text())
                print(self.mylabel_datetimesn3.text())
                print(self.mylabel_hyphen2.text())
                print(self.mylabel_newname2.text())
                print(self.mylabel_lineEdit_sn.text())
                print("^^^^^^^^^^^^^^^^")

                #原文件名
                print(os.path.split(archFilename)[1])
                #print(self.rename.newname1)

                #新文件名
                if self.mylabel_newname1.text() == "<原名称>":
                    newName1 = os.path.split(archFilename)[1][:-4]
                elif self.mylabel_newname1.text() == "无":
                    newName1 = ''
                else:
                    newName1 = self.mylabel_newname1.text()


                print(newName1)   

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
