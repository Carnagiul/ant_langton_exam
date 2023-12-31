import random

iteration = 0
ant_count = 1
matrice = [];

size_cell = 0

width_grid = 0
max_width_grid = 1000
min_width_grid = 50

height_grid = 0
max_height_grid = 1000
min_height_grid = 50

min_zoom_x = 0
max_zoom_x = 1000

min_zoom_y = 0
max_zoom_y = 0

game_running = False

ants = []

# def increase_zoom(x, y):
	#need to check first if x is nearest of min_zoom_x or max_zoom_x
	#need to check first if y is nearest of min_zoom_y or max_zoom_y
	#if max_zoom_x - min_zoom_x < 10xsize_cell then return
	

def get_max_zoom_x():
	global max_zoom_x
	return max_zoom_x

def get_min_zoom_x():
	global min_zoom_x
	return min_zoom_x

def get_max_zoom_y():
	global max_zoom_y
	return max_zoom_y

def get_min_zoom_y():
	global min_zoom_y
	return min_zoom_y

def set_max_zoom_x(new_zoom_x):
	global max_zoom_x
	max_zoom_x = new_zoom_x

def set_min_zoom_x(new_zoom_x):
	global min_zoom_x
	min_zoom_x = new_zoom_x

def set_max_zoom_y(new_zoom_y):
	global max_zoom_y
	max_zoom_y = new_zoom_y

def set_min_zoom_y(new_zoom_y):
	global min_zoom_y
	min_zoom_y = new_zoom_y

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

	# Define the size of the cell based on the size of the grid

	# if 50 <= width_grid <75 and 50 <= height_grid <75 :
	# 	size_cell = 10
	# elif 75 <= width_grid <130 and 75<= height_grid <130 :
	# 	size_cell = 5
	# elif height_grid< 100 and width_grid>100 :
	# 	size_cell = 8
	# else :
	# 	size_cell = 3
	define_new_matrix()

def set_ant_count(new_ant_count):
	global ant_count
	ant_count = new_ant_count

def get_ant_count():
    global ant_count
    return ant_count

def define_new_matrix():
	global matrice, width_grid, height_grid
	
	set_min_zoom_x(0)
	set_min_zoom_y(0)
	set_max_zoom_x(width_grid)
	set_max_zoom_y(height_grid)
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

def create_new_ant(id):
	global ants, max_width_grid, max_height_grid
	ant = {
		"label" : "Ant " + str(id),
		"color" : "red",
		"enabled": True,
		"positions": {
			"x": random.randint(0, width_grid),
			"y": random.randint(0, height_grid),
			"yaw": 0,
		}
	}
	ants.append(ant)
	return ant

def check_ant(id):
	global ants
	if ants[id]['positions']['x'] < 0:
		ants[id]['positions']['x'] = get_width_grid() - 1
	elif ants[id]['positions']['x'] >= get_width_grid():
		ants[id]['positions']['x'] = 0
	if ants[id]['positions']['y'] < 0:
		ants[id]['positions']['y'] = get_height_grid() - 1
	elif ants[id]['positions']['y'] >= get_height_grid():
		ants[id]['positions']['y'] = 0
	if ants[id]['positions']['yaw'] < 0:
		ants[id]['positions']['yaw'] = 3
	elif ants[id]['positions']['yaw'] >= 4:
		ants[id]['positions']['yaw'] = 0
	


def moveAnt(id, updated_cell):
	global ants

	old_x = ants[id]['positions']['x']
	old_y = ants[id]['positions']['y']
	old_yaw = ants[id]['positions']['yaw']
	if updated_cell:
		ants[id]['positions']['yaw'] = ants[id]['positions']['yaw'] + 1
	else:
		ants[id]['positions']['yaw'] = ants[id]['positions']['yaw'] - 1
	check_ant(id)
	if ants[id]['positions']['yaw'] == 0:
		ants[id]['positions']['x'] = ants[id]['positions']['x'] + 1
	elif ants[id]['positions']['yaw'] == 1:
		ants[id]['positions']['y'] = ants[id]['positions']['y'] - 1
	elif ants[id]['positions']['yaw'] == 2:
		ants[id]['positions']['x'] = ants[id]['positions']['x'] - 1
	elif ants[id]['positions']['yaw'] == 3:
		ants[id]['positions']['y'] = ants[id]['positions']['y'] + 1

	check_ant(id)

	next_x = ants[id]['positions']['x']
	next_y = ants[id]['positions']['y']
	next_yaw = ants[id]['positions']['yaw']

	print({old_x, old_y, old_yaw}, {next_x, next_y, next_yaw})	

def get_ant(i):
	global ants
	return ants[i]

def debugAnts():
	global ants
	print(ants)

def update_ant_color(id, color):
	global ants
	ants[id]['color'] = color
	print(ants[id], color, ants[id]['color'])

def update_count_ants(new_count):
	global ants
	while len(ants) > new_count:
		ants.pop()
	while new_count > len(ants):
		create_new_ant(len(ants))

def get_game_running():
	global game_running
	return game_running

def start_game():
	global game_running
	game_running = True

def stop_game():
	global game_running
	game_running = False

def reset_counter():
	global iteration
	iteration = 0

def reset_matrice():
	define_new_matrix()

def reset_game():
	stop_game()
	reset_counter()
	reset_matrice()
