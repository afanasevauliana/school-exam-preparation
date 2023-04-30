for n in range(1, 100):
    A = '0' + n * '1' + n * '2' + '0'
    while '00' not in A:
        A = A.replace('011', '20', 1)
        A = A.replace('022', '10', 1)
        A = A.replace('01', '220', 1)
        A = A.replace('02', '110', 1)
        B = A
        if (B.count('1') == 47) and (B.count('2') < 70):
            print(B.count('2'))