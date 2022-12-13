# SudokuSolver
This Program helps in solving Sudoku .I implemented functions that solve some small functionality, which will come together to create a Sudoku solver.
A Sudoku is a puzzle with 81 numbers which is the form of a 9×9 grid that is broken into rows,columns and blocks with the constraint that each row, column and block has unique elements from 1 to 9 i.e. no row,column or block has a repeating element. Each cell has one number inside it and there is only one valid solution for a Sudoku.
The task is that we will be given a partially filled Sudoku with only one valid solution.Our task will be to solve the Sudoku using backtracking.
Some keywords that we have used -
1. Row: It is a row in the grid, it’s numbering starts from 1 and goes till 9. Refer to Figure 2 for
some more clarity.
2. Column: It is a column in the grid, it’s numbering starts from 1 and goes till 9. Refer to Figure
2 for some more clarity.
3. Block: A Block is a 3 × 3 grid with 9 numbers. Each number inside the grid is unique. A
Sudoku is made of 9 blocks the numbering can be seen in Figure 3. B1 denotes the first block.
4. Position: Denoted by pos in the skeleton code. It defines the position of a cell, it is a pair of
two integers i.e. (row, column). It starts with (1, 1) for the first cell and the last cell will have
position (9, 9). In fig. 1 the value at (2, 2) is 8.
5. List: It is a list of 9 numbers. It can be a block, a row or a column.
A Sudoku is denoted by a list of lists, with each sub-list inside the outer list as a row of the Sudoku.Each position inside the list of list is an integer. If there is a 0 present it means that position is empty
Backtracking is an
algorithmic technique for recursively solving problems by attempting to develop a solution progressively,one piece at a time, and discarding any solutions that do not satisfy the problem’s criteria at any point in time. The function Sudoku_solver() will use this backtracking algorithm.
Important Note:
1. All the indexing is from 1 to 9 but indexing in arrays, tuples and lists is from 0 to 8 so please
make sure you keep this in mind while implementing your code.
2. You are not supposed to print any thing inside the functions.
3. All functions will be graded separately but make sure the basic functions work because the later
ones will call them and if they have an error you will fail the later functions as well.
4. For all of the functions only valid input will be given, no edge-cases or invalid inputs will be
checked.
5. Each function has a level and a list of dependencies which include the functions which have to be
implemented before that particular function.

