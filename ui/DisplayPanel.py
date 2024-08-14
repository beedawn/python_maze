"""
File: DisplayPanel.py
Author: Brandon "Bee" Schmersal
Date: 2024-08-04

Description: A DisplayPanel object, which displays the metrics associated with the algorithms running,
and their results.

"""

import tkinter as tk
from ui import config
from . import AlgorithmFrame


class DisplayPanel(tk.Frame):
    def __init__(self, parent):
        #initialize parent
        super().__init__(parent)
        #initialize status label
        self.status_label = tk.Label(parent, text="Status")
        #place status label
        self.status_label.place(x=config.MARGIN_WIDTH, y=config.MARGIN_TOP + 220)
        #initialize goal_output
        self.goal_output = tk.Label(parent, text="")
        #place goal_output
        self.goal_output.place(x=config.MARGIN_WIDTH + 80, y=config.MARGIN_TOP + 220)
        #initialize status text box
        self.status_text = tk.Text(parent, height=1, width=10, bg="white", fg="black")
        #place status text box
        self.status_text.place(x=config.MARGIN_WIDTH, y=config.MARGIN_TOP + 240)
        #set status text box initial text
        self.status_text.insert(tk.INSERT, "Ready")
        #initialize total nodes label
        self.total_nodes_label = tk.Label(parent, text="Total nodes")
        #place total nodes label
        self.total_nodes_label.place(x=config.MARGIN_WIDTH, y=config.MARGIN_TOP + 530)
        #initialize total nodes count label, gets total number of nodes/cells in the maze
        self.total_nodes_count = tk.Label(parent, text=config.NUM_CELLS ** 2)
        #place total nodes count label
        self.total_nodes_count.place(x=config.MARGIN_WIDTH + 75, y=config.MARGIN_TOP + 530)


        #build algorithm data display frames
        #initialize bfs frame
        self.bfs_frame = AlgorithmFrame.AlgorithmFrame(parent, "BFS")
        #place bfs frame
        self.bfs_frame.place(x=config.MARGIN_WIDTH, y=config.MARGIN_TOP + 350, width=150, height=90)
        #initialize dfs frame
        self.dfs_frame = AlgorithmFrame.AlgorithmFrame(parent, "DFS")
        #place dfs frame
        self.dfs_frame.place(x=config.MARGIN_WIDTH, y=config.MARGIN_TOP + 260, width=150, height=90)
        #initialize A* frame
        self.astar_frame = AlgorithmFrame.AlgorithmFrame(parent, "A*")
        #place A* frame
        self.astar_frame.place(x=config.MARGIN_WIDTH, y=config.MARGIN_TOP + 440, width=150, height=90)

    #updates status field text box
    def update_ui_status_field(self, status):
        #delete values in field
        self.status_text.delete('1.0', tk.END)
        #insert new text into field
        self.status_text.insert(tk.END, str(status))

    #sets goal display to default(empty)
    def set_goal_text_default(self):
        #set text in goal_text to ""
        self.goal_output.config(text="", fg='black', bg='white')

    #handles true or false response from algorithms, and updates the goal text field
    def handle_result(self, result):
        #if result is true, print green Goal!
        if result:
            self.goal_output.config(text="Goal!", fg='white', bg='green')
        #if result is false, print red "No Goal!"
        else:
            self.goal_output.config(text="No Goal!", fg='white', bg='red')
