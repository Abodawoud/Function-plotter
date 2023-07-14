from PySide2.QtWidgets import QPushButton
"""Class MyPushButton"""


class MyPushButton(QPushButton):
    """Customized button from QPushButton"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        font = self.font()
        font.setPointSize(10)
        self.setFont(font)
        self.setStyleSheet("display: flex; height: 30px;")
