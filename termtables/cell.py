from typing import List, Tuple, Dict
from collections import OrderedDict


def _pad(string: str, left_pad=0, right_pad=0) -> str:
    output = string
    pad_char = " "
    if left_pad > 0:
        output = (pad_char * left_pad) + output
    if right_pad > 0:
        output = output + (pad_char * right_pad)
    return output


class Row:
    def __init__(self, grid: bool=True) -> None:
        self.grid = grid
        self._cell_list: List[Cell] = []
        self._marker_cell_length = 0 # the longest cell in header or row

    def _add_row(self, lst: List[Tuple[str, int, int]]) -> None:
        for x in lst:
            self._cell_list.append(Cell(*lst[0]))

    def add_row(self, row: List[str]) -> None:
        self._update_marker_cell_length(row)

    def add_header(self, row: List[str]) -> None:
        self._update_marker_cell_length(row)

    def _update_marker_cell_length(self, lst: List[str]) -> None:
        """Updates self._marker_cell attribute"""
        self._marker_cell_length = len(sorted(lst)[-1])

    def render(self):
        output = []
        if self.grid:
            for c in self._cell_list:
                output.append("|")
                output.append(c._render())
        return "".join(output)


class Cell:
    """A single cell."""

    def __init__(self, string, left_pad, right_pad) -> None:
        self.string = string
        self.left_pad = left_pad
        self.right_pad = right_pad

    def _render(self):
        self.output = _pad(self.string, self.left_pad, self.right_pad)
        return self.output

