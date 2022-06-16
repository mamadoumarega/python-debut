class Voiture(object):

    def __init__(self):
        self._roues = 4

    def _get_roues(self):
        print('Récupération des roues')
        return self._roues

    def _set_roues(self, nbr_roues):
        print('Modification des roues')
        self._roues = nbr_roues

    # premiere façon de mettre en place des proprietes
    roues = property(_get_roues, _set_roues)


voiture1 = Voiture()
print(voiture1._roues)
voiture1.roues = 5
print(voiture1.roues)
