# source= 'https://stepik.org/lesson/27987/step/1?adaptive=true&unit=9186'
# Floor-space of the room

# Residents of the Malevia country often experiment with the plan of their rooms. Rooms can be triangular, rectangular and round.
# To quickly calculate the floorage it is required to write a program, which gets the type of the room shape
#  and the relevant parameters as input - the program should output the area of the resulting room.

# The value of 3.14 is used instead of the number π in Malevia.

# Input format used by the Malevians:
# triangle
# a
# b
# c
# where a, b and c — lengths of the triangle sides.
# rectangle
# a
# b
# where a and b —lengths of the rectangle sides.
# circle
# r
# where r — circle radius.
# Sample Input 1:
# rectangle
# 4
# 10
# Sample Output 1:
# 40.0
# Sample Input 2:
# circle
# 5
# Sample Output 2:
# 78.5
# Sample Input 3:
# triangle
# 3
# 4
# 5
# Sample Output 3:
# 6.0
figure = input()
type_figure = ['triangle', 'rectangle', 'circle']
if figure == type_figure[0]:
    a, b, c = [float(input()) for i in range(3)]
    p = (a + b + c) / 2
    s = (p* (p-a) * (p-b) * (p-c)) ** 0.5
elif figure == type_figure[1]:
    a,b=int(input()), int(input())
    s=a * b
elif figure == type_figure[2]:
    s = int(input())**2*3.14
else:
    print('ti eban?')
print(s)