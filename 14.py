alf = 'ABRTY'
k = 0

for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    s = x1 + x2 + x3 + x4 + x5
                    k += 1
                    if x1 + x2 != 'AA' and x2 + x3 != 'AA' and x3 + x4 != 'AA' and x4 + x5 != 'AA':
                        if s.count('Y') == 0:
                            print(k)
                            break

# Ответ: 131