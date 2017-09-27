# -*- coding: UTF8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from main import Ui_MainWindow
from rename import Ui_Form


class MainClass(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainClass, self).__init__(parent=None)
        self.Ui = Ui_MainWindow()
        self.Ui.setupUi(self)
        self.Ui.pushButton_rename.clicked.connect(self.rename)  # 编辑按钮打开重命名窗体


    # 打开子窗体
    def rename(self):
        """打开重命名窗体"""
        self.rename = Ui_Form()
        self.Form = QtWidgets.QWidget()
        self.rename.setupUi2(self.Form)
        self.rename.pushButton_ok.clicked.connect(self.getRenameFormat)  # 参数传递
        self.rename.pushButton_cancel.clicked.connect(self.appclose)  # 关闭窗体
        self.Form.show()

    def getRenameFormat(self):
        """将参数传递到main"""
        self.Ui.lineEdit_rename.setText(self.rename.newname1 + self.rename.hyphen1 + self.rename.datetimesn + self.rename.hyphen2 + self.rename.newname2)
        #传递给main隐藏标签
        self.Ui.label_1.setText(self.rename.newname1)
        self.Ui.label_2.setText(self.rename.hyphen1)
        self.Ui.label_3.setText(self.rename.datetimesn)
        self.Ui.label_4.setText(self.rename.hyphen2)
        self.Ui.label_5.setText(self.rename.newname2)
        self.Ui.label_6.setText(self.rename.lineEdit_sn.text()) #中缀序号位数
        #中缀日期

        self.Ui.label_8.setText(self.rename.datetimesn1)
        self.Ui.label_9.setText(self.rename.datetimesn2)
        #self.Ui.label_7.setText(self.rename.datetimesn3)  # 中缀拍摄日期序列位数




        self.Form.close()

    def appclose(self):
        """关闭重命名框"""
        self.Form.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainApp = MainClass()
    MainApp.show()
    sys.exit(app.exec_())
