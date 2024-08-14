"""
File: AlgorithmFrame.py
Author: Brandon "Bee" Schmersal
Date: 2024-08-04

Description: A AlgorithmPanel object, which provides buttons linked to each algorithm.

"""

import tkinter as tk
from ui import config
from algorithms import bfs_search, dfs_search, astar_search
from counter import Counter


class AlgorithmPanel(tk.Frame):
    def __init__(self, parent, ui):
        #initialize parent
        super().__init__(parent)
        #initialize ui
        self.ui = ui
        #initialize Counter
        self.counter = Counter()
        #initialize algorithm_label
        self.algorithm_label = tk.Label(self, text="Algorithms")
        #place algorithm_label relative to frame
        self.algorithm_label.place(x=0, y=0)
        #initialize solve_dfs_button
        self.solve_dfs_button = tk.Button(self, text="Solve DFS",
                                          command=lambda: self.handle_button(dfs_search,
                                                                             self.ui.display_panel.dfs_frame), width=14)
        #place solve dfs_button
        self.solve_dfs_button.place(x=0, y=20)
        #initialize solve_bfs_button
        self.solve_bfs_button = tk.Button(self, text="Solve BFS",
                                          command=lambda: self.handle_button(bfs_search,
                                                                             self.ui.display_panel.bfs_frame), width=14)
        #place solve_bfs_button
        self.solve_bfs_button.place(x=0, y=50)

        #initialize solve_astar_button
        self.solve_astar_button = tk.Button(self, text="Solve A*",
                                            command=lambda: self.handle_button(astar_search,
                                                                               self.ui.display_panel.astar_frame),
                                            width=14)
        #place solve_astar_button
        self.solve_astar_button.place(x=0, y=80)

    #generic method to handle each algorithm button, takes method and relevant frame
    def handle_button(self, algorithm_function, frame):
        if not self.ui.busy:
            self.ui.busy = True
            #set goal text to default - an empty string
            self.ui.display_panel.set_goal_text_default()
            #clear visited cells from maze
            self.ui.MazeInstance.Navigator.clear_visited(self.ui.MazeInstance)
            #move agent to starting position
            self.ui.MazeInstance.Navigator.move_agent(config.STARTING_POSITION, self.ui.MazeInstance)
            #redraw grid
            self.ui.draw_grid(self.ui.MazeInstance)
            #set status field text to "Processing"
            self.ui.display_panel.update_ui_status_field("Processing")
            #wait for status_field text to update
            self.ui.root_tk.after(500)
            #start counter timer
            self.counter.start_timer()
            #execute algorithm, and capture result and steps
            result, steps = algorithm_function(self.ui.MazeInstance.Navigator,
                                               self.ui.MazeInstance, self.ui)
            #algorithm finished, end timer
            self.counter.end_timer()
            #set counter steps with result from algorithm
            self.counter.set_steps(steps)
            #set visited nodes with number of visited cells in maze
            self.counter.set_nodes(self.ui.MazeInstance.Navigator.count_visited_cells(self.ui.MazeInstance))
            #redraw grid
            self.ui.draw_grid(self.ui.MazeInstance)
            #updates ui elements within passed frame
            frame.update_frame(self.counter)
            #add data to file_writer file_data list
            self.ui.file_writer.file_data.append(
                [self.ui.MazeInstance.uuid, self.ui.MazeInstance.maze_type, config.NUM_CELLS, config.NUM_CELLS,
                 config.STARTING_POSITION,
                 config.GOAL_POSITION, algorithm_function.__name__, self.counter.get_total_time(),
                 self.counter.steps, self.counter.nodes_visited_count])
            #set status field text back to "Ready
            self.ui.display_panel.update_ui_status_field("Ready")
            #updates goal text to display green "Goal!" or red "No Goal!"
            self.ui.display_panel.handle_result(result)
            self.ui.busy = False
