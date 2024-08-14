"""
File: AlgorithmFrame.py
Author: Brandon "Bee" Schmersal
Date: 2024-08-04

Description: A AlgorithmFrame object, which displays Counter information relevant to an algorithm to the UI.

"""

import tkinter as tk
from counter import Counter

class AlgorithmFrame(tk.LabelFrame):
    def __init__(self, parent, frameText):
        #initialize parent
        super().__init__(parent, text=frameText)
        #initialize counter
        self.counter = Counter()
        #initialize timer_label
        self.timer_label = (tk.Label(self, text="Timer"))
        #place timer label in ui frame grid
        self.timer_label.grid(column=0, row=0)
        #initialize timer_output
        self.timer_output = tk.Label(self, text="0")
        #place timer_output in ui frame grid
        self.timer_output.grid(column=1, row=0)
        #initialize steps label
        self.steps_label = tk.Label(self, text="Steps")
        #place steps_label in ui frame grid
        self.steps_label.grid(column=0, row=1)
        #initialize steps_output label
        self.steps_output = tk.Label(self, text="0")
        #place steps_output in ui frame grid
        self.steps_output.grid(column=1, row=1)
        #initialize nodes_label
        self.nodes_label = tk.Label(self, text="Nodes Visted")
        #place nodes_label in ui frame grid
        self.nodes_label.grid(column=0, row=2)
        #initialize nodes_output
        self.nodes_output = tk.Label(self, text="0")
        #place nodes_output in ui frame grid
        self.nodes_output.grid(column=1, row=2)

    #updates ui timer with counter total time
    def update_ui_timer(self):
        #gets total time from counter and puts into timer_output label
        self.timer_output.config(text=round(self.counter.get_total_time(), 4))

    #updates ui nodes visited with total nodes visited count
    def update_ui_nodes_visited(self):
        #put total nodes visited count into nodes_ouput label
        self.nodes_output.config(text=self.counter.nodes_visited_count)

    #updates ui visisted with total steps from counter
    def update_ui_steps(self):
        #put total steps into steps output label in ui
        self.steps_output.config(text=self.counter.steps)

    #updates frame with counter values
    def update_frame(self, counter):
        #set passed counter to frame counter
        self.counter = counter
        #update timer based on new counter
        self.update_ui_timer()
        #update nodes visited based on new counter
        self.update_ui_nodes_visited()
        #update steps based on new counter
        self.update_ui_steps()

    #resets UI to default, all zeros
    def reset_ui(self):
        #zero out counter
        self.counter.reset()
        #update timer ui based on new zeroed counter
        self.update_ui_timer()
        #update steps up based on new zeroed counter
        self.update_ui_steps()
        #update nodes visisted ui based on new zeroed counter
        self.update_ui_nodes_visited()

