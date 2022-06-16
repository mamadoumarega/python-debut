from abc import ABC, abstractmethod


class Animal(ABC):

    @property
    @abstractmethod
    def diet(self):
        return self.diet

    @property
    def alimentation(self):
        return self._alimentation

    @alimentation.setter
    def alimentation(self, aliment):
        self._alimentation = aliment
        if aliment in self.diet:
            self._alimentation = aliment
        else:
            raise ValueError(f'Cet animal ne mange pas de {aliment}')

    @abstractmethod
    def nourrir(self):
        pass


class Lion(Animal):

    @property
    def diet(self):
        return ['viande', 'steak', 'gazelle']

    def nourrir(self, time):
        print(f'Le lion mange de {self.alimentation} à {time} h')

    pass


lion = Lion()
lion.alimentation = 'viande'
lion.nourrir(15)
