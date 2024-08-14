"""
File: test_FileWriter.py
Author: Brandon "Bee" Schmersal
Date: 2024-08-04

Description: A suite of unit tests for the FileWriter class.

"""
from file_writer import FileWriter
import unittest


class Test_FileWriter(unittest.TestCase):
    def setUp(self):
        #setup test FileWriter
        self.FileWriter = FileWriter()
        #setup expected data_fields
        self.data_fields = ["maze_id","maze_type", "maze_height", "maze_width", "starting_position", "goal_position",
                            "algorithm", "time", "steps", "nodes"]
        #initialize empty file_data list
        self.file_data = []

class TestInit(Test_FileWriter):
    def test_data_fields(self):
        #assert FileWriter's file_data_fields match data_fields
        self.assertEqual(self.FileWriter.file_data_fields, self.data_fields)

    def test_file_data(self):
        #assert FileWriter's file_data matches empty file_data
        self.assertEqual(self.FileWriter.file_data, self.file_data)


if __name__ == '__main__':
    unittest.main()
