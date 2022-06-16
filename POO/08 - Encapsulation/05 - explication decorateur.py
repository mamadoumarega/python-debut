# Un décorateur c'est une fonction qui permet de modifier le comportement d'autres fonctions
# c'est util quand on veut ajouter un même code à plusiseurs fonctions
# ce sera très util dans le cadre de control commun

user = 'Tom'


def mon_decorateur(fonction):
    def control():
        print('Accès refusé')

    if user != 'Sam':
        return control

    return fonction


@mon_decorateur
def fonction1():
    print('Execution de la tache n°1')


# si le user c'est Sam
# alors éxecution de la tache n°1
fonction1()
