class Voiture:

    # attributs de classe
    # sorte de constantes
    # communes à toutes les voitures
    roues = 4
    moteur = 1

    def __init__(self):
        self.name = 'clio 4'


class VoitureSport(Voiture):
    def __init__(self):
        self.name = 'Ferrari'


voiture1 = VoitureSport()
voiture = Voiture()
voiture2 = Voiture()


print(voiture1.name)
print(voiture1.roues)

voiture1.roues = 1
print(voiture1.roues)

print(voiture2.roues)




# le constructeur de la classe enfant a écrasé le constructeur de la parent