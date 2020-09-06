l = input().split(' ')
k = set([x for x in l if l.count(x) > 1])
        
print(*k)