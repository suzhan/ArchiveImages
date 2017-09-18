# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rename.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Ui_Form(object):

	def __init__(self):
		"""定时刷新"""
		super(Ui_Form, self).__init__()
		self.timer = QTimer()
		self.timer.timeout.connect(self.operate)
		self.timer.start(200)

	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(580, 314)

		# 示例
		self.label_example = QtWidgets.QLabel(Form)
		self.label_example.setGeometry(QtCore.QRect(90, 20, 450, 20))
		font = QtGui.QFont()
		font.setFamily("微软雅黑")
		font.setPointSize(12)
		font.setWeight(75)
		self.label_example.setFont(font)
		self.label_example.setObjectName("label_example")

		# 前缀文件名
		self.comboBox_name = QtWidgets.QComboBox(Form)
		self.comboBox_name.setGeometry(QtCore.QRect(20, 70, 121, 22))
		self.comboBox_name.setObjectName("comboBox_name")
		# add
		# self.comboBox_name.currentIndexChanged(0)
		# addend
		self.comboBox_name.addItem("")
		self.comboBox_name.addItem("")
		self.comboBox_name.addItem("")
		# 前缀连接符号
		self.comboBox_hyphen1 = QtWidgets.QComboBox(Form)
		self.comboBox_hyphen1.setGeometry(QtCore.QRect(150, 70, 71, 22))
		self.comboBox_hyphen1.setObjectName("comboBox_hyphen1")
		self.comboBox_hyphen1.addItem("")
		self.comboBox_hyphen1.addItem("")
		self.comboBox_hyphen1.addItem("")
		self.comboBox_hyphen1.addItem("")
		# 中缀拍摄日期时间
		self.comboBox_datetime = QtWidgets.QComboBox(Form)
		self.comboBox_datetime.setGeometry(QtCore.QRect(230, 70, 121, 22))
		self.comboBox_datetime.setObjectName("comboBox_datetime")
		self.comboBox_datetime.addItem("")
		self.comboBox_datetime.addItem("")
		self.comboBox_datetime.addItem("")
		# 后缀连接符
		self.comboBox_hyphen2 = QtWidgets.QComboBox(Form)
		self.comboBox_hyphen2.setGeometry(QtCore.QRect(360, 70, 61, 22))
		self.comboBox_hyphen2.setObjectName("comboBox_hyphen2")
		self.comboBox_hyphen2.addItem("")
		self.comboBox_hyphen2.addItem("")
		self.comboBox_hyphen2.addItem("")
		self.comboBox_hyphen2.addItem("")
		# 后缀文件名
		self.comboBox_name2 = QtWidgets.QComboBox(Form)
		self.comboBox_name2.setGeometry(QtCore.QRect(430, 70, 121, 22))
		self.comboBox_name2.setObjectName("comboBox_name2")
		self.comboBox_name2.addItem("")
		self.comboBox_name2.addItem("")
		self.comboBox_name2.addItem("")
		# 确定
		self.pushButton_ok = QtWidgets.QPushButton(Form)
		self.pushButton_ok.setGeometry(QtCore.QRect(220, 280, 75, 23))
		self.pushButton_ok.setObjectName("pushButton_ok")
		# 取消
		self.pushButton_cancel = QtWidgets.QPushButton(Form)
		self.pushButton_cancel.setGeometry(QtCore.QRect(300, 280, 75, 23))
		self.pushButton_cancel.setObjectName("pushButton_cancel")
		# 前缀新文件名层
		self.stackedWidget_newName = QtWidgets.QStackedWidget(Form)
		self.stackedWidget_newName.setGeometry(QtCore.QRect(20, 100, 151, 21))
		self.stackedWidget_newName.setObjectName("stackedWidget_newName")
		self.page = QtWidgets.QWidget()
		self.page.setObjectName("page")
		self.stackedWidget_newName.addWidget(self.page)
		self.page_1 = QtWidgets.QWidget()
		self.page_1.setObjectName("page_1")
		self.lineEdit_newName = QtWidgets.QLineEdit(self.page_1)
		self.lineEdit_newName.setGeometry(QtCore.QRect(0, 0, 121, 20))
		self.lineEdit_newName.setObjectName("lineEdit_newName")
		self.stackedWidget_newName.addWidget(self.page_1)
		# 后缀新文件名层
		self.stackedWidget_newName2 = QtWidgets.QStackedWidget(Form)
		self.stackedWidget_newName2.setGeometry(QtCore.QRect(420, 100, 161, 21))
		self.stackedWidget_newName2.setObjectName("stackedWidget_newName2")
		self.page_2 = QtWidgets.QWidget()
		self.page_2.setObjectName("page_2")
		self.stackedWidget_newName2.addWidget(self.page_2)
		self.page_3 = QtWidgets.QWidget()
		self.page_3.setObjectName("page_3")
		self.lineEdit_newName2 = QtWidgets.QLineEdit(self.page_3)
		self.lineEdit_newName2.setGeometry(QtCore.QRect(10, 0, 121, 20))
		self.lineEdit_newName2.setObjectName("lineEdit_newName2")
		self.stackedWidget_newName2.addWidget(self.page_3)
		self.label = QtWidgets.QLabel(Form)
		self.label.setGeometry(QtCore.QRect(270, 100, 31, 31))
		font = QtGui.QFont()
		font.setFamily("微软雅黑")
		font.setPointSize(18)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.groupBox = QtWidgets.QGroupBox(Form)
		self.groupBox.setGeometry(QtCore.QRect(20, 140, 531, 131))
		self.groupBox.setTitle("")
		self.groupBox.setObjectName("groupBox")

		# 序号
		self.stackedWidget = QtWidgets.QStackedWidget(Form)
		self.stackedWidget.setGeometry(QtCore.QRect(26, 146, 521, 121))
		self.stackedWidget.setObjectName("stackedWidget")
		self.page_sn = QtWidgets.QWidget()
		self.page_sn.setObjectName("page_sn")
		self.label_sn = QtWidgets.QLabel(self.page_sn)
		self.label_sn.setGeometry(QtCore.QRect(220, 10, 54, 12))
		self.label_sn.setObjectName("label_sn")
		self.lineEdit_sn = QtWidgets.QLineEdit(self.page_sn)
		self.lineEdit_sn.setGeometry(QtCore.QRect(220, 30, 113, 20))
		self.lineEdit_sn.setObjectName("lineEdit_sn")
		self.label_snLength = QtWidgets.QLabel(self.page_sn)
		self.label_snLength.setGeometry(QtCore.QRect(220, 60, 81, 20))
		self.label_snLength.setObjectName("label_snLength")
		self.horizontalSlider_sn = QtWidgets.QSlider(self.page_sn)
		self.horizontalSlider_sn.setGeometry(QtCore.QRect(220, 90, 111, 19))
		self.horizontalSlider_sn.setOrientation(QtCore.Qt.Horizontal)
		self.horizontalSlider_sn.setObjectName("horizontalSlider_sn")
		# add 滑条序号使用位数
		self.horizontalSlider_sn.setMinimum(1)
		self.horizontalSlider_sn.setMaximum(10)
		self.horizontalSlider_sn.valueChanged.connect(self.changeSnValue)
		# add_end

		# 按日期时间
		self.stackedWidget.addWidget(self.page_sn)
		self.page_datetime = QtWidgets.QWidget()
		self.page_datetime.setObjectName("page_datetime")
		self.comboBox_10 = QtWidgets.QComboBox(self.page_datetime)
		self.comboBox_10.setGeometry(QtCore.QRect(210, 50, 81, 22))
		self.comboBox_10.setObjectName("comboBox_10")
		self.comboBox_10.addItem("")
		self.comboBox_10.addItem("")
		self.comboBox_10.addItem("")
		self.comboBox_10.addItem("")
		self.label_14 = QtWidgets.QLabel(self.page_datetime)
		self.label_14.setGeometry(QtCore.QRect(140, 40, 41, 31))
		font = QtGui.QFont()
		font.setFamily("微软雅黑")
		font.setPointSize(26)
		self.label_14.setFont(font)
		self.label_14.setObjectName("label_14")
		self.label_15 = QtWidgets.QLabel(self.page_datetime)
		self.label_15.setGeometry(QtCore.QRect(310, 40, 41, 31))
		font = QtGui.QFont()
		font.setFamily("微软雅黑")
		font.setPointSize(26)

		self.label_15.setFont(font)
		self.label_15.setObjectName("label_15")
		#日期
		self.radioButton_yyyymmdd_1 = QtWidgets.QRadioButton(self.page_datetime)
		self.radioButton_yyyymmdd_1.setGeometry(QtCore.QRect(30, 10, 89, 16))
		self.radioButton_yyyymmdd_1.setObjectName("radioButton_yyyymmdd_1")
		self.radioButton_mmddyy_1 = QtWidgets.QRadioButton(self.page_datetime)
		self.radioButton_mmddyy_1.setGeometry(QtCore.QRect(30, 70, 89, 16))
		self.radioButton_mmddyy_1.setObjectName("radioButton_mmddyy_1")
		self.radioButton_mmddyyyy_1 = QtWidgets.QRadioButton(self.page_datetime)
		self.radioButton_mmddyyyy_1.setGeometry(QtCore.QRect(30, 50, 89, 16))
		self.radioButton_mmddyyyy_1.setObjectName("radioButton_mmddyyyy_1")
		self.radioButton_yymmdd_1 = QtWidgets.QRadioButton(self.page_datetime)
		self.radioButton_yymmdd_1.setGeometry(QtCore.QRect(30, 30, 89, 16))
		self.radioButton_yymmdd_1.setObjectName("radioButton_yymmdd_1")
		self.radioButton_mmdd_1 = QtWidgets.QRadioButton(self.page_datetime)
		self.radioButton_mmdd_1.setGeometry(QtCore.QRect(30, 90, 89, 16))
		self.radioButton_mmdd_1.setObjectName("radioButton_mmdd_1")
        #时间,加入另一个redioButtonGroup 分组
		self.radioButton_hhmm_1 = QtWidgets.QRadioButton(self.page_datetime)
		self.radioButton_hhmm_1.setGeometry(QtCore.QRect(390, 60, 89, 16))
		self.radioButton_hhmm_1.setObjectName("radioButton_hhmm_1")
		self.radioButton_hhmmss_1 = QtWidgets.QRadioButton(self.page_datetime)
		self.radioButton_hhmmss_1.setGeometry(QtCore.QRect(390, 30, 89, 16))
		self.radioButton_hhmmss_1.setObjectName("radioButton_hhmmss_1")
		self.buttonGroup = QtWidgets.QButtonGroup(Form)
		self.buttonGroup.setObjectName("buttonGroup")
		self.buttonGroup.addButton(self.radioButton_hhmm_1)
		self.buttonGroup.addButton(self.radioButton_hhmmss_1)

		self.stackedWidget.addWidget(self.page_datetime)
		self.page_date = QtWidgets.QWidget()
		self.page_date.setObjectName("page_date")

		# 按日期+序号
		self.radioButton_yyyymmdd_2 = QtWidgets.QRadioButton(self.page_date)
		self.radioButton_yyyymmdd_2.setGeometry(QtCore.QRect(30, 10, 89, 16))
		self.radioButton_yyyymmdd_2.setObjectName("radioButton_yyyymmdd_2")
		self.radioButton_yymmdd_2 = QtWidgets.QRadioButton(self.page_date)
		self.radioButton_yymmdd_2.setGeometry(QtCore.QRect(30, 30, 89, 16))
		self.radioButton_yymmdd_2.setObjectName("radioButton_yymmdd_2")
		self.radioButton_mmddyyyy_2 = QtWidgets.QRadioButton(self.page_date)
		self.radioButton_mmddyyyy_2.setGeometry(QtCore.QRect(30, 50, 89, 16))
		self.radioButton_mmddyyyy_2.setObjectName("radioButton_mmddyyyy_2")
		self.radioButton_mmddyy_2 = QtWidgets.QRadioButton(self.page_date)
		self.radioButton_mmddyy_2.setGeometry(QtCore.QRect(30, 70, 89, 16))
		self.radioButton_mmddyy_2.setObjectName("radioButton_mmddyy_2")
		self.radioButton_mmdd_2 = QtWidgets.QRadioButton(self.page_date)
		self.radioButton_mmdd_2.setGeometry(QtCore.QRect(30, 90, 89, 16))
		self.radioButton_mmdd_2.setObjectName("radioButton_mmdd_2")
		self.label_10 = QtWidgets.QLabel(self.page_date)
		self.label_10.setGeometry(QtCore.QRect(140, 40, 41, 31))
		font = QtGui.QFont()
		font.setFamily("微软雅黑")
		font.setPointSize(26)
		self.label_10.setFont(font)
		self.label_10.setObjectName("label_10")
		self.comboBox_8 = QtWidgets.QComboBox(self.page_date)
		self.comboBox_8.setGeometry(QtCore.QRect(210, 50, 81, 22))
		self.comboBox_8.setObjectName("comboBox_8")
		self.comboBox_8.addItem("")
		self.comboBox_8.addItem("")
		self.comboBox_8.addItem("")
		self.comboBox_8.addItem("")
		self.label_11 = QtWidgets.QLabel(self.page_date)
		self.label_11.setGeometry(QtCore.QRect(310, 40, 41, 31))
		font = QtGui.QFont()
		font.setFamily("微软雅黑")
		font.setPointSize(26)
		self.label_11.setFont(font)
		self.label_11.setObjectName("label_11")
		self.label_sn_2 = QtWidgets.QLabel(self.page_date)
		self.label_sn_2.setGeometry(QtCore.QRect(360, 10, 54, 12))
		self.label_sn_2.setObjectName("label_sn_2")

		self.lineEdit_sn2 = QtWidgets.QLineEdit(self.page_date)
		self.lineEdit_sn2.setGeometry(QtCore.QRect(360, 30, 113, 20))
		self.lineEdit_sn2.setObjectName("lineEdit_sn2")

		self.label_snLength_2 = QtWidgets.QLabel(self.page_date)
		self.label_snLength_2.setGeometry(QtCore.QRect(360, 60, 81, 20))
		self.label_snLength_2.setObjectName("label_snLength_2")

		# 按拍摄日期
		self.horizontalSlider_date = QtWidgets.QSlider(self.page_date)
		self.horizontalSlider_date.setGeometry(QtCore.QRect(360, 90, 111, 19))
		self.horizontalSlider_date.setOrientation(QtCore.Qt.Horizontal)
		self.horizontalSlider_date.setObjectName("horizontalSlider_date")
		# add 滑条序号使用位数
		self.horizontalSlider_date.setMinimum(1)
		self.horizontalSlider_date.setMaximum(10)
		self.horizontalSlider_date.valueChanged.connect(self.changeDateSnValue)
		# add_end

		self.stackedWidget.addWidget(self.page_date)

		self.label_2 = QtWidgets.QLabel(self.page_sn)
		self.label_2.setGeometry(QtCore.QRect(340, 90, 54, 12))
		self.label_2.setObjectName("label_2")

		self.label_3 = QtWidgets.QLabel(self.page_date)
		self.label_3.setGeometry(QtCore.QRect(480, 90, 31, 16))
		self.label_3.setObjectName("label_3")

		self.retranslateUi(Form)
		self.stackedWidget_newName.setCurrentIndex(0)  # 默认值
		self.stackedWidget_newName2.setCurrentIndex(0)  # 默认值
		self.stackedWidget.setCurrentIndex(2)  # 默认值
		self.horizontalSlider_sn.setValue(4)  # 滑条，默认4位
		self.horizontalSlider_date.setValue(4)  # 滑条，默认4位

		QtCore.QMetaObject.connectSlotsByName(Form)

		# add
		self.comboBox_name.currentIndexChanged[str].connect(self.setWidgetStack_newname)  # 开头文件名
		self.comboBox_name2.currentIndexChanged[str].connect(self.setWidgetStack_newname2)  # 文件名结束
		self.comboBox_datetime.currentIndexChanged[str].connect(self.setWidgetStack_datetime)  # 按日期时间序号

		self.comboBox_hyphen1.activated[str].connect(self.changeHyphen1)
		self.comboBox_hyphen2.activated[str].connect(self.changeHyphen2)
		# self.comboBox_datetime.activated[str].connect(self.changeDateTime)

		# add end

		self.newname1 = ''
		self.hyphen1 = ''
		self.datetimesn = ''
		self.hyphen2 = ''
		self.newname2 = ''

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		self.label_example.setText(_translate("Form", "示例:"))
		self.comboBox_hyphen1.setItemText(0, _translate("Form", "下划线"))
		self.comboBox_hyphen1.setItemText(1, _translate("Form", "连字符"))
		self.comboBox_hyphen1.setItemText(2, _translate("Form", "空格"))
		self.comboBox_hyphen1.setItemText(3, _translate("Form", "无"))

		self.comboBox_datetime.setItemText(0, _translate("Form", "拍摄日期"))
		self.comboBox_datetime.setItemText(1, _translate("Form", "拍摄日期时间"))
		self.comboBox_datetime.setItemText(2, _translate("Form", "序号"))

		self.comboBox_hyphen2.setItemText(0, _translate("Form", "下划线"))
		self.comboBox_hyphen2.setItemText(1, _translate("Form", "连字符"))
		self.comboBox_hyphen2.setItemText(2, _translate("Form", "空格"))
		self.comboBox_hyphen2.setItemText(3, _translate("Form", "无"))

		self.comboBox_name.setItemText(0, _translate("Form", "原名称"))
		self.comboBox_name.setItemText(1, _translate("Form", "新名称"))
		self.comboBox_name.setItemText(2, _translate("Form", "无"))

		self.comboBox_name2.setItemText(0, _translate("Form", "原名称"))
		self.comboBox_name2.setItemText(1, _translate("Form", "新名称"))
		self.comboBox_name2.setItemText(2, _translate("Form", "无"))
		self.pushButton_ok.setText(_translate("Form", "确定"))
		self.pushButton_cancel.setText(_translate("Form", "取消"))

		self.label.setText(_translate("Form", "┆"))
		self.label_sn.setText(_translate("Form", "序号"))
		self.label_snLength.setText(_translate("Form", "序号码长度"))
		self.comboBox_10.setItemText(0, _translate("Form", "下划线"))
		self.comboBox_10.setItemText(1, _translate("Form", "连字符"))
		self.comboBox_10.setItemText(2, _translate("Form", "空格"))
		self.comboBox_10.setItemText(3, _translate("Form", "无"))
		self.label_14.setText(_translate("Form", "+"))
		self.label_15.setText(_translate("Form", "+"))
		self.radioButton_yyyymmdd_1.setText(_translate("Form", "yyyymmdd"))
		self.radioButton_mmddyy_1.setText(_translate("Form", "mmddyy"))
		self.radioButton_hhmm_1.setText(_translate("Form", "hhmm*"))
		self.radioButton_hhmmss_1.setText(_translate("Form", "hhmmss*"))
		self.radioButton_mmddyyyy_1.setText(_translate("Form", "mmddyyyy"))
		self.radioButton_yymmdd_1.setText(_translate("Form", "yymmdd"))
		self.radioButton_mmdd_1.setText(_translate("Form", "mmdd"))
		self.radioButton_yyyymmdd_2.setText(_translate("Form", "yyyymmdd"))
		self.radioButton_yymmdd_2.setText(_translate("Form", "yymmdd"))
		self.radioButton_mmddyyyy_2.setText(_translate("Form", "mmddyyyy"))
		self.radioButton_mmddyy_2.setText(_translate("Form", "mmddyy"))
		self.radioButton_mmdd_2.setText(_translate("Form", "mmdd"))
		self.label_10.setText(_translate("Form", "+"))
		self.comboBox_8.setItemText(0, _translate("Form", "下划线"))
		self.comboBox_8.setItemText(1, _translate("Form", "连字符"))
		self.comboBox_8.setItemText(2, _translate("Form", "空格"))
		self.comboBox_8.setItemText(3, _translate("Form", "无"))
		self.label_11.setText(_translate("Form", "+"))
		self.label_sn_2.setText(_translate("Form", "序号"))
		self.label_snLength_2.setText(_translate("Form", "序号码长度"))

		self.label_2.setText(_translate("Form", ""))
		self.label_3.setText(_translate("Form", ""))

	def operate(self):
		"""自动刷新示例"""
		# 前缀名称
		if self.comboBox_name.currentText() == "新名称":
			self.newname1 = self.lineEdit_newName.text()  # 将新文件名提交到示例
		elif self.comboBox_name.currentText() == "原名称":
			self.newname1 = '<原名称>'
		else:
			self.newname1 = ''
		# 后缀名称
		if self.comboBox_name2.currentText() == "新名称":
			self.newname2 = self.lineEdit_newName2.text()  # 将新文件名提交到示例
		elif self.comboBox_name2.currentText() == "原名称":
			self.newname2 = '<原名称>'
		else:
			self.newname2 = ''

			# 前缀连接符
		if self.comboBox_hyphen1.currentText() == '下划线':
			self.hyphen1 = "_"
		elif self.comboBox_hyphen1.currentText() == '连字符':
			self.hyphen1 = "-"
		elif self.comboBox_hyphen1.currentText() == '空格':
			self.hyphen1 = ' '
		else:
			self.hyphen1 = ''

		# 后缀连接符
		if self.comboBox_hyphen2.currentText() == '下划线':
			self.hyphen2 = "_"
		elif self.comboBox_hyphen2.currentText() == '连字符':
			self.hyphen2 = "-"
		elif self.comboBox_hyphen2.currentText() == '空格':
			self.hyphen2 = ' '
		else:
			self.hyphen2 = ''

		#中缀
		if self.comboBox_datetime.currentText() == "拍摄日期":
			if self.radioButton_yyyymmdd_2.isChecked() == True:
				self.datetimesn1 = '20171130'
			elif self.radioButton_yymmdd_2.isChecked() == True:
				self.datetimesn1 = '171130'
			elif self.radioButton_mmddyyyy_2.isChecked() == True:
				self.datetimesn1 = '11302017'
			elif self.radioButton_mmddyy_2.isChecked() == True:
				self.datetimesn1 = '113017'
			elif self.radioButton_mmdd_2.isChecked() == True:
				self.datetimesn1 = '1130'
			else:
				self.datetimesn1 = ''

			if self.comboBox_8.currentText() == '下划线':
				self.datetimesn2 = '_'
			elif self.comboBox_8.currentText() == '连字符':
				self.datetimesn2 = '-'
			elif self.comboBox_8.currentText() == '空格':
				self.datetimesn2 = ' '
			else:
				self.datetimesn2 = ''

			#整合按 "拍摄日期+序列号"
			self.datetimesn = self.datetimesn1 + self.datetimesn2 + self.lineEdit_sn2.text()

		elif self.comboBox_datetime.currentText() == "拍摄日期时间":
			if self.radioButton_yyyymmdd_1.isChecked() == True:
				self.datetimesn1 = '20171130'
			elif self.radioButton_yymmdd_1.isChecked() == True:
				self.datetimesn1 = '171130'
			elif self.radioButton_mmddyyyy_1.isChecked() == True:
				self.datetimesn1 = '11302017'
			elif self.radioButton_mmddyy_1.isChecked() == True:
				self.datetimesn1 = '113017'
			elif self.radioButton_mmdd_1.isChecked() == True:
				self.datetimesn1 = '1130'
			else:
				self.datetimesn1 = ''

			if self.comboBox_10.currentText() == '下划线':
				self.datetimesn2 = '_'
			elif self.comboBox_10.currentText() == '连字符':
				self.datetimesn2 = '-'
			elif self.comboBox_10.currentText() == '空格':
				self.datetimesn2 = ' '
			else:
				self.datetimesn2 = ''

			if self.radioButton_hhmmss_1.isChecked() == True:
				self.datetimesn3 = '150922'
			elif self.radioButton_hhmm_1.isChecked() == True:
				self.datetimesn3 = '1509'
			else:
				self.datetimesn3 = ''

			# 整合按 "拍摄日期+日期时间"
			self.datetimesn = self.datetimesn1 + self.datetimesn2 + self.datetimesn3

		else:
			self.datetimesn = self.mysnvalue  # 将中缀的序号提交到示例

		# 刷新示例
		self.label_example.setText('示例：' + self.newname1 + self.hyphen1 + self.datetimesn + self.hyphen2 + self.newname2 + '.JPG')

	def setWidgetStack_newname(self, text):
		"""文件名前缀,当选择新名称时显示输入框"""
		if text == "新名称":
			self.stackedWidget_newName.setCurrentIndex(1)
		elif text == "原名称":
			self.stackedWidget_newName.setCurrentIndex(0)
		else:
			self.stackedWidget_newName.setCurrentIndex(0)

	def setWidgetStack_newname2(self, text):
		"""文件名作后缀，当选择新名称时显示输入框"""
		if text == "新名称":
			self.stackedWidget_newName2.setCurrentIndex(1)
		elif text == "原名称":
			self.stackedWidget_newName2.setCurrentIndex(0)
		else:
			self.stackedWidget_newName2.setCurrentIndex(0)

	def setWidgetStack_datetime(self, text):
		"""中缀，按选择变更不同的子页面"""
		if text == "拍摄日期":
			self.stackedWidget.setCurrentIndex(2)
		if text == "拍摄日期时间":
			self.stackedWidget.setCurrentIndex(1)
		if text == "序号":
			self.stackedWidget.setCurrentIndex(0)
			self.datetimesn = self.mysnvalue

	def changeDateSnValue(self, value):
		"""中缀中拍摄日期滑条"""
		print(value)
		self.datesnvalue = str(0) * value
		self.label_3.setText(str(value))
		self.lineEdit_sn2.setText(str(self.datesnvalue))

	def changeSnValue(self, value):
		"""中缀中序号滑条"""
		print(value)
		self.mysnvalue = str(0) * value
		self.label_2.setText(str(value))
		self.lineEdit_sn.setText(str(self.mysnvalue))


	def changeHyphen1(self, text):
		"""前缀连接符"""
		# print(text)
		pass

	def changeHyphen2(self, text):
		"""后缀连接符"""
		# print(text)
		pass


if __name__ == "__main__":
	import sys

	app = QtWidgets.QApplication(sys.argv)
	Form = QtWidgets.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())
