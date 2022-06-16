class Animal:
    def __init__(self, age = 1):
        print('Un nouveau animal')
        self.age = age


scoby = Animal(27)
print(scoby.age)

scoby2 = Animal()
print(scoby2.age)

# Les variables d'instances sont spécifiques à chaque objet
# elles définissent l'etat de l'objet
# je peux avoir des valeurs par défaut et si un parametre est manquant
# imaginons qu'on ne connnaissait pas l'age de l'animal par défaut chaque animal sans age aura 1 ans

# constructeur est une methode unpeu spéciale
# appelée à la construction
# et qui permet d'initialiser des valeurs pour cet objet
