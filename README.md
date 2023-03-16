# Puzzle-Shortest-Path-CS-325-Portfolio-Project

- This is the Portfolio project for CS 325 - Algorithms, a problem from HW 8 that is allowed to be posted to a public GitHub profile after grades are released.

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



# Description of Algorithm

- An algorithm to solve the problem would involve using a priority queue implemented using a
min heap, and a distances matrix equal in size to the original puzzle. The algorithm would first
push the source onto the heap, then explore all valid neighbors by pushing them to the priority
queue. Each element in the queue can consist of a tuple, with the first element being the
current distance (what the queue will be sorted by), the second being the current cell, the third
being a list of the path of edges, and the fourth being a string with the current moves to reach
the cell position so far, e.g ‐ “RDRD”.

- The algorithm can then use a while loop to run while the heap is not a length of zero, and use
BFS to explore the puzzle until it reaches the destination cell. Once there, the algorithm will
return the shortest path as a list of edges and the move set as a string.

- Each time a neighbor is added to the priority queue, a deep copy is made of the current path list
and move string to reach the new cell. This way each path will have its own separate list of
moves.

- The distances matrix is used so that a neighbor is not added to the priority queue if the distance
to reach it is higher than
