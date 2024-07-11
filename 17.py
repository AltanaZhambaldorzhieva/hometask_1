def prost(n):
    k = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            return False
    return True


l = []
for x1 in range(0, 50):
    for x2 in range(0, 50):
        for x3 in range(0, 50):
            for x4 in range(0, 50):
                s = '0' + '1' * x1 + '2' * x2 + '3' * x3 + '4' * x4 + '0'
                while not ('00' in s):
                    s = s.replace('033', '21120', 1)
                    s = s.replace('034', '22120', 1)
                    s = s.replace('04', '220', 1)
                    s = s.replace('030', '100', 1)
                if len(s) == 65:
                    sum = s.count('1') + s.count('2') * 2 + s.count('3') * 3 + s.count('4') * 4
                    if prost(sum):
                        l.append(x4)
print(max(l))

# Ответ: -