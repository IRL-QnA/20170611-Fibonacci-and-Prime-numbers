a = 1
b = 0
for i in range(1, 21):
    c = a + b
    a = b
    b = c
    print(i, c)