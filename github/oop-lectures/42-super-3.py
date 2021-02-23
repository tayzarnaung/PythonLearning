class A:
    def foo(self):
        print("A")


class B(A):
    def foo(self):
        print("B")


class C(A):
    def foo(self):
        print("C")
        super(C, self).foo()


class D(C, B):
    def foo(self):
        print("D")
        super(D, self).foo()
        # super().foo()

d = D()
d.foo()
print(D.mro())