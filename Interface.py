import tkinter as tk
from tkinter import *
from tkinter import messagebox
from grid_manager_template import *
from grid_tk_template import *
from Framesbase import *
from config import *
from window import *

def render():    
    # ----------------- Frame principale -----------------

    # main_frm = tk.Frame(root,height= height, bg='aliceblue')
    # main_frm.grid(row=0, column=1, sticky='nsew')

    # ----------------- MenuBar -----------------

    # renderMenu()

    # ------------------- LabelFrames -------------------
    # compteur
    lbl_compteur = tk.LabelFrame(main_frm, width= 55, height= 50, text = 'Compteur')
    lbl_compteur.grid(row=1, column=0, sticky= 'nsew', columnspan=2)
    lbl_compteur.columnconfigure(0,weight=1)

    # nombre de fourmis à entrer
    lbl_nb_fourmis = tk.LabelFrame(main_frm, width= 55, height= 50, text = 'Nombre de fourmis')
    lbl_nb_fourmis.grid(row=2, column=0, sticky= 'nsew', columnspan=2)
    lbl_nb_fourmis.columnconfigure(0,weight=1)
    nb_fourmis = 1

    # choix des couleurs
    lbl_cell_color = tk.LabelFrame(main_frm, width= 55, height= 50, text = 'Couleurs des fourmis')
    lbl_cell_color.grid(row=3, column=0, sticky= 'nsew', columnspan=2)
    lbl_cell_color.columnconfigure(0,weight=1)

    # initialisation des labels des choix de couleurs
    color_labels = ['1', '2', '3', '4']
    lbl_color_fourmi = []
    
    update_count_ants(2)

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
    entry_val.set('3')

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
    color_f2.set(color_f2)
    color_f3.set(color_f3)
    color_f4.set('couleur : ')

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
        if nb_fourmis <= 0:
            nb_fourmis = 1
        if nb_fourmis > 4:
            nb_fourmis = 4

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
        compteur.config(text=str(increase_iteration()))

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
            
            #Si tu commente deja cette ligne cela te fera gagner un peu de perf
            # print('label : ', label,'position : ',posx_fourmi, posy_fourmi)

            posx_fourmi, posy_fourmi = tore(posx_fourmi, posy_fourmi)

            set_cell_text(canvas, posx_fourmi, posy_fourmi, ' ')
  
            color = COLORS['bg']
            movement = set_matrice(posx_fourmi, posy_fourmi)

            if movement :
                ant['orientation'] = droite(ant['orientation'])
                color = ant_colors[label]
            else:
                ant['orientation'] = gauche(ant['orientation'])

            set_color_cell(canvas, posx_fourmi, posy_fourmi, color)

            # position actuelle de la fourmi
            posx_bis, posy_bis = deplacer(ant['orientation'],posx_fourmi, posy_fourmi)
            posx_bis, posy_bis = tore(posx_bis, posy_bis)

            # définition de la position pour le prochain déplacement
            ant['position'] = posx_bis, posy_bis
            set_cell_text(canvas, posx_bis, posy_bis, '¤')

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
    root.bind('<Control-z>', reinitialiser)
    limit_entry()
    # start()

    
if __name__ == "__main__":
    
    show_start_frame()
    verify_grid()

    cpt = 0
    check = False
    after_id = None

    initWindow()