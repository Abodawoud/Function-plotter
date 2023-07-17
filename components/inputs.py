from PySide2.QtWidgets import QLineEdit


class MyLineEdit(QLineEdit):
    """Customized linedit from QLineEdit"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        font = self.font()
        font.setPointSize(10)
        self.setFont(font)
        self.setStyleSheet("padding: 4px; border-radius: 5px;")
