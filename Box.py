import time

move = {0: [1, 5],
        1: [0, 2, 6],
        2: [1, 3, 7],
        3: [2, 4, 8],
        4: [3, 9],
        5: [0, 6, 10],
        6: [1, 5, 7, 11],
        7: [2, 6, 8, 12],
        8: [3, 7, 9, 13],
        9: [4, 8, 14],
        10: [5, 11],
        11: [6, 10, 12],
        12: [7, 11, 13],
        13: [8, 12, 14],
        14: [9, 13]}

allowed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']


class Pair:
    def __init__(self, array, prev, pre_e):
        self.ol = array
        self.prev = prev
        self.pre_e = pre_e


def is_symmetric(array):
    if not array:
        return False
    for i in range(5):
        if array[i] != array[i + 10]:
            return False
    print("Congratulation")
    return True


# input is a current state array, return a allowed swapped states pair
# this method works for auto run, not manual run
def get_allowed_input(array):
    index = array.index('e')
    result =[]
    for i in move[index]:
        result.append(swap(array, i))
    return result


# input is a current state array, and a number for position to swap.
# this method works for auto run, not manual run
def swap(array, num):
    result = list(array)
    i = result.index('e')
    j = num
    temp = result[i]
    result[i] = result[j]
    result[j] = temp

    result = Pair(result, num, i)
    return result


# input is a current state array, heuristic is num of symetric.
def heuristic(array):
    result = 0
    for i in range(5):
        if array[i] == array[i+10]:
            result += 1
    return result


# to print out the table
def print_table(array):
    for i in range(15):
        if i % 5 == 4:
            if array[i] == 'e':
                print('%')
            else:
                print(array[i])
        else:
            if array[i] == 'e':
                print('% ' + " ", end='')
            else:
                print(array[i] + "  ", end='')


def visual_trace(array, path):
    with open('./visual_output.txt', 'a+') as f:
        f.write('%%%%%%%%%%%%%%%%%%%%%%%%%\n')
        for i, v in enumerate(path):
            array = list(map(lambda x: '%' if x is 'e' else x, array))
            string = ''
            for x in range(0, 4):
                string += array[x]+' '
            string += array[4]+'\n'
            for x in range(5, 9):
                string += array[x]+' '
            string += array[9]+'\n'
            for x in range(10, 14):
                string += array[x]+' '
            string += array[14]+'\n'
            f.write(string)
            f.write('%d step, %d move\n' % (i, v))

            # this is to swap
            result = list(array)
            i = result.index('%')
            j = v
            temp = result[i]
            result[i] = result[j]
            result[j] = temp

            array = result

        string = ''
        for x in range(0, 4):
            string += array[x] + ' '
        string += array[4] + '\n'
        for x in range(5, 9):
            string += array[x] + ' '
        string += array[9] + '\n'
        for x in range(10, 14):
            string += array[x] + ' '
        string += array[14] + '\n'
        f.write(string)
        f.write('$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n')
        f.close()




class Box:

    def __init__(self, array):
        self.ol = array
        self.empty_position = -1
        self.start_time = time.time()
        self.end_time = 0
        self.out_order = []

    def manual_run(self):
        self._locate_empty('manual')

    def auto_run(self):
        self._locate_empty('auto')

    def _locate_empty(self, mode):
        self.empty_position = self.ol.index('e')
        if self.empty_position != -1:
            if mode == 'manual':
                self._start_game()
            elif mode == 'auto':
                self._start_auto_game()
        else:
            print("There should be empty space in the input.")
            self.exit_game(False)
            self.end_time = time.time()

    def _start_auto_game(self):
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        init = Pair(self.ol, 100, 100)
        openlist = [init]
        closelist = []
        openlist_ol= [init.ol]
        closelist_ol=[]

        while len(openlist) is not 0:
            current_pair = openlist[0]
            if is_symmetric(current_pair.ol):
                break
            else:
                allowed_positions = get_allowed_input(current_pair.ol)
                closelist.append(current_pair)
                closelist_ol.append(current_pair.ol)
                openlist.remove(current_pair)
                openlist_ol.remove(current_pair.ol)
                open_add = list(filter(lambda x: x.ol not in closelist_ol and x.ol not in openlist_ol, allowed_positions))
                openlist += open_add
                for i in open_add:
                    openlist_ol.append(i.ol)
                openlist.sort(key=lambda x: heuristic(x.ol), reverse=True)

        solution_path = []
        node = openlist[0]
        while node.prev is not 100:
            solution_path.append(node.prev)
            back_state = swap(node.ol, node.pre_e)
            for i in closelist:
                if back_state.ol == i.ol:
                    node = i
        solution_path = solution_path[::-1]
        result_path = []
        for i in solution_path:
            result_path.append(chr(i+97))
        self.out_order = result_path

        visual_trace(self.ol, solution_path)
        self.end_time = time.time()
        print('xx')

    def _start_game(self):
        counter = 0
        self._print_table()

        while not is_symmetric(self.ol) and counter<50:
            valid_input = False
            while not valid_input:
                print("Enter the move : ( allowed input : ", self._print_allowed_input(), ")")
                read_in = input("Input : ")

                if read_in in allowed:
                    read_in = int(allowed.index(read_in))
                    if read_in in move[self.empty_position]:
                        read_in_origin = chr(read_in+97)
                        self.out_order.append(read_in_origin)
                        self._swap(read_in, self.empty_position)
                        valid_input = True
                        self.empty_position = read_in
                        counter += 1
                        self._print_table()
                    else:
                        print("Invalid move")
                else:
                    print("Enter a to o")
        self.end_time = time.time()

    def _print_allowed_input(self):
        array = []
        for i in move[self.empty_position]:
            array.append(allowed[i])
        return array

    def _swap(self, i, j):
        temp = self.ol[i]
        self.ol[i] = self.ol[j]
        self.ol[j] = temp

    @staticmethod
    def exit_game(self, fault):
        if fault:
            print()
        else:
            print()

    def _print_table(self):
        for i in range(15):
            if i % 5 == 4:
                if self.ol[i] == 'e':
                    print('%')
                else:
                    print(self.ol[i])
            else:
                if self.ol[i] == 'e':
                    print('% ' + " ", end='')
                else:
                    print(self.ol[i] + "  ", end='')

    def output_string(self):
        string_o = ''
        for i in self.out_order:
            string_o += chr(ord(i)-32)
        string_o += '\n'
        time_consume = self.end_time - self.start_time
        time_consume = str(time_consume*1000.000)
        string_o += time_consume
        string_o += 'ms\n'
        return string_o
