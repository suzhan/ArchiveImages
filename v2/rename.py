# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rename.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(564, 324)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 10, 251, 20))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(160, 70, 81, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(250, 70, 81, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(340, 70, 81, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(70, 70, 81, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(Form)
        self.comboBox_5.setGeometry(QtCore.QRect(430, 70, 81, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(70, 130, 441, 141))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 20, 89, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 40, 89, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 60, 89, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 80, 89, 16))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 100, 89, 16))
        self.radioButton_5.setObjectName("radioButton_5")
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_6.setGeometry(QtCore.QRect(150, 60, 81, 22))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(120, 70, 21, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(250, 60, 21, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(280, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(280, 20, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(280, 72, 54, 20))
        self.label_5.setObjectName("label_5")
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider.setGeometry(QtCore.QRect(280, 110, 111, 19))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 280, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 280, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "示例       <原名称>_2017.09.29_000.jpg"))
        self.comboBox.setItemText(0, _translate("Form", "下划线"))
        self.comboBox.setItemText(1, _translate("Form", "连字符"))
        self.comboBox.setItemText(2, _translate("Form", "空格"))
        self.comboBox.setItemText(3, _translate("Form", "无"))
        self.comboBox_2.setItemText(0, _translate("Form", "拍摄日期"))
        self.comboBox_2.setItemText(1, _translate("Form", "序号"))
        self.comboBox_2.setItemText(2, _translate("Form", "拍摄日期/时间"))
        self.comboBox_3.setItemText(0, _translate("Form", "下划线"))
        self.comboBox_3.setItemText(1, _translate("Form", "连字符"))
        self.comboBox_3.setItemText(2, _translate("Form", "空格"))
        self.comboBox_3.setItemText(3, _translate("Form", "无"))
        self.comboBox_4.setItemText(0, _translate("Form", "原名称"))
        self.comboBox_4.setItemText(1, _translate("Form", "新名称"))
        self.comboBox_4.setItemText(2, _translate("Form", "无"))
        self.comboBox_5.setItemText(0, _translate("Form", "原名称"))
        self.comboBox_5.setItemText(1, _translate("Form", "新名称"))
        self.comboBox_5.setItemText(2, _translate("Form", "无"))
        self.radioButton.setText(_translate("Form", "yyyymmdd"))
        self.radioButton_2.setText(_translate("Form", "yymmdd"))
        self.radioButton_3.setText(_translate("Form", "mmddyyyy"))
        self.radioButton_4.setText(_translate("Form", "mmddyy"))
        self.radioButton_5.setText(_translate("Form", "mmdd"))
        self.comboBox_6.setItemText(0, _translate("Form", "下划线"))
        self.comboBox_6.setItemText(1, _translate("Form", "连字符"))
        self.comboBox_6.setItemText(2, _translate("Form", "空格"))
        self.comboBox_6.setItemText(3, _translate("Form", "无"))
        self.label_2.setText(_translate("Form", "+"))
        self.label_3.setText(_translate("Form", "+"))
        self.label_4.setText(_translate("Form", "结尾号码"))
        self.label_5.setText(_translate("Form", "号码长度"))
        self.pushButton.setText(_translate("Form", "确定"))
        self.pushButton_2.setText(_translate("Form", "取消"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
