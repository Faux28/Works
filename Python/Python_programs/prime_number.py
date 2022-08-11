x = [1, -3, 6, 9, 8, 33, 5, 11, 2, 3, 3, 6, -75, 10, 4, 0]

result = []

en_x = list(set(x))  # to remove duplicate
en_x.sort()
print(en_x)

for i in en_x:
    if i <= 1:
        continue
    for a in range(2, i):
        if i % a == 0:
            break
    else:
        result.append(i)

print(result)


"""
To find the range of prime numbers
"""
num = int(input('enter the number'))
if not num <= 1:
    pn = []
    for i in range(2, num+1):
        for n in range(2, i):
            if i % n == 0:
                # print(f'{i} equals {n} * {i//n}')
                break
        else:                               # we can use else for loop
            pn.append(i)
            # print(f'{i} is a prime number')
    print(f'The prime numbers are {pn}')
else:
    print(f'{num} is not prime number')
