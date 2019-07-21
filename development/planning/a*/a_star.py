#!/usr/bin/env python

"""
Author: George Murray 
Date: 07/19/2019

Simple search program to find the shortest path to a given goal
and return a grid that shows the path to the goal
"""

# Standard imports
import math
import numpy as np

def search(grid, init, goal, cost):
    """Search function to find the shortest path from a given start to a given goal
    
    Arguments:
        grid {Matrix} -- A grid(graph) that our function will search against
        init {Array} -- Starting position in (X, Y) coordinates
        goal {Array} -- Goal position in (X, Y) coordinates
        cost {Int} -- Cost of traversing each grid cell
    """
    # Initialize an expanded grid to keep track of when all the nodes were expanded
    expanded = [[-1 for row in range(len(grid[0]))] for col in range(len(grid[1]) - 1)]

    # Set the expansion time of the starting node
    expanded[init[0]][init[1]] = 0

    # Initialize an action grid to keep track of the actions
    action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid[1]) - 1)]

    
    # Initialize a grid of closed grid cells to keep track of which grid cells we have closed
    closed = [[1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]]

    # All the different ways we can expand
    delta = [[-1, 0],  # go up
             [0, -1],  # go left
             [1, 0],  # go down
             [0, 1]]  # go right

    delta_name = ['^', '<', 'v', '>']
    # Initialize the starting nodes x, y, and g values
    x = init[0]
    y = init[1]
    g = 0
    # Counter for expansion time
    expansion_time = 1
    # Initialize an opened list to keep track of nodes to expand and add our starting (init) grid cell to that list
    opened = [[g, x, y]]

    # Flags to keep track of whether we should continue searching.
    found = False
    resign = False

    # Actual search
    while found is False and resign is False:
        # Check to see if we have searched the whole grid and not found a path
        if len(opened) == 0:
            resign = True
            print("Failed to find a path")
        else:
            # Get the element with the smallest G-Value
            opened.sort()
            opened.reverse()
            next = opened.pop()
            x = next[1]
            y = next[2]
            g = next[0]

            # Check if we have found our goal
            if x == goal[0] and y == goal[1]:
                found = True
                print("Found goal: ", next)
                print("Expansion Grid")
                # Print out the expansion grid
                for row in expanded:
                    print(row)
                print("Path")
                # Initialize a policy grid to output the path
                policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid[1]) - 1)]
                x = goal[0]
                y = goal[1]
                policy[x][y] = '*'
                while x != init[0] or y != init[1]:
                    x2 = x - delta[action[x][y]][0]
                    y2 = y - delta[action[x][y]][1]
                    policy[x2][y2] = delta_name[action[x][y]]
                    x = x2
                    y = y2
                for row in policy:
                    print(row)
            else:
                # Expand the winning element and add to opened list
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    # Check to make sure the expansion is within the confines of the grid
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        # Check to make sure we have not already expanded into the current node and that it is not an obstacle
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            # Add the new node to the opened list
                            g2 = g + cost
                            # Calculate heuristic (Euclidean distance from current node to goal node)
                            heuristic = np.linalg.norm(np.asarray([x2, y2]) - np.asarray(goal))
                            g2 += heuristic
                            opened.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i
                            expanded[x2][y2] = expansion_time
                            expansion_time += 1


def main():
    grid = [[0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]

    init = [0, 0]
    goal = [len(grid)-1, len(grid[0])-1]
    cost = 1
    search(grid, init, goal, cost)

if __name__ == '__main__':
    main()