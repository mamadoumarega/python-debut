import random

from hero import Hero
from enemy import Enemy
from utils import Utils


class Game(Utils):

    # Attributs de classe
    levels_of_difficulty = {
        "1": 5,
        "2": 10,
        "3": 20
    }

    list_heroes_name = ['Seong Gi-hun', 'Kang Sae-byeok', 'Cho Sang-woo']

    def __init__(self):
        self.__levels = 0
        self.__hero_selected = {}
        self.__current_enemy = {}
        self.__enemy_list = []
        self.__heroes_list = []

    ##
    ## GETTERS
    ##
    @property
    def levels(self):
        return self.__levels

    @property
    def hero_selected(self):
        return self.__hero_selected

    @property
    def current_enemy(self):
        return self.__current_enemy

    @property
    def enemy_list(self):
        return self.__enemy_list

    @property
    def heroes_list(self):
        return self.__heroes_list

    ##
    ## SETTERS
    ##
    @levels.setter
    def levels(self, levels):
        self.__levels = levels

    @hero_selected.setter
    def hero_selected(self, hero_selected):
        self.__hero_selected = hero_selected

    @current_enemy.setter
    def current_enemy(self, current_enemy):
        self.__current_enemy = current_enemy

    @enemy_list.setter
    def enemy_list(self, enemy_list):
        self.__enemy_list = enemy_list

    @heroes_list.setter
    def heros_list(self, heroes_list):
        self.__heroes_list = heroes_list


    ##
    ## METHOD THAT CREATES HEROES
    ##
    def __create_heroes(self):
        print('Heroes creation...')
        i = 1
        loss = 2
        while i <= 3:
            hero_name = Game.list_heroes_name[i - 1]
            marbles = i * 15
            malus = loss
            bonus = i
            self.heroes_list.append(Hero(hero_name, marbles, malus, bonus))
            loss -= 1
            i += 1


    ##
    ## METHOD THAT CREATES ENEMIES
    ##
    def __create_enemies(self):
        print('Enemies creation...')
        i = 1
        while i <= 20:
            self.__enemy_list.append(Enemy(f"Enemy n° {i}", self.random_values(1, 20), self.random_values(35, 100)))
            i += 1

    ##
    ## METHOD THAT ASK PLAYER TO CHOOSE A LEVEL OF DIFFICULTY
    ##
    def __ask_level_of_dificulty(self):
        while True:
            level_choice = input('Choose a level between (1) - Easy / (2) - Hard / (3) - Impossible')
            if Game.levels_of_difficulty.get(level_choice) is not None:
                self.__levels = Game.levels_of_difficulty.get(level_choice)
                print(f'You are brave ! You will have to fight {self.__levels} enemies !')
                break

    ##
    ## METHOD THAT ASK PLAYER TO CHOOSE A HERO TO PLAY THE GAME
    ##
    def __ask_to_choose_hero(self):
        # INTRODUCE HEROES
        for index, hero in enumerate(self.__heroes_list):
            hero.introduce_my_self(index + 1)

        while True:
            hero_choice = input('Which hero will you be ?')
            if hero_choice.isnumeric() and 0 < int(hero_choice) <= len(self.__heroes_list):
                print('toto')
                self.__hero_selected = self.__heroes_list[int(hero_choice) -1]
                break

        print(f'Welcome to you {self.hero_selected.name} ! Get ready for the fight !')


    ##
    ## METHOD THAT ASK PLAYER TO CHOOSE A SCREAM WAR IN CASE OF VICTORY
    ##
    def __ask_scream_war(self):
        scream = input('Please enter a scream war in case of victory !')
        self.hero_selected.scream_war = scream

    ##
    ## METHOD STARTS ALL THE FIGHTS
    ##
    def __fights(self):

        i = 1
        while i <= self.levels and not self.hero_selected.dead:
            ## Choose a random enemy
            self.current_enemy = random.choice(self.enemy_list)

            print(f'Fight n°{i} - You still have {self.hero_selected.marbles} marbles to fight !')
            ## Introduce the encounter
            self.current_enemy.introduce_my_self()

            win_the_fight = False
            cheat = False
            ## Check if current enemy is older tha 70
            if self.current_enemy.age > 70:
                ## choose to cheat or not
                cheat = self.hero_selected.cheat()
                if cheat:
                    ## If I cheat I win the game directly win no bonus
                    self.hero_selected.win(self.current_enemy.marbles)
                    self.current_enemy.lose()
                    self.enemy_list.remove(self.current_enemy)

            if not cheat:
                ## If I don't cheat I have to choose an odd or even number
                win_the_fight = self.hero_selected.choose_odd_or_even(self.current_enemy.marbles)

                if win_the_fight:
                    self.hero_selected.win(self.hero_selected.gain, self.current_enemy.marbles)
                    self.current_enemy.lose()
                    # Take out the enemy from the game
                    self.enemy_list.remove(self.current_enemy)
                else:
                    self.hero_selected.lose(self.current_enemy.marbles)
                    self.current_enemy.win()

            i += 1

        else:
            if not self.hero_selected.dead:
                self.hero_selected.scream()
            else:
                print(f'HAHAHAHAHA ! You lost the game fighting with {self.current_enemy.name} ! See in you in hell !')


    ##
    ## METHOD THAT STARTS THE GAME
    ##
    def start(self):
        print('Game starting')
        self.__create_heroes()
        self.__create_enemies()
        self.__ask_level_of_dificulty()
        self.__ask_to_choose_hero()  # dans cette méthode je vais faire les héros se présenter
        self.__ask_scream_war()
        self.__fights()