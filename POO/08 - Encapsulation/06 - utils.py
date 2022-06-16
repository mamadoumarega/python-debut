class Voiture:

    def __init__(self):
        self._roues = 4

    # Decorateur qui permet de mettre en place une propriete accesseur
    @property
    def roues(self):
        print('Récupération des roues')
        return self._roues

    @roues.setter
    def roues(self, number):
        print('Modification des roues')
        self._roues = number


voiture1 = Voiture()
voiture1.roues = 5

# attribut dir
print(dir(voiture1))

# attribut __dict__
print(voiture1.__dict__)
print(voiture1)
