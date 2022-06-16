import random
from abc import ABC, abstractmethod


##################################--- DEFINITION DES CLASSES ----##################################


# classe abstraite joueur qui sera héritée par Hero & Ennemi
class Joueur(ABC):

    #######################---properties---####################

    @property
    def marbles(self):
        pass

    @property
    def name(self):
        pass

    #######################---methods---#####################
    @marbles.setter
    def marbles(self):
        pass

    @name.setter
    def name(self, name):
        pass


# Hero que le joueur incarnera

class Hero(Joueur):

    #######################---properties---####################

    def __init__(self, name, marbles, gain, loss, scream_war):
        self.__name = name
        self.__marbles = marbles
        self.__gain = gain
        self.__loss = loss
        self.__scream_war = scream_war

    @property
    def marbles(self):
        return self.__marbles

    @property
    def name(self):
        return self.__name

    @property
    def gain(self):
        return self.__gain

    @property
    def loss(self):
        return self.__loss

    @property
    def scream_war(self):
        return self.__scream_war

    #######################---methods---#####################
    @marbles.setter
    def marbles(self, marbles):
        self.__marbles = marbles

    @name.setter
    def name(self, name):
        self.__name = name

    @gain.setter
    def gain(self, gain):
        self.__gain = gain

    @loss.setter
    def loss(self, loss):
        self.__loss = loss

    @scream_war.setter
    def scream_war(self, scream_war):
        self.__scream_war = scream_war


# Ennemis que le joueur affrontera
class Ennemi(Joueur):

    def __init__(self, name):
        self.__name = name
        self.__marbles = random.randint(1, 20)
        self.__age = random.randint(18, 80)

    @property
    def marbles(self):
        return self.__marbles

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, n):
        self.__name = n

    @marbles.setter
    def marbles(self, m):
        self.__marbles = m

    @age.setter
    def age(self, a):
        self.__age = a


######################################################################################################

### Génération des héros :

h1 = Hero('Seong Gi-hun', 15, 1, 2, 'bb')
h2 = Hero('Kang Sae-byeok', 25, 2, 1, 'nn')
h3 = Hero('Cho Sang-woo', 35, 3, 0, 'jj')
liste_hero = [h1, h2, h3]

## Génération des ennemis
list_ennemis = []
for i in range(20):
    list_ennemis.append(Ennemi(f'Ennemi {i + 1}'))


##################################---- DEFINITION DES FONCTIONS--##########################################
##fonction choix difficulte
def choix_difficulte():
    while True:
        print('Veuillez choisir votre niveau de difficulté :')
        choix = input('1. Facile     2. Difficile     3. Impossible\n')
        if choix.isnumeric():
            if 3 >= int(choix) >= 1:
                return int(choix) - 1
                break


# fonction choix personnage
def choix_perso():
    while True:
        print('Veuillez choisir votre personnage :')
        choix = input('1. Seong Gi-hun     2. Kang Sae-byeok     3. Cho Sang-woo\n')
        if choix.isnumeric():
            if 3 >= int(choix) >= 1:
                return int(choix) - 1
                break


# fonction qui prend le pari de l'utilisateur, définit si il a perdu ou gagné
# Arguments : Joueur actuel, Ennemi
# Retour : Le nombre de billes du joueur après son pari
def isPair(player, ennemi):
    while True:
        choix = input(f'Votre ennemi est {ennemi.name}. Son nombre de billes est-il pair ?\n(o)ui ou (n)on >').lower()
        if choix == 'n' or choix == 'o':
            break
    if (ennemi.marbles % 2 == 0 and choix == 'o') or (ennemi.marbles % 2 == 1 and choix == 'n'):
        print(
            f'Gagné ! Votre enemi avait {ennemi.marbles} billes. Votre bonus vous ajoute {player.gain} billes supplémentaires.')
        player.marbles += (ennemi.marbles + player.gain)
    else:
        print(
            f'Perdu... Votre enemi avait {ennemi.marbles} billes. Votre malus vous enlève {player.loss} billes supplémentaires.')
        player.marbles -= (ennemi.marbles + player.loss)
    return player.marbles


def isOlder(player, ennemi):
    while True:
        choix = input(
            BOLD + f"Votre ennemi a {ennemi.age} ans et n'a pas toute sa tête, voulez-vous tricher et lui voler ses billes ?\n(o)ui ou (n)on >" + ENDC).lower()
        if choix == 'o' or choix == 'n':
            break
    if choix == 'o':
        player.marbles += ennemi.marbles
        print(
            f"Vous avez arnaqué votre ennemi. Il avait {ennemi.marbles} billes.\nVous ne bénéficiez pas du bonus de {player.gain} billes pour ce round.")
        return True
    else:
        return False


def jeu():
    nb_rounds = liste_difficulte[choix_difficulte()] - 1
    hero_actuel = liste_hero[choix_perso()]
    print(f'Vous avez choisis {hero_actuel.name}, le jeu durera {nb_rounds} rounds.')

    essai = 0

    while essai < nb_rounds:

        arnaque = False
        ennemi_actuel = list_ennemis[random.randint(1, len(list_ennemis) - 1)]
        if ennemi_actuel not in liste_loosers:
            print(WARNING + f'---------------------Round {essai + 1}/{nb_rounds + 1}---------------------' + ENDC)
            liste_loosers.append(ennemi_actuel)
            print(f'Vous avez actuellement ' + OKBLUE + f'{hero_actuel.marbles} billes.' + ENDC)
            if ennemi_actuel.age > 70:
                arnaque = isOlder(hero_actuel, ennemi_actuel)

            if not arnaque:
                if (isPair(hero_actuel, ennemi_actuel)) < 1:
                    break
        else:
            continue
        essai += 1
    return hero_actuel.marbles


######################################################################################################

##################################----PROGRAMME PRINCIPAL----#########################################
if __name__ == '__main__':

    OKBLUE = '\033[94m'  # couleur bleue qu'on printera lors de l'affichage des billes actuelles
    WARNING = '\033[93m'  # couleur pour l'annoncement des rounds
    OKGREEN = '\033[92m'  # couleur verte lorsque le joueur gagne le jeu
    FAIL = '\033[91m'  # couleur rouge lorsque le joueur perd le jeu
    BOLD = '\033[1m'  # texte en gras lorsqu'un vieux apparaît
    ENDC = '\033[0m'  # stoper la couleur du dessus

    # liste des rounds des difficultés (ordre croissant)
    liste_difficulte = [5, 10, 20]

    # liste des ennemis déjà battus
    liste_loosers = []

    res = jeu()

    if res < 1:
        print(FAIL + 'Vous avez échoué aux jeu des billes. Un garde va venir vous tuer' + ENDC)
    else:
        print(
            OKGREEN + f'Félicitation vous avez gagné en finissant avec {res} billes ! Vous avez gagné 46.6 milliards de won sud-coréens.' + ENDC)

######################################################################################################
