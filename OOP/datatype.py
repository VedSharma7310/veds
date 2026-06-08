class Fraction:
    def __init__(self,n,d):
        self.n = n
        self.d = d
        
    def __str__(self):
        return f"{self.n}/{self.d}"
    
    def __add__(self,other):
        temp_num = (self.n*other.d)+(other.n*self.d)
        temp_den = (self.d*other.d)
        return f"{temp_num}/{temp_den}"
    
    def __sub__(self,other):
        temp_num = (self.n*other.d)-(other.n*self.d)
        temp_den = (self.d*other.d)
        return f"{temp_num}/{temp_den}"
    
    def __mul__(self,other):
        temp_num = self.n*other.n
        temp_den = self.d*other.d
        return f"{temp_num}/{temp_den}"
    
    def __truediv__(self, other):
        temp_num = self.n*other.d
        temp_den = self.d*other.n
        return f"{temp_num}/{temp_den}"
        
ob = Fraction(3,4)
ob2 = Fraction(5,6)

print(ob+ob2)
print(ob-ob2)
print(ob*ob2)
print(ob/ob2)
