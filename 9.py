alf = 'AEKP'
k = 0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                s = x1 + x2 + x3 + x4
                k += 1
                if s.count('A') == 0:
                    print(k)
                    break

# Ответ: 86

