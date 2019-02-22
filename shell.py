def shell(l):
    gap = len(l)
    while gap > 1:
        gap = gap // 2
        for i in range(gap, len(l)):
            for j in range(i % gap, i, gap):
                if l[j] > l[i]:
                    l[i], l[j] = l[j], l[i]
    return l

#时间复杂度(选择合适增量)：O(n3/2)
#空间复杂度：O(n√n)
#稳定性：不稳定

