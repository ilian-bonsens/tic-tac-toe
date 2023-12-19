import random
from morpionV2 import boutons, liste_cases_vides


def ia(board, signe):
    if liste_cases_vides:
        row, column = random.choice(liste_cases_vides)
        board[row][column]['text'] = signe
        return board

board = boutons
signe = "O"

