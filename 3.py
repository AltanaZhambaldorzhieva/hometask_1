for x1 in '123456789':
    for x2 in '0123456789':
        for x3 in '0123456789':
            s_1 = int(x1) * int(x2)
            s_2 = int(x2) * int(x3)
            x = str(max(s_1, s_2)) + str(min(s_1, s_2))
            if x == '123':
                print(x1 + x2 + x3)

# Ответ: 134