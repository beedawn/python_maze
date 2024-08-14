"""
File: Counter.py
Author: Brandon "Bee" Schmersal
Date: 2024-08-04

Description: A Counter object, which tracks metrics of the agent in the maze
The Counter class member attributes include:
 start and ending time (start_time, end_time)
 steps - movements agents have taken
 nodes_visited_count - number of nodes visited

"""
import time


class Counter:
    def __init__(self):
        #initialize start time
        self.start_time = 0
        #initialize end time
        self.end_time = 0
        #initialize steps
        self.steps = 0
        #initialize nodes_visited count
        self.nodes_visited_count = 0

    #resets all members to 0
    def reset(self):
        #reset start time
        self.start_time = 0
        #reset end time
        self.end_time = 0
        #reset steps
        self.steps = 0
        #reset nodes visited count
        self.nodes_visited_count = 0

    #sets the timer starting time
    def start_timer(self):
        #set start time with current time
        self.start_time = time.time()

    #sets the timer ending time
    def end_timer(self):
        #checks to make sure there is a start time, otherwise no point in calling end time
        if self.start_time != 0:
            #sets end time to current time
            self.end_time = time.time()

    #sets steps variable
    def set_steps(self, steps):
        self.steps = steps

    #sets nodes_visited_count variable
    def set_nodes(self, nodes):
        self.nodes_visited_count = nodes

    #gets timers total time
    def get_total_time(self):
        #total time = end_time - start_time
        return self.end_time - self.start_time
