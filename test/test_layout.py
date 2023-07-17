from PySide2.QtCore import Qt
from PySide2.QtTest import QTest
from PySide2.QtWidgets import QMessageBox
import sys
from unittest.mock import patch
sys.path.append("..")
from container.layout import MainLayout


def test_plot_valid_inputs(qtbot):
    main_layout = MainLayout()
    qtbot.addWidget(main_layout)

    qtbot.keyClicks(main_layout.input_1_f_of_x, "x**2")
    qtbot.keyClicks(main_layout.input_2_x_min, "-5")
    qtbot.keyClicks(main_layout.input_3_x_max, "5")
    QTest.mouseClick(main_layout.btn, Qt.LeftButton)

    assert main_layout.sc.axes.lines


def test_plot_invalid_function(qtbot):
    main_layout = MainLayout()
    qtbot.addWidget(main_layout)

    qtbot.keyClicks(main_layout.input_1_f_of_x, "x^")
    qtbot.keyClicks(main_layout.input_2_x_min, "-5")
    qtbot.keyClicks(main_layout.input_3_x_max, "5")

    with patch.object(QMessageBox, "critical") as mock_critical:
        QTest.mouseClick(main_layout.btn, Qt.LeftButton)

        error_message = "F(X) is not valid"
        mock_critical.assert_called_with(main_layout, "Error", error_message)

def test_parse_plot(qtbot):
    main_layout = MainLayout()
    qtbot.addWidget(main_layout)

    qtbot.keyClicks(main_layout.input_1_f_of_x, "")
    qtbot.keyClicks(main_layout.input_2_x_min, "-5")
    qtbot.keyClicks(main_layout.input_3_x_max, "5")

    with patch.object(QMessageBox, "critical") as mock_critical:
        QTest.mouseClick(main_layout.btn, Qt.LeftButton)

        error_message = "F(X) is empty"
        mock_critical.assert_called_with(main_layout, "Error", error_message)

def test_x_y_ranges_plot(qtbot):
    main_layout = MainLayout()
    qtbot.addWidget(main_layout)

    qtbot.keyClicks(main_layout.input_1_f_of_x, "x^2")
    qtbot.keyClicks(main_layout.input_2_x_min, "5")
    qtbot.keyClicks(main_layout.input_3_x_max, "-5")

    with patch.object(QMessageBox, "critical") as mock_critical:
        QTest.mouseClick(main_layout.btn, Qt.LeftButton)

        error_message = "X-min can not be greater than X-max"
        mock_critical.assert_called_with(main_layout, "Error", error_message)

def test_toggle_grid(qtbot):
    main_layout = MainLayout()
    qtbot.addWidget(main_layout)

    assert not main_layout.grid_enabled
    assert main_layout.grid_toggle.text() == "Show Grid"

    QTest.mouseClick(main_layout.grid_toggle, Qt.LeftButton)

    assert main_layout.grid_enabled
    assert main_layout.grid_toggle.text() == "Hide Grid"

def test_toggle_legend(qtbot):
    main_layout = MainLayout()
    qtbot.addWidget(main_layout)

    assert not main_layout.legend_enabled
    assert main_layout.legend_toggle.text() == "Show Legend"

    QTest.mouseClick(main_layout.legend_toggle, Qt.LeftButton)

    assert main_layout.legend_enabled
    assert main_layout.legend_toggle.text() == "Hide Legend"

    QTest.mouseClick(main_layout.legend_toggle, Qt.LeftButton)

    assert not main_layout.legend_enabled
    assert main_layout.legend_toggle.text() == "Show Legend"

@patch('PySide2.QtWidgets.QInputDialog.getText', return_value=("My X Label", True))
def test_set_x_label(qtbot):
    main_layout = MainLayout()
    qtbot.addWidget(main_layout)

    QTest.mouseClick(main_layout.x_label, Qt.LeftButton)

    assert main_layout.sc.axes.get_xlabel() == "My X Label"


@patch('PySide2.QtWidgets.QInputDialog.getText', return_value=("My Y Label", True))
def test_set_y_label(qtbot):
    main_layout = MainLayout()
    qtbot.addWidget(main_layout)

    QTest.mouseClick(main_layout.y_label, Qt.LeftButton)

    assert main_layout.sc.axes.get_ylabel() == "My Y Label"

@patch('PySide2.QtWidgets.QInputDialog.getText', return_value=("My X Label", True))
@patch('PySide2.QtWidgets.QInputDialog.getText', return_value=("My Y Label", True))
def test_clear(qtbot, mock_get_text):
    main_layout = MainLayout()
    qtbot.addWidget(main_layout)

    main_layout.input_1_f_of_x.setText("x^2")
    main_layout.input_2_x_min.setText("-5")
    main_layout.input_3_x_max.setText("5")
    main_layout.plot()

    QTest.mouseClick(main_layout.x_label, Qt.LeftButton)
    QTest.mouseClick(main_layout.y_label, Qt.LeftButton)
    QTest.mouseClick(main_layout.grid_toggle, Qt.LeftButton)
    QTest.mouseClick(main_layout.legend_toggle, Qt.LeftButton)
    QTest.mouseClick(main_layout.btn_clear, Qt.LeftButton)

    assert not main_layout.sc.axes.lines
    assert not main_layout.grid_enabled
    assert not main_layout.legend_enabled
    assert not main_layout.lines
    assert main_layout.grid_toggle.text() == "Show Grid"
    assert main_layout.legend_toggle.text() == "Show Legend"
    assert not main_layout.grid_toggle.isChecked()
    assert not main_layout.legend_toggle.isChecked()
