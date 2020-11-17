class Pessoa:
    def __init__ (self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso 

p1 = Pessoa("RC",52,180,89)

print(p1.nome)
print(p1)
