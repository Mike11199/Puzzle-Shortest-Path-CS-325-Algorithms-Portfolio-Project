# Name:             Michael Iwanek
# OSU Email:        iwanekm@oregonstate.edu
# Course:           CS325 - Algorithms
# Assignment:       Assignment #8 - Graph Algorithms 2 - Problem #3 (PORTFOLIO PROJECT)
# Due Date:         03/06/23 @ 11:59PM - Monday
# Description:      Given a 2-D puzzle of size MxN (N rows and M columns), reach the destination cells covering the minimum number of cells.  Each puzzle element is
#                   either a "-" for an empty or passable element, or '#' for an obstacle that cannot be passed.  One can move left, right, up, or down.

import heapq
import copy

def solve_puzzle(Board, Source, Destination):
    
    # print(Board)
    # print(Source)
    # print(Destination)
    
    # variables to check if a move (U, D, R, L) is valid
    puzzle_row_max = len(Board) - 1
    puzzle_col_max = len(Board[0]) - 1
    
    # create matrix equal to the size of the original matrix with all elements at infinity - to track distances
    distances = [[float('inf') for _ in range((puzzle_col_max+1))] for _ in range((puzzle_row_max+1))]
    
    # grab row/col of start position and update distance for that to zero
    row = Source[0]
    col = Source[1]    
    distances[row][col] = 0
        
    # create variables for tracking the path of edges throughout the graph - and a move_string of the moves (U, D, R, L)
    path = []
    move_string = ''
    path.append(Source)
    
    # create list to be used by the min-heap priority queue and push tuple of the start distance, source cell, path of edges, and move_string to it
    pathway_priority_queue = []            
    heapq.heappush(pathway_priority_queue, (0, Source, path, move_string))       
    

    while len(pathway_priority_queue) > 0:
        
        # push tuple with minimum distances from the priority queue to explore next
        minimum_next_path= heapq.heappop(pathway_priority_queue)           
        
        # grab current location in puzzle from the tuple
        current_source = minimum_next_path[1]                        
        row = current_source[0]
        col = current_source[1]
        
        # grab distance so far on path from tuple
        current_distance = minimum_next_path[0]
        
        # create deep copies of the current path of edges and string of moves
        current_path = copy.deepcopy(minimum_next_path[2])
        current_move_string =  copy.deepcopy(minimum_next_path[3])
        
        
        # RETURN ANSWER HERE
        if current_source == Destination:
            return (current_path, current_move_string)
        
        # Move DOWN if a valid move (not outside puzzle), if not an obstacle in way, and if a shorter route to new pos doesn't already exist
        if valid_move(row+1, col, puzzle_row_max, puzzle_col_max):
            if Board[row+1][col] != '#':
                if current_distance +1 < distances[row+1][col]:
                    distances[row+1][col] = current_distance +1
                    local_move_string = copy.deepcopy(current_move_string)
                    local_move_string += 'D'
                    local_path = copy.deepcopy(current_path)
                    local_path.append((row+1,col))
                    heapq.heappush(pathway_priority_queue, (current_distance+1, (row+1,col), local_path, local_move_string))       
        
        # Move UP if a valid move (not outside puzzle), if not an obstacle in way, and if a shorter route to new pos doesn't already exist
        if valid_move(row-1, col, puzzle_row_max, puzzle_col_max):
            if Board[row-1][col] != '#':
                if current_distance +1 < distances[row-1][col]:
                    distances[row-1][col] = current_distance +1        
                    local_move_string = copy.deepcopy(current_move_string)
                    local_move_string += 'U' 
                    local_path = copy.deepcopy(current_path)
                    local_path.append((row-1,col))
                    heapq.heappush(pathway_priority_queue, (current_distance+1, (row-1,col), local_path, local_move_string))       
        
        # Move RIGHT if a valid move (not outside puzzle), if not an obstacle in way, and if a shorter route to new pos doesn't already exist
        if valid_move(row, col+1, puzzle_row_max, puzzle_col_max):
            if Board[row][col+1] != '#':
                if current_distance +1 < distances[row][col+1]:
                    distances[row][col+1] = current_distance +1   
                    local_move_string = copy.deepcopy(current_move_string)
                    local_move_string += 'R'                        
                    local_path = copy.deepcopy(current_path)
                    local_path.append((row,col+1))
                    heapq.heappush(pathway_priority_queue, (current_distance+1, (row,col+1), local_path, local_move_string))       
        
        # Move LEFT if a valid move (not outside puzzle), if not an obstacle in way, and if a shorter route to new pos doesn't already exist
        if valid_move(row, col-1, puzzle_row_max, puzzle_col_max):
            if Board[row][col-1] != '#':
                if current_distance +1 < distances[row][col-1]:
                    distances[row][col-1] = current_distance +1  
                    local_move_string = copy.deepcopy(current_move_string)
                    local_move_string += 'L'   
                    local_path = copy.deepcopy(current_path)
                    local_path.append((row,col-1))
                    heapq.heappush(pathway_priority_queue, (current_distance+1, (row,col-1), local_path, local_move_string))       


    return None  #if unsolvable puzzle we will never reach the other return statement following ("if current_source == Destination:"")

