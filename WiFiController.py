import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QProxyStyle
from PyQt5.QtGui import QIcon
from wifiUI import wifiUI

class WiFiController(QPushButton):
    def __init__(self):
        super(WiFiController, self).__init__()
        self.setText("Wi-Fi")
        self.clicked.connect(lambda: self.clickHandler())
        self.wifiUI = wifiUI()


    def setQWidget(self,widget):
        self.widget = widget
        self.wifiUI.setQWidget(widget)

    def clickHandler(self):
        self.widget.hide()
        self.wifiUI.show()