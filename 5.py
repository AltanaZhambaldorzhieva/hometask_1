for x1 in '123456789':
    for x2 in '0123456789':
        for x3 in '0123456789':
            for x4 in '0123456789':
                s1 = int(x1) + int(x2)
                s2 = int(x2) + int(x3)
                s3 = int(x3) + int(x4)
                m = str((s1 + s2 + s3) - max(s1, s2, s3) - min(s1, s2, s3))
                m1 = max(s1, s2, s3)
                s = m + str(m1)
                if s == '613':
                    print(x1 + x2 + x3 + x4)


# Ответ: 9424