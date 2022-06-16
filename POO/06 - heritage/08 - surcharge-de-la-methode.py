class Voiture:
    roues = 4
    moteur = 1

    def __init__(self, name):
        self.name = name


class VoitureSport(Voiture):

    def __init__(self, name, color):
        # l'appel du constructeur parent
        super().__init__(name)
        # Surcharge du constructeur parent
        self.color = color


voiture1 = VoitureSport('Ferrari', 'rouge')
print(voiture1.name)

voiture2 = Voiture('Clio')
print(voiture2.name)
