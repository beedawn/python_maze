"""
File: Cell.py
Author: Brandon "Bee" Schmersal
Date: 2024-08-04

Description: A cell object, which is a cell within a maze.
The Cell class member attributes include:
 drawing coordinates (drawX, drawY)
 height and width in pixels (height, width)
 walls (wall_top, wall_bottom, wall_left, wall_right)
 if the cell has been visited by an agent (visited)
 row, col - the cells position within the maze

"""
from ui import config


class Cell:
    def __init__(self, x, y, col, row):
        #Sets the starting coordinates for which the cell should be drawn
        #within the UI
        self.drawX = x
        self.drawY = y

        #height and width of the cell
        self.height = config.CELL_WIDTH_HEIGHT
        self.width = config.CELL_WIDTH_HEIGHT

        #Walls of the cell
        self.wall_top = True
        self.wall_bottom = True
        self.wall_left = True
        self.wall_right = True

        #Has the cell been visited by the agent
        self.visited = False

        #cells row and column position within the maze matrix
        self.row = row
        self.col = col

    #returns location of the cell within the maze
    def get_location(self):
        return self.row, self.col

    #removes left wall from cell
    def remove_left_wall(self):
        self.wall_left = False

    #removes right wall from cell
    def remove_right_wall(self):
        self.wall_right = False

    #removes bottom wall from cell
    def remove_bottom_wall(self):
        self.wall_bottom = False

    #removes top wall from cell
    def remove_top_wall(self):
        self.wall_top = False

    #marks cell as visited by the agent
    def mark_visited(self):
        self.visited = True


