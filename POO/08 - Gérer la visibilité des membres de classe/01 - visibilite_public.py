class Visibilite:

    def __init__(self):
        self.public = 'Variable public'

    @property
    def maVariable(self):
        print('Récupération de ma varible')
        return self.public


objet = Visibilite()
# affiche variable public
print(objet.public)
