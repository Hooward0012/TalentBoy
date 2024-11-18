sum = 0

for i in range(10):
    sum += i
    for j in range(5):
        sum += i
        print(f'i:{i}, j:{j}, sum:{sum} ')