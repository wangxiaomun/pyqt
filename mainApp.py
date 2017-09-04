import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QProxyStyle
from PyQt5.QtGui import QIcon

class mainUI(QWidget):
    def __init__(self):
        super(mainUI, self).__init__()
        self.leftlist = QVBoxLayout()
        self.leftlist.addSpacing(20)

        self.rigthlist = QVBoxLayout()
        self.rigthlist.addSpacing(20)

        self.leftlist.addWidget(QPushButton("one"))
        self.leftlist.addWidget(QPushButton("three"))
        self.leftlist.addWidget(QPushButton("five"))
        self.leftlist.addWidget(QPushButton("seven"))

        self.rigthlist.addWidget(QPushButton("two"))
        self.rigthlist.addWidget(QPushButton("four"))
        self.rigthlist.addWidget(QPushButton("six"))
        self.rigthlist.addWidget(QPushButton("eight"))

        hbox = QHBoxLayout()
        hbox.addLayout(self.leftlist)
        hbox.addLayout(self.rigthlist)


        self.setLayout(hbox)
        self.setGeometry(300, 300, 800, 480)
        self.setStyleSheet("""
                .QPushButton {
                    background:  rgb(66, 184, 221); /* #4CAF50;  Green */
                    color: white;
                    padding: 20px 40px;
                    font-size: 24px;
                    max-width: 100px;
                    max-height: 30px;
                    border-radius: 4px;
                    }
                QPushButton:pressed{
                    border: 4px solid black;
                    background: grey
                    }

                """)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myStyle = QProxyStyle('Fusion')
    app.setStyle(myStyle)
    ex = mainUI()
    sys.exit(app.exec_())
