class Visibilite:

    def __init__(self, name):
        self.__name = name

    @property
    def ma_variable(self):
        return self.__name


objet = Visibilite('Toto')
# erreur visibility has no attribute
# print(objet.__prive)
print(objet.ma_variable)
