"""
File: test_Cell.py
Author: Brandon "Bee" Schmersal
Date: 2024-08-04

Description: A suite of unit tests for the Cell class.

"""

import unittest
from cell import Cell
from ui import config

drawX = 10
drawY = 10
col = 5
row = 5


class Test_Cell(unittest.TestCase):
    def setUp(self):
        #setup test cell
        self.cell = Cell(drawX, drawY, col, row)

class TestInit(Test_Cell):
    def test_cell_constructor(self):
        #assert drawX value in cell is equal to drawX
        self.assertEqual(self.cell.drawX, drawX)
        #assetr drawY value in cell is equal to drawY
        self.assertEqual(self.cell.drawY, drawY)
        #assert cell height is equal to height defined in config
        self.assertEqual(self.cell.height, config.CELL_WIDTH_HEIGHT)
        #assert cell width is equal to width defined in config
        self.assertEqual(self.cell.width, config.CELL_WIDTH_HEIGHT)
        #assert cell col is equal to col
        self.assertEqual(self.cell.col, col)
        #assert cell row is equal to row
        self.assertEqual(self.cell.row, row)
        #assert walls are built correctly
        self.assertEqual(self.cell.wall_top, True)
        self.assertEqual(self.cell.wall_bottom, True)
        self.assertEqual(self.cell.wall_left, True)
        self.assertEqual(self.cell.wall_right, True)

    def test_cell_location(self):
        #assert get_location returns column and row of cell
        self.assertEqual(self.cell.get_location(), (row, col))

    def test_cell_remove_left_wall(self):
        #remove left wall from cell
        self.cell.remove_left_wall()
        #assert left wall has been removed
        self.assertEqual(self.cell.wall_left, False)

    def test_cell_remove_right_wall(self):
        #remove right wall from cell
        self.cell.remove_right_wall()
        #assert right wall has been removed
        self.assertEqual(self.cell.wall_right, False)

    def test_cell_remove_top_wall(self):
        #remove top wall from cell
        self.cell.remove_top_wall()
        #assert top wall has been removed
        self.assertEqual(self.cell.wall_top, False)

    def test_cell_remove_bottom_wall(self):
        #remove bottom wall from cell
        self.cell.remove_bottom_wall()
        #assert bottom wall has been removed
        self.assertEqual(self.cell.wall_bottom, False)

    def test_cell_mark_visited(self):
        #mark cell as visited
        self.cell.mark_visited()
        #assert cell indicates it's been visited
        self.assertEqual(self.cell.visited, True)


if __name__ == '__main__':
    unittest.main()
