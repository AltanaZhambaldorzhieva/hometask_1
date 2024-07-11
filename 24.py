k = []
for x1 in range(1, 1000):
    s = '1' * x1
    while '111' in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '11', 1)
    s1 = s.count('1')
    k.append(s1)
    m = max(k)
    if s.count('1') == m:
        print(len(s))

# Ответ: 1