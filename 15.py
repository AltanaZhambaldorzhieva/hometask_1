alf = 'ABELRYI'
k = 0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            s = x1 + x2 + x3
            if s.count('B') == 1:
                k += 1
                if s.count('A') == 0:
                    print(k)
                    break

# Ответ: 20