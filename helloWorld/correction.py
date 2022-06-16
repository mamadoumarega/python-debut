import random

##
## NIVEAU DE DIFFICULTÉ
##

levels = {
    "1": 5,
    "2": 10,
    "3": 20
}

##
## PERSONNAGE DE DÉPART
##

characters = (
    {'name': "Seong Gi-hun", "marbles": 15, "loss": 2, "gain": 1, "scream_war": "WIPEOUT !!!"},
    {'name': "Kang Sae-byeok", "marbles": 25, "loss": 1, "gain": 2, "scream_war": "WHASASASASASA......"},
    {'name': "Cho Sang-woo", "marbles": 35, "loss": 0, "gain": 3, "scream_war": "You are dead ! ...not a big surprise"}
)


##
## ADVERSAIRES
##


def marbles():
    return random.randint(1, 20)


enemies = (
    {'name': 'Robert', "marbles": marbles(), "age": 28, 'dead': False},
    {'name': 'Philipe', "marbles": marbles(), "age": 71, 'dead': False},
    {'name': 'Simon', "marbles": marbles(), "age": 35, 'dead': False},
    {'name': 'Pascale', "marbles": marbles(), "age": 100, 'dead': False},
    {'name': 'Julie', "marbles": marbles(), "age": 38, 'dead': False},
    {'name': 'Lucas', "marbles": marbles(), "age": 81, 'dead': False},
    {'name': 'Lèa', "marbles": marbles(), "age": 44, 'dead': False},
    {'name': 'Kevin', "marbles": marbles(), "age": 50, 'dead': False},
    {'name': 'Alphonse', "marbles": marbles(), "age": 29, 'dead': False},
    {'name': 'Jean-Baptiste', "marbles": marbles(), "age": 62, 'dead': False},
    {'name': 'Violet', "marbles": marbles(), "age": 77, 'dead': False},
    {'name': 'Margot', "marbles": marbles(), "age": 99, 'dead': False},
    {'name': 'Lou', "marbles": marbles(), "age": 18, 'dead': False},
    {'name': 'Louis', "marbles": marbles(), "age": 22, 'dead': False},
    {'name': 'Maurice', "marbles": marbles(), "age": 34, 'dead': False},
    {'name': 'Léo', "marbles": marbles(), "age": 45, 'dead': False},
    {'name': 'Xavier', "marbles": marbles(), "age": 16, 'dead': False},
    {'name': 'Mathilde', "marbles": marbles(), "age": 77, 'dead': False},
    {'name': 'Delphine', "marbles": marbles(), "age": 98, 'dead': False},
    {'name': 'Sherlock', "marbles": marbles(), "age": 21, 'dead': False}
)

cheat_answers = {
    'y' : True,
    'n' : False
}


def check_if_odd_or_even(nbr_marbles_of_enemy, choice):
    if nbr_marbles_of_enemy % 2 == 0:  # le chiffre est pair
        if choice == 2:
            return True
    else:  # le chiffre est impair
        if choice == 1:
            return True
    return False


# Choisir la difficulté

nbr_of_encounters = 0

while True:
    level_choice = input('Choose a level between (1) - Easy / (2) - Hard / (3) - Impossible')
    if levels.get(level_choice) is not None:
        nbr_of_encounters = levels.get(level_choice)
        break

print(f'You have to face {nbr_of_encounters} ennemies to win the game ! will you survive? ')

# Présentation des personnages
print('You will have to choose among those characters :')
for character in characters:
    print(f" {character['name']} starts the game with {character['marbles']} marbles,"
          f"a bonus of {character['gain']} and a malus of {character['loss']}")

# Choisir un personnage
hero = {}

while True:
    hero_choice = input(
        'Choose a hero to play the game ! (1) - Seong Gi-hun / (2) - Kang Sae-byeok / (3) - Cho Sang-woo')
    if hero_choice.isnumeric() and 0 <= int(hero_choice) - 1 < len(characters):
        hero = characters[int(hero_choice) - 1]
        break

print(f"You choose to play the game with {hero['name']}."
      f"You start the game {hero['marbles']} marbles, a bonus of {hero['gain']} and a malus of {hero['loss']} ")

# Lancer le jeu

i = 1

while i <= nbr_of_encounters and hero['marbles'] > 0:
    # Ennemy to face
    ennemy = random.choice(enemies)

    # je regarde si l'ennemi n'a pas déjà été vaincu
    if not ennemy['dead']:
        print(
            f"Encounter n° {i} - You are facing {ennemy['name']} and you still have {hero['marbles']} marbles in your hand \n"
            f"To win the fight you have to guess if the number of marbles in your ennemy's hand is an even number or a odd number."
            )

        # si je tombe sur un vieux de plus de 70 ans
        cheat_answer = False
        if ennemy['age'] > 70:
            while True:
                cheat_answer = input(f'Your ennemy is a old as he is {ennemy["age"]} '
                                     f'years old hehehe, do you wanna cheat on him? (Y)es or (N)o > ').lower()
                if cheat_answer == 'y' or cheat_answer == 'n':
                    cheat_answer = cheat_answers.get(cheat_answer)
                    break

        if not cheat_answer:
            # your choice odd - even
            answer = input("What is your answer ? (1) - Odd / (2) - Even")
            win = False
            while True:
                if answer.isnumeric() and 0 < int(answer) < 3:
                    win = check_if_odd_or_even(ennemy['marbles'], int(answer))
                    break

            # Encounter handling
            if win:
                print(f"Well done, you beat this ennemy, since he had {ennemy['marbles']} marbles >")
                hero['marbles'] += ennemy['marbles'] + hero['gain']
                print(f"You win {ennemy['marbles']} marbles from your enemy plus your bonus of {hero['gain']}")
                # identifier l'ennemi comme mort
                ennemy['dead'] = True
            else:
                print(f"Too bad, you lost this fight, since your enemy had {ennemy['marbles']} marbles >")
                hero['marbles'] -= (ennemy['marbles'] + hero['loss'])
                print(f"You loose {ennemy['marbles']} marbles from your enemy minus your malus of {hero['loss']}")
                # si on perds on donne une partie de nos billes à l'ennemi
                ennemy['marbles'] += hero['marbles']
        else:
            hero['marbles'] += ennemy['marbles']
            ennemy['dead'] = True
            print(f"You are a mean person ! the poor grandpa died because of your evilness ! \n"
                  f"He had {ennemy['marbles']} marbles but as you cheated you have no bonus on this one !")

        i += 1
else:
    if hero['marbles'] > 0:
        print(f"{hero['scream_war']} !!! Congratulations ! You won the game !")
    else:
        print('HAHAHAHAHA !! You loooose the game !')