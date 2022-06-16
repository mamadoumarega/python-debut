class Voiture(object):

    def __init__(self):
        self._roues = 4

    # Decorateur qui permet de mettre en place une propriete
    @property
    def roues(self):
        print('Récupération des roues')
        return self._roues


voiture1 = Voiture()
print(voiture1._roues)
