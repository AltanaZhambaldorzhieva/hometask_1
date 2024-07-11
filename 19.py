k = []
for x1 in range(1, 50):
    for x2 in range(1, 50):
        for x3 in range(1, 50):
            s = '0' + '1' * x1 + '2' * x2 + x3 * '3' + '0'
            while not ('00' in s):
                s = s.replace('01', '220', 1)
                s = s.replace('02', '1013', 1)
                s = s.replace('03', '120', 1)
            if s.count('1') == 13 and s.count('2') == 18:
                m = x1 + x2 + x3 + 2
                k.append(m)
print(max(k))

# Ответ: 16