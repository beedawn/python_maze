"""
File: MazePanel.py
Author: Brandon "Bee" Schmersal
Date: 2024-08-04

Description: A MazePanel object, which provides buttons linked to maze generation.

"""

import tkinter as tk
from maze import Maze
import uuid

#builds maze control panel Frame in ui for generate Maze buttons and reset player to start
class MazePanel(tk.Frame):
    def __init__(self, parent, ui):
        #initialize parent
        super().__init__(parent)
        #initialize ui
        self.ui = ui
        #sets label for frame
        self.maze_label = tk.Label(self, text="Maze")
        #places label relatively in frame
        self.maze_label.place(x=0, y=0)
        #initialize generate looping maze button
        self.generate_looping_maze_button = tk.Button(self, text="Generate Looping Maze",
                                                      command=self.maze_generator_looping_button,
                                                      width=14)
        #plaze generate looping maze button
        self.generate_looping_maze_button.place(x=0, y=20)
        #initialize Generate Labyrinth button
        self.generate_labyrinth_button = tk.Button(self, text="Generate Labyrinth",
                                                   command=self.maze_generator_labyrinth_button,
                                                   width=14)
        #place generate labyrinth maze button
        self.generate_labyrinth_button.place(x=0, y=50)

        #initialize animation_checkbox
        self.animation_checkbox = tk.Checkbutton(self, text="Animation",
                                                 onvalue=1, offvalue=0, command=self.toggle_animation)
        #place animation_checkbox
        self.animation_checkbox.place(x=0, y=80)

    #method to run when Generate Looping Maze button is pushed
    def maze_generator_looping_button(self):
        self.handle_maze_construction(self.ui.MazeInstance.MazeBuilder.construct_random_maze_looping)

    def maze_generator_labyrinth_button(self):
        self.handle_maze_construction(self.ui.MazeInstance.MazeBuilder.construct_random_maze_labyrinth)

    def toggle_animation(self):
        self.ui.animation = not self.ui.animation

    def handle_maze_construction(self, maze_construct):
        if not self.ui.busy:
            self.reset_maze()
            self.ui.MazeInstance.uuid = uuid.uuid4()
            maze_construct(self.ui.MazeInstance, self.ui)
            self.show_built_maze()

    def reset_maze(self):
        self.ui.MazeInstance = Maze(0)
        self.ui.display_panel.set_goal_text_default()
        self.ui.display_panel.astar_frame.reset_ui()
        self.ui.display_panel.bfs_frame.reset_ui()
        self.ui.display_panel.dfs_frame.reset_ui()
        self.ui.display_panel.update_ui_status_field("Processing")
        self.ui.root_tk.after(500)

    def show_built_maze(self):
        self.ui.draw_grid(self.ui.MazeInstance)
        self.ui.display_panel.update_ui_status_field("Ready")
