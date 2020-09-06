# Учитывая положительное целое число NN. Найдите количество натуральных чисел меньше, чемNN так,
# что их сумма цифр (в десятичной системе счисления) равна сумме цифр в числе NN.
# Выведите количество таких целых чисел.

# Пример ввода :

# 123
# Пример вывода :


n = input()
k = list(n)
cnt=0
for i, item in enumerate(k):
    k[i] = int(item)
for i in range(int(n)):
    s=list(str(i))
    for j, item in enumerate(s):
        s[j] = int(item)
    if sum(k)==sum(s):
        cnt+=1
print(cnt)


# i=1
# cnt=0
# for sums in range(1,n+1):
def digits(n):
    return sum(int(d) for d in str(n))

n = int(input())
m = digits(n)
numbers = [i for i in range(n) if digits(i) == m]
print(len(numbers))