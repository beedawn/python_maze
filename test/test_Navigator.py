"""
File: test_Navigator.py
Author: Brandon "Bee" Schmersal
Date: 2024-08-04

Description: A suite of unit tests for the Navigator class.

"""
import unittest
from counter import Counter
from ui import config
from navigator import Navigator
from cell import Cell
import time
from unittest.mock import patch, Mock

zero = 0


class Test_Navigator(unittest.TestCase):
    def setUp(self):
        #setup test counter
        self.counter = Counter()
        #setup maze mock
        self.Maze = Mock()
        #create maze_grid
        maze_grid = [[Cell(col, row, col, row) for col in range(0, 8)] for row in range(0, 8)]
        #associate maze_grid with mock maze_grid
        self.Maze.maze_grid = maze_grid
        #set mock maze_grid player cell
        self.Maze.player_cell = self.Maze.maze_grid[1][1]
        #set mock maze_grid goal cell
        self.Maze.goal_cell = self.Maze.maze_grid[2][2]
        #initialize test navigator
        self.Navigator = Navigator()


class TestInit(Test_Navigator):
    def test_movement(self):
        #set position to move to
        position = (0, 1)
        #move player from starting position to defined position
        self.Navigator.move_agent(position, self.Maze)
        #unpack position
        row, col = position
        #assert player has been moved to new position
        self.assertEqual(self.Maze.maze_grid[row][col], self.Maze.player_cell)

    def test_clear_visited(self):
        #initialize position
        position = (0, 0)
        #set cell in position location to visited True
        self.Maze.maze_grid[position[0]][position[1]].visited = True
        #count number of visited cells
        visited_count = self.Navigator.count_visited_cells(self.Maze)
        #assert visited count matches visited cells
        self.assertEqual(visited_count, 1)
        #clear out visited cells
        self.Navigator.clear_visited(self.Maze)
        #get new visited count
        visited_count_cleared = self.Navigator.count_visited_cells(self.Maze)
        #assert no cells are visited
        self.assertEqual(visited_count_cleared, 0)

    def test_get_neighbors(self):
        #get player position
        player_position = self.Maze.player_cell.get_location()
        #unpack row and col from player_position
        row, col = player_position
        #get expected neighbors for each associated neighbor
        bottom_neighbor = self.Maze.maze_grid[row + 1][col]
        right_neighbor = self.Maze.maze_grid[row][col + 1]
        top_neighbor = self.Maze.maze_grid[row - 1][col]
        left_neighbor = self.Maze.maze_grid[row][col + -1]

        #remove all walls of current cell so player can move
        self.Maze.maze_grid[row][col].wall_bottom = False
        self.Maze.maze_grid[row][col].wall_right = False
        self.Maze.maze_grid[row][col].wall_top = False
        self.Maze.maze_grid[row][col].wall_left = False
        #get neighbors from get_neighbord method to compare against
        neighbors = self.Navigator.get_neighbors(self.Maze.player_cell, self.Maze)
        #assert neighbors matches expected List
        self.assertEqual(neighbors, [top_neighbor, left_neighbor, bottom_neighbor, right_neighbor])
        #assert neighbors matches expected length, 4
        self.assertEqual(len(neighbors), 4)

    def test_visited_navigator(self):
        #set a cell to visited
        self.Maze.maze_grid[0][0].visited = True
        #count total visited cells
        visited_count = self.Navigator.count_visited_cells(self.Maze)
        #assert visited count matched expected count of 1
        self.assertEqual(visited_count, 1)

    def test_maze_bounds(self):
        #get results from get_maze_bounds method
        lower_maze_bounds, upper_maze_bounds = self.Navigator.get_maze_bounds(self.Maze)
        #assert lower bounds is 0
        self.assertEqual(lower_maze_bounds, 0)
        #assert upper bounds is length of maze_grid -1 to account for 0 index
        self.assertEqual(upper_maze_bounds, len(self.Maze.maze_grid) - 1)


if __name__ == '__main__':
    unittest.main()
