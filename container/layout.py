from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from components.btns import MyPushButton
from components.inputs import MyLineEdit
from components.labels import MyLabel

"""Create the MainLayout Class"""


class MainLayout(QWidget):
    """Class that inherits from the QWidget to get all Features(Btns, Layouts,
    Line-edits, Inputdialog)"""

    def __init__(self):
        super().__init__()

        layout1 = QVBoxLayout()
        layout_f = QHBoxLayout()
        layout_x = QHBoxLayout()
        layout_btn = QHBoxLayout()

        self.label_1 = MyLabel("F(X)")
        self.input_1_f_of_x = MyLineEdit()
        self.label_2 = MyLabel("Xmin.")
        self.input_2_x_min = MyLineEdit()
        self.label_3 = MyLabel("Xmax.")
        self.input_3_x_max = MyLineEdit()

        self.btn = QPushButton("Plot")
        font = self.btn.font()
        font.setPointSize(10)
        self.btn.setFont(font)
        self.btn.setFixedHeight(35)

        self.x_label = MyPushButton("X label")
        self.y_label = MyPushButton("Y label")
        self.graph_title = MyPushButton("Change graph Title")
        self.grid_toggle = MyPushButton("Show Grid_line")
        self.legend_toggle = MyPushButton("Show Legend")
        self.btn_clear = MyPushButton("Clear")

        layout_f.addWidget(self.label_1)
        layout_f.addWidget(self.input_1_f_of_x)

        layout1.addLayout(layout_f)

        layout_x.addWidget(self.label_2)
        layout_x.addWidget(self.input_2_x_min)
        layout_x.addWidget(self.label_3)
        layout_x.addWidget(self.input_3_x_max)

        layout1.addLayout(layout_x)

        layout1.addWidget(self.btn)
        layout_btn.addWidget(self.x_label)
        layout_btn.addWidget(self.y_label)
        layout_btn.addWidget(self.graph_title)
        layout_btn.addWidget(self.grid_toggle)
        layout_btn.addWidget(self.legend_toggle)
        layout_btn.addWidget(self.btn_clear)

        layout1.addLayout(layout_btn)

        layout1.setSpacing(10)
        self.setLayout(layout1)
        layout1.setContentsMargins(10, 10, 10, 10)
