# -*- coding: utf-8 -*-

"""
整理图片视频程序V1
作者：suzhan
Email: suzhan.cn@gmail.com
功能：
可选源目录及存储目标目录，
可以整理的文件类型：.jpg, .png', .nef, .mp4, .3gp, .flv, .mkv, .mov
从文件的exif中得出拍摄日期，移动到存储目录，默认路径是 archives_[原目录名]
如果目标文件中存在与源文件的MD5,sha1，文件大小都一样的文件就忽略处理，直接删除
整理后删除源文件夹中的空目录。
"""

import sys, os
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QFileDialog, QPushButton, QLineEdit, QGridLayout, QTextEdit
from PyQt5.QtGui import QIcon
from archiveImagesThread import GetPostThread

class Ui_Form(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(Form)
        self.testThread = GetPostThread() #GetpostThread 参数传递地

        #建立信号槽连接
        self.testThread.postSignal.connect(self.getPostSlot)  #getpostthread.py run 线程送过来的信号， 主线程获得信号，并将它与信号处理函数（槽函数）相连接
        self.testThread.finished.connect(self.threadFinished)  # 完成时的线程处理

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(910, 520)
        icon=QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("arch.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)

        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 5, 871, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.lineEdit_src = QtWidgets.QLineEdit(self.gridLayoutWidget)  #源目录
        self.lineEdit_src.setObjectName("lineEdit_src")
        self.gridLayout.addWidget(self.lineEdit_src, 0, 1, 1, 1)

        self.lineEdit_dst = QtWidgets.QLineEdit(self.gridLayoutWidget)  #存储目录
        self.lineEdit_dst.setObjectName("lineEdit_dst")
        self.gridLayout.addWidget(self.lineEdit_dst, 1, 1, 1, 1)

        self.pushButton_src = QtWidgets.QPushButton(self.gridLayoutWidget)  #选择源
        self.pushButton_src.setObjectName("pushButton_src")
        self.pushButton_src.clicked.connect(lambda: self.srcBtnClicked(self.lineEdit_src.text())) # 选择源文件夹按钮后将参数传到 lineEdit_src
        self.gridLayout.addWidget(self.pushButton_src, 0, 0, 1, 1)


        self.pushButton_dst = QtWidgets.QPushButton(self.gridLayoutWidget)  #选择目标
        self.pushButton_dst.setObjectName("pushButton_dst")
        self.pushButton_dst.clicked.connect(lambda: self.dstBtnClicked(self.lineEdit_dst.text()))  # 选择目标文件夹按钮后将参数传到 lineEdit_dst
        self.gridLayout.addWidget(self.pushButton_dst, 1, 0, 1, 1)

        # 信息显示框
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 100, 871, 340))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.progressBar = QtWidgets.QProgressBar(Form)    #进度条
        self.progressBar.setGeometry(QtCore.QRect(20, 450, 871, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")

        self.gridLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(600, 470, 291, 51))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.startBtn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.startBtn.setObjectName("startBtn")
        self.startBtn.clicked.connect(self.startBtnClicked)  # 开始信号
        self.gridLayout_3.addWidget(self.startBtn, 0, 1, 1, 1)

        self.stopBtn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.stopBtn.setObjectName("stopBtn")
        self.stopBtn.setEnabled(False)
        self.stopBtn.clicked.connect(self.stopBtnClicked)  # 停止信号
        self.gridLayout_3.addWidget(self.stopBtn, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图片视频归档整理V1 suzhan.cn@gmail.com"))
        self.pushButton_src.setText(_translate("Form", " 选择整理目录 "))
        self.pushButton_dst.setText(_translate("Form", " 选择存储目录 "))
        #self.label.setText(_translate("Form", ""))
        self.startBtn.setText(_translate("Form", "开始"))
        self.stopBtn.setText(_translate("Form", "停止"))

    def srcBtnClicked(self, filePath):
        '''选择源文件夹'''
        self.sPath=QFileDialog.getExistingDirectory()
        self.lineEdit_src.setText(self.sPath)

        #设定默认存储目录为 archives_原文件夹名
        dirname = os.path.split(self.sPath)[1]
        self.dPath = os.path.dirname(self.sPath) + '/' + 'archives_' + dirname
        if not os.path.exists(self.dPath):
            os.makedirs(self.dPath)
        self.lineEdit_dst.setText(self.dPath)

        return self.sPath, self.dPath

    def dstBtnClicked(self, filePath):
        '''选择目标文件夹'''
        self.dPath=QFileDialog.getExistingDirectory()
        self.lineEdit_dst.setText(self.dPath)
        return self.dPath

    def startBtnClicked(self):
        '''开始整理'''
        self.progressBar.setValue(0)
        src = self.lineEdit_src.text()
        if src == "":
            #print("没有选择源文件夹")
            self.textBrowser.append("请选择整理目录。")
            return
        if not os.listdir(self.sPath):
            self.textBrowser.append("您所选择的整理目录为空目录。")
            return

        self.textBrowser.clear()   #清空结果
        self.textBrowser.append("开始整理")

        filename_list = []

        #将需整理的文件放入数组
        for root, dirs, files in os.walk(self.sPath, True):
            for filename in files:
                filename = os.path.join(root, filename)
                f, e = os.path.splitext(filename)
                if e.lower() not in ('.jpg', '.png', '.nef', '.mp4', '.3gp', '.flv', '.mkv', '.mov'):
                    continue
                filename_list.append(filename)
            #print(filename_list)

        totalCount = len(filename_list)
        self.progressBar.setMaximum(totalCount)  #设置进度值总数
        self.testThread.setSubReddit_src(self.sPath) # 取得源文件夹的路径,传送给
        self.testThread.setSubReddit_dst(self.dPath)  # 取得目标文件夹的路径,传送给
        self.testThread.setArchFilename(filename_list) #文件列表线程
        self.testThread.start()   #开始执行archThread线程
        self.startBtn.setEnabled(False)  # 设置开始按钮为禁用
        self.stopBtn.setEnabled(True)  # 设置停止按钮为启用

    def stopBtnClicked(self):
        '''停止整理'''
        #print("stop")
        self.testThread.terminate()
        self.startBtn.setEnabled(True)  # 设置开始按钮为禁用
        self.stopBtn.setEnabled(False)  # 设置停止按钮为雇用

    def threadFinished(self):
        '''完成整理'''
        #self.progressBar.setValue(0)  #进度条值清空



        if self.testThread.isRunning():
            self.testThread.terminate()
        self.textBrowser.append("整理结束。")
        self.cel(self.sPath)
        self.startBtn.setEnabled(True)  # 设置开始按钮为禁用
        self.stopBtn.setEnabled(False)  # 设置停止按钮为雇用

    def getPostSlot(self, top_post): #将整理结果显示到文本框textBrowser
        #print(top_post)   #打印执行结果 top_post 是getposttheard.py 执行结果
        self.textBrowser.append(top_post)  #消息打印到文本框textBrowser
        self.progressBar.setValue(self.progressBar.value() + 1) #处理一个进度条+1

    def cel(self, sPath):
        """
        删除空文件及空文件夹
        """
        for root, dirs, files in os.walk(self.sPath):
            for file in files:
                myfile = os.path.join(root, file)
                if not os.path.getsize(myfile):
                    os.remove(myfile)
                    #print('清理空文件:', myfile)
                    self.textBrowser.append('清理空文件:' + myfile)

            for dir in dirs:
                mydir = os.path.join(root, dir)
                if not os.listdir(mydir):
                    #shutil.rmtree(mydir)
                    os.rmdir(mydir)
                    #print('清理空文件夹:', mydir)
                    self.textBrowser.append('清理空文件夹:'+ mydir)
        self.textBrowser.append("清理源路径空目录完成。")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

