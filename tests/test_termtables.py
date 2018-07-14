import pytest

from termtables.cell import _pad, Cell, Row


def test_cell_padding_single():
    s = "Data String"
    assert _pad(s, 1, 1) == " Data String "


def test_cell_padding_double():
    s = "Data String"
    assert _pad(s, 2, 2) == "  Data String  "


def test_cell_padding_long_right():
    s = "Data String"
    assert _pad(s, 2, 10) == "  Data String          "


def test_cell_render():
    c = Cell("Data String", 1, 1)
    assert c._render() == " Data String "


def test_row_render():
    r = Row(grid=True)
    r.add_row([
        ("Data String", 1, 1),
    ])
    assert r.render() == "| Data String "
