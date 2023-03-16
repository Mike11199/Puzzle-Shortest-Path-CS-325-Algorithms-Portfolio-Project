# Puzzle-Shortest-Path-CS-325-Portfolio-Project

- This is the Portfolio project for CS 325 - Algorithms, a problem from the course that is allowed to be posted to a public GitHub profile after grades are released.

# Description of Problem

![image](https://user-images.githubusercontent.com/91037796/225496432-37989d16-cba0-4893-a606-d61324f4bd9d.png)


```js
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

```



![image](https://user-images.githubusercontent.com/91037796/225496467-280148b0-164c-417a-8a10-13b5f3d82b5a.png)



# Description of Algorithm (Solution)

- My implementation of an algorithm to solve this problem involves using a priority queue backed with a min heap data structure, and a distances matrix equal in size to the original puzzle. The distances matrix is initailized with all distances set to infinity, similar to djikstra's algorithm.  The algorithm first pushes the source onto the heap/priority queue, then explores all valid neighbors by pushing them to the priority
queue as well. 

![image](https://user-images.githubusercontent.com/91037796/225496958-e6eff3cf-fee1-4bc6-a863-4391af3fde24.png)


- Each element in the queue can consist of a tuple, with the first element being the
current distance (what the queue will be sorted by), the second being the current cell, the third
being a list of the path of edges, and the fourth being a string with the current moves to reach
the cell position so far, e.g ‐ “RDRD”.

```python
    # create list/array to be used as the underlying data structure of the min-heap priority queue     
    pathway_priority_queue = []          
    
    # push tuple of the start distance, source cell, path of edges, and move_string to priority queue
    heapq.heappush(pathway_priority_queue, (0, Source, path, move_string))    
```

- The algorithm can then use a while loop to run while the heap is not a length of zero, and use
BFS to explore the puzzle until it reaches the destination cell. Once there, the algorithm will
return the shortest path as a list of edges and the move set as a string.

- Each time a neighbor is added to the priority queue, a deep copy is made of the current path list
and move string to reach the new cell. This way each path will have its own separate list of
moves.

- The distances matrix is used so that a neighbor is not added to the priority queue if the distance
to reach it is higher than an already explored distance. This way, cycles and inefficient paths are
terminated early.

- For example, the solution to the above puzzle is the following path generated by the algorithm:

```js
output =(
[(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), 
(3, 7), (4, 7), (5, 7), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6), (9, 7), (9, 8), (9, 9)], 
'RRRDDDRRRRDDLDDDDRRR')
```
