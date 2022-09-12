#!/usr/bin/python3
# 101-safe_function.py

import sys


def safe_function(fct, *args):
    """Executes a function safely.
    Args:
        fct: The function to execute.
        args: Arguments for fct.
    Returns:
        If an error occurs - None.
        Otherwise - the result of the call to fct.
    """
    try:
        result = fct(*args)
    except ZeroDivisionError:
        result = None
        sys.stderr.write("Exception: division by zero\n")
    except IndexError:
        result = None
        sys.stderr.write("Exception: list index out of range\n")

    return result