def valid_move(row, column, board_row, board_column):
    """
    Helper function to see if a future path in the puzzle is a valid one (not outside puzzle with would cause an array index error).
    """
    
    if row < 0 or row > board_row:
        return False
    elif column < 0 or column > board_column:
        return False
    else:
        return True
    

def main():

    # ***example #1 - using puzzle_1 but different starting/ end points***
    # Input: puzzle, (0,2), (2,2)
    # Expected Output: [(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)]
    example_1_source = (0,2)
    example_1_destination = (2,2)

    # ***example #2 - using puzzle_1 but different starting/ end points***
    # Input: puzzle, (0,0), (4,4)
    # Expected Output: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
    example_2_source = (0,0)
    example_2_destination = (4,4)

    # ***example #3 - using puzzle_1 but different starting/ end points***
    # Input: puzzle, (0,0), (4,0)
    # Expected Output: None - as destination outside puzzle bounds
    example_3_source = (0,0)
    example_3_destination = (4,0)

    # ***Gradescope Test #2 - using puzzle_2***
    example_4_source = (0,2)
    example_4_destination = (3,0)

    puzzle_1 = [ 
                ['-', '-', '-', '-', '-'], 
                ['-', '-', '#', '-', '-'], 
                ['-', '-', '-', '-', '-'], 
                ['#', '-', '#', '#', '-'], 
                ['-', '#', '-', '-', '-'] 
                ]

    puzzle_2 = [
                ['-', '-', '-'], 
                ['-', '-', '-'], 
                ['-', '-', '-'], 
                ['-', '-', '-']
                ]


    # large puzzle test
    example_5_source = (0,0)
    example_5_destination = (9,9)
    puzzle_3 = [
                ['-', '-', '-', '-', '#', '-', '-', '-', '-', '-'],
                ['-', '#', '-', '-', '#', '-', '-', '#', '#', '-'],
                ['-', '#', '-', '-', '#', '#', '-', '-', '#', '-'],
                ['-', '#', '#', '-', '-', '-', '-', '-', '#', '#'],
                ['-', '-', '#', '-', '-', '-', '#', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '#', '-', '-', '-', '-'],
                ['#', '-', '-', '-', '-', '#', '-', '#', '-', '-'],
                ['-', '#', '-', '#', '#', '-', '-', '#', '#', '#'],
                ['-', '#', '-', '-', '#', '-', '-', '#', '-', '-'],
                ['-', '-', '-', '-', '#', '-', '-', '-', '-', '-']
                ]

    # shortest path in puzzle_3 = 
                # ['X', 'X', 'X', 'X', '#', '-', '-', '-', '-', '-'],
                # ['-', '#', '-', 'X', '#', '-', '-', '#', '#', '-'],
                # ['-', '#', '-', 'X', '#', '#', '-', '-', '#', '-'],
                # ['-', '#', '#', 'X', 'X', 'X', 'X', 'X', '#', '#'],
                # ['-', '-', '#', '-', '-', '-', '#', 'X', '-', '-'],
                # ['-', '-', '-', '-', '-', '#', 'X', 'X', '-', '-'],
                # ['#', '-', '-', '-', '-', '#', 'X', '#', '-', '-'],
                # ['-', '#', '-', '#', '#', '-', 'X', '#', '#', '#'],
                # ['-', '#', '-', '-', '#', '-', 'X', '#', '-', '-'],
                # ['-', '-', '-', '-', '#', '-', 'X', 'X', 'X', 'X']
                


    # s/b: ([(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)], 'LDDR')
    print(solve_puzzle(puzzle_1, example_1_source, example_1_destination ))  

    # Expected Output: ([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)], 'RRRRDDDD')
    print(solve_puzzle(puzzle_1, example_2_source, example_2_destination ))  

    # Expected Output: None as destination outside bounds
    print(solve_puzzle(puzzle_1, example_3_source, example_3_destination )) 

    # Expected Output: ([(0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0)], 'LLDDD')
    print(solve_puzzle(puzzle_2, example_4_source, example_4_destination )) 

    #  **LARGE PUZZLE TEST**
    # Solution = 'RRRD DDRR RRDD LDDD DRRR'
    print(solve_puzzle(puzzle_3, example_5_source, example_5_destination )) 
    
    
    
if __name__ == '__main__':
    main()
