"""
File: Maze.py
Author: Brandon "Bee" Schmersal
Date: 2024-08-04

Description: A Maze object, which contains the uuid, maze_type, Navigator, MazeBuilder,
maze_grid, player_cell and goal_cell.
The Maze class member attributes include:
 uuid - unique id for each generated maze
 maze_type - type of maze, labyrinth or looping_maze
 Navigator - instance of Navigator class
 MazeBuilder - instance of MazeBuilder class
 maze_grid - matrix of Cell objects
 player_cell - agent's position
 goal_cell - goal position

"""

from ui import config
from navigator import Navigator
from maze_builder import MazeBuilder


class Maze:
    def __init__(self, uuid, maze_type=None):
        #takes generated uuid to differentiate each maze when written to file
        self.uuid = uuid
        #stores maze type "looping_maze" or "labyrinth"
        self.maze_type = maze_type
        #associates a Navigator object with the maze
        self.Navigator = Navigator()
        #associates a MazeBuilder object with the maze
        self.MazeBuilder = MazeBuilder()
        #constructs the matrix of cells and stores to maze_grid
        self.maze_grid = self.MazeBuilder.construct_maze_grid()
        #agent/player starting location, imported from config
        self.player_cell = self.maze_grid[config.STARTING_POSITION[0]][config.STARTING_POSITION[1]]
        #location of the goal, imported from config
        self.goal_cell = self.maze_grid[config.GOAL_POSITION[0]][config.GOAL_POSITION[1]]


