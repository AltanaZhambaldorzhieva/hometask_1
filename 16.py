alf = 'OLЬGA'

k = 0
for x1 in 'OLGA':
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    s = x1 + x2 + x3 + x4 + x5
                    if s.count(x1) == 1 and s.count(x2) == 1 and s.count(x3) == 1 and s.count(x4) == 1 and s.count(x5) == 1:
                        if (x2 + x3 not in 'AЬ' or 'OЬ') and (x3 + x4 not in 'AЬ' or 'OЬ') and (x4 + x5 not in 'AЬ' or 'OЬ'):
                            k += 1
print(k)

# Ответ: -
