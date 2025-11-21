class Complex:
  
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im
    def __str__(self):
        return f'{self.re} + {self.im}i'
    def __add__(self, other):
        return Complex((self.re+other.re), (self.im+other.im))
    
c1=Complex(1,2)
c2=Complex(3,4)
print(c1+c2)