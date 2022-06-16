class Animal:
    # attributs de classe
    attribut_class = 0

    def __init__(self, age=1):
        print('Un nouveau animal')
        self.age = age

        # Mettre en place un compteur pour avoir combien de fois ma classe a été creer
        Animal.attribut_class += 1

class Cat(Animal):
    # le compteur de la classe parent a été appelé implicitement
    # donc l'attribut de class animal
    pass



scoby = Animal(25)
scoby2 = Animal(26)
scoby3 = Animal(27)


print(scoby.age)
print(Animal.attribut_class)

cat1 = Cat()
print(Animal.attribut_class)

##
## Les attributs de classe peuvent être utilisés comme des constantes au niveau de la classe (ce qui est la manière dont nous les utilisons dans MP3FileInfo),
# mais ils ne sont pas vraiment des constantes. Vous pouvez également les modifier. Il n'y a pas de constantes en Python. Tout est modifiable en faisant un effort.
##