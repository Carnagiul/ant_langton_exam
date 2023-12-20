import tkinter as tk
from tkinter import *
from tkinter import messagebox, PhotoImage
from grid_manager_template import *
from grid_tk_template import *

# interfaces
def fenetre():
    """ initialisation de la taille de la grille par l'utilisateur """
    window = Tk()
    window.title('Langton grid')
    width = 500
    height = 200

    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x0 = (ws/2) - (width/2)
    y0 = (hs/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x0, y0))
    window.resizable(False, False)

    main_label = Label(window, text = 'Choississez les dimmensions de la grille', font= ('arial', 10), justify='center', anchor= 'n' )
    main_label.grid(row=0, column=1, padx=5, pady = 5)

    lbl1 = Label(window, text = 'Longueur de la grille : ')
    lbl2 = Label(window, text = 'Hauteur de la grille : ')
    lbl1.grid(row = 1, column= 0)
    lbl2.grid(row = 2, column= 0, pady=2)

    width_scale = Scale(window, from_=50, to=150, orient="horizontal", variable = IntVar(), resolution = 5)
    width_scale.grid(row = 1, column=1)

    height_scale = Scale(window, from_=50, to=150, orient="horizontal", variable = IntVar(),resolution = 5)
    height_scale.grid(row=2, column=1, pady = 2)

    def valider():
        global width_grid, height_grid

        width_grid = width_scale.get()
        height_grid = height_scale.get()
        width_scale.config(state = 'disabled')
        height_scale.config(state= 'disabled')
        window.destroy()

    Button(window, text = 'Valider', command=valider).grid(row=3, column = 2, sticky='se')

    window.mainloop()

def limit_size_cell():
    global size_cell, width_grid, height_grid

    if 50<= width_grid <75 and 50<= height_grid <75 :
        size_cell = 10
    elif 75 <= width_grid <130 and 75<= height_grid <130:
        size_cell = 5
    
    elif height_grid< 100 and width_grid>100:
        size_cell = 8
    else:
        size_cell = 3
    
