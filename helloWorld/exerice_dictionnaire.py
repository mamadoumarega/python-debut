# Donner la possibilité à l'internaute de taper un chiffre ex 2021
# parcourir chaque caractere de la string et le transformer en lettre
# 2 deviendra deux : deux zéro deux un

chiffre = {
    '0': "zéro",
    '1': "un",
    '2': "deux",
    '3': "trois",
    '4': "quatre",
    '5': "cinq",
    '6': "six",
    '7': "sept",
    '8': "huit",
    '9': "neuf"
}

number = input('enter a number ')
for x in number:
    if number.isnumeric():
        print(chiffre[x], end=' ')
    else:
        print('entrer un chiffre')