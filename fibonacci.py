def fibonacci(num):
    a = 0
    sequencia = [0, 1]
    print(sequencia)

    proximo = sequencia[a] + sequencia[a + 1]
    sequencia.append(proximo)
    print(sequencia)

    primeiro = segundo
        segundo = proximo

    return sequencia

fibonacci(6)  # [0, 1, 1, 2, 3, 5]
