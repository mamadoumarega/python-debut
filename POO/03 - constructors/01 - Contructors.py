# C'est une fonction qui est appelée lorsqu'on crée un objet

class Animal:
    # le mot self fait reference à l'objet crée
    # grace à ce mot clef on va pouvoir acceder aux attributs et methodes de la classe
    def __init__(self):
        print('Un animal vient detre crée')
        pass
