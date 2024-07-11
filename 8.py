def per(n):
    m = str(bin(n)[2::])
    if int(n) % 2 == 0:
        m += '00'
    else:
        m += '11'
    r = int(m, 2)
    return r


for n in range(1, 1000):
    if per(n) < 134:
        print(n)

# Ответ: 32