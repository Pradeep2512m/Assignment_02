x = 6
Sum = 0
for i in range (999, 10000):

    Sum = sum(map(int, str(i)))

    if Sum == x:
        num = i

        result = list(set(map(int, str(num))))

        if len(result) == 4:
            print(result)