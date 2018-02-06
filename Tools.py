
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




