from tkinter import Tk, Label, Canvas, Button, S, W, E

tours = 0
plateau = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Matrice qui represente le plateau de jeu

def interface():
    global canvas
    fenetre = Tk()
    fenetre.title("Tic Tac Toe")

    label = Label(fenetre, text="Tic Tac Toe")
    label.grid(columnspan=2)

    canvas = Canvas(fenetre, width=550, height=550, background='grey')
    canvas.bind("<Button-1>", click)
    ligne1 = canvas.create_line(183, 0, 183, 550)
    ligne2 = canvas.create_line(368, 0, 368, 550)
    ligne3 = canvas.create_line(0, 183, 551, 183)
    ligne4 = canvas.create_line(0, 368, 551, 368)
    canvas.grid(columnspan=2)

    bouton_quitter = Button(fenetre, text='Quitter', command=fenetre.destroy)
    bouton_quitter.grid(row=2, column=0, padx=3, pady=3, sticky=S+W+E)

    bouton_reload = Button(fenetre, text='Recommencer')
    bouton_reload.grid(row=2, column=1, padx=3, pady=3, sticky=S+W+E)

    fenetre.mainloop()

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
        if tours % 2 == 0: # Croix
            canvas.create_line(183*c+18, 183*l+18, 183*(c+1)-18, 183*(l+1)-18, width = 5.5, fill = 'blue')
            canvas.create_line(183*c+18, 183*(l+1)-18, 183*(c+1)-18, 183*l+18, width = 5.5, fill = 'blue')
            plateau[l][c] = 1 # Met à jour la matrice
        else: # Rond
            canvas.create_oval(183*c+18, 183*l+18, 183*(c+1)-18, 183*(l+1)-18, width = 5.5, outline = 'red')
            plateau[l][c] = 2 # Met à jour la matrice

interface()
