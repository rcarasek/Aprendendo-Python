def bubble_sort(lst):
    for passnum in range(len(lst) - 1, 0, -1):
        for i in range(passnum):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp


lst = [54,26,93,17,77,31,44,55,20,1,155,2,3,9,4,200,1]
bubble_sort(lst)
print("sorted %s" %lst) 
