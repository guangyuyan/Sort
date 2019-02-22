def insert_sort(l):
    i = 0
    while i < len(l):
        for j in range(0, i):
            if l[j] > l[i]:
                l.insert(j, l.pop(i))
#                break
        i += 1
    return l

print(insert_sort([3,2,1,4,2]))