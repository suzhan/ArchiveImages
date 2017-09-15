from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi2(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 297)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(260, 240, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.hostlnedt = QtWidgets.QLineEdit(Dialog)
        self.hostlnedt.setGeometry(QtCore.QRect(120, 20, 113, 27))
        self.hostlnedt.setObjectName("hostlnedt")
        self.hostlbl = QtWidgets.QLabel(Dialog)
        self.hostlbl.setGeometry(QtCore.QRect(20, 26, 81, 21))
        self.hostlbl.setObjectName("hostlbl")
        self.usernamelbl = QtWidgets.QLabel(Dialog)
        self.usernamelbl.setGeometry(QtCore.QRect(20, 90, 51, 17))
        self.usernamelbl.setObjectName("usernamelbl")
        self.userlnedt = QtWidgets.QLineEdit(Dialog)
        self.userlnedt.setGeometry(QtCore.QRect(120, 80, 113, 27))
        self.userlnedt.setObjectName("userlnedt")
        self.passwdlbl = QtWidgets.QLabel(Dialog)
        self.passwdlbl.setGeometry(QtCore.QRect(20, 140, 81, 20))
        self.passwdlbl.setObjectName("passwdlbl")
        self.passwdlnedit = QtWidgets.QLineEdit(Dialog)
        self.passwdlnedit.setGeometry(QtCore.QRect(120, 130, 113, 27))
        self.passwdlnedit.setObjectName("passwdlnedit")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "登陆mysql"))
        self.hostlnedt.setText(_translate("Dialog", "localhost"))
        self.hostlbl.setText(_translate("Dialog", "HOST地址"))
        self.usernamelbl.setText(_translate("Dialog", "用户名"))
        self.passwdlbl.setText(_translate("Dialog", "数据库密码"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi2(Dialog)
    Dialog.show()
    sys.exit(app.exec_())