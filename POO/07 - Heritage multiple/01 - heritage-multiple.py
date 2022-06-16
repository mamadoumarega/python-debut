class Voiture:

    def __init__(self, name, year, model,brand):
        print('Une voiture est créee')
        self.name = name
        self.year = year
        self.model = model
        self.brand = brand


class Citroen:

    def __init__(self):
        self.hydraulic_suspension = True
        self.moteur = 'Architecture à plat'


class Ds3(Voiture, Citroen):

    def __init__(self, name, year, model, brand):
        super().__init__(name, year, model, brand)

        # Solution
        Voiture.__init__(self, name, year,model,brand)
        Citroen.__init__(self)
        # Je peux meme rajouter si je peux un attribut propre a la classe Ds3


ds3 = Ds3('Nouvelle DS3', 2018, 'Ds3', 'Citroen')
print(ds3.name)
# c'est cool ça fonctionne par contre si je fais le code suivant erreur
print(ds3.hydraulic_suspension) # ici il me dit que j'ai