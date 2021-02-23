# Python supports multiple inheritance and uses a depth-first order when searching for methods.

# This search pattern is call MRO (Method Resolution Order)

# As per the MRO output, it starts in class D, then B, A, and lastly C.

# The method lookup flow in this case is : D -> B -> A -> C

# Both A and C contains 'dothis()'. Let's trace how the lookup happens.

class A(object):

    def dothis(self):
        print("doing this in A")


class B(A):
    pass


class C(object):
    def dothis(self):
        print("doing this in C")


class D(B, C):
    pass

d_instance = D()
d_instance.dothis()  # <== This should print from class A.

print("\nPrint the Method Resolution Order")
print(D.mro())
