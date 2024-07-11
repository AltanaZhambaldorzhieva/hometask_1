k = 0
m = []
num = '0123456'
for x1 in '123456':
    for x2 in num:
        for x3 in num:
            for x4 in num:
                s = x1 + x2 + x3 + x4
                k += 1
                if s[0] > s[1] > s[2] > s[3]:
                    m.append(k)
print(len(m))

# Ответ: 35