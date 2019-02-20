def bubble_sort(l):
    i = 0
    while i < len(l):
        j = 1
        while j < len(l) - i:
            if l[j] < l[j - 1]:
                tmp = l[j]
                l[j] = l[j - 1]
                l[j - 1] = tmp
            j += 1
        i +=1
    return l


l = [2, 4, 3, 1]
print(bubble_sort(l))