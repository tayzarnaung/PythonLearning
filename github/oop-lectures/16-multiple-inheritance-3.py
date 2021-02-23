# By default, the lookup should go D -> B -> A -> C -> A.
# the MRO skips the classes which occur multiple times in the path.

# Hence the lookup will be D -> B -> C -> A.


class A(object):

    def dothis(self):
        print("doing this in A")


class B(A):
    pass


class C(A):
    def dothis(self):
        print("doing this in C")


class D(B, C):
    pass

d_instance = D()
d_instance.dothis()

print("\nPrint the Method Resolution Order")
print(D.mro())
