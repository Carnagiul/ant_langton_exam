import tkinter as tk
from tkinter import *
from tkinter import messagebox
from config import *
from grid_manager_template import *
from grid_tk_template import *
from tkinter.colorchooser import askcolor

window = None
frame = None
canvas = None

window_preview = None
frame_preview = None

ant_count_scale = None

ant_entries = None
ant_labels = None
ant_buttons = None

def update_window():
	global window, frame, canvas, ant_count_scale
	def update():
		if get_game_running():
			for i in range(ant_count_scale.get()):
				ant = get_ant(i)
				if ant['enabled']:
					x = ant['positions']['x']
					y = ant['positions']['y']
					color = '#FFFFFF'
					updated_cell = set_matrice(x, y)
					if updated_cell:
						color = ant['color']
						if canvas.find_withtag('c_'+str(x)+'_'+str(y)) == ():
							canvas.create_rectangle(x * get_size_cell(), y * get_size_cell(), (x + 1) * get_size_cell(), (y + 1) * get_size_cell(), fill=color, tags=('c_'+str(x)+'_'+str(y)))
					else:
						# Remove the existing canvas item with the specified tag
						canvas.delete('c_'+str(x)+'_'+str(y))
					moveAnt(i, updated_cell)
			increase_iteration()
			window.after(100, update)  # Schedule the next update after 100 milliseconds
	update()


