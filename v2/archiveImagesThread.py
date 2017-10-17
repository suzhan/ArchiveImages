import os
from cmath import e

import requests
import re
import shutil
import hashlib
import time
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal

import exiftool


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

        self.filelist = []

        # a = self.mylabel_0.text()

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

    def get_top_post(self, d, a):
        """对源目录中的文件进行处理"""

        directory = d["File:Directory"]  # 文件目录
        filename = d["File:FileName"]  # 文件名
        filetype = d["File:FileType"]  # 文件类型
        sourceFile = d["SourceFile"]  # 源文件，带路径

        #创建日期,
        if filetype == "JPEG" or  filetype == "NEF":
            try:
                d["EXIF:CreateDate"]
            except:
                try:
                    d["XMP:CreateDate"]
                except:
                    try:
                        d["XMP:DateTimeOriginal"]
                    except:
                        try:
                            d["EXIF:DateTimeOriginal"]
                        except:
                            createdate = "no-createdate"
                        else:
                            createdate = d["EXIF:DateTimeOriginal"]
                    else:
                        createdate = d["XMP:DateTimeOriginal"]
                else:
                    createdate = d["XMP:CreateDate"]
            else:
                createdate = d["EXIF:CreateDate"]
        elif filetype == "MP4" or filetype == "MOV":
            try:
                d["QuickTime:CreateDate"]
            except:
                createdate = "no-createdate"
            else:
                createdate = d["QuickTime:CreateDate"]
        else:
            createdate = "no-createdate"


        #相机类型
        if filetype == "JPEG" or filetype == "NEF":
            try:
                d["EXIF:Model"]
            except:
                model = "no-model"
            else:
                model = d["EXIF:Model"]
        elif filetype == "MOV":
            try:
                d["QuickTime:Model"]
            except:
                model = "no-model"
            else:
                model = d["QuickTime:Model"]
        else:
            model = "no-model"

        # 镜头类型
        try:
            d["MakerNotes:Lens"]
        except:
            lens = "no-lens"
        else:
            lens = d["MakerNotes:Lens"]


        # 经度
        try:
            d["EXIF:GPSLongitude"]
        except:
            GPSLongitude = "no-GPS"
        else:
            GPSLongitude = d["EXIF:GPSLongitude"]

        # 纬度
        try:
            d["EXIF:GPSLatitude"]
        except:
            GPSLatitude = "no-GPS"
        else:
            GPSLatitude = d["EXIF:GPSLatitude"]

        #修改格式为2008-10-22 16:28:39
        if createdate == "no-createdate":
            createdate = "no-createdate"
        else:
            createdate = createdate.replace(':', '-')[:10] + createdate[10:]

        #地理位置
        if GPSLongitude == "no-GPS":
            location = "no-GPS"
        else:
            location = '{},{}'.format(str(GPSLatitude),str(GPSLongitude))


        print("----------------------------------")
        print('filename:' + filename)
        print('filetype:' + filetype)
        print('createdate:' + createdate)
        print('model:' + model)
        print('lens:' + lens)
        print('GPSLongitude:' + str(GPSLongitude))
        print('GPSLatitude:' + str(GPSLatitude))
        #print(self.geocode(location))
        print("-----------------------------------")

        if self.myRadioButton_date.isChecked() == True:
            if createdate == "no-createdate":
                dst = f'{self.subreddits_dst}/no-createdate/no-createdate/'
            else:
                dst = f'{self.subreddits_dst}/{createdate[0:4]}/{createdate[:10]}/'

        elif self.myRadioButton_cameraType.isChecked() == True :
            # 如果按相机类型

            if model == "no-model":
                dst = f'{self.subreddits_dst}/no-model/no-model/'
            else:
                dst = f'{self.subreddits_dst}/{createdate[0:4]}/{model}/'

        elif self.myRadioButton_lensType.isChecked() == True :
            # 如果按镜头类型

            if lens == "no-lens":
                dst = f'{self.subreddits_dst}/no-lens/no-lens/'
            else:
                dst = f'{self.subreddits_dst}/{createdate[0:4]}/{lens}/'

        elif self.myRadioButton_GPS.isChecked() == True :
            # 如果按GSP
            # self.geocode(location) 找出地理位置

            if GPSLongitude == "no-GPS":
                dst = f'{self.subreddits_dst}/no-GPS/no-GPS/'
            else:
                dst = f'{self.subreddits_dst}/{createdate[0:4]}/{self.geocode(location)}/'
        else:
            pass


        # 建立存储目标目录名
        if not os.path.exists(dst):
            os.makedirs(dst)

        tt = str(len(self.myfilenames))

        # 如果存储目录存在同名文件，检测hashe值及文件大小， 如果一样，不作处理, 如只是同命，更命后再复制
        dubfilelist = self.find_dub_filename(directory + '/' + filename)

        info = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " " + str(a) + "/" + str(tt) + " " + "文件:" + \
               filename + " " + "拍摄时间:" + createdate + " "

        # 如果源目录与目标目录没有重复文件名的
        if len(dubfilelist) == 0:
            # 如果选择重命名
            if self.myCheckBox_rename.isChecked() == True:
                # 原文件名
                # print("原文件名")
                # print(os.path.split(archFilename)[1])
                bb = self.reFilename(filename, createdate, a) + os.path.splitext(filename)[1]
                shutil.copy2(filename, dst)
                # print(dst + '/' + os.path.split(archFilename)[1]) #原文件名
                # print(dst + '/' + bb) #新名路径
                shutil.move(dst + '/' + os.path.split(filename)[1], dst + '/' + bb)

                # 如果选择删除文件
                if self.myCheckBox_del == True:
                    os.remove(filename)

                top_post = info + "移动到:" + os.path.split(dst)[1]

            else:
                shutil.copy(sourceFile, dst)

                # 如果选择删除文件
                if self.myCheckBox_del == True:
                    os.remove(sourceFile)

                top_post = info + "移动到:" + '..' + dst[-17:]
        else:

            if self.calculate_hashes(filename) in dubfilelist:
                top_post = info + "已存在，不作复制"  # 有重复的文件
            else:
                # 只是文件名重复，修改为文件名再复制，加上拍摄日期如 DSC_1689_2017-07-15.jpg
                newfilename = f'{os.path.splitext(filename)[0]}{"_"}{createdate[:10]}{os.path.splitext(filename)[1]}'

                shutil.move(filename, newfilename)
                shutil.copy2(newfilename, dst)

                if self.myCheckBox_del == True:  # 如果选择删除文件
                    os.remove(filename)

                top_post = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + str(a) + "/" + str(tt) + " " + \
                           os.path.split(filename)[1] + " " + "文件名已存在, 变更文件名为" + newfilename + "复制"

        return top_post


    def reFilename(self, filename, t, a):
        """
        重命名文件名
        """
        # 新文件名前缀名称
        if self.mylabel_newname1.text() == "<原名称>":
            newName1 = os.path.split(filename)[1][:-4]
        elif self.mylabel_newname1.text() == "无":
            newName1 = ''
        else:
            newName1 = self.mylabel_newname1.text()

        # 新文件名前缀连接符
        newName2 = self.mylabel_hyphen1.text()

        # print(self.mylabel_datetimesn1.text())
        # 中缀
        if self.mylabel_datetimesn1.text() == "20171130":  # yyyymmdd
            newName3_1 = t.replace('-', '')[:8]
        elif self.mylabel_datetimesn1.text() == "171130":  # yymmdd
            newName3_1 = t.replace('-', '')[2:8]
        elif self.mylabel_datetimesn1.text() == "11302017":  # mmddyyyy
            newName3_1 = t.replace('-', '')[4:8] + t[0:4]
        elif self.mylabel_datetimesn1.text() == "113017":  # mmddyy
            newName3_1 = t.replace('-', '')[4:8] + t[2:4]
        elif self.mylabel_datetimesn1.text() == "1130":  # mmdd
            newName3_1 = t.replace('-', '')[4:8]
        else:
            newName3_1 = ''

        newName3_2 = self.mylabel_datetimesn2.text()

        if self.mylabel_datetimesn3.text() == "150922":

            newName3_3 = self.t.replace(':', '')[11:] + '_' + str(a)

        elif self.mylabel_datetimesn3.text() == "1509":
            newName3_3 = self.t.replace(':', '')[13:] + '_' + str(a)
            print(newName3_3)
        else:
            b = len(str(self.mylabel_datetimesn3.text()))
            c = len(str(a))
            newName3_3 = (str(0) * (b - c)) + str(a)  # 中缀位数

        # 整合newName3
        newName3 = str(newName3_1) + str(newName3_2) + str(newName3_3)

        newName4 = self.mylabel_hyphen2.text()

        # 新文件名后缀名称
        if self.mylabel_newname2.text() == "<原名称>":
            newName5 = os.path.split(filename)[1][:-4]
        elif self.mylabel_newname2.text() == "无":
            newName5 = ''
        else:
            newName5 = self.mylabel_newname2.text()

        # 文件名整合
        newName = newName1 + newName2 + newName3 + newName4 + newName5
        print(newName)

        return newName

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

    def geocode(self, location):
        """检测GPS地理位置，国内版用高德地图API, 国际版使用google map api"""

        # 高德
        # parameters = {'location': location, 'key': 'af1bd859d39559bf7d226107ab9fb899'}
        # base = 'http://restapi.amap.com/v3/geocode/regeo';
        # response = requests.get(base, parameters)
        # answer = response.json()
        #
        # return answer['regeocode']['formatted_address']

        # goole map api
        parameters = {'latlng': location , 'key': 'AIzaSyBLUVoW6RXJozTtq-WQ8OMHgKiT3zU4m4g'}
        base = 'https://maps.googleapis.com/maps/api/geocode/json'
        response = requests.get(base, parameters)
        #print(response.url)
        answer = response.json()
        #print(answer)
        return answer['results'][1]['formatted_address']
        # google map api   不同的精度需要调整[2] 里边的数字
        #0 Bei Huan Nan Hai Li Jiao, Nanshan Qu, Shenzhen Shi, Guangdong Sheng, China, 518057
        #3  Nanshan, Shenzhen, Guangdong, China, 518057
        #2  Shenzhen, Guangdong, China
        #1  Nanshan, Shenzhen, Guangdong, China
        #5  China

    def run(self):
        a = 0
        # for archFilename in self.myfilenames:  # 需处理的图像列表传到线程类中
        #    a = a + 1
        #    top_post = self.get_top_post(archFilename, a)  # 进行归档处理
        #    self.postSignal.emit(top_post)  # run方法中处理并获得数据，然后通过信号将其发出
        with exiftool.ExifTool() as et:
            metadata = et.get_metadata_batch(self.myfilenames)
        for d in metadata:
            a = a + 1
            print(d)
            top_post = self.get_top_post(d, a)
            # time.sleep(5)
            self.postSignal.emit(top_post)
