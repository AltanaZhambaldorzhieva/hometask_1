def per(n):
    m = str(bin(n)[2::])
    m += str(m.count('1') % 2)
    m += str(m.count('1') % 2)
    r = int(m, 2)
    return r


for i in range(1, 1000):
    if per(i) > 125:
        print(i)
        break

# Ответ: 31