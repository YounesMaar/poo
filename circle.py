from math import pi


class cercle: 
    def __init__(self, a, b, r):
        self.a = a 
        self.b = b
        self.r = r

    def surface(self):

        self.surface = pi * self.a * self.r**2

        print(self.surface)
        

    def perimetre(self):

        self.perimetre = 2 * pi * self.a * self.r

        print(self.perimetre)
        
    def equation(self, y, x):
        
        self.equation = (x - self.a) ** 2 + (y-self.b) **2 - (self.r**2)

        return self.equation

    def test_appartenance(self, x, y): 

        if self.equation == 0: 
            
            print(f'le point: ({x},{y}) appartient au cercle ')

        else: 
            print(f'le point: ({x},{y}) n\'appartient pas au cercle')

    
