i = 0
while i < 5:
    print(f'i : {i}')
    i += 1
else:
    print('fin de la boucle')

#################################
list_names = ['Jules', 'Julien', 'Adam', 'Sarah', 'Omar', 'Mamadou']
i = 0
while i < len(list_names):
    print(f'Salut {list_names[i]}')
    i += 1

# Afficher en console la forme suivante en utilisant la boucle while

#####
##
####
##
##

i = 0
list_diez = [5,2,4,2,2]
while i < len(list_diez):
    print('#' * list_diez[i])
    i += 1

list_kilos = [171,788,1981,99]
i = 0
while i < len(list_kilos):
    poids = round(list_kilos[i] * 2.2, 2)
    print(f'poids converti {poids}')
    i += 1




