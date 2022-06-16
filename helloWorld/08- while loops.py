# convertisseur de poids

# on va demander à l'internaute son poids
# en quelle unité est exprimé ce poids ( (k)ilos or (l)bs )

# si le poids est exprimé en kilos -> convertir en lbs ( weight * 2.2 )
# si le poids est exprimé en lbs -> convertir en kilos ( weight * 0.45 )

# si l'unité de mesure renseignée n'est ni un kilos ni un lbs alors afficher un msg 'wront unit'

# Bonus : KILOS / kilos / kg / klos
# gérer le cas ou pour l'unité de mesure on a pas un k pour kilos mais KILOS / kilos / kg / klos / kilogrammes

# controller si le poids qu'il nous donne est bien un chiffre
# arrondir le poids converti


# Mega Bonus
# lui reposer la question de l'unité de mesure tant qu'il précise pas un l ou un k

unity = ['KILO', 'kilos', 'kg', 'kilogrammes', 'klos']

has_converted = False

while True:
    if has_converted:
        poids = input('Entrer votre poids ')
        if poids.isnumeric():
           while True:
               unite = input("Quelle est l'unité ? ").lower()
               poids = float(poids)
               if unite in unity:
                   print(f'poids converti {round(poids * 2.2, 2)}')
                   has_converted = True
                   break
               elif unite.startswith('l'):
                   print(f'poids converti {round(poids * 2.2, 2)}')
                   has_converted = True
                   break
               else:
                   print('Wrong unit')
        else:
            print('Please enter a number')
        break
    else:
        print('bye bye')
        break


