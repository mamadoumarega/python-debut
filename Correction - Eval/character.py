from abc import ABC, abstractmethod

class Character(ABC):

    def __init__(self, name, marbles):
        self.__name = name
        self.__marbles = marbles
        self.__dead = False

    @property
    def name(self):
        return self.__name

    @property
    def marbles(self):
        return self.__marbles

    @property
    def dead(self):
        return self.__dead

    @name.setter
    def name(self, name):
        self.__name = name

    @marbles.setter
    def marbles(self, marbles):
       self.__marbles = marbles

    @dead.setter
    def dead(self, dead):
        self.__dead = dead

    @abstractmethod
    def win(self):
        print('gagné')

    @abstractmethod
    def lose(self):
        print('perdu')

    @abstractmethod
    def introduce_my_self(self):
        pass