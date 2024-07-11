def per(n):
    m = str(bin(n)[2:])
    m += str(bin(n % 4)[2:])
    k = int(m, 2)
    return k


c = 0
for i in range(1000000000, 1789456123 + 1):
    if per(i):
        c += 1
print(c)

# Ответ: -