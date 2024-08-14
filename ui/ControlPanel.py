"""
File: ControlPanel.py
Author: Brandon "Bee" Schmersal
Date: 2024-08-04

Description: A ControlPanel object, which serves a container for MazePanel and AlgorithmPanel

"""
import tkinter as tk
from ui import config
from . import MazePanel, AlgorithmPanel


class ControlPanel(tk.Frame):
    def __init__(self, parent, ui):
        #initialize parent
        super().__init__(parent)
        #initialize maze_panel
        self.maze_panel = MazePanel.MazePanel(parent, ui)
        #place maze_panel
        self.maze_panel.place(x=config.MARGIN_WIDTH, y=config.MARGIN_TOP, height=125, width=175)
        #initialize algorithm_panel
        self.algorithm_panel = AlgorithmPanel.AlgorithmPanel(parent, ui)
        #place algorithm_panel
        self.algorithm_panel.place(x=config.MARGIN_WIDTH, y=config.MARGIN_TOP + 110, height=150, width=175)
