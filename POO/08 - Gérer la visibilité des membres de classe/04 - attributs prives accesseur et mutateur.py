class Visibilite:

    def __init__(self, name):
        self.__name = name

    # Accesseur
    def retourner_nom(self):
        return self.__name

    def modifier(self, name):
        self.__name = name


objet = Visibilite('Toto')
print(objet.retourner_nom())
objet.modifier('Tata')

print(objet.retourner_nom())

