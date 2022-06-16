# Un attribut de classe est un attribut partagé par toutes les instances de la classe
# c'est à dire l'espace mémoire d'un attribut de classe est un espace partagé pour toutes les instances / objets n'ayant pas
# leur propre espace mémoire

class Animal:

    def __init__(self):
        print('Un nouveau animal')
        # definition d'un attribut
        self.age = 0  # variable d'instance en python
# Toutes les instances de la classe qui seront crées à partir de la classe animal auront l'attribut
# 0 comme valeur par defaut

# le constructor il initialise des variables des variables d'instances stockés en mémoire qui seront
# stockés durant toute la durée de l'objet

scoby = Animal()
print(dir(scoby))
