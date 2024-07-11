for x2 in range(3, 10000 + 1):
    s = '5' + x2 * '2'
    while ('52' in s) or ('1122' in s) or ('2222' in s):
        if '52' in s:
            s = s.replace('52', '11', 1)
        elif '2222' in s:
            s = s.replace('2222', '5', 1)
        elif '1122' in s:
            s = s.replace('1122', '25', 1)
    if s.count('1') + s.count('2') * 2 + s.count('5') * 5 == 64:
        print(x2)
        break

# Ответ: 152