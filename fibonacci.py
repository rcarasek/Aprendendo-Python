def fibonacci(num):
    primeiro = 0
    segundo = 1
    sequencia = [0, 1]

    if num < 3:
        print("nao deu !!!")
    else:
        proximo = primeiro + segundo
        print(sequencia)
        sequencia = sequencia + proximo
        print(sequencia)

        primeiro = segundo
        segundo = proximo

    return sequencia

fibonacci(6)  # [0, 1, 1, 2, 3, 5]
