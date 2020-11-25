class Pessoa:
    def __init__ (self, nome, data_nasc, altura, peso):
        self.nome = nome
        self.data_nasc = data_nasc
        self.altura = altura
        self.peso = peso 

p1 = Pessoa("RC","13/05/50",1.70,89.5)

print(p1.nome, p1.altura, "m   ", p1.data_nasc)
