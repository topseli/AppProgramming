# -*- coding: utf-8 -*-
""" login_view.py - presenter for the login prompt"""
__author__ = "topseli"
__license__ = "0BSD"


import os
import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QMessageBox


class AddProductView(QtWidgets.QWidget):

    create_product_button_signal = pyqtSignal(dict)

    def __init__(self):
        super(AddProductView, self).__init__()
        self.init_ui()

    def init_ui(self):
        path = os.path.dirname(os.path.abspath(__file__)) + '/add_product_view.ui'
        uic.loadUi(path, self)

    def show_warning(self, e):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("The server is not responding")
        msg.setWindowTitle("Connection error")
        msg.setDetailedText(str(e))
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    @pyqtSlot()
    def on_create_product_button_clicked(self):
        product_info = {
            "product_name": self.product_name_input.text(),
            "description": self.description_input.text(),
            "stock": int(self.ammount_input.text()),
            "price": float(self.price_input.text()),
            "size": int(self.size_input.text()),
        }
        self.create_product_button_signal.emit(product_info)


def run():
    APP = QtWidgets.QApplication(sys.argv)
    APP_WINDOW = AddProductView()
    APP_WINDOW.back_button.clicked.connect(sys.exit)
    APP_WINDOW.show()
    APP.exec_()


if __name__ == '__main__':
    run()
