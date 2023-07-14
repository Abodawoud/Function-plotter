from PySide2.QtWidgets import QLabel
"""Class MyLabel"""


class MyLabel(QLabel):
    """Customized label from QLabel"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        font = self.font()
        font.setPointSize(10)
        self.setFont(font)
        self.setStyleSheet("color: white; font-weight: bold; font-family: Arial;")
