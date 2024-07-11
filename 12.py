num = '012345678'
k = 0
m = []
for x1 in '12345678':
    for x2 in num:
        for x3 in num:
            for x4 in num:
                for x5 in num:
                    s = x1 + x2 + x3 + x4 + x5
                    k += 1
                    if s[0] > s[1] > s[2] > s[3] > s[4]:
                        m.append(k)
print(len(m))

# Ответ: 126
