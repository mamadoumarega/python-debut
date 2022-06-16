# Exercice
# Mettre en place une méthode qui permet de changer de prénom
# un nouvel attribut
# une nouvelle méthode

class Personne:

    def __init__(self, age, name):
        print('Une nouvelle personne')
        self.age = age
        self.name = name

    def vieillir(self):
        self.age += 1

    def change_name(self, name):
        self.name = name

    def hello(self):
        print(f"Salut tout le monde je m'appelle {self.name} et j'ai {self.age} ans")


mamadou = Personne(26, 'Mamadou')
mamadou.hello()



