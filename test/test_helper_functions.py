import sys
import pytest
import numpy as np
import sympy
sys.path.append("..")
from components.exceptions import friendly_error_msg
from components.helper_functions import (
    parse_F_of_x,
    handle_old_function,
    parse,
    x_axis,
    X_Y_Ranges,
)


def test_parse_F_of_x():
    """Test the F_of_x"""

    with pytest.raises(friendly_error_msg) as error:
        parse_F_of_x("")

    assert str(error.value) == "F(X) is empty"
    assert parse_F_of_x("x^2") == sympy.parse_expr("x**2")

def test_handle_old_function():
    assert handle_old_function("x^2") == "x**2"

def test_parse():
    """Test the Syntax error of (f(x))"""

    with pytest.raises(friendly_error_msg) as error:
        parse("x^")
    assert str(error.value) == "F(X) is not valid"

def test_x_axis():
    """Test x-axis"""

    assert x_axis("1", "5") == (1.0, 5.0)

    with pytest.raises(friendly_error_msg):
        x_axis("a", "5")

def test_X_Y_Ranges():
    """Test X_Y_Ranges"""

    function_parsed = sympy.parse_expr("x**2")
    x_min = 1.0
    x_max = 5.0
    x_data, y_data = X_Y_Ranges(function_parsed, x_min, x_max)
    assert len(x_data) == 1000
    assert len(y_data) == 1000
    assert np.allclose(x_data[0], x_min)
    assert np.allclose(x_data[-1], x_max)
    assert np.allclose(y_data[0], x_min ** 2)
    assert np.allclose(y_data[-1], x_max ** 2)

    with pytest.raises(friendly_error_msg)as error:
        X_Y_Ranges(function_parsed, 5.0, 1.0)
    assert str(error.value) == "X-min can not be greater than X-max"
