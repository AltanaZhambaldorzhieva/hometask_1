for x1 in range(0, 100):
    for x2 in range(0, 100):
        for x3 in range(0, 100):
            s = '0' + '1' * x1 + '2' * x2 + '3' * x3 + '0'
            while not ('00' in s):
                s = s.replace('01', '210', 1)
                s = s.replace('02', '320', 1)
                s = s.replace('03', '3012', 1)
            if s.count('1') == 26 and s.count('2') == 54 and s.count('3') == 48:
                ans = x1 + x2 + x3 + 2
                print(ans)

# Ответ: 36