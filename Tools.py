

def is_valid(str):
    bool_flag = True
    order_array = str.split(' ')
    if len(order_array) != 15:
        print('Not exactly 15 candies in the box')
        bool_flag = False
        return bool_flag
    for i in order_array:
        if not (i.isalpha() and len(i) == 1):
            print('input should be a character')
            bool_flag = False
            return bool_flag
    return bool_flag


def empty(string):
    if string is 'E':
        return '*'
    else:
        return string


def output_file(string):
    with open('./output.txt', 'w+') as f:
        f.write(string)




