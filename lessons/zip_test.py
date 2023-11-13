"""Test my zip function!"""

__author__ = "730387751"

from lessons.zip import zip


def test_zip_empty() -> None:
    """Test zip with empty lists."""
    assert zip([], []) == {}


def test_zip_chr() -> None:
    """Test zip with characters."""
    assert zip(["a", "b", "c"], [1, 2, 3]) == {"a": 1, "b": 2, "c": 3}


def test_zip_names() -> None:
    """Test zip with names."""
    assert zip(["lauren", "charlie", "julia"], [4, 5, 6]) == {"lauren": 4, "charlie": 5, "julia": 6}