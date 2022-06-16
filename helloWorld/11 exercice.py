# faire devinner un chiffre secret à l'utilisateur

# générer un chiffre aléatoire entre 1 et 10

# l'utilisateur aura 3 chances pour trouver le chiffre secret
# si il trouve le chiffre secret avant d'avoir écouler ses 3 chances -> la partie s'arrête c'est gagné
# si il ne trouve pas le chiffre secret avant d'avoir écouler ses 3 chances -> la partie s'arrête c'est perdu

# si le chiffre proposé par l'internaute est supérieur au chiffre secret lui indiquer que son chiffre est trop grand
# et lui indiquer le nombre de poinds de vie restant

# si le chiffre proposé par l'internaute est inférieur au chiffre secret lui indiquer que son chiffre est trop petit
# et lui indiquer le nombre de poinds de vie restant

# Bonus
# si l'internaute ne nous donne pas un chiffre entre 1 et 10 alors je lui repose la question sans lui faire
# perdre de point

# Bonus 2
# lui proposer de rejouer la partie à la fin de la première partie
import  random

def jeu(essais, min, max):
    answer = input('Do you wanna play? (y)es or (n)o')
    if answer=='y':
        nb = random.randint(min, max)
        win = False
        for essais in range(essais):
            while True:
                choix = input("Choisissez un chiffre entre 1 et 10 ")
                if choix.isnumeric():
                    if 10 >= int(choix) >= 1:
                        break
            choix = int(choix)
            if choix == nb:
                print('gagné')
                win = True
                break
            elif choix > nb:
                print('chiffre trop grand')
                print(f'nombre de pts de vie prestant : {3 - (essais + 1)}')
            elif choix < nb:
                print('chiffre trop petit')
                print(f'nombre de pts de vie prestant : {3 - (essais + 1)}')
        if not win:
            print('perdu')
        jeu(essais, min, max)


jeu(3,1,10)




















