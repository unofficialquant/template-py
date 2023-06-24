from src.add import add_one, add_three, add_two


def test_add_one():
    """Test add_one."""
    assert add_one(1) == 2
    assert add_one(0) == 1
    assert add_one(-1) == 0
    assert add_one(1.5) == 2.5
    assert add_one(0.5) == 1.5
    assert add_one(-0.5) == 0.5


def test_add_two():
    """Test add_two."""
    assert add_two(1) == 3
    assert add_two(0) == 2
    assert add_two(-1) == 1
    assert add_two(1.5) == 3.5
    assert add_two(0.5) == 2.5
    assert add_two(-0.5) == 1.5


def test_add_three():
    """Test add_three."""
    assert add_three(1) == 4
    assert add_three(0) == 3
    assert add_three(-1) == 2
    assert add_three(1.5) == 4.5
    assert add_three(0.5) == 3.5
    assert add_three(-0.5) == 2.5
