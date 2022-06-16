class Visibilite:

    def __init__(self):
        self._protected = 'Variable protégée'

    @property
    def protected(self):
        return self._protected


objet = Visibilite()
# affiche la variable Variable protégée
print(objet.protected)
