def per(n):
    m = str(bin(n)[2:])
    if int(m) % 2 == 0:
        m += '0'
        num = '10' + m[2::]
        num_1 = int(num, 2)
    else:
        m += '1'
        num = '11' + m[2::]
        num_1 = int(num, 2)
    return num_1


for n in range(1, 1000):
    if per(n) < 35:
        print(n)

# Ответ: 24
