"""
File: FileWriter.py
Author: Brandon "Bee" Schmersal
Date: 2024-08-04

Description: A FileWriter object, which writes data to a file.
The FileWriter class member attributes include:
 file_data_fields - headers for csv file
 file_data - data written to file

"""

import os
import csv
import uuid


class FileWriter:
    def __init__(self):
        #sets file fields for csv
        self.file_data_fields = ["maze_id", "maze_type", "maze_height", "maze_width", "starting_position", "goal_position",
                                 "algorithm", "time",
                                 "steps", "nodes"]
        #initialize empty data list
        self.file_data = []

    #checks that data being written matches the length of file_data_fields
    def __check_length(self):
        #iterate through each sublist in file_data
        for sublist in self.file_data:
            #check that length of sublist is the same as length of file_data_fields
            if not len(sublist) == len(self.file_data_fields):
                return False
        else:
            return True

    #ensures file_data is a list
    def __check_type(self):
        #checks file_data is list type
        if isinstance(self.file_data, list):
            return True
        #if file_data is not a list
        else:
            return False

    #check structure of data in file_data and ensure its the expected types
    def __check_structure(self):
        #iterate through all sublists in file_data
        for sublist in self.file_data:
            if not (
                    #checks first element of file_data sublist is uuid, should be uuid of maze_id
                    isinstance(sublist[0], uuid.UUID) and
                    #checks second element of file_data is a str, should be maze_type str
                    isinstance(sublist[1], str) and
                    #checks that third element of file_data is an int, should be maze_height int
                    isinstance(sublist[2], int) and
                    #checks that fourth element of file_data is an int, should be maze_width int
                    isinstance(sublist[3], int) and
                    #checks that fifth element of file_data is a tuple, should be tuple of two ints, starting position
                    isinstance(sublist[4], tuple) and
                    #checks that sixth element of file data is tuple, should be tuple of two ints, goal_position
                    isinstance(sublist[5], tuple) and
                    #checks that seventh element of file data is str, should be algorithm str
                    isinstance(sublist[6], str) and
                    #checks that eighth element of file data is float, should be time float
                    isinstance(sublist[7], float) and
                    #checks that ninth element is int, should be steps int
                    isinstance(sublist[8], int) and
                    #checks that tenth element is int, should be nodes int
                    isinstance(sublist[9], int)
            ):
                #if file_data doesn't match
                return False
        #file data matches structure
        return True

    #writes file_data to data.csv
    def add_to_file(self):
        #set initial value of saved
        saved = "Not Saved!"

        #check that data stored in file_data matches appropriate length, types, structure, and contains data
        if self.__check_length() and self.__check_type() and self.__check_structure() and self.file_data:
            #initialize file_name, name of file to be written
            file_name = "data.csv"
            #get uuid from file_data
            uuid = self.file_data[0][0]
            #initialize a variable that toggles if the provided uuid is already in the csv file
            uuid_exists = False
            #check if file_name file already exists in file structure
            if os.path.exists(file_name):
                #file exists, open file as a csv file
                with open(file_name, newline='') as csvfile:
                    #initialize data_reader to read file
                    data_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                    #iterate through rows in data_reader
                    for row in data_reader:
                        #see if uuid data in file_name matches uuid of data about to be inserted into file
                        if row[0] == str(uuid):
                            #print message stating uuid exists in file
                            print("uuid exists in file")
                            #toggle uuid boolean
                            uuid_exists = True
                            #print message to UI indicating the file has been saved previously
                            saved = "Already Saved"
                            break
                #if uuid is not present in the file about to be written to, but file exists
                if not uuid_exists:
                    #open file as a csv file
                    with open(file_name, 'a', newline='') as csvfile:
                        #initialize csvwriter to write data
                        csvwriter = csv.writer(csvfile)
                        #write file data to file
                        csvwriter.writerows(self.file_data)
                        #update ui to present saved message
                        saved = "Saved"
            #file with name of file_name does not exist, so create a new file
            else:
                #write a new file
                with open(file_name, 'w', newline='') as csvfile:
                    #create csvwriter to write data
                    csvwriter = csv.writer(csvfile)
                    #add file_data_field headers to file
                    csvwriter.writerow(self.file_data_fields)
                    #add file_data under file_data_field headers
                    csvwriter.writerows(self.file_data)
                    #update ui to present saved message
                    saved = "Saved"
        #data written, clear stored data to avoid duplicates
        self.file_data = []
        #return saved string to forward to UI component
        return saved



