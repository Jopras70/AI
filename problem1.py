from collections import deque

# Function to check if the cell is within the bounds of the maze and is a valid path (not a wall).
def valid(x, y, maze):
	return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != "1"

def find_path_bfs(maze):
	start = None
	goal = None

	# Find the start and goal positions in the maze.
	for i in range(len(maze)):
		for j in range(len(maze[0])):
			if maze[i][j] == "S":
				start = (i, j)
			if maze[i][j] == "G":
				goal = (i, j)

	if (start is None or goal is None):
		return []

	visited = set()
	# Queue stores current position and path.
	queue = deque([(start, [])])  

	# Values that added to each currrent axis that will produce a new axis value
	# New axis value is needed to get a posible direction
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]
	while queue:
		(x, y), path = queue.popleft()
		visited.add((x, y))
		# Return the path if the goal is reached.
		if (x, y) == goal:
			return path  
		#Iteration to get posible direction 
		for i in range(4):
			new_x, new_y = x + dx[i], y + dy[i]
			if valid(new_x, new_y, maze) and (new_x, new_y) not in visited:
				new_path = path + [(new_x, new_y)]
				queue.append(((new_x, new_y), new_path))

	return []

if __name__ == '__main__':
	# Maze from the question translate into "1","0","S","G"
	# "1" represent wall
	# "0" represent path that can be passed
	# "S" represent start point
	# "G" represent goal/end point
	maze = [
		["1","1","1","1","1","1","1","1","1","1","1"],
		["1","S","1","0","0","0","0","0","1","0","1"],
		["1","0","1","0","1","1","1","0","1","0","1"],
		["1","0","1","0","1","G","0","0","1","0","1"],
		["1","0","1","0","1","1","1","0","1","0","1"],
		["1","0","1","0","1","0","0","0","0","0","1"],
		["1","0","1","0","1","1","1","1","1","0","1"],
		["1","0","0","0","0","0","1","0","0","0","1"],
		["1","0","1","0","1","1","1","1","1","0","1"],
		["1","0","1","0","0","0","0","0","0","0","1"],
		["1","1","1","1","1","1","1","1","1","1","1"]
	]

	path = find_path_bfs(maze)
	
	if path:
			print("Graph that show path from S to G:")
			for x, y in path:
				if maze[x][y] != "G":
					maze[x][y] = "*" 
			for row in maze:
				print(" ".join(row))
	else:
		print("No path found")


	
		