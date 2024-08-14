"""
File: FileWriter.py
Author: Brandon "Bee" Schmersal
Date: 2024-08-04

Description: A MazeBuilder object, which builds a randomly generated Maze.

"""
import random
from ui import config
from cell import Cell
import uuid


class MazeBuilder:
    #constructs a matrix of cell objects
    def construct_maze_grid(self):
        new_maze = [
            # calculates coordinates of where to draw cell x coordinate: ix + (config.CELL_WIDTH_HEIGHT * 0.6)
            # and where to draw y coordinate: iy + (config.CELL_WIDTH_HEIGHT * 0.6)
            [Cell(ix + (config.CELL_WIDTH_HEIGHT * 0.6), iy + (config.CELL_WIDTH_HEIGHT * 0.6),
                  # then calculates row and column of each cell by dividing ix by the cell_width height
                  int(ix / config.CELL_WIDTH_HEIGHT), int(iy / config.CELL_WIDTH_HEIGHT)) for ix in
             #sets range from 0 to CANVAS_WIDTH - CELL_WIDTH_HEIGHT, and increments by CELL_WIDTH_HEIGHT
             range(0, config.CANVAS_WIDTH - config.CELL_WIDTH_HEIGHT, config.CELL_WIDTH_HEIGHT)] for iy
            in
            # sets range from 0 to CANVAS_WIDTH - CELL_WIDTH_HEIGHT, and increments by CELL_WIDTH_HEIGHT
            range(0, config.CANVAS_HEIGHT - config.CELL_WIDTH_HEIGHT, config.CELL_WIDTH_HEIGHT)]
        #returns maze
        return new_maze

    def construct_random_maze_labyrinth(self, maze, ui):
        maze.maze_type = "labyrinth"
        #visited set, initialized with agent's starting location
        visited = {maze.player_cell.get_location()}
        #queue list, initialized with agent's starting cell
        queue = [maze.player_cell]
        while queue:
            #get player cells location
            current_player_position = maze.player_cell.get_location()
            #get list of navigable neighbors, returns None within the list if neighbor is maze boundary
            neighbor_list = self.get_neighbors_explore(maze)
            # filters out neighbors that have been visited from the visited list,
            # and filters out neighbors that are None and puts the remnants into the unvisited_neighbors list
            unvisited_neighbors = self.filter_neighbors(neighbor_list, visited)
            #ensures unvisited neighbors is not empty
            if unvisited_neighbors:
                #random int to use to determine next neighbor to go to, ranges from 0 to length of
                # unvisited_neighbors-1 to account for 0 index
                random_int = random.randint(0, len(unvisited_neighbors) - 1)
                #randomly picks neighbor from unvisited_neighbors
                next_cell = unvisited_neighbors[random_int]
                #get location/position of neighbor
                next_position = next_cell.get_location()
                #add position of neighbor to visited
                visited.add(next_position)
                #add neighbor to queue
                queue.append(next_cell)
            #if no neighbors, we need to go backwards
            else:
                #get cell off of right side/end of queue
                back_cell = queue.pop()
                #get position of the cell we captured
                next_position = back_cell.get_location()
            #destroy wall for neighbor, or redundant destruction of wall that is already destroyed if we move backwards
            #however this simplifies code structure
            self.destroy_wall(current_player_position, next_position, maze)
            #move agent to either future neighbor, or backwards depending on value of next_position
            maze.Navigator.move_agent(next_position, maze)
            # update ui each frame if animation is enabled
            ui.show_animation()

    def construct_random_maze_looping(self, maze, ui):
        maze.maze_type = "looping_maze"
        # visited set, initialized with agent's starting location
        visited = {maze.player_cell.get_location()}
        # queue list, initialized with agent's starting cell
        queue = [maze.player_cell]
        while queue:
            #gets player's location
            current_player_position = maze.player_cell.get_location()
            # get list of navigable neighbors, returns None within the list if neighbor is walled off
            neighbor_list = self.get_neighbors_explore(maze)
            # filters out neighbors that have been visited from the visited list,
            # and filters out neighbors that are None and puts the remnants into the unvisited_neighbors list
            unvisited_neighbors = self.filter_neighbors(neighbor_list, visited)
            # random int to use to determine next neighbor to go to, ranges from 0 to length of
            # unvisited_neighbors-1 to account for 0 index
            random_int = random.randint(0, len(neighbor_list) - 1)
            # randomly picks neighbor from unvisited_neighbors
            next_cell = neighbor_list[random_int]
            # assign next position to current players position, in the event a new position is not found
            next_position = current_player_position
            #check if random neighbor exists, and is not visited
            if next_cell is not None and next_cell.get_location() not in visited:
                #get random int for unvisited neighbors
                random_int = random.randint(0, len(unvisited_neighbors) - 1)
                #assign next cell to a random neighbor
                next_cell = unvisited_neighbors[random_int]
                #get next cells location and assign it to position to be moved to
                next_position = next_cell.get_location()
                #add position of neighbor to move to, to visited
                visited.add(next_position)
                #add cell of neighbor to move to, to queue
                queue.append(next_cell)
            #if cell is none, or cell is in visited
            else:
                #check if cell has unvisited neighbors, and that the unvisited neighbors aren't None aka
                # not edge of the maze
                if len(unvisited_neighbors) > 0 and None not in unvisited_neighbors:
                    #get random int based on unvisited_neighbors length
                    random_int = random.randint(0, len(unvisited_neighbors) - 1)
                    #get location of randomly chosen neighbor
                    unvisited_neighbor_location = unvisited_neighbors[random_int].get_location()
                    #set next_position to destroy walls and move to, to the location of the unvisited neighbor
                    next_position = unvisited_neighbor_location
                #if unvisited neighbors is a maze boundary, or there are no unvisited_neighbors
                elif None in unvisited_neighbors or len(unvisited_neighbors) == 0:
                    #pop from right side/end of queue to get last cell player was in
                    back_cell = queue.pop()
                    #set next_position to the location of the previous cell
                    next_position = back_cell.get_location()
            # destroy walls between future neighbor we're moving to, or redundantly destroy walls between current cell
            # and cell we were at previously
            self.destroy_wall(current_player_position, next_position, maze)
            #move to next_position, either random unvisited neighbor, or backwards
            maze.Navigator.move_agent(next_position, maze)
            # update ui each frame if animation is enabled
            ui.show_animation()

    #destroys walls between the two given cells, in the provided maze
    def destroy_wall(self, current_position, next_position, maze):
        #get current row and column from current_position
        current_row, current_col = current_position
        #get row and column from future position
        next_row, next_col = next_position
        #lower maze bounds, always zero
        maze_lower_bounds = 0
        #upper maze bounds for rows, length of maze row
        maze_upper_bounds_rows = len(maze.maze_grid) - 1
        #upper maze bounds for columns, length of a column
        maze_upper_bounds_cols = len(maze.maze_grid[0]) - 1
        #if future row is within maze bounds, and future column is in maze bounds
        if (maze_lower_bounds <= next_row <= maze_upper_bounds_rows
                and maze_lower_bounds <= next_col <= maze_upper_bounds_cols):
            #get the cell the player is currently in
            current_cell = maze.maze_grid[current_row][current_col]
            #get the cell of next_position
            next_cell = maze.maze_grid[next_row][next_col]
            #if current row is greater than next row, and columns are equal then we are moving upward
            if current_row > next_row and current_col == next_col:
                #destroy top wall of the current cell player occupies
                current_cell.remove_top_wall()
                #destroy bottom wall of cell player is about to occupy
                next_cell.remove_bottom_wall()
            #if current row is less than next row and columns are equal then we are moving downward
            if current_row < next_row and current_col == next_col:
                #destroy bottom wall of current cell player occupies
                current_cell.remove_bottom_wall()
                #destroy top wall of cell player is about to occupy
                next_cell.remove_top_wall()
            #if current row and next row are equal and current column is less than next column
            # then we are moving right
            if current_row == next_row and current_col < next_col:
                # destroy right wall from cell player occupies
                current_cell.remove_right_wall()
                # destroy left wall from cell player is about to occupy
                next_cell.remove_left_wall()
            # if current row and next row are equal and current column is greater than next column
            # then we are moving left
            if current_row == next_row and current_col > next_col:
                # destroy left wall from cell player occupies
                current_cell.remove_left_wall()
                # destroy right wall from cell player is about to occupy
                next_cell.remove_right_wall()

    #gets neighbors for the players current location, can see over walls
    def get_neighbors_explore(self, maze):
        #lower bounds of maze, always 0
        maze_lower_bounds = 0
        # upper bounds of maze, length of maze grid -1 to account for 0 index
        maze_upper_bounds = len(maze.maze_grid) - 1
        #get row and column from the players current location
        current_position_row, current_position_col = maze.player_cell.get_location()
        #checks that the current row is greater than lower maze bounds
        if maze_lower_bounds < current_position_row:
            #assign neighbor one row above current position to top_neighbor
            top_neighbor = maze.maze_grid[current_position_row - 1][current_position_col]
        else:
            #otherwise we hit the top edge of the maze, return none
            top_neighbor = None
        # checks that maze row is less than upper bounds
        if current_position_row < maze_upper_bounds:
            # assign neighbor one row below current position to bottom_neighbor
            bottom_neighbor = maze.maze_grid[current_position_row + 1][current_position_col]
        else:
            # otherwise we hit the bottom edge of the maze, return none
            bottom_neighbor = None
        # checks that current column is greater than lower maze bounds
        if maze_lower_bounds < current_position_col:
            # assign neighbor one column to the left of current position to left_neighbor
            left_neighbor = maze.maze_grid[current_position_row][current_position_col - 1]
        else:
            # otherwise we hit the left edge of the maze, return none
            left_neighbor = None
        #checks that current column is less than upper maze bounds
        if current_position_col < maze_upper_bounds:
            # assign neighbor one column to the right of current position to right_neighbor
            right_neighbor = maze.maze_grid[current_position_row][current_position_col + 1]
        else:
            # otherwise we hit right edge of the maze, return none
            right_neighbor = None
        # return constructed list of neighbors, order matters.
        return [top_neighbor, left_neighbor, bottom_neighbor, right_neighbor]

    # filters out neighbors that are none, and neighbors that are in provided visited list
    def filter_neighbors(self, neighbors, visited):
        #new list to return
        filtered_list = []
        #iterate through neighbors list
        for neighbor in neighbors:
            #check if neighbor item in neighbors is nont none, and neighbor item's location is not in visited
            if neighbor is not None and neighbor.get_location() not in visited:
                # append to filtered_list
                filtered_list.append(neighbor)
        #return new list
        return filtered_list

    #clears visited cells from maze
    def clear_visited_cells(self, maze):
        #loop  through list rows
        for row in range(len(maze.maze_grid)):
            #loop through list columns
            for col in range(len(maze.maze_grid[row])):
                #set visited member for each cell to false
                maze.maze_grid[row][col].visited = False
