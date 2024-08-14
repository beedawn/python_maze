"""
File: Navigator.py
Author: Brandon "Bee" Schmersal
Date: 2024-08-04

Description: A Navigator object, which moves the agent within the Maze.

"""
class Navigator:
    #takes a position and moves the player to that position
    def move_agent(self, position, maze):
        #unpack row and column
        new_row, new_col = position
        #set player cell within maze to the cell at the provided row and column
        maze.player_cell = maze.maze_grid[new_row][new_col]

    #gets all non walled off neighbors for a given cell in the given maze
    def get_neighbors(self, cell, maze):
        # unpack row and column from provided cell
        current_position_row, current_position_col = cell.get_location()
        #get upper and lower maze bounds with provided maze
        maze_lower_bounds, maze_upper_bounds = self.get_maze_bounds(maze)
        #constructs top neighbor, gets cell above current position, or None if above neighbor walled off
        top_neighbor = self.construct_neighbor(maze_lower_bounds, current_position_row, cell.wall_top,
                                               cell.get_location(), -1, 0, maze)
        # constructs bottom neighbor, gets cell below current position, or None if below neighbor walled off
        bottom_neighbor = self.construct_neighbor(current_position_row, maze_upper_bounds, cell.wall_bottom,
                                                  cell.get_location(), 1, 0, maze)
        # constructs left neighbor, gets cell to the left of current position, or None if left neighbor walled off
        left_neighbor = self.construct_neighbor(maze_lower_bounds, current_position_col, cell.wall_left,
                                                cell.get_location(), 0, -1, maze)
        # constructs right neighbor, gets cell to the right of current position, or None if right neighbor walled off
        right_neighbor = self.construct_neighbor(current_position_col, maze_upper_bounds, cell.wall_right,
                                                 cell.get_location(), 0, 1, maze)
        #returns list of neighbors, order matters
        return [top_neighbor, left_neighbor, bottom_neighbor, right_neighbor]

    # checks provided neighbor is within the maze bounds, takes left_check (lefthand side of < conditional)
    # right_check (right hand side of < conditional) a wall boolean
    # position parameter (tuple of row, col)
    # row and column parameters to determine location of neighbor
    # and the maze to get the neighbor from
    def construct_neighbor(self, left_check, right_check, wall, position, row, col, maze):
        # unpack row and column from position
        current_position_row, current_position_col = position
        # check if left is less than right and wall is False
        if left_check < right_check and not wall:
            # return position of the neighbor
            return maze.maze_grid[current_position_row + row][current_position_col + col]
        else:
            #neighbor walled off, return None
            return None

    #simplifies redundant maze bounds logic, gets lower maze bounds, zero
    # and upper maze bounds length of maze_grid row -1
    def get_maze_bounds(self, maze):
        # lower maze bounds, zero
        maze_lower_bounds = 0
        # upper maze bounds, length of maze_grid - 1 to account for 0 index
        maze_upper_bounds = len(maze.maze_grid) - 1
        #returns lower and upper maze bounds
        return maze_lower_bounds, maze_upper_bounds

    #sets all cells visited member to false
    def clear_visited(self, maze):
        # iterates through each row in maze_grid
        for row in range(len(maze.maze_grid)):
            # iterates through each column in maze_grid
            for col in range(len(maze.maze_grid[row])):
                # set visited member to False
                maze.maze_grid[row][col].visited = False

    #finds and counts all visited cells
    def count_visited_cells(self, maze):
        # set count to zero
        count = 0
        # iterate through each row in maze_grid
        for row in range(len(maze.maze_grid)):
            # iterate through each column in maze_grid
            for col in range(len(maze.maze_grid[row])):
                #is visited true?
                if maze.maze_grid[row][col].visited:
                    # increase count by 1
                    count += 1
        #return sum of visited cells
        return count
