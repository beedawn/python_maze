"""
File: bfs.py
Author: Brandon "Bee" Schmersal
Date: 2024-08-04

Description: An implementation of Breadth First Search algorithm, with arguments:
 navigator to conduct agent movements
 maze which the agent exists in
 ui to update with agent position

 returns void
"""
def bfs_search(navigator, maze, ui):
    #initialize stack with player starting cell
    stack = [maze.player_cell]
    #initialize visited set with player starting location
    visited = set(maze.player_cell.get_location())
    #set steps to 1, to account for starting cell
    steps = 1
    while stack:
        #get cell from left side/beginning of stack
        current_cell = stack.pop(0)
        #mark cell as visited
        current_cell.mark_visited()
        #runs if animation is true, a lot slower but draws each frame
        ui.show_animation()
        #get neighbors list of neighbors that are not walled off
        neighbors_list = navigator.get_neighbors(current_cell, maze)
        #iterate through neighbors list
        for neighbor in neighbors_list:
            #check neighbor is not none
            if neighbor is not None:
                #get position of neighbor
                next_position = neighbor.get_location()
                #check neighbor has not been visited
                if next_position not in visited:
                    #add neighbor location to visited set
                    visited.add(next_position)
                    #add neighbor to stack list
                    stack.append(neighbor)
                    #move to selected neighbor
                    navigator.move_agent(next_position, maze)
                    #we moved, so increase step counter
                    steps += 1
                #check if neighbor we moved to is goal
                if neighbor is maze.goal_cell:
                    #goal found, print message
                    print("goal found by BFS! in", steps, "steps")
                    return True, steps
    #no goal found, print message
    print("No path to goal found")
    return False, steps
