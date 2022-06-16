# dictionnaires sont des tableaux d'associations cles/valeurs

mamadou = {
    'first_name': 'mamadou',
    'name': 'Marega',
    'age': 26,
    'is_student': True,
    'hobbies': ['Foot', 'Séries']
}

# Afficher le prenom
print(mamadou['first_name'])


# modifier son age
mamadou['age'] = 27
print(mamadou)


#afficher la date de naissance de mamadou
# si cette clé n'existe pas dans le dictionnaire
# afficher une date par defaut
print(mamadou.get('birth_date', '01/01/1995'))
