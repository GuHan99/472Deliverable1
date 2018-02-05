
def isValid(str):
    bool = True
    order_array = str.split(' ')
    if len(order_array) != 15:
        print('Not exactly 15 candies in the box')
        bool = False
        return bool
    for i in order_array:
        if not (i.isalpha() and len(i) == 1):
            print('input should be a character')
            bool = False
            return bool
    return bool


def empty(str):
    if str is 'E':
        return '*'
    else:
        return str

def present(str):
    order_array = str.split(' ')
    refined_array = list(map(lambda x: x.upper(), order_array))
    # refined_array = list(map(lambda x: empty, refined_array))

    print('%s %s %s %s %s' % (refined_array[0], refined_array[1], refined_array[2], refined_array[3], refined_array[4]))
    print('%s %s %s %s %s' % (refined_array[5], refined_array[6], refined_array[7], refined_array[8], refined_array[9]))
    print('%s %s %s %s %s' % (refined_array[10], refined_array[11], refined_array[12], refined_array[13], refined_array[14]))




