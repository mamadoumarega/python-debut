class Humain:
    pass


# Instanciation d'une classe
# Je vais instancier la classe comme une fonction et creer à partir de l'objet

sam = Humain()
print(sam)
# l'objet sam a une place en mémoire qui pointe vers la position 0x0000028EB8A7EE60
sara = Humain()
print(sara)
# l'objet sara a une autre place
print(type(sara))