import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_main_Window import Ui_ChenSpider
from Ui_mysqllogin import Ui_Dialog
from Ui_about import Ui_Dialog3

# part 1
# 实例化启动qt应用
app=QtWidgets.QApplication(sys.argv)
# 将chenSpider设为主窗口实例
ChenSpider=QtWidgets.QMainWindow()
# 　取得UI class 的实例
ui=Ui_ChenSpider()
# 将UI 应用到　主窗口 chenSpider　上　
ui.setupUi(ChenSpider)
# part 2　登录mysql
Dialog=QtWidgets.QDialog()
ui2=Ui_Dialog()
ui2.setupUi2(Dialog)
# part 3 关于界面
Dialog3=QtWidgets.QDialog()
ui3=Ui_Dialog3()
ui3.setupUi3(Dialog3)

# part 4
# 设计信号-槽点
# 建立对象实例化的访问
bttn=ui.loginmysqlbttn
bttn.clicked.connect(Dialog.show)

bttn2=ui.aboutbttn
bttn2.clicked.connect(Dialog3.show)

if __name__ == "__main__":
    # 展示主窗口　chenSpider
    ChenSpider.show()
    sys.exit(app.exec_())​