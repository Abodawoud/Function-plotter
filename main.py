import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import (QPalette, QColor, QIcon)
from container.layout import MainLayout
"""Create the MainWindow Class"""


class MainWindow(QMainWindow):
    """Class that inherits from the QMainWindow to get all Features"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Function Plotter")
        self.setGeometry(600, 100, 1000, 900)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#2c2c2c"))
        self.setPalette(palette)

        appIcon = QIcon("math.png")
        self.setWindowIcon(appIcon)

        layout = MainLayout()
        self.setCentralWidget(layout)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
