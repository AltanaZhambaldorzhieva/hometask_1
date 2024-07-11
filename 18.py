for x2 in range(1, 50):
    s = 10 * '1' + x2 * '2'
    while '21' in s:
        s = s.replace('21', '5', 1)
    if s.count('1') + s.count('2') * 2 + s.count('5') * 5 == 34:
        print(x2)
        break

# Ответ: 12