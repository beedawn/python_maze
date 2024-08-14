"""
File: config.py
Author: Brandon "Bee" Schmersal
Date: 2024-08-04

Description: A config file for the configuration of the model.

"""

#Size of the entire UI Window
WINDOW_SIZE = '800x600'
#Margins between the window frame and UI elements
MARGIN_WIDTH = 25
MARGIN_TOP = 25
#Number of cells maze should consist of in a square
NUM_CELLS = 40
#Height and width of each cell in pixels
CELL_WIDTH_HEIGHT = 10
#Calculates the canvas height, the canvas is the element of the UI in which the maze is placed
CANVAS_HEIGHT = (NUM_CELLS + 1) * CELL_WIDTH_HEIGHT
#Calculates the canvas width
CANVAS_WIDTH = (NUM_CELLS + 1) * CELL_WIDTH_HEIGHT
#Set the wall color
BOUNDING_WALL_COLOR = 'black'
#Set the maze's background color
CANVAS_BACKGROUND_COLOR = 'white'
#Agent's starting position
STARTING_POSITION = (int(NUM_CELLS / 2), int(NUM_CELLS / 2))
#Position of the goal
GOAL_POSITION = (0, 0)

