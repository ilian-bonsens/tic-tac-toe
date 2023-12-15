from tkinter import *
#import random
tours = 0
plateau = [[0, 0, 0], # Matrice qui represente le plateau de jeu
           [0, 0, 0],
           [0, 0, 0]]

def interface():
    global canvas
    fenetre = Tk()
    fenetre.title("Tic Tac Toe")
    fenetre.iconbitmap("images/icone.ico")
    frame = Frame(fenetre)

    label = Label(fenetre, text="Tic Tac Toe")
    label.grid(columnspan=2)

    for row in range(3):
        for column in range(3):
            plateau[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                        command= lambda row=row, column=column: next_turn(row,column))
            plateau[row][column].grid(row=row,column=column)

    # création du canvas
    #canvas = Canvas(fenetre, width=550, height=550, background='grey')
    #canvas.bind("<Button-1>", click)
    # Création des lignes du morpion
    #ligne1 = canvas.create_line(183, 0, 183, 550)
    #ligne2 = canvas.create_line(368, 0, 368, 550)
    #ligne3 = canvas.create_line(0, 183, 551, 183)
    #ligne4 = canvas.create_line(0, 368, 551, 368)
    #canvas.grid(columnspan=2)

    # Bouton recommencer
    bouton_restart= Button(fenetre, text='Recommencer')
    bouton_restart.grid(row=2, column=1, padx=3, pady=3, sticky=S+W+E)
    
    fenetre.mainloop()

# Fonction qui gère les clics
def click(event):
    X = event.x
    Y = event.y
    global tours
    print(tours)
    print(f"{X}, {Y}")
    tours += 1
    l = Y // 183 # Ligne du clic
    c = X // 183 # Colonne du clic
    if plateau[l][c] == 0: # Vérifie si la case est vide
        if tours % 2 == 0: # Création de la croix si le tour est pair
            canvas.create_line(183*c+18, 183*l+18, 183*(c+1)-18, 183*(l+1)-18, width = 5.5, fill = 'blue')
            canvas.create_line(183*c+18, 183*(l+1)-18, 183*(c+1)-18, 183*l+18, width = 5.5, fill = 'blue')
            plateau[l][c] = 1 # Met à jour la matrice
        else: # Creation du rond si le tour est impair
            canvas.create_oval(183*c+18, 183*l+18, 183*(c+1)-18, 183*(l+1)-18, width = 5.5, outline = 'red')
            plateau[l][c] = 2 # Met à jour la matrice

def win():
    # Vérifie les lignes
    for i in range(3):
        if plateau[i][0] == plateau[i][1] == plateau[i][2] != 0:
            print("Victoire sur la ligne", i)
            # faire page resultat
    # Vérifie les colonnes
    for i in range(3):
        if plateau[0][i] == plateau[1][i] == plateau[2][i] != 0:
            print("Victoire sur la colonne", i)
            # faire page resultat
    # Vérifie les diagonales
    if plateau[0][0] == plateau[1][1] == plateau[2][2] != 0:
        print("Victoire sur la diagonale")
        # faire page resultat')
    if plateau[0][2] == plateau[1][1] == plateau[2][0] != 0:
        print("Victoire sur la diagonale")
        # faire page resultat

#def menu():

interface()