def render():
    
    # ----------------- Positionnement de la fenetre + canva -----------------
    width = int(canvas['width']) + 400
    height = int(canvas['height'])

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    x0 = (ws/2) - (width/2)
    y0 = (hs/2) - (height/2)

    root.geometry('%dx%d+%d+%d' % (width, height, x0, y0))
    root.resizable(False, False)

    canvas.grid(row=0, column=0, sticky='nsew')
    
    # ----------------- Frame principale -----------------

    main_frm = tk.Frame(root,height= height, bg='aliceblue')
    main_frm.grid(row=0, column=1, sticky='nsew')

    # ----------------- MenuBar -----------------
    def options(event=None):
        info = Toplevel()
        info.title("Options : Langton")

        window_x = 650
        window_y = 300
        x0 = (info.winfo_screenwidth()/2) - (window_x/2)
        y0 = (info.winfo_screenheight()/2) - (window_y/2)

        multiline_text =  """
        - Nombre de fourmis :\n
            Vous pouvez insérer dans l'entry un nombre de fourmi entre 1 et 4.\n Pour valider le nombre il vous suffit de cliquer sur le bouton 'ok'.\n
        - Couleurs des fourmis :\n
            Une fois le nombre de fourmis entré, vous pouvez choisir les couleurs des fourmis avec les RadioButtons;\n Si vous souhaitez entrer une couleur autre que celles proposées une entry est disponible.\n 
        - Boutons :\n
            'Valider' : valide l'ensemble des caractéristiques entrées au préalable ;
            'Lancer' : lance le développement de la fourmi dans l'interface ;
            'Reinitialiser' : permet de rénitialiser l'ensemble des options des fourmis et détruit le canvas ;
            'stop' : permet d'arrêter la boucle de façon temporaire. \n """

        Label(info, text = "Présentation des différentes options de l'interface :",anchor='center' ).pack()
        Label(info, text = multiline_text, anchor = 'w', justify = 'left').pack(padx = 5, pady = 5)

        info.geometry('%dx%d+%d+%d' % (window_x, window_y, x0, y0))
        info.mainloop()

    def commands(event=None):
        info = Toplevel()
        info.title("Comandes : Langton")

        window_x = 650
        window_y = 300
        x0 = (info.winfo_screenwidth()/2) - (window_x/2)
        y0 = (info.winfo_screenheight()/2) - (window_y/2)

        multiline_text =  """ 
        - 'barre espace' : lancer et stoper le/les déplacements des fourmis ;\n
        - 'Ctrl-Z' : associé au bouton réinitialiser ;\n
        - 'Ctrl-Q' : associé à la commande quitter ;\n
        - 'Ctrl-A' : lance le menu Jeu ;\n
        - 'Ctrl-W' : lance le menu Options ;\n
        - 'Ctrl-C' : lance le menu Commandes ;\n
        - 'Ctrl-S' : lance le menu Couleurs."""

        Label(info, text = "Présentation des différentes commandes de l'interface :", anchor='center' ).pack(padx = 5, pady = 5)
        Label(info, text = multiline_text, anchor = 'nw', justify = 'left').pack(padx = 5, pady = 5)

        info.geometry('%dx%d+%d+%d' % (window_x, window_y, x0, y0))
        info.mainloop()

    def jeu(event=None):
        info = Toplevel()
        info.title("Commandes : Langton")

        window_x = 650
        window_y = 400
        x0 = (info.winfo_screenwidth()/2) - (window_x/2)
        y0 = (info.winfo_screenheight()/2) - (window_y/2)

        multiline_text =  """ La fourmi de Langton ou Automate cellulaire de Langton est un modèle d'automate cellulaire\n représentant un comportement émergent, où des motifs (ici, des cellules) évoluent à partir de règles simples.\n
            - Une position initiale : initialisé de façon aléatoire dans la grille.\n
            - Une direction initiale : initialisé vers le nord mais modifié après chaque déplacement.\n
            - Des règles de déplacement, basées sur la couleur de la cellule sur laquelle elle se trouve :\n
                -> Si la cellule sous la fourmi est blanche, elle change la couleur de la cellule en la couleur de la fourmi,\n
                la fourmi s'oriente vers la droite et avance.\n
                -> Si la cellule sous la fourmi est de couleur, elle change la couleur de la cellule en blanc,\n
                la fourmi s'oriente à gauche et avance.\n
            A partir d'un certain temps, la fourmi génère des motifs complexes comme des Autoroutes,
            un escalier ou encore un pont. """
        
        Label(info, text = "Présentation de la fourmi de Langton", anchor='center' ).pack(padx = 5, pady = 5)
        Label(info, text = multiline_text, anchor = 'nw', justify = 'left').pack(padx = 5, pady = 5)

        info.geometry('%dx%d+%d+%d' % (window_x, window_y, x0, y0))
        info.mainloop()

    def colors_possibility(event=None):
        info = Toplevel()
        info.title("Couleurs")

        window_x = 600
        window_y = 630

        x0 = (info.winfo_screenwidth()/2) - (window_x/2)
        y0 = (info.winfo_screenheight()/2) - (window_y/2)

        info.geometry('%dx%d+%d+%d' % (window_x, window_y, x0, y0))
        Label(info, text= 'Possibilités de couleurs').grid(row=0, padx=5, pady=5)
        
        img = PhotoImage(file= 'colors.png')
        cnv = Canvas(info, width=600,height= 600,bg= 'white' )
        cnv.create_image(0,0, image = img, anchor = NW)
        cnv.grid(row=1,column=0)

        info.mainloop()

    def quitter(event = None):
        if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter l'automate fourmi de Langton?"):
            root.destroy()

    menubar = Menu(root)
    menubar.add_command(label = "Jeu", command=jeu)
    menubar.add_command(label="Options", command=options)
    menubar.add_command(label="Commandes", command=commands)
    menubar.add_command(label="Couleurs", command=colors_possibility)
    menubar.add_command(label="Quitter", command=quitter)

    root.config(menu = menubar)

    # ------------------- LabelFrames -------------------
    # compteur
    lbl_compteur = tk.LabelFrame(main_frm, width= 55, height= 50, text = 'Compteur')
    lbl_compteur.grid(row=1, column=0, sticky= 'nsew', columnspan=2)
    lbl_compteur.columnconfigure(0,weight=1)

    # nombre de fourmis à entrer
    lbl_nb_fourmis = tk.LabelFrame(main_frm, width= 55, height= 50, text = 'Nombre de fourmis')
    lbl_nb_fourmis.grid(row=2, column=0, sticky= 'nsew', columnspan=2)
    lbl_nb_fourmis.columnconfigure(0,weight=1)

    # choix des couleurs
    lbl_cell_color = tk.LabelFrame(main_frm, width= 55, height= 50, text = 'Couleurs des fourmis')
    lbl_cell_color.grid(row=3, column=0, sticky= 'nsew', columnspan=2)
    lbl_cell_color.columnconfigure(0,weight=1)

    # initialisation des labels des choix de couleurs
    color_labels = ['1', '2', '3', '4']
    lbl_color_fourmi = []
    
    # création des labels de couleurs
    for i, lbl in enumerate(color_labels):

        lbl_fourmis_color = tk.LabelFrame(lbl_cell_color, width= 55, height= 50, text = 'Couleurs de fourmis '+str(lbl) )
        lbl_fourmis_color.grid(row=i, column=0, sticky= 'nsew',columnspan=2)

        lbl_color_fourmi.append(lbl_fourmis_color)

    # ------------------- Label / Entry -------------------
    
    compteur = Label(lbl_compteur, font=FONT['text_val'], text= str(cpt), justify='center')
    compteur.grid(row=0, column=0, columnspan=1)

    # label indiquant le nombre à entrer
    l= Label(lbl_nb_fourmis, text= 'Entrez un nombre de fourmis : ', font=FONT['text_val'])
    l.grid(row=0, column=0)

    # initialisation de l'entry
    entry_val = tk.IntVar()
    entry_val.set('1')

    entry_nb_fourmis = Entry(lbl_nb_fourmis, textvariable=entry_val)
    entry_nb_fourmis.grid(row=0, column=1)

    # ------------------- RadioButtons -------------------
        
    # initialisation des valeurs
    radiobuttons = []
    entries = []
    colors = ['red', 'blue', 'green', 'couleur : ']

    color_f1 = tk.StringVar()
    color_f2 = tk.StringVar()
    color_f3 = tk.StringVar()
    color_f4 = tk.StringVar()
    
    color_f1.set('red')
    color_f2.set('red')
    color_f3.set('red')
    color_f4.set('red')

    # création des différents RadioButtons selon la couleur indiqué par 'colors'
    for i, color in enumerate(colors):

        # ----------- Fourmi 1 -----------
        rb_1 = tk.Radiobutton(lbl_color_fourmi[0], variable=color_f1, text=color, value=color, command=lambda color=color_f1: color_fourmi(color, 0), state='disabled')
        rb_1.grid(row=0, column=i, padx=2, pady=2)
        
        # ----------- Fourmi 2 -----------
        rb_2 = tk.Radiobutton(lbl_color_fourmi[1], variable=color_f2, text=color, value=color, command=lambda color=color_f2: color_fourmi(color, 1), state='disabled')
        rb_2.grid(row=0, column=i, padx=2, pady=2)

        # ----------- Fourmi 3 -----------
        rb_3 = tk.Radiobutton(lbl_color_fourmi[2], variable=color_f3, text=color, value=color, command=lambda color=color_f3: color_fourmi(color, 2), state='disabled')
        rb_3.grid(row=0, column=i, padx=2, pady=2)

        # ----------- Fourmi 4 -----------
        rb_4 = tk.Radiobutton(lbl_color_fourmi[3], variable=color_f4, text=color, value=color, command=lambda color=color_f4: color_fourmi(color, 3), state='disabled')
        rb_4.grid(row=0, column=i, padx=2, pady=2)

        if color == 'couleur : ':

            # ----------- Fourmi 1 -----------
            rb_1 = tk.Radiobutton(lbl_color_fourmi[0], variable=color_f1, text=color, value=color, command=lambda color=color_f1: color_entry(color, 0), state='disabled')
            rb_1.grid(row=0, column=i, padx=2, pady=2)

            entry_color_cell_1 = Entry(lbl_color_fourmi[0], width = 18,state='disabled')
            entry_color_cell_1.grid(row=0,column=i+1)

            # ----------- Fourmi 2 -----------
            rb_2 = tk.Radiobutton(lbl_color_fourmi[1], variable=color_f2, text=color, value=color, command=lambda color=color_f2: color_entry(color, 1), state='disabled')
            rb_2.grid(row=0, column=i, padx=2, pady=2)

            entry_color_cell_2 = Entry(lbl_color_fourmi[1], width = 18, state='disabled')
            entry_color_cell_2.grid(row=0,column=i+1)

            # ----------- Fourmi 3 -----------
            rb_3 = tk.Radiobutton(lbl_color_fourmi[2], variable=color_f3, text=color, value=color, command=lambda color=color_f3: color_entry(color, 2), state='disabled')
            rb_3.grid(row=0, column=i, padx=2, pady=2)

            entry_color_cell_3 = Entry(lbl_color_fourmi[2], width = 18,state='disabled')
            entry_color_cell_3.grid(row=0,column=i+1)

            # ----------- Fourmi 4 -----------
            rb_4 = tk.Radiobutton(lbl_color_fourmi[3], variable=color_f4, text=color, value=color, command=lambda color=color_f4: color_entry(color, 3), state='disabled')
            rb_4.grid(row=0, column=i, padx=2, pady=2)

            entry_color_cell_4 = Entry(lbl_color_fourmi[3], width = 18, state='disabled')
            entry_color_cell_4.grid(row=0,column=i+1)

            entries.append((entry_color_cell_1,entry_color_cell_2, entry_color_cell_3, entry_color_cell_4))

        radiobuttons.append((rb_1, rb_2, rb_3, rb_4))
    
    # ------------------- Fonctions interactives -------------------
    # Variable pour suivre l'état du bouton
    bouton_etat = tk.StringVar()
    bouton_etat.set("Arrêter")

    def valider():
        """ valide l'ensemble des entrées indiqués par l'utilisateur """
        global check
        check = True
        state_radiobtn()
        startbtn['state'] = 'active'
    
    def start():
        """ lance le programme de déplacement des fourmis"""
        global after_id
        btn_valid.config(state= 'disabled')

        # after_id est nécéssaire pour pouvoir stopper le programme
        after_id = dep_fourmi()
    def stop():
        """ met en pause le déplacement de la fourmi"""
        global after_id
        root.after_cancel(after_id)
        after_id = None
    
    def gestion_barre_espace(event):
        
        if event.keysym == 'space' and startbtn['state'] == 'active':
            if bouton_etat.get() == "Démarrer":
                stop()
                bouton_etat.set("Arrêter")
            else:
                start()
                bouton_etat.set("Démarrer")

    def reinitialiser(event=None):
        global check
        check = True
        state_radiobtn()
        entry_nb_fourmis.configure(state='normal')
        btnok.configure(state= 'normal')
        
    def limit_entry():
        """ vérifie la valeur de l'Entry, limité à un intervalle de 1 à 4 """

        global nb_fourmis, check
        nb_fourmis = int(entry_nb_fourmis.get())
        check = False

        if nb_fourmis <= 4 and nb_fourmis >0:
            entry_nb_fourmis['bg']='white'
            entry_nb_fourmis.config(state='disabled')
            btnok['state'] = 'disabled'
            btn_valid['state'] = 'active' 
            fourmis_pos(nb_fourmis)
            state_radiobtn()

        else:
            entry_nb_fourmis['bg']='salmon'
            messagebox.showerror('Erreur', "Le nombre de fourmis n'est pas adapté.\nVous pouvez entrer un nombre maximal de 4 fourmis.")
            entry_val.set("")

    def state_radiobtn():
        """ modifie l'état des radioButtons selon le nombre entré dans l'Entry """
        global nb_fourmis, check
        state = 'disabled' if check == True else 'normal'
        
        for rb in radiobuttons:
            for i in range(nb_fourmis):
                for entry in entries:
                    
                    if len(radiobuttons) > nb_fourmis:
                            rb[i].config(state= state)
                            entry[i].config(state= state)
                    else:
                        rb[i].config(state= state)
                        entry[i].config(state=state)
                    
    def compteur_label():
        """ compte le nombre de déplacements des fourmis """
        compteur.config(text=str(cpt))

