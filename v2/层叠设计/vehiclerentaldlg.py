# -*- coding: utf-8 -*-

"""
Module implementing VehicleRentalDlg.
"""
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog,QApplication

from Ui_vehiclerentaldlg import Ui_VehicleRentalDlg


class VehicleRentalDlg(QDialog, Ui_VehicleRentalDlg):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(VehicleRentalDlg, self).__init__(parent)
        self.setupUi(self)
        self.vehicleComboBox.setFocus()

    @pyqtSlot(int)
    def on_weightSpinBox_valueChanged(self, amount):
        self.mileageLabel.setText("{0} miles".format(8000 / amount))


    @pyqtSlot(str)
    def on_vehicleComboBox_currentIndexChanged(self, text):
        if text == "Car":
            self.mileageLabel.setText("1000 miles")
        else:
            self.on_weightSpinBox_valueChanged(
                    self.weightSpinBox.value())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = VehicleRentalDlg()
    form.show()
    app.exec_()