def renderMenu():
	global window, frame, canvas, window_preview, frame_preview, ant_count_scale
	
	def ant_count_changed(*args):
		ant_count = ant_count_scale.get()

		if len(ant_entries) > 0:
			while ant_count < len(ant_entries):
				ant_entries.pop().grid_remove()
				ant_labels.pop().grid_remove()
				ant_buttons.pop().grid_remove()
		
		update_count_ants(ant_count)
		debugAnts()
		
		while ant_count > len(ant_buttons):
			i = len(ant_buttons)
			label = tk.Label(window_preview, text=f"Ant {i + 1}")
			label.grid(row=3 + i, column=0, padx=5, pady=5)
			ant_labels.append(label)

			color_entry = tk.Entry(window_preview, width=10)
			color_entry.grid(row=3 + i, column=1, padx=5, pady=5)
			ant_entries.append(color_entry)

			color_button = tk.Button(window_preview, text="Pick Color", command=lambda i=i: pick_color(i))
			color_button.grid(row=3 + i, column=2, padx=5, pady=5)
			ant_buttons.append(color_button)


	def pick_color(i):
		initial_color = ant_entries[i].get()

		# Provide a default color if the entry is empty
		if not initial_color:
			initial_color = "black"

		color = askcolor(initialcolor=initial_color)
		if color[1] is not None:
			ant_entries[i].delete(0, tk.END)
			ant_entries[i].insert(0, color[1])
			update_ant_color(i, color[1])
				
	def options(event=None):
		info = Tk()
		info.title("Options : Langton")

		window_x = 650
		window_y = 300
		x0 = (info.winfo_screenwidth()/2) - (window_x/2)
		y0 = (info.winfo_screenheight()/2) - (window_y/2)

		multiline_text =  """
		- Nombre de fourmis :\n Vous pouvez insérer dans l'entry un nombre de fourmi entre 1 et 4.\n Pour valider le nombre il vous suffit de cliquer sur le bouton 'ok'.\n
		- Couleurs des fourmis :\n Une fois le nombre de fourmis entré, vous pouvez choisir les couleurs des fourmis avec les RadioButtons;\n Si vous souhaitez entrer une couleur autre que celles proposées une entry est disponible.\n 
		- Boutons :\n 'Reinitialiser' : permet de rénitialiser l'ensemble des options des fourmis et détruit le canvas; \n 'stop' : permet d'arrêter la boucle de façon temporaire; \n """

		Label(info, text = "Présentation des différentes options de l'interface :",anchor='center' ).pack(padx = 5, pady = 5)
		Label(info, text = multiline_text, anchor = 'w', justify = 'left').pack(padx = 5, pady = 5)

		info.geometry('%dx%d+%d+%d' % (window_x, window_y, x0, y0))

	def commands(event=None):
		info = Tk()
		info.title("Comandes : Langton")

		window_x = 650
		window_y = 300
		x0 = (info.winfo_screenwidth()/2) - (window_x/2)
		y0 = (info.winfo_screenheight()/2) - (window_y/2)

		multiline_text =  """ - 'barre espace' : lancer et stoper le/les déplacements des fourmis;\n - 'Ctrl-Z' : associé au bouton réinitialiser;\n - 'Ctrl-Q' : associé à la commande quitter;\n - 'Ctrl-A' : lance le menu Jeu;\n - 'Ctrl-W' : lance le menu Options;\n - 'Ctrl-C' : lance le menu Commandes."""
		Label(info, text = "Présentation des différentes commandes de l'interface :", anchor='center' ).pack(padx = 5, pady = 5)
		Label(info, text = multiline_text, anchor = 'nw', justify = 'left').pack(padx = 5, pady = 5)

		info.geometry('%dx%d+%d+%d' % (window_x, window_y, x0, y0))

	def jeu(event=None):
		info = Tk()
		info.title("Commandes : Langton")

		window_x = 650
		window_y = 400
		x0 = (info.winfo_screenwidth()/2) - (window_x/2)
		y0 = (info.winfo_screenheight()/2) - (window_y/2)

		multiline_text =  """ La fourmi de Langton ou Automate cellulaire de Langton est un modèle d'automate cellulaire\n représente un comportement émergent, où des motifs (ici, des cellules) évoluent à partir de règles simples.\n
			- Une position initiale : initialisé de façon aléatoire dans la grille.\n
			- Une direction initiale : initialisé vers le nord mais modifié après chaque déplacement.\n
			- Des règles de déplacement, basées sur la couleur de la cellule sur laquelle elle se trouve :\n
				-> Si la cellule sous la fourmi est blanche, elle change la couleur de la cellule en la couleur de la fourmi,\n
				la fourmi s'oriente vers la droite et avance.\n
				-> Si la cellule sous la fourmi est de couleur, elle change la couleur de la cellule en blanc,\n
				la fourmi s'oriente à gauche et avance.\n
			A partir d'un certain temps, la fourmi génère des motifs complexes comme des Autoroutes, un escalier ou encore un pont. """
		Label(info, text = "Présentation de la fourmi de Langton", anchor='center' ).pack(padx = 5, pady = 5)
		Label(info, text = multiline_text, anchor = 'nw', justify = 'left').pack(padx = 5, pady = 5)

		info.geometry('%dx%d+%d+%d' % (window_x, window_y, x0, y0))
    
	def colors_possibility(event=None):
		
		info = Tk()
		info.title("Couleurs")

		window_x = 800
		window_y = 600
		img1 = PhotoImage(file= 'colors.png')
		#img2 = PhotoImage(file = 'colors_2.png')

		Label(info, text= 'Possibilités de couleurs').grid(row=0, padx=10, pady=5)

		cnv1 = Canvas(info, width= window_x/2, height = window_y, bg= 'blue' )
		#cnv2 = Canvas(info,width= window_x/2, height = window_y, bg='green' )
		cnv1.create_image(0,0, image = img1, anchor = NW)
		#cnv2.create_image(0,0, image = img2, anchor = NW)

		cnv1.grid(row=1,column=0)
		#cnv2.grid(row=1, column=1)

		x0 = (info.winfo_screenwidth()/2) - (window_x/2)
		y0 = (info.winfo_screenheight()/2) - (window_y/2)

		info.geometry('%dx%d+%d+%d' % (window_x, window_y, x0, y0))

	def quitter(event = None):
		global window
		if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter l'automate fourmi de Langton?"):
			window_preview.destroy()
			window.destroy()

	def start():
		if not get_game_running():
			for i in range(ant_count_scale.get()):
				color = ant_entries[i].get()
				if color:
					update_ant_color(i, color)
				else:
					messagebox.showerror("Erreur", "Veuillez choisir une couleur pour la fourmi " + str(i + 1))
					return
				
			if messagebox.askokcancel("Start", "Voulez-vous vraiment lancer le jeu?"):
				start_game()
				start.config(text="Stop", command=stop)
				update_window()
		else:
			if messagebox.askokcancel("Stop", "Voulez-vous vraiment stopper le jeu?"):
				stop_game()
				start.config(text="Start", command=start)
	
	def stop():
		if messagebox.askokcancel("Stop", "Voulez-vous vraiment stopper le jeu?"):
			stop_game()
			start.config(text="Start", command=start)
	
	def reset():
		if messagebox.askokcancel("Reset", "Voulez-vous vraiment réinitialiser le jeu?"):
			reset_game()
			start.config(text="Start", command=start)
	
	menubar = Menu(window_preview)
	menubar.add_command(label = "Jeu", command=jeu)
	menubar.add_command(label="Options", command=options)
	menubar.add_command(label="Commandes", command=commands)
	menubar.add_command(label="Couleurs", command= colors_possibility)
	menubar.add_command(label="Quitter", command=quitter)

	window_preview.bind('<Control-w>', options)
	window_preview.bind('<Control-c>', commands)
	window_preview.bind('<Control-q>', quitter)
	window_preview.bind('<Control-a>', jeu)

	row = tk.LabelFrame(window_preview, width=300, height=100, text='Ant Count')
	row.grid(row=1, column=0)
	ant_count_scale = Scale(window_preview, from_=1, to=4, orient="horizontal", resolution=1, command=ant_count_changed)
	ant_count_scale.grid(row=2, column=0)

	start = tk.Button(window_preview, text="Start", command=start)
	start.grid(row=0, column=0, padx=5, pady=5)

	reset = tk.Button(window_preview, text="Reset", command=reset)
	reset.grid(row=0, column=1, padx=5, pady=5)

	# Store the dynamically created entry widgets and labels
	ant_entries = []
	ant_labels = []
	ant_buttons = []

	window_preview.config(menu = menubar)
	ant_count_changed()


def initWindow():
	global window, frame, canvas, window_preview, frame_preview

	window = Tk()
	window.title('Langton')
	window_preview = Tk()
	window_preview.title('Commands')


	grid = create_random_grid_lc(get_width_grid(), get_height_grid(), [0,1])
	canvas = custom_grid_canvas(window, grid, get_size_cell(), margin=10, gutter=2, show_vals=False, outline=False)

	width = int(canvas['width'])
	height = int(canvas['height'])

	ws = window.winfo_screenwidth()
	hs = window.winfo_screenheight()

	x0 = (ws/2) - (width/2)
	y0 = (hs/2) - (height/2)

	window.geometry('%dx%d+%d+%d' % (width, height, x0, y0))
	window.resizable(False, False)

	window_preview.geometry('%dx%d+%d+%d' % (800, height, 200, y0))
	window_preview.resizable(False, False)

	canvas.grid(row=0, column=0, sticky='nsew')

	frame = tk.Frame(window,bg='red')
	frame.grid(row=0, column=1, sticky='nsew')

	frame_preview = tk.Frame(window_preview,bg='red')
	frame_preview.grid(row=0, column=1, sticky='nsew')
	update_count_ants(1)
	renderMenu()
	window.mainloop()
	window_preview.mainloop()
