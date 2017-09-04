import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QProxyStyle
from PyQt5.QtGui import QIcon

class WiFiController(QPushButton):
    def __init__(self):
        super(WiFiController, self).__init__()
        self.setText("Wi-Fi")
        self.clicked.connect(lambda: self.clickHandler())
        self.stack = QWidget()

    def clickHandler(self):
        hbox = QHBoxLayout()
        hbox.addWidget(QPushButton("nine"))
        hbox.addWidget(QPushButton("ten"))
        self.stack.setLayout(hbox)