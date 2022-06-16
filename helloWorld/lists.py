ma_liste = ['Sam', True, 27, ['mma', 'box thai', 'moto'] ]

# afficher sam
print(ma_liste[0])

# modifier la valeur 27 en 28
ma_liste[2] = 28
print(ma_liste)

# afficher le mot mma
print(ma_liste[3][0])


#afficher une decoupe des 3
print('decoupage', ma_liste[:3])
print(ma_liste[0:3])

# ajouter un element a la liste
ma_liste[3].append('Escalade')

# ajouter velo apres escalade


# trier
ma_liste[3].sort()

# copier

new_liste = ma_liste.copy()
print(new_liste)