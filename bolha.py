def bubble_sort(lst):
    print(len(lst))
    for passnum in range(len(lst) - 1, 0, -1):
        # print(passnum)
        for i in range(passnum):
            if lst[i] > lst[i + 1]:
                lst[i + 1], lst[i] = lst[i],lst[i + 1]
"""                
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
"""

lst = [54,26,93,17,77]
bubble_sort(lst)
print("lista ordenada %s" %lst) 
