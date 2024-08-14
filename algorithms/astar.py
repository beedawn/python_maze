"""
File: astar.py
Author: Brandon "Bee" Schmersal
Date: 2024-08-04

Description: An implementation of A* search algorithm, with arguments:
 navigator to conduct agent movements
 maze which the agent exists in
 ui to update with agent position

 returns void
"""
import sys


def astar_search(navigator, maze, ui):
    #initialize boolean to determine if goal was found to terminate while loop
    found = False
    #initialize unvisited set
    unvisited = {}
    #initialize visited set
    visited = {}
    #fill unvisited set with [sys.maxsize, sys.maxsize, None] for each cell in the maze
    # where each node is set up as [g_value, f_value, previous_cell]
    #g_value is the cost from the starting cell to the current cell
    #f_value which is the total cost of cheapest path from start to goal through current cell
    fill_unvisited_cells(unvisited, maze)
    #get f_value by determining heuristic of starting cell to goal cell
    f_value = cost(maze.player_cell, maze.goal_cell)
    #get players start location
    start_location = (maze.player_cell.get_location())
    #update start locations g, f, and previous_cell in unvisited
    unvisited[start_location] = [0, f_value, None]
    while not found:
        #get cell with lowest f_value
        current_cell = get_lowest_f_value_key(unvisited)
        #unvisited exhausted, so get_min returns None
        if current_cell is None:
            #print message no goal found
            print("no goal found")
            #set steps to visited length
            steps = len(visited)
            return False, steps
        #is the current cell equal to the maze goal cell's location?
        elif current_cell == maze.goal_cell.get_location():
            #set found to true to break loop
            found = True
            #move unvisited cell to visited for traversal
            visited[current_cell] = unvisited[current_cell]
        #is current_cell not None?
        elif current_cell is not None:
            #unpack row and col from current_cell
            row, col = current_cell
            #get neighbors of current cell using row and col to collect cell object from grid
            neighbor_list = navigator.get_neighbors(maze.maze_grid[row][col], maze)
            #iterate through all cells in neighbor_list
            for neighbor in neighbor_list:
                #check neighbor is not none
                if neighbor is not None:
                    #get position of neighbor
                    next_position = neighbor.get_location()
                    #check neighbor has not been visited
                    if next_position not in visited:
                        #cost to move cells is 1
                        cost_to_move = 1
                        #calculate g_value for current cell, g_value of current cell + cost to move to neighbor
                        g_value = unvisited[current_cell][0] + cost_to_move
                        #check if current g_value  is less than next position's g_value
                        if g_value < unvisited[next_position][0]:
                            #f(n) = g(n) + h(n) where cost is our heuristic
                            f_value = g_value + cost(neighbor, maze.goal_cell)
                            #assign g_value to 0 in unvisited
                            unvisited[next_position][0] = g_value
                            #assign f_value to 1 in unvisited
                            unvisited[next_position][1] = f_value
                            #assign current cell as previous cell for neighbor in unvisited
                            unvisited[next_position][2] = current_cell
            #add current cell to visited set
            visited[current_cell] = unvisited[current_cell]
            #delete current cell from unvisited set
            del unvisited[current_cell]
            #mark cell visited to update UI
            maze.maze_grid[row][col].mark_visited()
            # move to selected neighbor
            navigator.move_agent(current_cell, maze)
            # runs if animation is true, a lot slower but draws each frame
            ui.show_animation()
    #get steps from visited length
    steps = len(visited)
    #need to enumerate through visited cells so we can move agent in UI
    for cell in visited:
        #move agent along visited/optimal path
        navigator.move_agent(cell, maze)
    #print message that goal was found and steps
    print("goal found by A* in", steps, "steps")
    return True, steps

#fills unvisited set with all possible nodes in graph with infinity values
def fill_unvisited_cells(unvisited, maze):
    #iterates through each row in maze_grid
    for row in range(len(maze.maze_grid)):
        #iterates through each column in maze_grid
        for col in range(len(maze.maze_grid[row])):
            #sets associated position in unvisited to infinity [g_value, f_value, previous node]
            #and sets previous node to none, as maze has not been traversed yet
            unvisited[(row, col)] = [sys.maxsize, sys.maxsize, None]

#cost is manhattan distance heuristic
def cost(cell, goal):
    #unpack current cell location
    current_cell_row, current_cell_col = cell.get_location()
    #unpack goal location
    goal_cell_row, goal_cell_col = goal.get_location()
    #return absolute value of current cell row - goal cell row + absolute value of current cell col - goal cell col
    return abs(current_cell_row - goal_cell_row) + abs(current_cell_col - goal_cell_col)

#gets lowest f value from unvisited and returns associated key
def get_lowest_f_value_key(unvisited):
    #assign lowest value infinity
    lowest_value = sys.maxsize
    #assign lowest key to none
    lowest_key = None
    #iterate through all items in unvisited dictionary
    for item in unvisited.items():
        #get f_value from current item
        f_value = item[1][1]
        #check if f_score is lower than lowest value
        if f_value < lowest_value:
            #assign f_score to lowest_value
            lowest_value = f_value
            #assign associated key to lowest key
            lowest_key = item[0]
    return lowest_key
