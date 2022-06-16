class Voiture:

    def __init__(self, marque, model):
        self.__marque = marque
        self.__model = model

    @property
    def model(self):
        return self.__model

    @property
    def marque(self):
        return self.__marque

    @model.setter
    def model(self, model):
        self.__model = model

    @marque.setter
    def marque(self, marque):
        self.__marque = marque


voiture1 = Voiture('Renault', 'clio')
print(voiture1.model)
print(voiture1.marque)


class VoitureSport(Voiture):
    pass


vSport = VoitureSport('ferrari', '250')
print(vSport.__dict__)

print(vSport._Voiture__marque) # Acces a la propriete prive


