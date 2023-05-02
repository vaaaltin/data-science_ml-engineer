class A:
    def __init__(self, value, mult):
        self.value = value
        self.mult = mult
        self.out = []
        print("class A")

    def fun(self):
        for _ in range(self.mult):
            self.out.append(self.value)

class B(A):
    def fun(self):
        for _ in range(self.mult*2):
            self.out.append(self.value)
        
        print(self.out)

class C(B):
    pass

c = C("hat", 3)
c.fun()