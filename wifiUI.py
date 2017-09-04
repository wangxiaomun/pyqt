import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QProxyStyle

class wifiUI(QWidget):
    def __init__(self):
        super(wifiUI, self).__init__()
        self.leftlist = QVBoxLayout()
        self.leftlist.addSpacing(20)

        self.rigthlist = QVBoxLayout()
        self.rigthlist.addSpacing(20)

        self.backbutton = QPushButton("Back")
        self.leftlist.addWidget(self.backbutton)
        self.rigthlist.addWidget(QPushButton("two"))
        self.backbutton.clicked.connect(lambda: self.clickHandler())
        hbox = QHBoxLayout()
        hbox.addLayout(self.leftlist)
        hbox.addLayout(self.rigthlist)

        self.setLayout(hbox)
        self.setGeometry(300, 300, 800, 480)
        self.setCSS()

    def setQWidget(self,widget):
        self.widget = widget

    def clickHandler(self):
        self.hide()
        self.widget.show()

    def setCSS(self):
        self.setStyleSheet("""
            .QPushButton{
                background:  rgb(66, 184, 221); /* #4CAF50;  Green */
                color: white;
                padding: 20px 40px;
                font-size: 24px;
                max-width: 100px;
                max-height: 30px;
                border-radius: 4px;
                }
            .QPushButton:pressed {
                border: 4px solid black;
                background: grey
                }
            """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myStyle = QProxyStyle('Fusion')
    app.setStyle(myStyle)
    ex = wifiUI()
    sys.exit(app.exec_())
