class A:
    def m1(self):
        print('La méthode m1 de la classe A')


class B(A):
    def m1(self):
        print('La méthode m1 de la classe B')


class C(B):
    def m1(self):
        print('La méthode m1 de la classe C')


class D(B, C):
    def m1(self):
        print('La méthode m1 de la classe D')


# le MRO en python
ma_class = D()
ma_class.m1()

print(D.mro())

# Eh bien  c'est la régle du premier chemin directe vers la classe la plus profonde qui a la priorité sur la
# gauche-droite
# la classe D herite de la classe B qui elle meme herite de la classe A.