# -----------------------------------------------------------------------------------------------------------------------------------------------
    # développement de la fourmi

    def fourmis_pos(nb):
        """ récupère les positions et les couleurs des fourmis.
        Les positions sont choisies de façon aléatoires dans le canvas, les couleurs sont entrées par l'utilisateur via les RadioButtons """
        global ants, ant_colors
        ant_colors = {label: 'red' for label in range(nb)}
        ants = [{'label' : label, 'position' : get_pos(grid, random.randint(0, len(grid) - 1), random.randint(0, len(grid[0]) - 1)), 'orientation': 0} for label in range(nb)]
        #print(ants)

    def droite(orientation):
        """ oriente la fourmi vers sa droite"""
        orientation = (orientation+1)%4
        return orientation

    def gauche(orientation):
        """ oriente la fourmi vers sa gauche"""
        orientation = (orientation-1)%4
        return orientation

    def deplacer(orientation, posx, posy):
        """ deplace la fourmi selon son orientation """
        delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        return neighbour(grid, posx, posy, delta[orientation], tore=True)

    def color_fourmi(color, label):
        """ récupere les couleurs des différentes fourmis des RadioButtons """
        global ant_colors
        ant_colors[label] = color.get()
    
    def color_entry(color, label):
        """ récupère les couleurs des radioButton avec des entries emet un message d'erreur si la valeur entrée n'est pas une couleur """
        global ant_colors
        color= entries[0][label].get()

        try: # test si la couleur est correcte
            tk.Label(root, text="", bg=color)
            entries[0][label].config(state='disabled')
            ant_colors[label] = color

        except tk.TclError: # sinon affiche une erreur

            entries[0][label].delete(0, END)
            entries[0][label].config(bg = 'salmon')
            color_var = color_f1 if label == 0 else (color_f2 if label == 1 else (color_f3 if label == 2 else color_f4))
            color_var.set('red')
            messagebox.showerror('Erreur', " Aucune couleur n'a été entré \n Veuillez cliquer sur le RadioButton après avoir entré votre couleur.")
            
    def tore(posx, posy):
        """ récupère la position de la fourmi donné et retourne la position en faisant du canvas un tore """
        posx = (posx + int(get_lines_columns(canvas)[0]))%int(get_lines_columns(canvas)[0])
        posy = (posy + int(get_lines_columns(canvas)[1]))%int(get_lines_columns(canvas)[1])
        return posx, posy
    
    def dep_fourmi():
        """ permet de déplacer la fourmi et de l'afficher dans le canva """
        global canvas, ants, cpt, ant_colors, after_id
        
        for ant in ants:

            label = ant['label']

            posx_fourmi, posy_fourmi = ant['position']
            print('label : ', label,'position : ',posx_fourmi, posy_fourmi)

            posx_fourmi, posy_fourmi = tore(posx_fourmi, posy_fourmi)

            set_cell_text(canvas, posx_fourmi, posy_fourmi, ' ')
            
            if get_color_cell(canvas, posx_fourmi, posy_fourmi) == COLORS['bg']:
                set_color_cell(canvas, posx_fourmi, posy_fourmi, ant_colors[label])
                ant['orientation'] = droite(ant['orientation'])

            else:
                set_color_cell(canvas, posx_fourmi, posy_fourmi, COLORS['bg'])
                ant['orientation'] = gauche(ant['orientation'])

            # position actuelle de la fourmi
            posx_bis, posy_bis = deplacer(ant['orientation'],posx_fourmi, posy_fourmi)
            posx_bis, posy_bis = tore(posx_bis, posy_bis)

            # définition de la position pour le prochain déplacement
            ant['position'] = posx_bis, posy_bis
            set_cell_text(canvas, posx_bis, posy_bis, '¤')

        cpt +=1
        compteur_label()
        after_id = root.after(10, dep_fourmi)

    # ------------------- Buttons -------------------

    # valide l'entry
    btnok = tk.Button(lbl_nb_fourmis, width=4, height=2, text='ok', bg='light grey', command=limit_entry)
    btnok.grid(row=0, column=2, padx=2, pady=2, sticky='nsew')

    # lance les fourmis
    startbtn = tk.Button(main_frm, width=55, height=5, text='lancer', bg='grey', command=start, state= 'disabled')
    startbtn.grid(row=0, column=0, sticky='nsew')

    # rend accessible le lancer
    btn_valid = Button(main_frm, text = "Valider", command = valider, width = 55, state='disabled')
    btn_valid.grid(row=4,column=0)

    # remet à zéro les options entrées
    btn_opt0 = Button(main_frm, text = "Reinitialiser", command = reinitialiser, width = 55, state='active')
    btn_opt0.grid(row=5, column=0)

    # arrete le cheminement de la fourmi
    btnstop = Button(main_frm, text = "Stop", command = stop, width = 55, state='active')
    btnstop.grid(row=6, column=0)

    # ------------------- Commands -------------------
    root.bind('<space>', gestion_barre_espace)
    root.bind('<Control-w>', options)
    root.bind('<Control-z>', reinitialiser)
    root.bind('<Control-q>', quitter)
    root.bind('<Control-c>', commands)
    root.bind('<Control-a>', jeu)
    root.bind('<Control-s>',colors_possibility )
    
if __name__ == "__main__":

    width_grid = 0
    height_grid = 0
    size_cell = 0
    
    fenetre()
    limit_size_cell()

    root = Tk()
    root.title('Langton')
    
    grid = create_random_grid_lc(width_grid, height_grid, [0,1])
    canvas = grid_canvas(root, grid, size_cell, margin=10, gutter=2, show_vals=False, outline=False)
    cpt = 0
    check = False
    after_id = None
    
    render()
    root.mainloop()
    
    