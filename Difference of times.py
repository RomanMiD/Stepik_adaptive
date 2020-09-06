h1, m1, s1, h2, m2, s2 = [int(input()) for i in range(6)]
seconds = (h2 - h1)*3600 + (m2 - m1)*60 + (s2 - s1)
print(seconds)