def mergeSort(lista):

    if len(lista) > 1:
        meio = len(lista)//2
        listaDaEsquerda = lista[:meio]
        listaDaDireita = lista[meio:]

        mergeSort(listaDaEsquerda)
        mergeSort(listaDaDireita)

        i = 0
        j = 0
        k = 0

        while i < len(listaDaEsquerda) and j < len(listaDaDireita):

            if listaDaEsquerda[i] < listaDaDireita[j]:
                lista[k]=listaDaEsquerda[i]
                i += 1
            else:
                lista[k]=listaDaDireita[j]
                j += 1
            k += 1

        while i < len(listaDaEsquerda):

            lista[k]=listaDaEsquerda[i]
            i += 1
            k += 1

        while j < len(listaDaDireita):
            lista[k]=listaDaDireita[j]
            j += 1
            k += 1


lst = [529,584,172,227,490,591,192,175,603,510,631,157,650,400,116,568,602,698,547,53,730,43,45,119,21,527,733,333,38,954,735,567,537,907,793,27,497,985,202,100,495,833,257,144,232,372,711,834,70,257,887,800,300,932,918,320,458,650,653,496,604,387]
mergeSort(lst)
print("lista ordenada %s" %lst) 