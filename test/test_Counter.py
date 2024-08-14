"""
File: test_Counter.py
Author: Brandon "Bee" Schmersal
Date: 2024-08-04

Description: A suite of unit tests for the Counter class.

"""
import unittest
from counter import Counter
from ui import config
import time

zero = 0


class Test_Counter(unittest.TestCase):
    def setUp(self):
        #setup test counter
        self.counter = Counter()


class TestInit(Test_Counter):
    def test_counter_constructor(self):
        #assert counter starts with 0 values for each member
        self.assertEqual(self.counter.start_time, zero)
        self.assertEqual(self.counter.end_time, zero)
        self.assertEqual(self.counter.steps, zero)
        self.assertEqual(self.counter.nodes_visited_count, zero)

    def test_counter_reset(self):
        #start counter timer
        self.counter.start_timer()
        #set steps to 5
        self.counter.set_steps(5)
        #set nodes to 5
        self.counter.set_nodes(5)
        #wait a bit so timer can time
        time.sleep(1)
        #end timer
        self.counter.end_timer()
        #reset counter
        self.counter.reset()
        #ensure counter values are now zeros
        self.assertEqual(self.counter.get_total_time(), 0)
        self.assertEqual(self.counter.nodes_visited_count, 0)
        self.assertEqual(self.counter.steps, 0)

    def test_counter_start_timer(self):
        #get current time
        current_time = time.time()
        #start timer
        self.counter.start_timer()
        #assert start time is roughly equal to current time
        self.assertEqual(round(self.counter.start_time), round(current_time))

    def test_counter_end_timer(self):
        #start timer
        self.counter.start_timer()
        #get current time
        current_time = time.time()
        #end timer
        self.counter.end_timer()
        #assert end_time is roughly equal to current time
        self.assertEqual(round(self.counter.end_time), round(current_time))

    def test_counter_timer(self):
        #start timer
        self.counter.start_timer()
        #wait a second to let timer time
        time.sleep(1)
        #end the timer
        self.counter.end_timer()
        #assert total time is roughly equal to 1 second
        self.assertEqual(round(self.counter.get_total_time()), 1)

    def test_counter_steps(self):
        #test setting steps
        self.counter.set_steps(5)
        #ensure steps are set
        self.assertEqual(self.counter.steps, 5)

    def test_counter_nodes_visited(self):
        #test visited nodes count
        self.counter.nodes_visited_count = 1
        #assert nodes_visited_count matches inserted value
        self.assertEqual(self.counter.nodes_visited_count, 1)

if __name__ == '__main__':
    unittest.main()
