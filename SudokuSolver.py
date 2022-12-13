from typing import Tuple, List


def input_sudoku() -> List[List[int]]:
	"""Function to take input a sudoku from stdin and return
	it as a list of lists.
	Each row of sudoku is one line.
	"""
	sudoku= list()
	for _ in range(9):
		row = list(map(int, input().rstrip(" ").split(" ")))
		sudoku.append(row)
	return sudoku

def print_sudoku(sudoku:List[List[int]]) -> None:
	"""Helper function to print sudoku to stdout
	Each row of sudoku in one line.
	"""
	for i in range(9):
		for j in range(9):
			print(sudoku[i][j], end = " ")
		print()


def get_block_num(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
	"""This function takes a parameter position and returns
	the block number of the block which contains the position.
	"""
	# your code goes here
	l1=[[1,2,3],[4,5,6],[7,8,9]]
	for n in range(3):
		if pos[0] in range(3*n+1,3*n+4):
			for k in range(3):
				if pos[1] in range(3*k+1,3*k+4):
					return(l1[n][k])

	return 0

def get_position_inside_block(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
	"""This function takes parameter position
	and returns the index of the position inside the corresponding block.
	"""
	# your code goes here
	l2=[[1,2,3],[4,5,6],[7,8,9]]
	n1=pos[0]%3-1
	n2=pos[1]%3-1
	return(l2[n1][n2])
	return 0


def get_block(sudoku:List[List[int]], x: int) -> List[int]:
	"""This function takes an integer argument x and then
	returns the x^th block of the Sudoku. Note that block indexing is
	from 1 to 9 and not 0-8.
	"""
	# your code goes here
	l3=[[1,2,3],[4,5,6],[7,8,9]]
	l4=[[1,4,7],[2,5,8],[3,6,9]]
	for i in range(3):
		if x in l3[i]:
			j=i
	for o in range(3):
		if x in l4[o]:
			k=o
	m=[]
	for  u  in range(3*j+1,3*j+4):
		for v in range(3*k+1,3*k+4):
			m.append(get_row(sudoku,u)[v-1])
	return(m)
	return list()
	

def get_row(sudoku:List[List[int]], i: int)-> List[int]:
	"""This function takes an integer argument i and then returns
	the ith row. Row indexing have been shown above.
	"""
	# your code goes here
	return(sudoku[i-1])
	return list()

def get_column(sudoku:List[List[int]], x: int)-> List[int]:
	"""This function takes an integer argument i and then
	returns the ith column. Column indexing have been shown above.
	"""
	# your code goes here
	column=[]
	y=x-1
	for i in range(9):
		column.append(sudoku[i][y])
	return(column)

	return list()

def find_first_unassigned_position(sudoku : List[List[int]]) -> Tuple[int, int]:
	"""This function returns the first empty position in the Sudoku. 
	If there are more than 1 position which is empty then position with lesser
	row number should be returned. If two empty positions have same row number then the position
	with less column number is to be returned. If the sudoku is completely filled then return `(-1, -1)`.
	"""
	# your code goes here
	for i in range(9):
		for j in range(9):
			if sudoku[i][j]==0:
				return((i+1,j+1))
	return (-1,-1)

def valid_list(lst: List[int])-> bool:
	"""This function takes a lists as an input and returns true if the given list is valid. 
	The list will be a single block , single row or single column only. 
	A valid list is defined as a list in which all non empty elements doesn't have a repeating element.
	"""
	# your code goes here
	for i in range(len(lst)):
		if lst[i]!=0:
			c=lst.count(lst[i])
			if c>1:
				return(False)
	return True

def valid_sudoku(sudoku:List[List[int]])-> bool:
	"""This function returns True if the whole Sudoku is valid.
	"""
	# your code goes here
	a=1
	while valid_list(get_row(sudoku,a))==True and a<9:
		a+=1
	m=a
	b=1
	while valid_list(get_column(sudoku,b))==True and b<9:
		b+=1
	n=b
	c=1
	while valid_list(get_block(sudoku,c))==True and c<9:
		c+=1
	o=c
	if m==n==o==9:
		return (True)
	else:
		return(False)


def get_candidates(sudoku:List[List[int]], pos:Tuple[int, int]) -> List[int]:
	"""This function takes position as argument and returns a list of all the possible values that 
	can be assigned at that position so that the sudoku remains valid at that instant.
	"""
	# your code goes here
	block=get_block(sudoku,get_block_num(sudoku,pos))
	row=get_row(sudoku,pos[0])
	col=get_column(sudoku,pos[1])
	l5=[1,2,3,4,5,6,7,8,9]
	for f in range(9):
		if block[f] in l5:
			l5.remove(block[f])
		if row[f] in l5:
			l5.remove(row[f])
		if col[f] in l5:
			l5.remove(col[f])
	return(l5)
	return list()

def make_move(sudoku:List[List[int]], pos:Tuple[int, int], num:int) -> List[List[int]]:
	"""This function fill `num` at position `pos` in the sudoku and then returns
	the modified sudoku.
	"""
	# your code goes here
	sudoku[pos[0]-1][pos[1]-1]=num
	return sudoku

def undo_move(sudoku:List[List[int]], pos:Tuple[int, int]):
	"""This function fills `0` at position `pos` in the sudoku and then returns
	the modified sudoku. In other words, it undoes any move that you 
	did on position `pos` in the sudoku.
	"""
	# your code goes here
	sudoku[pos[0]-1][pos[1]-1]=0
	return sudoku

def sudoku_solver(sudoku: List[List[int]]) -> Tuple[bool, List[List[int]]]:
	""" This is the main Sudoku solver. This function solves the given incomplete Sudoku and returns 
	true as well as the solved sudoku if the Sudoku can be solved i.e. after filling all the empty positions the Sudoku remains valid.
	It return them in a tuple i.e. `(True, solved_sudoku)`.

	However, if the sudoku cannot be solved, it returns False and the same sudoku that given to solve i.e. `(False, original_sudoku)`
	"""
	# your code goes here
	def solve(cursudoku):
		x=find_first_unassigned_position(cursudoku)
		if x==(-1,-1):
			return(True)
		for y in get_candidates(cursudoku,x):
			make_move(cursudoku,x,y)
			if solve(cursudoku)==True:
				return(True)
			undo_move(cursudoku,x)
		return(False)
	if solve(sudoku)==True:
		return (True,sudoku)
	


	return (False, sudoku)



if __name__ == "__main__":

	# Input the sudoku from stdin
	sudoku = input_sudoku()

	# Try to solve the sudoku
	possible, sudoku = sudoku_solver(sudoku)

	
	if possible:
		print("Found a valid solution for the given sudoku :)")
		print_sudoku(sudoku)

	else:
		print("The given sudoku cannot be solved :(")
		print_sudoku(sudoku)
