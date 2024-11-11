class Add:
    def __init__(self, a, b):  
        self.a = a
        self.b = b

    def s(self):
        return self.a * self.b 

a = Add(7, 7)
print(a.s())  