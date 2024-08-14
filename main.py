"""
File: main.py
Author: Brandon "Bee" Schmersal
Date: 2024-08-04

Description: The main function which starts the program.

"""

import tkinter as tk
from ui import UI

if __name__ == "__main__":
    #build TK GUI
    root = tk.Tk()
    #pass TK GUI to UI module
    ui = UI(root)
    #execute loop
    root.mainloop()
