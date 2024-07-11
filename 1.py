for x1 in '123456789':
    for x2 in '0123456789':
        for x3 in '0123456789':
            sum_1 = int(x1) + int(x2)
            sum_2 = int(x2) + int(x3)
            x = str(max(sum_1, sum_2)) + str(min(sum_1, sum_2))
            if x == '1412':
                s = x1 + x2 + x3
                print(s)

# Ответ: 395