class Media:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.resultado = 0


    def calcmedia(self):
        self.resultado = (self.n1 + self.n2) / 2
        return self.resultado


    def maiornota(self):
        if self.n1 > self.n2:
            return self.n1
        else:
            return self.n2