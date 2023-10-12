from random import randint
# Constant that indicates access to the city cannot be reached
NAN = 2147483647
V =7
GENES="ABCDEFG"
# Structure of a GNOME defines the path traversed by the salesman while the fitness value of the path is stored in an integer
class Individual:
	def __init__(self) -> None:
		self.gnome = ""
		self.fitness = 0
		#Python magic method to define less then operator
	def __lt__(self, other):
		return self.fitness < other.fitness
	#Python magic method to define greater then operator
	def __gt__(self, other):
		return self.fitness > other.fitness

# Function to return a mutated GNOME
# Mutated GNOME is a string with a random interchange of two genes to create variation in species
def mutated_gene(gnome):
	while True:
		r = randint(1, V-1)
		r1 = randint(1, V-1)
		if r1 != r:
			temp = gnome[r]
			gnome[r] = gnome[r1]
			gnome[r1] = temp
			break
	return gnome

# Function to return a valid GNOME string required to create the population
def create_gnome(starting_point):
	gnome = []
	gnome.append(starting_point)
	while True:
		if len(gnome) == V:
			gnome.append(starting_point)
			break
		temp = randint(1, V-1)
		if not repeated(gnome, temp):
			gnome.append(temp)

	return gnome

# Function used to check is char repeated in s
def repeated(s, ch):
	for i in range(len(s)):
		if s[i] == ch:
			return True
	return False

# Function to return the fitness value of a gnome.
# The fitness value is the path length of the path represented by the GNOME.
def calculate_fitness(gnome,graph):
	f = 0
	for i in range(len(gnome) - 1):
		if graph[gnome[i]][gnome[i + 1]] == NAN:
			return NAN
		f += graph[gnome[i]][gnome[i + 1]]
	return f

# Function to translate index into city name
def gnome_to_cities(gnome):
	cities=""
	for i in range(len(gnome)):
		if(i < len(gnome)-1):
			cities+= GENES[gnome[i]]+" -> "
		else:
			cities+= GENES[gnome[i]]
	return cities

# Function to help execute genetic TSP solution.
def genetic_tsp(graph,starting_point,pop_size,max_gen):
	population = []
	temp = Individual()

	# Populating the GNOME pool.
	for i in range(pop_size):
		temp.gnome = create_gnome(starting_point)
		temp.fitness = calculate_fitness(temp.gnome,graph)
		population.append(temp)
	population.sort()

	# Iteration to perform population crossing and gene mutation.
	for gen in range(max_gen):
		new_population = []
		for i in range(pop_size):
			p1 = population[i]
			while True:
				new_g = mutated_gene(p1.gnome)
				new_gnome = Individual()
				new_gnome.gnome = new_g
				new_gnome.fitness = calculate_fitness(new_gnome.gnome,graph)
				if new_gnome.fitness <= population[i].fitness:
					new_population.append(new_gnome)
					break
		population = new_population
  
	print("Best Route:", gnome_to_cities(population[0].gnome))
	print("Shortest Distance:", population[0].fitness)
			
if __name__ == '__main__':     
	graph = [
		[0,12,10,NAN,NAN,NAN,12],
		[12,0,8,12,NAN,NAN,NAN],
		[10,8,0,11,3,NAN,9],
		[NAN,12,11,0,11,10,NAN],
		[NAN,NAN,3,11,0,6,7],
		[NAN,NAN,NAN,10,6,0,9],
		[12,NAN,9,NAN,7,9,0],
	]
	genetic_tsp(graph,0,10,100)