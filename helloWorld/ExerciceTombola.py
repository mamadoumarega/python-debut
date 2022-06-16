# Tombola

import random

# Il va falloir faire gagner aléatoirement 3 gagnants

# Pour cela vous allez définir 10 participants dans un tuple (femmes, hommes, femmes étrangères)
# chaque participant sera un dictionnaire avec un prénom, un sexe, et un solde (l'argent sur son compte)

list_players = (
    {'first_name': 'Sam', 'sexe': 'm', 'solde': 10_000, 'nationality': 'Maroc'},
    {'first_name': 'Léa', 'sexe': 'f', 'solde': 20_000, 'nationality': 'Française'},
    {'first_name': 'Jon', 'sexe': 'm', 'solde': 10_000, 'nationality': 'Française'},
    {'first_name': 'Claudia', 'sexe': 'f', 'solde': 5_000, 'nationality': 'Portugaise'},
    {'first_name': 'Luc', 'sexe': 'm', 'solde': 32_000, 'nationality': 'Française'},
    {'first_name': 'Sophie', 'sexe': 'f', 'solde': 4_000, 'nationality': 'Française'},
    {'first_name': 'Téa', 'sexe': 'f', 'solde': 1_000, 'nationality': 'Française'},
    {'first_name': 'Léo', 'sexe': 'm', 'solde': 8_000, 'nationality': 'Espagnol'},
    {'first_name': 'Maxime', 'sexe': 'm', 'solde': 5_000, 'nationality': 'Française'},
    {'first_name': 'Alex', 'sexe': 'm', 'solde': 5_000, 'nationality': 'Française'}
)

list_winners = []

# Le premier gagnant (du premier tour) gagnera 10_000 euros
# Le deuxième gagnant (du deuxième tour) gagnera 5_000 euros
# Le troisième gagnant (du troisième tour) gagnera 1_000 euros

list_rewards = [10_000, 5_000, 1_000]

# Règles

# un gagnant ne peut gagner qu'une seule fois
# parmis les trois gagnants je dois avoir au moins une femme qui gagne

has_woman_won = False

i = 0
while i < 3:
    winner = random.choice(list_players)

    # si je suis au dernier tour et qu'aucune femme n'a encore gagné et que le dernier gagnant du tour est un homme
    # alors je refais une gagner une autre personne jusqu'à avoir un femme française
    if i == 2 and not has_woman_won and winner['sexe'] == 'm':
        continue

    if winner not in list_winners: # éviter deux gagnants
        # si une femme gagne elle doit être française
        if winner['sexe'] == 'f' and winner['nationality'] != 'Française':
            continue

        if winner['sexe'] == 'f': # si une femme gagne je modifie la valeur du boolean
            has_woman_won = True

        winner['solde'] += list_rewards[i]
        list_winners.append(winner)
        print(f"Le gagnant de ce soir est : {winner['first_name']}, son nouveau solde est {winner['solde']} €")
        i += 1

        # A chaque qu'un gagnant gagnera faudra l'annoncer en tant que gagnant
        # afficher le montant gagné et mettre à jour son solde et afficher son nouveau solde


# Méga Bonus
# Seul un femme française pourra gagner un prix

# un homme étranger pourra gagner
