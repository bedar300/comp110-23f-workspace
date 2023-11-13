"""Write Three tests for the dictionary functions in dictionary.py."""


__author__ = "730387751"


from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_blank() -> None:
    """Tests invert function with no keys and values."""
    assert invert({}) == {}


def test_invert_one() -> None:
    """Tests invert function with one key and value."""
    assert invert({"a": "b"}) == {"b": "a"}


def test_invert_five() -> None:
    """Tests invert function with five keys and values."""
    assert invert({"a": "bc", "c": "de", "d": "ef", "e": "fg", "f": "gh"}) == {"bc": "a", "de": "c", "ef": "d", "fg": "e", "gh": "f"}


def test_favorite_color_one() -> None:
    """Tests favorite_color function with one key and value."""
    assert favorite_color({"susan": "purple"}) == "purple"


def test_favorite_color_five() -> None:
    """Tests favorite_color function with five keys and values."""
    assert favorite_color({"susan": "purple", "matt": "blue", "joe": "purple", "jane": "purple", "jill": "red"}) == "purple"


def test_favorite_color_blank() -> None:
    """Tests favorite_color function with no keys and values."""
    assert favorite_color({}) == ""


def test_count_one() -> None:
    """Tests count function with one key and value."""
    assert count(["a"]) == {"a": 1}


def test_count_ten() -> None:
    """Tests count function with ten keys and values."""
    assert count(["red", "blue", "blue", "red", "purple", "green", "red", "brown", "yellow", "blue"]) == {"red": 3, "blue": 3, "purple": 1, "green": 1, "brown": 1, "yellow": 1}


def test_count_blank() -> None:
    """Tests count function with no keys and values."""
    assert count([]) == {}


def test_alphabetizer_blank() -> None:
    """Tests alphabetizer function with no keys and values."""
    assert alphabetizer([]) == {}


def test_alphabetizer_five() -> None:
    """Tests alphabetizer function with five keys and values."""
    assert alphabetizer(["apple", "banana", "cherry", "berries", "elderberry"]) == {"a": ["apple"], "b": ["banana", "berries"], "c": ["cherry"], "e": ["elderberry"]}


def test_alphabetizer_different_cases() -> None:
    """Tests alphabetizer function with different cases."""
    assert alphabetizer(["Citrus", "circus"]) == {"c": ["Citrus", "circus"]}


def test_update_attendance_one() -> None:
    """Tests update_attendance function for adding one student to one day."""
    assert update_attendance({"monday": ["charlie"]}, "monday", "diana") == {"monday": ["charlie", "diana"]}


def test_update_duplicate_name() -> None:
    """Tests update_attendance function for adding duplicate student to one day."""
    assert update_attendance({"monday": ["charlie"]}, "monday", "charlie") == {"monday": ["charlie"]}


def test_update_attendance_new_day() -> None:
    """Tests update_attendance function for adding one student to a new day."""
    assert update_attendance({"monday": ["charlie"]}, "tuesday", "diana") == {"monday": ["charlie"], "tuesday": ["diana"]}