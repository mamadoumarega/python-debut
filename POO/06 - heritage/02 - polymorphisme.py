# Le polymorphisme c'est :
# le fait de créer des methodes pour des classes qui héritent de la classe Parent


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

    def travailler(self, travail):
        print(f"Salut je fais actuellement du {travail}")
        print(f"Surcharge de la methode travailler dans la classe Parent")


class Etudiant(Humain):
    pass

    def travailler(self, travail='mes devoirs'):
        print(f"Surcharge de la méthode travailler dans la classe Etudiant")
        print(f"Je fais actuellement du {travail}")


class Professor(Humain):

    def __init__(self):
        self.specialite = []


#
# sam = Professor()
# sam.modifier_attributs('Habbani', 'Samih', 27)
# sam.se_presenter()

# sam.specialite = ['Python', 'React JS']
# print(sam.specialite)

# on a pas eu besoin de redéfinir la méthode modifier_attributs ni les attributs d'ailleurs


# print(sam)

etud = Etudiant()
etud.travailler()
