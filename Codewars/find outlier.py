def find_outlier(integers):
    parzyste = None
    sum = 0
    for i in range(3):
        sum += integers[i] % 2
    
    if (sum == 0) or (sum == 1):
        for i in integers:
            if i % 2 != 0:
                return i
    else:
        for i in integers:
            if i % 2 == 0:
                return i
