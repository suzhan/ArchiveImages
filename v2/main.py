# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

import sys, os
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog,QStyleFactory,QApplication,QMessageBox,QTextBrowser
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
from archiveImagesThread import GetPostThread


class Ui_MainWindow(object):

    #rename_signal=pyqtSignal()
    def __init__( self, parent = None ):
        super().__init__()
        #sys.exit(app.exec_())
        
        self.archThread = GetPostThread() #GetpostThread 参数传递地

        #建立信号槽连接
        self.archThread.postSignal.connect(self.getPostSlot)  #getpostthread.py run 线程送过来的信号， 主线程获得信号，并将它与信号处理函数（槽函数）相连接
        self.archThread.finished.connect(self.threadFinished)  # 完成时的线程处理


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 685)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_src = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_src.setGeometry(QtCore.QRect(40, 40, 481, 23))
        self.lineEdit_src.setObjectName("lineEdit_src")
        #选择源
        self.pushButton_src = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_src.setGeometry(QtCore.QRect(530, 40, 75, 23))
        self.pushButton_src.setObjectName("pushButton_src")
        #add
        self.pushButton_src.clicked.connect(lambda: self.srcBtnClicked(self.lineEdit_src.text()))  # 选择源文件夹按钮后将参数传到 lineEdit_src
        #add_end
        #是否选择子文件夹
        self.checkBox_Subdirectory = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Subdirectory.setGeometry(QtCore.QRect(60, 70, 101, 16))
        self.checkBox_Subdirectory.setObjectName("checkBox_Subdirectory")

        #是否选择删除文件
        self.checkBox_del = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_del.setGeometry(QtCore.QRect(60, 90, 231, 16))
        self.checkBox_del.setObjectName("checkBox_del")

        self.groupBox_src = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_src.setGeometry(QtCore.QRect(20, 19, 601, 101))
        self.groupBox_src.setObjectName("groupBox_src")
        #重命名文件框
        self.lineEdit_rename = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_rename.setGeometry(QtCore.QRect(60, 180, 461, 23))
        self.lineEdit_rename.setObjectName("lineEdit_rename")
        #选择重命名格式
        self.pushButton_rename = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rename.setGeometry(QtCore.QRect(530, 180, 75, 23))
        self.pushButton_rename.setObjectName("pushButton_rename")

        #self.pushButton_rename.clicked.connect(Form.show)

        #是否选择重命令
        self.checkBox_rename = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_rename.setGeometry(QtCore.QRect(60, 150, 61, 20))
        self.checkBox_rename.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_rename.setObjectName("checkBox_rename")
        # add

        self.checkBox_rename.toggle()
        self.checkBox_rename.stateChanged.connect(self.changeRename)
        # add_end
        #按拍摄日期
        self.radioButton_date = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_date.setGeometry(QtCore.QRect(60, 220, 91, 20))
        self.radioButton_date.setObjectName("radioButton_date")

        #按相机型号
        self.radioButton_cameraType = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_cameraType.setGeometry(QtCore.QRect(60, 250, 91, 20))
        self.radioButton_cameraType.setObjectName("radioButton_cameraType")

        #按镜头型号
        self.radioButton_lensType = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_lensType.setGeometry(QtCore.QRect(60, 280, 91, 20))
        self.radioButton_lensType.setObjectName("radioButton_lensType")

        #按GPS范围
        self.radioButton_GPS = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_GPS.setGeometry(QtCore.QRect(60, 310, 91, 20))
        self.radioButton_GPS.setObjectName("radioButton_GPS")
        # add
        self.radioButton_GPS.toggle()
        self.radioButton_GPS.toggled.connect(self.changeGPS)
        # add_end

        #GPS范围滑条
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(180, 312, 250, 19))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        # add
        self.horizontalSlider.valueChanged.connect(self.changeGPSvalue)
        # add_end

        # GPS范围值,米距离
        self.label_gpsm=QtWidgets.QLabel(self.centralwidget)
        self.label_gpsm.setGeometry(QtCore.QRect(440, 312, 270, 12))
        self.label_gpsm.setObjectName("label_gpsm")

        self.groupBox_method = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_method.setGeometry(QtCore.QRect(20, 130, 601, 221))
        self.groupBox_method.setObjectName("groupBox_method")
        self.groupBox_dst = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_dst.setGeometry(QtCore.QRect(20, 360, 601, 80))
        self.groupBox_dst.setObjectName("groupBox_dst")
        #目的
        self.lineEdit_dst = QtWidgets.QLineEdit(self.groupBox_dst)
        self.lineEdit_dst.setGeometry(QtCore.QRect(20, 40, 481, 23))
        self.lineEdit_dst.setObjectName("lineEdit_dst")
        #选择目的文件夹
        self.pushButton_dst = QtWidgets.QPushButton(self.groupBox_dst)
        self.pushButton_dst.setGeometry(QtCore.QRect(510, 40, 75, 23))
        self.pushButton_dst.setObjectName("pushButton_dst")
        #add
        self.pushButton_dst.clicked.connect(lambda: self.dstBtnClicked(self.lineEdit_dst.text()))  # 选择源文件夹按钮后将参数传到 lineEdit_src
        #选择文件夹或选择源目标
        self.radioButton_select = QtWidgets.QRadioButton(self.groupBox_dst)
        self.radioButton_select.setGeometry(QtCore.QRect(110, 20, 91, 16))
        self.radioButton_select.setObjectName("radioButton_select")


        # add
        self.radioButton_select.toggle()
        self.radioButton_select.toggled.connect(self.changeDstSelect)

        # add_end

        self.radioButton_src = QtWidgets.QRadioButton(self.groupBox_dst)
        self.radioButton_src.setGeometry(QtCore.QRect(230, 20, 101, 16))
        self.radioButton_src.setObjectName("radioButton_src")
        # add
        self.radioButton_src.clicked.connect(self.changeSrc)
        # add_end

        #开始处理
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(400, 650, 75, 23))
        self.pushButton_start.setObjectName("pushButton_start")
        #开始整理
        self.pushButton_start.clicked.connect(self.startBtnClicked)  # 开始信号

        #停止处理
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(480, 650, 75, 23))
        self.pushButton_stop.setObjectName("pushButton_stop")
        #进度条
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 470, 581, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")

        self.groupBox_schedule = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_schedule.setGeometry(QtCore.QRect(20, 450, 601, 191))
        self.groupBox_schedule.setObjectName("groupBox_schedule")
        #处理进度消息
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 500, 581, 131))
        self.textBrowser.setObjectName("textBrowser")

        #隐藏标签，用于接受参数传递
        self.label_newname1 = QtWidgets.QLabel(self.centralwidget)
        self.label_newname1.setObjectName("label_newname1")
        self.label_newname1.setHidden(True)
        self.label_hyphen1 = QtWidgets.QLabel(self.centralwidget)
        self.label_hyphen1.setObjectName("label_hyphen1")
        self.label_hyphen1.setHidden(True)
        self.label_datetimesn1 = QtWidgets.QLabel(self.centralwidget)
        self.label_datetimesn1.setObjectName("label_datetimesn1")
        self.label_datetimesn1.setHidden(True)
        self.label_datetimesn2 = QtWidgets.QLabel(self.centralwidget)
        self.label_datetimesn2.setObjectName("label_datetimesn2")
        self.label_datetimesn2.setHidden(True)
        self.label_datetimesn3 = QtWidgets.QLabel(self.centralwidget)
        self.label_datetimesn3.setObjectName("label_datetimesn3")
        self.label_datetimesn3.setHidden(True)
        self.label_hyphen2 = QtWidgets.QLabel(self.centralwidget)
        self.label_hyphen2.setObjectName("label_hyphen2")
        self.label_hyphen2.setHidden(True)
        self.label_newname2 = QtWidgets.QLabel(self.centralwidget)
        self.label_newname2.setObjectName("label_newname2")
        self.label_newname2.setHidden(True)


        self.groupBox_schedule.raise_()
        self.groupBox_method.raise_()
        self.groupBox_src.raise_()

        self.lineEdit_src.raise_()
        self.pushButton_src.raise_()
        self.checkBox_Subdirectory.raise_()
        self.checkBox_del.raise_()
        self.lineEdit_rename.raise_()
        self.pushButton_rename.raise_()
        self.checkBox_rename.raise_()
        self.radioButton_date.raise_()
        self.radioButton_cameraType.raise_()
        self.radioButton_lensType.raise_()
        self.radioButton_GPS.raise_()
        self.horizontalSlider.raise_()
        self.groupBox_dst.raise_()
        self.pushButton_start.raise_()
        self.pushButton_stop.raise_()
        self.progressBar.raise_()
        self.textBrowser.raise_()
        #self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.checkBox_Subdirectory.setChecked(True)  # 设定默认值
        self.checkBox_del.setChecked(False)
        self.checkBox_rename.setChecked(False)
        self.radioButton_select.setChecked(True)  # 默认选中
        self.radioButton_date.setChecked(True)
        self.pushButton_rename.setDisabled(True)

        if not self.lineEdit_src.text():
            self.radioButton_src.setDisabled(True)
        else:
            self.radioButton_src.setDisabled(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_src.setText(_translate("MainWindow", "浏览"))
        self.checkBox_Subdirectory.setText(_translate("MainWindow", "包含子文件夹"))
        self.checkBox_del.setText(_translate("MainWindow", "处理文件后，将其从此文件夹中删除"))
        self.groupBox_src.setTitle(_translate("MainWindow", "来源"))
        self.lineEdit_rename.setText(_translate("MainWindow", ""))
        self.pushButton_rename.setText(_translate("MainWindow", "编辑"))
        self.checkBox_rename.setText(_translate("MainWindow", "重命名"))
        self.radioButton_date.setText(_translate("MainWindow", "按拍摄日期"))
        self.radioButton_cameraType.setText(_translate("MainWindow", "按相机型号"))
        self.radioButton_lensType.setText(_translate("MainWindow", "按镜头型号"))
        self.radioButton_GPS.setText(_translate("MainWindow", "按GPS范围"))
        self.groupBox_method.setTitle(_translate("MainWindow", "方法"))
        self.label_gpsm.setText(_translate("MainWindow", "经：±0米 纬：±0米"))
        self.groupBox_dst.setTitle(_translate("MainWindow", "目的地"))
        self.pushButton_dst.setText(_translate("MainWindow", "浏览"))
        self.radioButton_select.setText(_translate("MainWindow", "选择文件夹"))
        self.radioButton_src.setText(_translate("MainWindow", "选择源文件夹"))
        self.pushButton_start.setText(_translate("MainWindow", "开始"))
        self.pushButton_stop.setText(_translate("MainWindow", "取消"))
        #self.label.setText(_translate("MainWindow", ""))
        self.groupBox_schedule.setTitle(_translate("MainWindow", "进度"))


    def srcBtnClicked(self,filepath):
        '''选择源文件夹'''
        self.sPath = QFileDialog.getExistingDirectory()
        print(self.sPath)
        self.lineEdit_src.setText(self.sPath)
        self.radioButton_src.setDisabled(False)
        #判断是否为空目录,如空目录弹出窗口，并退出
        if not os.listdir(self.sPath):
            self.messages('所选择的来源目录为空目录。')
            return
        return self.sPath


    def changeRename(self,state):
        '''选择将文件更名'''
        self.pushButton_rename.setDisabled(False)


    def changeGPS(self,state):
        '''选择按GPS整理'''
        #print(state)
        #当选择按GPS整理时，滑条生效
        if state:
            self.horizontalSlider.setEnabled(True)
        else:
            self.horizontalSlider.setEnabled(False)

    def changeGPSvalue(self, value):
        #print(value)
        #经度1秒 = 23.6m 纬度1秒 = 大约30.9m
        Longitude = value * 24
        Latitude = value * 31
        self.label_gpsm.setText('经：±' +str(Longitude)+'米' + ' ' + '纬：±' +  str(Latitude)+'米')

    def changeDstSelect(self):
        """选择一个目录作为存储目录"""
        self.pushButton_dst.setDisabled(False)
        self.lineEdit_dst.setText("") #清空目标目录框

    def changeSrc(self, filepath ):
        """选择源目录作为存储目录"""
        self.pushButton_dst.setDisabled(True)
        #如果没有选择源目录
        if  not self.lineEdit_src.text():
             print("请选择源文件夹")
        else:
             self.lineEdit_dst.setText(self.sPath)

    def dstBtnClicked(self, filepath ):
        """选择一个文件夹作为存储目录"""
        self.dPath = QFileDialog.getExistingDirectory()
        self.lineEdit_dst.setText(self.dPath)

    def startBtnClicked(self):
        """开始整理"""

        #如没有选择来源目录，弹窗口提示
        if not self.lineEdit_src.text():
            self.messages('请选择来源目录。')
            return
        # 如没有选择来源目录，弹窗口提示
        if not self.lineEdit_dst.text():
            self.messages('请选择存储目录。')
            return

        filename_list = []
        #将需整理的文件放入数组
        for root, dirs, files in os.walk(self.sPath, True):
            # 如果没选择子文件夹,限在根目录
            if self.checkBox_Subdirectory.isChecked() == False:
                dirs[:] = []
            for filename in files:
                filename = os.path.join(root, filename)
                f, e = os.path.splitext(filename)
                if e.lower() not in ('.jpg', '.jpeg', '.png', '.nef', '.mp4', '.3gp', '.flv', '.mkv', '.mov'):
                    continue
                filename_list.append(filename)
                
        #处理进度消息显示总文件数
        self.textBrowser.clear()   #清空结果
        self.textBrowser.append("开始整理")

        self.textBrowser.append('共' +str(len(filename_list))+'文件')

        self.progressBar.setMaximum(len(filename_list))  #设置进度值总数
        self.archThread.setSubReddit_src(self.sPath) # 取得源文件夹的路径,传送给archiveImagesThread.py
        self.archThread.setSubReddit_dst(self.dPath)  # 取得目标文件夹的路径,传送给archiveImagesThread.py
        self.archThread.setCheckBox_del(self.checkBox_del)  # 是否确认删除原文件,传送给archiveImagesThread.py
        self.archThread.setArchFilename(filename_list) #文件列表线程,传送给archiveImagesThread.py
        self.archThread.setCheckBox_rename(self.checkBox_rename)  # 是否重命名,传送给archiveImagesThread.py
        self.archThread.setLineEdit_rename(self.lineEdit_rename)  # 重命名格式,传送给archiveImagesThread.py
        self.archThread.setRadioButton_date(self.radioButton_date)   # 选择按拍摄日期处理， 传送给archiveImagesThread.py
        self.archThread.setRadioButton_cameraType(self.radioButton_cameraType)   # 选择按相机类型处理， 传送给archiveImagesThread.py
        self.archThread.setRadioButton_lensType(self.radioButton_lensType)   # 选择按镜头类型处理， 传送给archiveImagesThread.py
        self.archThread.setRadioButton_GPS(self.radioButton_GPS)   # 选择按GPS处理， 传送给archiveImagesThread.py

        #重命名传递到archiveImagesThread.py
        self.archThread.setlabel_newname1(self.label_newname1)
        self.archThread.setlabel_hyphen1(self.label_hyphen1)
        self.archThread.setlabel_datetimesn1(self.label_datetimesn1)
        self.archThread.setlabel_datetimesn2(self.label_datetimesn2)
        self.archThread.setlabel_datetimesn3(self.label_datetimesn3)  #中缀序号，拍摄日期序号，拍摄时间日期中的时间
        self.archThread.setlabel_hyphen2(self.label_hyphen2) #中缀序列号
        self.archThread.setlabel_newname2(self.label_newname2) #中缀拍摄日期序列号



        self.archThread.start()   #开始执行archThread线程
        
        self.pushButton_start.setEnabled(False)  # 设置开始按钮为禁用
        self.pushButton_stop.setEnabled(True)  # 设置停止按钮为启用
        
    def getPostSlot(self, top_post): #将整理结果显示到文本框textBrowser
        """处理过程"""
        self.textBrowser.append(top_post)
        self.progressBar.setValue(self.progressBar.value() + 1) #处理一个进度条+1
        
        
    def threadFinished(self):
        '''完成整理'''
        #self.progressBar.setValue(0)  #进度条值清空
        #if self.archThread.isRunning():
        #    self.archThread.terminate()
        #self.label.setText("整理结束。")
        self.textBrowser.append("整理完成！")

        self.pushButton_start.setEnabled(True)  # 设置开始按钮为禁用
        self.pushButton_stop.setEnabled(False)  # 设置停止按钮为雇用
   
    
    def messages(self, messages):
        """没有选择来源目录时，弹出窗口提示"""
        infoBox = QMessageBox()
        #infoBox.setIcon(QMessageBox.Information)
        infoBox.setText(messages + "       ")
        infoBox.setInformativeText("")
        infoBox.setWindowTitle("消息")
        #infoBox.setDetailedText("Detailed Text")
        infoBox.setStandardButtons(QMessageBox.Ok)
        infoBox.setEscapeButton(infoBox.exec_())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()  #取得ui的class实例
    ui.setupUi(MainWindow)  #将ui实例绘制到窗口实例上﻿​
    MainWindow.show()      # 展示窗口﻿​
    sys.exit(app.exec_())
    

