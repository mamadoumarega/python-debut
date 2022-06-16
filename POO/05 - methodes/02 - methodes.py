# Exercice
class Personne:

    def __init__(self, age, prenom):
        print('Une nouvelle personne')
        self.age = age
        self.prenom = prenom

    # Mettre en place une méthode qui permet de changer de prénom
    # un nouvel attribut
    # une nouvelle méthode

    def vieillir(self):
        self.age += 1

    def changeName(self, prenom):
        self.prenom = prenom


mamadou = Personne(26, 'Mamadou')
print(mamadou.age)
print(mamadou.prenom)

print(mamadou.vieillir())
print(mamadou.changeName('mamadou'))
