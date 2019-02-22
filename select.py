def select(l):
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            min_idx = i
            if l[min_idx] > l[j]:
                tmp = l[min_idx]
                l[min_idx] = l[j]
                l[j] = tmp
    return l

print(select([9,7,1,3,8]))