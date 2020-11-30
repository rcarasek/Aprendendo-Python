def fibonacci(num):
    a = 0
    sequencia = [0, 1]

    while a < num-1:
        print(sequencia)
        proximo = sequencia[a] + sequencia[a + 1]
        sequencia.append(proximo)
        a = a + 1

    return sequencia

x = input('Quantos itens?')
x = int(x)
fibonacci(x)
print(x)
