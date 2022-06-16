from character import Character
from utils import Utils


class Hero(Character, Utils):

    def __init__(self, name, marbles, loss, gain):
        super().__init__(name, marbles)
        self.__loss = loss
        self.__gain = gain
        self.__scream_war = ''

    @property
    def loss(self):
        return self.__loss

    @property
    def gain(self):
        return self.__gain

    @property
    def scream_war(self):
        return self.__scream_war

    @loss.setter
    def loss(self, loss):
        self.__loss = loss

    @gain.setter
    def gain(self, gain):
        self.__gain = gain

    @scream_war.setter
    def scream_war(self, scream_war):
        self.__scream_war = scream_war

    ##
    ## METHODS THAT MAKES OUR HERO WIN THE CURRENT FIGHT
    ##
    def win(self, marbles_enemy, bonus=0):
        print(f"Well done, you beat this enemy, since he had {marbles_enemy} marbles >")
        print(
            f"You win {marbles_enemy} marbles from your enemy plus your bonus of {bonus} marbles")
        self.marbles += marbles_enemy + bonus


    ##
    ## METHODS THAT MAKES OUR HERO LOSE THE FIGHT
    ##
    def lose(self, marbles_enemy):
        print(f"Too bad, you lost this fight, since your enemy had {marbles_enemy} marbles >")
        print(
            f"You lose {marbles_enemy} marbles from your enemy minus your malus of {self.loss}")
        self.marbles -= (marbles_enemy + self.loss)

        # I have don't have any marbles left, I lose the entire game
        if self.marbles <= 0:
            self.dead = True


    ##
    ## METHOD THAT ASK THE PLAYER IF HE WANTS TO CHEAT OR NOT
    ##
    def cheat(self):
        while True:
            cheat_answer = input('Your enemy is old, you can cheat on him? Do you want to cheat ? (Y)es or (N)o').lower()
            if cheat_answer == 'y' or cheat_answer == 'n':
                return True if cheat_answer == 'y' else False

    ##
    ## METHODS THAT MAKES OUR HERO CHOOSE BETWEEN AND ODD OR EVEN NUMBER AND RETURN RESULT
    ##
    def choose_odd_or_even(self, marbles_enemy):
        while True:
            answer = input("What is your answer ? (1) - Odd / (2) - Even")
            if answer.isnumeric() and 0 < int(answer) < 3:
                win = self.check_odd_or_even(marbles_enemy, int(answer))
                break
        return win

    ##
    ## METHODS THAT MAKES OUR HERO SCREAM IN CASE OF VICTORY
    ##
    def scream(self):
        print(self.scream_war)

    ##
    ## METHODS THAT MAKE OUR HERO INTRODUCE HIMSELF
    ##
    def introduce_my_self(self, number_choice):
        print(f"Press ({number_choice}) to choose {self.name} ! you will start the game with {self.marbles} marbles "
              f"and a bonus of {self.__gain} marbles when you win a fight"
              f"and a malus of {self.__loss} marbles when you loose a fight")