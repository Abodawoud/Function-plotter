import numpy as np
from components.exceptions import freindly_error_msg
import sympy

def parse_F_of_x(function_text=""):
    """Parsing the f(x)"""

    function_text = function_text.replace(" ", "")
    if function_text == "":
        raise freindly_error_msg("F(X) is empty")
    handle_new_function = handle_old_function(function_text)
    parse_new_function = parse(handle_new_function)
    return parse_new_function

def handle_old_function(function_text: str):
    """Handle the function"""

    function_text = function_text.replace("^", "**")
    return function_text

def parse(function_text: str):
    """Susbtitute the range of x in the f(x)"""

    try:
        function_text = sympy.parse_expr(function_text)
    except (sympy.SympifyError, TypeError, SyntaxError):
        raise freindly_error_msg("F(X) is not valid")
    return function_text

def x_axis(x_min_text, x_max_text):
    """Get the x-data"""

    try:
        x_min = float(x_min_text)
        x_max = float(x_max_text)
        if x_min > x_max:
            raise freindly_error_msg("X-min can not be greater than X-max")
        return (x_min, x_max)
    except (TypeError, ValueError) as e:
        error_msg = "In valid X-min or X-max " + str(e)
        raise freindly_error_msg(error_msg)

def X_Y_Ranges(function_parsed, x_min, x_max):
    """Get the x range and y range"""

    x = sympy.symbols('x')
    expr_func = sympy.lambdify(x, function_parsed)

    x_data = np.linspace(x_min, x_max, 1000)
    y_data = expr_func(x_data)

    return x_data, y_data
