from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QMessageBox
from components.btns import MyPushButton
from components.inputs import MyLineEdit
from components.labels import MyLabel
from components.helper_functions import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from components.exceptions import freindly_error_msg
"""Create the MatplotCanvas Class"""


class MatplotCanvas(FigureCanvas):
    """Class that inherits from the FigureCanvas to get all Features"""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.set_facecolor("#d3d3d3")
        self.axes = fig.add_subplot(111)
        super(MatplotCanvas, self).__init__(fig)

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

        self.sc = MatplotCanvas(self, width=5, height=4, dpi=100)
        layout1.addWidget(self.sc)

        layout1.setSpacing(10)
        self.setLayout(layout1)
        layout1.setContentsMargins(10, 10, 10, 10)

        self.btn.clicked.connect(self.plot)

        self.grid_enabled = False
        self.legend_enabled = False
        self.lines = {}

    def plot(self):
        """Create the plot from helper functions that process inputs to give
        a specific input to the matplot"""

        try:
            f_x = self.input_1_f_of_x.text()
            xmin_input = self.input_2_x_min.text()
            xmax_input = self.input_3_x_max.text()
            parsed_function = parse_F_of_x(f_x)
            x_min, x_max = x_axis(xmin_input, xmax_input)
            x_range, y_range = X_Y_Ranges(parsed_function, x_min, x_max)
            line, = self.sc.axes.plot(x_range, y_range)
            self.lines[f_x] = line
            self.sc.draw()
        except freindly_error_msg as e:
            error_message = str(e)
            QMessageBox.critical(self, "Error", error_message)
