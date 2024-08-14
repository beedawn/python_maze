"""
File: UI.py
Author: Brandon "Bee" Schmersal
Date: 2024-08-04

Description: A UI object, which configures the UI, and contains all elements within the UI.

"""

from maze import Maze
from ui import config
from main import tk

from keyboard import Keyboard
from . import ControlPanel, DisplayPanel
from file_writer import FileWriter


#main UI class
class UI(tk.Canvas):
    def __init__(self, root_tk):
        #builds maze canvas
        tk.Canvas.__init__(self, root_tk, width=config.CANVAS_WIDTH, height=config.CANVAS_HEIGHT,
                           bg=config.CANVAS_BACKGROUND_COLOR)
        #initialize tk parent element
        self.root_tk = root_tk
        #set window size
        self.root_tk.geometry(config.WINDOW_SIZE)
        #set window title
        self.root_tk.title('aMAZEing')
        #generate initial maze, with uuid of 0
        self.MazeInstance = Maze(0)
        #places maze canvas within window
        self.place(x=config.MARGIN_WIDTH + 175, y=config.MARGIN_TOP, anchor="nw")
        #draws maze grid
        self.draw_grid(self.MazeInstance)
        #initialize control panel, which contains algorithm buttons
        self.control_panel = ControlPanel.ControlPanel(root_tk, self)
        #place control panel
        self.control_panel.place(x=config.MARGIN_WIDTH, y=config.MARGIN_TOP, height=100, width=100)
        #initialize save data button
        self.save_data_button = tk.Button(root_tk, text="Save Data", command=self.save_data, width=7)
        #place save data button
        self.save_data_button.place(x=config.MARGIN_WIDTH + 50, y=config.MARGIN_TOP - 10)
        #initialize keyboard class
        self.keyboard_controller = Keyboard(self)
        #initialize display_panel
        self.display_panel = DisplayPanel.DisplayPanel(root_tk)
        #initialize file_writer
        self.file_writer = FileWriter()
        self.animation = False
        self.busy = False

    #draws the maze grid
    def draw_grid(self, maze):
        #deletes old grid from ui
        self.delete('grid')
        #iterates through maze_grid row
        for row in range(len(maze.maze_grid)):
            #iterates through maze_grid col
            for column in range(len(maze.maze_grid[row])):
                #capture individual cell
                cell = maze.maze_grid[row][column]
                #check if cell has a top wall
                if cell.wall_top:
                    #if top wall exists, draw top wall line
                    self.create_line(cell.drawX, cell.drawY, cell.drawX + config.CELL_WIDTH_HEIGHT,
                                     cell.drawY, fill=config.BOUNDING_WALL_COLOR, tags='grid')
                #check if cell has bottom wall
                if cell.wall_bottom:
                    #if bottom wall exists, draw bottom wall line
                    self.create_line(cell.drawX, cell.drawY + config.CELL_WIDTH_HEIGHT,
                                     cell.drawX + config.CELL_WIDTH_HEIGHT,
                                     cell.drawY + config.CELL_WIDTH_HEIGHT,
                                     fill=config.BOUNDING_WALL_COLOR, tags='grid')
                #check if cell has right wall
                if cell.wall_right:
                    #if right wall exists, draw right wall line
                    self.create_line(cell.drawX + config.CELL_WIDTH_HEIGHT, cell.drawY,
                                     cell.drawX + config.CELL_WIDTH_HEIGHT,
                                     cell.drawY + config.CELL_WIDTH_HEIGHT,
                                     fill=config.BOUNDING_WALL_COLOR, tags='grid')
                #check if cell has left wall
                if cell.wall_left:
                    #if left wall exists, draw left wall line
                    self.create_line(cell.drawX, cell.drawY, cell.drawX, cell.drawY + config.CELL_WIDTH_HEIGHT,
                                     fill=config.BOUNDING_WALL_COLOR,
                                     tags='grid')
                #is this cell the cell the player is in?
                if cell == maze.player_cell:
                    #if it is, insert tutle emoji
                    self.create_text(
                        (cell.drawX + config.CELL_WIDTH_HEIGHT / 2, cell.drawY + config.CELL_WIDTH_HEIGHT / 2),
                        text="🐢", fill='blue', font='tkDefaultFont 10', tags='grid')
                #is this cell the goal cell?
                if cell == maze.goal_cell:
                    #if so, fill with green g
                    self.create_text(
                        (cell.drawX + config.CELL_WIDTH_HEIGHT / 2, cell.drawY + config.CELL_WIDTH_HEIGHT / 2),
                        text="g", fill='green', font='tkDefaultFont 10', tags='grid')
                #has the cell been visited?
                if cell.visited:
                    #if so, fill with footprint emoji
                    self.create_text(
                        (cell.drawX + config.CELL_WIDTH_HEIGHT / 2, cell.drawY + config.CELL_WIDTH_HEIGHT / 2),
                        text="👣", fill='brown', font='tkDefaultFont 7', tags=('grid', 'visited'))

    #saves data to file
    def save_data(self):
        #activates method to write data to file
        saved = self.file_writer.add_to_file()
        #updates status field in UI with messaged from saved
        self.display_panel.update_ui_status_field(saved)

    def show_animation(self):
        if self.animation:
            # update ui redraw grid
            self.draw_grid(self.MazeInstance)
            # Force Tkinter to update, without this it will not show each frame
            self.update()
