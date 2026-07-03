def calcul_moyenne(notes):
    total = 0
    for note in notes:
        total+=note
    return total/len(notes)
notes=[5,12,52]

print(calcul_moyenne(notes))