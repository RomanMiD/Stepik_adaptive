summ = 0
sum_squares= 0
while True:
    a = int(input())
    summ+= a
    sum_squares+=a**2
    if summ == 0:
        break
print(sum_squares)