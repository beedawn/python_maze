"""
File: test_MazeBuilder.py
Author: Brandon "Bee" Schmersal
Date: 2024-08-04

Description: A suite of unit tests for the MazeBuilder class.

"""
import unittest
from unittest.mock import patch
from maze_builder import MazeBuilder
from ui import config
from cell import Cell


class MockMazeBuilder:

    def construct_maze_grid():
        cell1 = Cell(0, 0, 0, 0)
        cell2 = Cell(1, 1, 1, 1)
        cell3 = Cell(2, 2, 2, 2)
        cell4 = Cell(3, 3, 3, 3)
        return [[cell1, cell2, cell3, cell4]]


class Test_MazeBuilder(unittest.TestCase):
    @patch('maze_builder.MazeBuilder', MockMazeBuilder)
    def setUp(self):
        #setup maze_builder
        self.maze_builder = MazeBuilder()
        #setup mazegrid
        self.mazegrid = MockMazeBuilder.construct_maze_grid()

class TestInit(Test_MazeBuilder):
    def test_maze_constructor(self):
        #assert mazegrid matches construct_maze_grid column count
        self.assertEqual(len(self.mazegrid[0]), 4)
        #assert mazegrid matches construct_maze_grid row count
        self.assertEqual(len(self.mazegrid), 1)


if __name__ == '__main__':
    unittest.main()
