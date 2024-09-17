import random
numbers = list(range(3, 21))
random_num = random.choice(numbers)
print(f"Рандомное число: {random_num}")
list_= []
for i in range(1, random_num):
    for j in range(1, random_num):
        if (i + j) > 0 and random_num % (i + j) == 0:
            pair = tuple(sorted((i,j)))
            if pair[0] != pair[1] and pair not in list_:
                list_.append(pair)
list_.sort(key = lambda x: x[0])
output = ''.join(f'{pair[0]}{pair[1]}' for pair in list_)
if output:
    print(f"числа для вставки {random_num} - {output}")
