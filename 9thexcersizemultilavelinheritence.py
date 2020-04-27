class Electronics:
    def __init__(self, E_pro1, E_pro2, E_pro3, E_pro4):
        self.E_pro1 = E_pro1
        self.E_pro2 = E_pro2
        self.E_pro3 = E_pro3
        self.E_pro4 = E_pro4
    def Electronics_Products(self):
        print(f"Our first Electronics produnct is {self.E_pro1} and second produnct is {self.E_pro2} the 3rd produnct  is {self.E_pro3} te last produnct is {self.E_pro4}")
class pocket_products(Electronics):
    def __init__(self, E_pro1, E_pro2, E_pro3, E_pro4):
        self.E_pro1 = E_pro1
        self.E_pro2 = E_pro2
        self.E_pro3 = E_pro3
        self.E_pro4 = E_pro4
    def Electronics_Products(self):
        print(f"Our first pocket_products  is {self.E_pro1} and second produnct is {self.E_pro2} the 3rd produnct  is {self.E_pro3} te last produnct is {self.E_pro4}")
class Mobile(pocket_products):
    def __init__(self, color, Ram,Rom,Compeny):
        self.color = color
        self.Ram = Ram
        self.Rom = Rom
        self.Compeny = Compeny
    def Electronics_Products(self):
        print(f"Our mobile color  is {self.color} and Ram is {self.Ram} the Rom  is {self.Rom} te last produnct is {self.Compeny}")
sony = pocket_products("red","6GB","64GB","Sonyericson")

print(sony.color)
