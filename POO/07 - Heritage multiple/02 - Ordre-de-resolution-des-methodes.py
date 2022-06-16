class A:
    def m1(self):
        print('La méthode m1 de la classe A')


class B(A):
    def m1(self):
        print('La méthode m1 de la classe B')


class C(A):
    def m1(self):
        print('La méthode m1 de la classe C')


class D(B, C):
    def m1(self):
        print('La méthode m1 de la classe D')


# le MRO en python
ma_class = D()
ma_class.m1()

print(D.mro())
