# liste non modifiable
mon_tuple = ('Sam', True, 27, ['mma', 'box thai', 'moto'])

print(mon_tuple[0])

# mon_tuple[0] erreur

mon_tuple[3][0] = 'Judo'
print(mon_tuple)

mon_tuple[3].append('toto')
print(mon_tuple)
