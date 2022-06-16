class Humain:

    def __init__(self):
        self.name = ''
        self.first_name = ''
        self.age = 0

    def modifier_attributs(self, name, first_name, age):
        self.name = name
        self.first_name = first_name
        self.age = age

    def se_presenter(self):
        print(f"Salut je m'appel {self.name} {self.first_name} et j'ai {self.age} ans !")


class Etudiant(Humain):
    pass


class Professor(Humain):

    def __init__(self):
        self.specialite = []


#
sam = Professor()
sam.modifier_attributs('Habbani', 'Samih', 27)
sam.se_presenter()

sam.specialite = ['Python', 'React JS']
print(sam.specialite)

# on a pas eu besoin de redéfinir la méthode modifier_attributs ni les attributs d'ailleurs


print(sam)
