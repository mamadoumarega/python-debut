from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def nourir(self):
        pass


class Lion(Animal):

    def nourrir(self):
        print('Nourrir le lion avec le steack de gazelle')

    def methode_lion(self):
        print('ttttttttttt')


class Panda(Animal):

    def nourrir_panda(self):
        print('Nourrir le panda avec du bambou')


class Koala(Animal):

    def nourrir_koala(self):
        print('nourrir avec des feuilles d\'eucalyptus')
        pass


# affichage
lion = Lion()


panda = Panda()

koala = Koala()
