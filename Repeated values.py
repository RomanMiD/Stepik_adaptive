inp = input().split()
inp.sort()
result = []
print(inp)
for i in range(len(inp),-1):
    if inp[i]==inp[i-1]:
        result.append(inp[i])

        
print(result)