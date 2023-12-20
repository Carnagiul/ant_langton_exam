avaible_colors = [
	"red", "green", "blue", "yellow"
];

iteration = 0
ant_count = 1
matrice = [];

size_cell = 0

width_grid = 0
max_width_grid = 150
min_width_grid = 50

height_grid = 0
max_height_grid = 150
min_height_grid = 50

ants = [
	{
		"label" : "Ant 1",
		"color" : "red",
		"enabled": True,
		"positions": {
			"x": -1,
			"y": -1,
		}
	},
	{
		"label" : "Ant 2",
		"color" : "green",
		"enabled": False,
		"positions": {
			"x": -1,
			"y": -1,
		}
	},
	{
		"label" : "Ant 3",
		"color" : "blue",
		"enabled": False,
		"positions": {
			"x": -1,
			"y": -1,
		}
	},
	{
		"label" : "Ant 4",
		"color" : "yellow",
		"enabled": False,
		"positions": {
			"x": -1,
			"y": -1,
		}
	},
]


def set_width_grid(new_width):
    global width_grid
    width_grid = new_width

def set_height_grid(new_height):
    global height_grid
    height_grid = new_height

def get_width_grid():
    global width_grid
    return width_grid

def get_height_grid():
    global height_grid
    return height_grid

def verify_grid():
	global size_cell, width_grid, height_grid
	if width_grid < min_width_grid :
		width_grid = min_width_grid
	if width_grid > max_width_grid :
		width_grid = max_width_grid
	if height_grid < min_height_grid :
		height_grid = min_height_grid
	if height_grid > max_height_grid :
		height_grid = max_height_grid

	if 50 <= width_grid <75 and 50 <= height_grid <75 :
		size_cell = 10
	elif 75 <= width_grid <130 and 75<= height_grid <130 :
		size_cell = 5
	elif height_grid< 100 and width_grid>100 :
		size_cell = 8
	else :
		size_cell = 3
	define_new_matrix()

def set_ant_count(new_ant_count):
	global ant_count
	ant_count = new_ant_count

def get_ant_count():
    global ant_count
    return ant_count

def define_new_matrix():
    global matrice, width_grid, height_grid

    # Define a new matrix based on width_grid and height_grid
    matrice = [[False for _ in range(width_grid)] for _ in range(height_grid)]

def increase_iteration():
	global iteration
	return ++iteration

def get_iteration():
	global iteration
	return iteration

def get_matrice():
    global matrice
    return matrice


def set_matrice(x, y):
	global matrice
	#print(x, y)
	matrice[y][x] = not matrice[y][x]
	return matrice[y][x]

def get_size_cell():
	global size_cell
	return size_cell

def set_size_cell(new_size):
	global size_cell
	size_cell = new_size

def get_avaible_color():
	global avaible_colors
	return avaible_colors

def create_new_ant(id):
	return {
		"label" : "Ant " + str(id),
		"color" : "red",
		"enabled": True,
		"positions": {
			"x": -1,
			"y": -1,
		}
	},

def update_count_ants(new_count):
	global ants
	ants.pop(len(ants) - new_count)
	print(len(ants))
