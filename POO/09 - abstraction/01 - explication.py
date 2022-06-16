class Lion:

    def nourrir(self):
        print('Nourrir le lion avec le steack de gazelle')


class Panda:

    def nourrir(self):
        print('Nourrir le panda avec du bambou')


class Koala:

    def nourrir(self):
        print('nourrir avec des feuilles d\'eucalyptus')


# si on souhaite les nourrir

lion = Lion()
lion.nourrir()

panda = Panda()
panda.nourrir()

koala = Koala()
koala.nourrir()

# le probleme c'est que si on doit nourrir des centaines d'animaux le processus sera long et complexe et difficilement
# maintenable

list_animal = [lion, panda, koala]

# for animal in list_animal:
# on sait pas quelle méthode appelée

# la solution sera l'abstraction
