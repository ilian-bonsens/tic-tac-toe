from tkinter import *
import random

window = Tk()
window.title("Tic-Tac-Toe")
window.iconbitmap("images/icone.ico")
window.geometry("650x600")
window.resizable(False,False)   
joueurs = ["Joueur 1","Joueur 2"]
joueur = random.choice(joueurs)
boutons =  [[0,0,0],
            [0,0,0],
            [0,0,0]]
label = Label(text=joueur + ' commence', font=('consolas',30), pady=15)

def menu():
    play_bouton = Button(text="Jouer avec un ami", font=('consolas',20), command=interface_jeu)
    play_bouton.place(x=180, y=150)
    play_bouton = Button(text="Jouer contre l'ordi", font=('consolas',20), command=interface_jeu)
    play_bouton.place(x=165, y=250)

    window.mainloop()

def interface_jeu():
    label.pack(side="top")

    reset_bouton = Button(text="Recommencer", font=('consolas',20), command=new_game)
    reset_bouton.pack(side="bottom", pady=15)

    frame = Frame(window)
    frame.pack(pady=20)

    for row in range(3):
        for column in range(3):
            boutons[row][column] = Button(frame, text="",font=('consolas',30), width=5, height=2,
                                        command= lambda row=row, column=column: next_turn(row,column))
            boutons[row][column].grid(row=row,column=column)
            
    window.mainloop()

def next_turn(row, column):

    global joueur

    if boutons[row][column]['text'] == "" and check_winner() is False:

        if joueur == joueurs[0]:

            boutons[row][column]['text'] = "X"

            if check_winner() is False:
                joueur = joueurs[1]
                label.config(text=("Tour de " + joueur))

            elif check_winner() is True:
                label.config(text=(joueur + " gagne"))

            elif check_winner() == "Egalité":
                label.config(text="Egalité!")

        else:

            boutons[row][column]['text'] = "O"

            if check_winner() is False:
                joueur = joueurs[0]
                label.config(text=("Tour de " + joueur))

            elif check_winner() is True:
                label.config(text=(joueur + " gagne"))

            elif check_winner() == "Egalité":
                label.config(text="Egalité !")

def check_winner():

    for row in range(3):
        if boutons[row][0]['text'] == boutons[row][1]['text'] == boutons[row][2]['text'] != "":
            boutons[row][0].config(bg="green")
            boutons[row][1].config(bg="green")
            boutons[row][2].config(bg="green")
            return True

    for column in range(3):
        if boutons[0][column]['text'] == boutons[1][column]['text'] == boutons[2][column]['text'] != "":
            boutons[0][column].config(bg="green")
            boutons[1][column].config(bg="green")
            boutons[2][column].config(bg="green")
            return True

    if boutons[0][0]['text'] == boutons[1][1]['text'] == boutons[2][2]['text'] != "":
        boutons[0][0].config(bg="green")
        boutons[1][1].config(bg="green")
        boutons[2][2].config(bg="green")
        return True

    elif boutons[0][2]['text'] == boutons[1][1]['text'] == boutons[2][0]['text'] != "":
        boutons[0][2].config(bg="green")
        boutons[1][1].config(bg="green")
        boutons[2][0].config(bg="green")
        return True

    elif empty_boxes() is False:

        for row in range(3):
            for column in range(3):
                boutons[row][column].config(bg="yellow")
        return "Egalité"

    else:
        return False


def empty_boxes():

    boxes = 9

    for row in range(3):
        for column in range(3):
            if boutons[row][column]['text'] != "":
                boxes -= 1

    if boxes == 0:
        return False
    else:
        return True

def new_game():

    global joueur

    joueur = random.choice(joueurs)

    label.config(text=joueur+" turn")

    for row in range(3):
        for column in range(3):
            boutons[row][column].config(text="",bg="#F0F0F0")

menu()