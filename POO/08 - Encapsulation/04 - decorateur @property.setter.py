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
print(voiture1.roues)
voiture1.roues = 5
print(voiture1.roues)
