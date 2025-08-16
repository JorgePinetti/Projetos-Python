class Carro:
    def __init__ (self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def apresentar (self):
        print(f'Carro escolhido : {self.modelo}, {self.marca}, {self.ano}')

c1 = Carro('Toyota', 'Hilux', 2025)
c2 = Carro('Fiat', 'Toro', 2025)

c1.apresentar()
c2.apresentar()