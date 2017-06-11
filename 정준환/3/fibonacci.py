a = 1
b = a
print(1, a)
for i in range(2, 21, 2):
    a = a + b
    print(i, b)
    if not i < 20: break
    print(i + 1, a)
    b = b + a