"""
File: Keyboard.py
Author: Brandon "Bee" Schmersal
Date: 2024-08-04

Description: A Keyboard object, which allows keyboard keys W,A,S,D to move the agent,
and I,J,K,L to destroy walls within the maze.

"""
class Keyboard:
    def __init__(self, ui):
        #binds ui to keyboard
        self.ui = ui
        #binds w,a,s,d keys to keyboard_move_agent method
        self.ui.bind_all("<w>", lambda event: self.keyboard_move_agent(event, self.ui.MazeInstance))
        self.ui.bind_all("<a>", lambda event: self.keyboard_move_agent(event, self.ui.MazeInstance))
        self.ui.bind_all("<s>", lambda event: self.keyboard_move_agent(event, self.ui.MazeInstance))
        self.ui.bind_all("<d>", lambda event: self.keyboard_move_agent(event, self.ui.MazeInstance))

        #binds i,j,k,l keys to keyboard_destroy_wall method
        self.ui.bind_all("<i>", lambda event: self.keyboard_destroy_wall(event))
        self.ui.bind_all("<j>", lambda event: self.keyboard_destroy_wall(event))
        self.ui.bind_all("<k>", lambda event: self.keyboard_destroy_wall(event))
        self.ui.bind_all("<l>", lambda event: self.keyboard_destroy_wall(event))

    #moves agent with w,a,s,d keys
    def keyboard_move_agent(self, event, maze):
        #gets neighbors, cannot see over walls
        (up, left, down, right) = self.ui.MazeInstance.Navigator.get_neighbors(maze.player_cell, maze)
        #initialize new_position variable which is populated if w,a,s,d keys are pressed
        new_position = None
        if event.keysym == 'w':
            #set new_position to up
            new_position = up
        elif event.keysym == 'a':
            #set new_position to left
            new_position = left
        elif event.keysym == 's':
            #set new_position to down
            new_position = down
        elif event.keysym == 'd':
            #set new_position to right
            new_position = right
        #ensure new_position is not none
        if new_position:
            #get location of postion to move to
            new_position_location = new_position.get_location()
            #move to new position
            maze.Navigator.move_agent(new_position_location, maze)
        #redraw maze in ui
        self.ui.draw_grid(self.ui.MazeInstance)

    def keyboard_destroy_wall(self, event):
        #get players current cell location
        current_location = self.ui.MazeInstance.player_cell.get_location()
        #get neighbors of current cell, this can see over walls
        (up, left, down, right) = self.ui.MazeInstance.MazeBuilder.get_neighbors_explore(self.ui.MazeInstance)
        #initalize future wall to destroy
        neighbor_wall_to_destroy = None
        if event.keysym == 'i':
            #set wall to be destroyed to up
            neighbor_wall_to_destroy = up
        elif event.keysym == 'j':
            # set wall to be destroyed to left
            neighbor_wall_to_destroy = left
        elif event.keysym == 'k':
            # set wall to be destroyed to down
            neighbor_wall_to_destroy = down
        elif event.keysym == 'l':
            # set wall to be destroyed to right
            neighbor_wall_to_destroy = right
        # make sure wall to destroy is not none
        if neighbor_wall_to_destroy:
            #get location of wall to destroy
            neighbor_wall_to_destroy_location = neighbor_wall_to_destroy.get_location()
            #destroy the walls between current cell and neighbor_wall_to_destroy
            self.ui.MazeInstance.MazeBuilder.destroy_wall(current_location, neighbor_wall_to_destroy_location,
                                                          self.ui.MazeInstance)
        #redraw maze grid in ui
        self.ui.draw_grid(self.ui.MazeInstance)
