class Animal:

    def __init__(self):
        print('Un animal')
        self.age = 0

    def vieillir(self):
        self.age += 1


scoby = Animal()
print(scoby.age)

# Appeler la méthode
scoby.vieillir()

print(scoby.age)