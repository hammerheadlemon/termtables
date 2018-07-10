import pytest

from termtables.cell import Cell


def test_cell():
    c = Cell()
    assert c
