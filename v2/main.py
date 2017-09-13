# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QFileDialog
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):
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
        #是否选择重命令
        self.checkBox_rename = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_rename.setGeometry(QtCore.QRect(60, 150, 61, 20))
        self.checkBox_rename.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_rename.setObjectName("checkBox_rename")

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
        #按焦距
        self.radioButton_focalLength = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_focalLength.setGeometry(QtCore.QRect(60, 310, 91, 20))
        self.radioButton_focalLength.setObjectName("radioButton_focalLength")
        #焦距范围
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(140, 310, 221, 19))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

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
        #选择文件夹或选择源目标
        self.radioButton_select = QtWidgets.QRadioButton(self.groupBox_dst)
        self.radioButton_select.setGeometry(QtCore.QRect(110, 20, 91, 16))
        self.radioButton_select.setObjectName("radioButton_select")
        self.radioButton_src = QtWidgets.QRadioButton(self.groupBox_dst)
        self.radioButton_src.setGeometry(QtCore.QRect(230, 20, 101, 16))
        self.radioButton_src.setObjectName("radioButton_src")
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
        self.radioButton_focalLength.raise_()
        self.horizontalSlider.raise_()
        self.groupBox_dst.raise_()
        self.pushButton_start.raise_()
        self.pushButton_stop.raise_()
        self.progressBar.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
        self.radioButton_focalLength.setText(_translate("MainWindow", "按焦距"))
        self.groupBox_method.setTitle(_translate("MainWindow", "方法"))
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
        if Qt.Checked == state:
            MainWindow.setWindowTitle("已经选择子文件夹")
            print("1")
        else:
            MainWindow.setWindowTitle("没有选择")
            print("0")
    def changeDel(self,state):
        '''选择将文件删除'''
        if Qt.Checked == state:
            MainWindow.setWindowTitle("已经选择将文件删除")
        else:
            MainWindow.setWindowTitle("没有选择")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
