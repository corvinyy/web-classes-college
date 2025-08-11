class Retangulo:
    def __init__(self, base, altura):
        
        self.base = base
        self.altura = altura

    
    def calculaPerimetro(self):
        perimetro = (self.base * 2) + (self.altura * 2)
        print(perimetro)

    def calculaArea(self):
        area = self.base * self.altura
        print(area)

while True:
    r1 = Retangulo(10, 4)
    r1.calculaPerimetro()
    r1.calculaArea()
    break