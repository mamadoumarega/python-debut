import random

list_characters = (
    {'name': 'Seon Gi-hun', 'marbles': 15, 'loss': 2, 'gain': 1, 'scream_war': 'bravo'},
    {'name': 'Kang Sae-byeok', 'marbles': 25, 'loss': 1, 'gain': 2, 'scream_war': 'bravo'},
    {'name': 'Cho Sang-woo', 'marbles': 35, 'loss': 0, 'gain': 3, 'scream_war': 'bravo'},
)

list_playersToFace = (
    {'name': 'Mamadou', 'marbles': 7, 'age': 26},
    {'name': 'Omar', 'marbles': 8, 'age': 21},
    {'name': 'Julien', 'marbles': 10, 'age': 27},
    {'name': 'Sarah', 'marbles': 7, 'age': 26},
    {'name': 'Jules', 'marbles': 11, 'age': 22},
    {'name': 'Alex', 'marbles': 17, 'age': 30},
    {'name': 'Alimatou', 'marbles': 15, 'age': 24},
    {'name': 'Allan', 'marbles': 9, 'age': 26},
    {'name': 'Lionel', 'marbles': 10, 'age': 33},
    {'name': 'Bruno', 'marbles': 16, 'age': 26},
    {'name': 'Zeyd', 'marbles': 4, 'age': 45},
    {'name': 'John', 'marbles': 13, 'age': 26},
    {'name': 'Jane', 'marbles': 5, 'age': 26},
    {'name': 'Demo', 'marbles': 3, 'age': 28},
    {'name': 'Vieu', 'marbles': 14, 'age': 80},
    {'name': 'Ibrahim', 'marbles': 16, 'age': 25},
    {'name': 'Haroun', 'marbles': 18, 'age': 24},
    {'name': 'Nawel', 'marbles': 12, 'age': 26},
    {'name': 'Pira', 'marbles': 11, 'age': 26},
    {'name': 'Eric', 'marbles': 10, 'age': 30},
)

choice = input('Veillez choisir le niveau Facile(facile | F) Difficile(difficile | D) Impossible(impossible|I)')
personnage = input('Saisir votre personnage')

isPresent = []
essai = 0

gamers = random.choice(list_characters)

if choice == 'F' or choice == 'facile':
    while essai < 5:
        if personnage == 'Seon Gi-hun':
            while True:
                guest = input('Le nombre est il pair ou impair O ou N ')
                if guest == 'O' or guest == 'N':
                    if gamers['marbles'] % 2 == 0 and guest == 'O' or gamers['marbles'] % 2 != 0 and guest == 'N':
                        print(list_characters[0]['scream_war'])
                        list_characters[0]['marbles'] += gamers['marbles'] + list_characters[0]['gain']
                        print(f"l'adversaire avait {gamers['marbles']}")
                        print(f"Le bonus est {list_characters[0]['gain']}")
                        print(f"Vous avez  {list_characters[0]['marbles']} billes")
                        isPresent.append(gamers)
                    else:
                        list_characters[0]['marbles'] -= gamers['loss'] + gamers['marbles']
                        print(f"l'adversaire avait {gamers['marbles']}")
                        print(f"Le bonus est {list_characters[0]['gain']}")
                        print(f"Vous avez  {list_characters[0]['marbles']} billes")
    essai += 1

if choice == 'Difficile' or choice == 'd':
    while essai < 10:
        if personnage == 'Kang Sae-byeok':
            while True:
                guest = input('Le nombre est il pair ou impair O ou N ')
                if guest == 'O' or guest == 'N':
                    if gamers['marbles'] % 2 == 0 and guest == 'O' or gamers['marbles'] % 2 != 0 and guest == 'N':
                        print(list_characters[1]['scream_war'])
                        list_characters[1]['marbles'] += gamers['marbles'] + list_characters[1]['gain']
                        print(f"l'adversaire avait {gamers['marbles']}")
                        print(f"Le malus est {list_characters[1]['gain']}")
                        print(f"Vous avez  {list_characters[1]['marbles']} billes")
                        isPresent.append(gamers)
                    else:
                        list_characters[0]['marbles'] -= gamers['loss'] + gamers['marbles']
                        print(f"l'adversaire avait {gamers['marbles']}")
                        print(f"Le malus est {list_characters[1]['gain']}")
                        print(f"Vous avez  {list_characters[1]['marbles']} billes")
    essai += 1

if choice == 'I' or choice == 'impossible':
    while essai < 20:
        if personnage == 'Cho Sang-woo':
            while True:
                guest = input('Le nombre est il pair ou impair O ou N ')
                if guest == 'O' or guest == 'N':
                    if gamers['marbles'] % 2 == 0 and guest == 'O' or gamers['marbles'] % 2 != 0 and guest == 'N':
                        print(list_characters[2]['scream_war'])
                        list_characters[2]['marbles'] += gamers['marbles'] + list_characters[2]['gain']
                        print(f"l'adversaire avait {gamers['marbles']}")
                        print(f"Le bonus est {list_characters[2]['gain']}")
                        print(f"Vous avez  {list_characters[2]['marbles']} billes")
                        isPresent.append(gamers)
                    else:
                        list_characters[0]['marbles'] -= gamers['loss'] + gamers['marbles']
                        print(f"l'adversaire avait {gamers['marbles']}")
                        print(f"Le malus est {list_characters[2]['gain']}")
                        print(f"Vous avez  {list_characters[2]['marbles']} billes")
    essai += 1
