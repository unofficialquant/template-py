"""Addition module."""


def _check_type(val: "int|float") -> None:
    """Check that the input is an int or float.

    Args:
        val (int|float): The number to check.

    Raises:
        TypeError: If the input is not an int or float.
    """
    if type(val) not in [int, float]:
        raise TypeError("val must be int or float")


def add_one(val: "int|float") -> "int|float":
    """Add one to the input.

    Args:
        val (int|float): The number to add one to.

    Returns:
        int|float: The result of adding one to the input.
    """
    _check_type(val)
    return val + 1


def add_two(val: "int|float") -> "int|float":
    """Add two to the input.

    Args:
        val (int|float): The number to add two to.

    Returns:
        int|float: The result of adding two to the input.
    """
    _check_type(val)
    return val + 2


def add_three(val: "int|float") -> "int|float":
    """Add three to the input.

    Args:
        val (int|float): The number to add three to.

    Returns:
        int|float: The result of adding three to the input.
    """
    _check_type(val)
    return val + 3
