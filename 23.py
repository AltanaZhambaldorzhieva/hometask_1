for x1 in range(1, 60):
    for x2 in range(1, 60):
        for x3 in range(1, 60):
            s = '0' + x1 * '1' + x2 * '2' + x3 * '3'
            while ('01' in s) or ('02' in s) or ('03' in s):
                s = s.replace('01', '2302', 1)
                s = s.replace('02', '10', 1)
                s = s.replace('03', '201', 1)
            if s.count('1') == 50 and s.count('2') == 12 and s.count('3') == 7:
                print(x1)
                break

# Ответ: 2