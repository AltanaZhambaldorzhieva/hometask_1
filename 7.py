for x1 in '123456789':
    for x2 in '0123456789':
        for x3 in '0123456789':
            for x4 in '0123456789':
                s = x1 + x2 + x3 + x4
                s1 = int(x1) * int(x2)
                s3 = int(x3) * int(x4)
                m1 = str(max(s1, s3))
                m2 = str(min(s1, s3))
                num = m1 + m2
                if num == '124':
                    print(s)
                    break

# Ответ: 1426
