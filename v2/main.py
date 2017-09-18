# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QFileDialog,QStyleFactory,QApplication
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    #rename_signal=pyqtSignal()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 579)
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
        # add

        self.checkBox_Subdirectory.toggle()
        self.checkBox_Subdirectory.stateChanged.connect(self.changeSubdirectory)
        # add_end
        #是否选择删除文件
        self.checkBox_del = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_del.setGeometry(QtCore.QRect(60, 90, 231, 16))
        self.checkBox_del.setObjectName("checkBox_del")
        # add

        self.checkBox_del.toggle()
        self.checkBox_del.stateChanged.connect(self.changeDel)
        # add_end
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
        # add
        self.radioButton_date.toggle()
        self.radioButton_date.toggled.connect(self.changeDate)
        # add_end
        #按相机型号
        self.radioButton_cameraType = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_cameraType.setGeometry(QtCore.QRect(60, 250, 91, 20))
        self.radioButton_cameraType.setObjectName("radioButton_cameraType")
        # add
        self.radioButton_cameraType.toggle()
        self.radioButton_cameraType.toggled.connect(self.changeCameraType)
        # add_end
        #按镜头型号
        self.radioButton_lensType = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_lensType.setGeometry(QtCore.QRect(60, 280, 91, 20))
        self.radioButton_lensType.setObjectName("radioButton_lensType")
        # add
        self.radioButton_lensType.toggle()
        self.radioButton_lensType.toggled.connect(self.changelensType)
        # add_end
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
        self.radioButton_src.toggle()
        self.radioButton_src.toggled.connect(self.changeSrc)
        # add_end

        #开始处理
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(400, 540, 75, 23))
        self.pushButton_start.setObjectName("pushButton_start")
        #停止处理
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(480, 540, 75, 23))
        self.pushButton_stop.setObjectName("pushButton_stop")
        #进度条
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 470, 581, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        #处理进度标签
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 500, 581, 31))
        self.label.setObjectName("label")

        self.groupBox_schedule = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_schedule.setGeometry(QtCore.QRect(20, 450, 601, 81))
        self.groupBox_schedule.setObjectName("groupBox_schedule")
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
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.checkBox_Subdirectory.setChecked(True)  # 设定默认值
        self.checkBox_del.setChecked(False)
        self.checkBox_rename.setChecked(False)
        self.radioButton_select.setChecked(True)  # 默认选中
        self.radioButton_date.setChecked(True)
        self.pushButton_rename.setDisabled(True)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_src.setText(_translate("MainWindow", "浏览"))
        self.checkBox_Subdirectory.setText(_translate("MainWindow", "包含子文件夹"))
        self.checkBox_del.setText(_translate("MainWindow", "处理文件后，将其从此文件夹中删除"))
        self.groupBox_src.setTitle(_translate("MainWindow", "来源"))
        self.lineEdit_rename.setText(_translate("MainWindow", "<原文件名>_<拍摄日期>.jpg"))
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
        self.label.setText(_translate("MainWindow", "处理中：                  文件名：                        状态：                12 / 100 总数  "))
        self.groupBox_schedule.setTitle(_translate("MainWindow", "进度"))


    def srcBtnClicked(self,filepath):
        '''选择源文件夹'''
        self.sPath=QFileDialog.getExistingDirectory()
        self.lineEdit_src.setText(self.sPath)

    def changeSubdirectory(self,state):
        '''选择子文件夹'''
        print(state)
        print(Qt.Checked)
        #if Qt.Checked == state:
        #    MainWindow.setWindowTitle("已经选择子文件夹")
        #else:
        #    MainWindow.setWindowTitle("取消选择子文件夹")


    def changeDel(self,state):
        '''选择将文件删除'''
        #if Qt.Checked == state:
        #    MainWindow.setWindowTitle("已经选择将文件删除")
        #else:
        #    MainWindow.setWindowTitle("取消选择将文件删除")


    def changeRename(self,state):
        '''选择将文件更名'''
        self.pushButton_rename.setDisabled(False)
        #if Qt.Checked == state:
        #    MainWindow.setWindowTitle("已经选择将文件更名")
        #else:
        #    MainWindow.setWindowTitle("取消选择将文件更名")

    def changeDate(self, state):
        '''选择按日期整理'''
        print(state)
        #if self.radioButton_date.isChecked():
        #    MainWindow.setWindowTitle("已经选择按日期整理")


    def changeCameraType(self,state):
        '''选择按相机类型整理'''
        print(state)
        #if self.radioButton_cameraType.isChecked():
        #    MainWindow.setWindowTitle("已经选择按相机类型整理")



    def changelensType(self,state):
        '''选择按镜头类型整理'''
        print(state)
        #if self.radioButton_lensType.isChecked():
        #    MainWindow.setWindowTitle("已经选择按镜头类型整理")

    def changeGPS(self,state):
        '''选择按镜头类型整理'''
        print(state)
        if state:
            self.horizontalSlider.setEnabled(True)
        else:
            self.horizontalSlider.setEnabled(False)

        #if self.radioButton_GPS.isChecked():
        #    MainWindow.setWindowTitle("已经选择按GPS整理")

    def changeGPSvalue(self, value):
        print(value)
        #经度1秒 = 23.6m 纬度1秒 = 大约30.9m
        Longitude = value * 24
        Latitude = value * 31
        self.label_gpsm.setText('经：±' +str(Longitude)+'米' + ' ' + '纬：±' +  str(Latitude)+'米')

    def clickPushButton_rename(self):
        print("xxxxxxxxxxxx")

    def changeDstSelect(self):
        """选择一个目录作为存储目录"""
        self.pushButton_dst.setDisabled(False)

    def changeSrc(self):
        """选择源目录"""
        self.pushButton_dst.setDisabled(True)

    def dstBtnClicked(self, filepath ):
        self.dPath=QFileDialog.getExistingDirectory()
        self.lineEdit_dst.setText(self.dPath)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()  #取得ui的class实例
    ui.setupUi(MainWindow)  #将ui实例绘制到窗口实例上﻿​
    MainWindow.show()      # 展示窗口﻿​
    sys.exit(app.exec_())

