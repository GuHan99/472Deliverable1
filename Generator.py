import random

pattern = ['4 10']


def get_pattern(level):
    level_array = []
    if level is '1':
        level_array = ['r', 'r', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'b', 'b', 'w', 'w', 'e']
    elif level is '2':
        level_array = ['r', 'r', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'w', 'w', 'y', 'y', 'e']
    elif level is '3':
        level_array = ['r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'w', 'w', 'y', 'y', 'g', 'g', 'e']
    elif level is '4':
        level_array = ['r', 'r', 'r', 'r', 'b', 'b', 'w', 'w', 'y', 'y', 'g', 'g', 'p', 'p', 'e']

    list = {}
    for i in level_array:
        random_num = random.randint(0, 14)
        while random_num in list.keys():
            random_num = random.randint(0, 14)
        list[random_num] = i
    sort_list = sorted(list.items())
    result = []
    for i in sort_list:
        result.append(i[1])
    result_ = ' '.join(result)

    return result_


sample_result = ''
for i in pattern:
    level = i.split(' ')[0]
    amount = int(i.split(' ')[1])
    for x in range(amount):
        result = get_pattern(level=level)
        sample_result += result + '\n'

with open('./input.txt', 'w+') as f:
    f.write(sample_result)


