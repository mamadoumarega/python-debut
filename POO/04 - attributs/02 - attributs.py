class Animal:

    def __init__(self):
        print('Un nouveau animal')
        self.age = 0


scoby = Animal()
# Pour acceder à l'age
print(scoby.age)
scoby.age = 2
print(scoby.age)
