from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog3(object):
    def setupUi3(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 296)
        self.dialogButtonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.dialogButtonBox.setGeometry(QtCore.QRect(190, 240, 181, 32))
        self.dialogButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.dialogButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dialogButtonBox.setObjectName("dialogButtonBox")
        self.author = QtWidgets.QLabel(Dialog)
        self.author.setGeometry(QtCore.QRect(40, 20, 191, 17))
        self.author.setObjectName("author")
        self.email = QtWidgets.QLabel(Dialog)
        self.email.setGeometry(QtCore.QRect(40, 50, 271, 17))
        self.email.setObjectName("email")
        self.github = QtWidgets.QLabel(Dialog)
        self.github.setGeometry(QtCore.QRect(40, 80, 351, 17))
        self.github.setObjectName("github")
        self.GPL = QtWidgets.QLabel(Dialog)
        self.GPL.setGeometry(QtCore.QRect(40, 110, 161, 17))
        self.GPL.setObjectName("GPL")

        self.retranslateUi(Dialog)
        self.dialogButtonBox.accepted.connect(Dialog.accept)
        self.dialogButtonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.author.setText(_translate("Dialog", "作者：陈严肃"))
        self.email.setText(_translate("Dialog", "联系邮箱：aschenyansu@foxmail.com"))
        self.github.setText(_translate("Dialog", "github: https://github.com/chenyansu/pyspidergui"))
        self.GPL.setText(_translate("Dialog", "本软件遵循GPL v2协议"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog3 = QtWidgets.QDialog()
    ui3 = Ui_Dialog()
    ui3.setupUi(Dialog3)
    Dialog3.show()
    sys.exit(app.exec_())