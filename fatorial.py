def fatorial(num):
    if (num < 1):
        print("Não deu!!!")
    else:
        a = num - 1
        fatorial = num
        while a > 1:
            fatorial = fatorial * a 
            a = a - 1
        print(fatorial)

    return num 

x = input('Fatorial de...?')
x = int(x)
fatorial(x)
