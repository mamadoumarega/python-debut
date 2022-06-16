class Voiture:

    def __init__(self):
        self.name = 'Ferrari'

    def retourner_model(self):
        return '250'


voiture1 = Voiture()
print(voiture1.retourner_model())