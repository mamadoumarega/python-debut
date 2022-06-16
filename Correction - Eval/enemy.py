from character import Character


class Enemy(Character):

    def __init__(self, name, marbles, age):
        super().__init__(name, marbles)
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    ##
    ## METHODS THAT MODIFIES ENEMY'S POINTS (MARBLES)
    ##
    def win(self):
        self.marbles *= 2

    ##
    ## METHODS THAT MAKES ENEMY DIES IF HE LOSES THE FIGHT
    ##
    def lose(self):
        self.dead = True

    ##
    ## METHODS THAT MAKE THE ENEMY'S ENCOUNTER INTRO
    ##
    def introduce_my_self(self):
        print(
            f"Your are fighting {self.name} ! Your ennemy is {self.age} years old !"
        )
