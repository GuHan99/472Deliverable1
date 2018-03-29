import time
import math
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

heuristic_matrix = [[13, 11, 10, 8, 5, 0], [15, 13, 10, 9, 5, 0], [15, 13, 11, 9, 7, 0], [16, 14, 12, 10, 8, 0]]
allowed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']


class Pair:
    def __init__(self, array, pre_e, gn):
        self.ol = array
        self.pre_e = pre_e
        self.gn = gn


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
def get_allowed_input(array, gn):
    index = array.index('e')
    result =[]
    for i in move[index]:
        result.append(swap(array, i, gn))
    return result


# input is a current state array, and a number for position to swap.
# this method works for auto run, not manual run
def swap(array, num, gn):
    result = list(array)
    i = result.index('e')
    j = num
    temp = result[i]
    result[i] = result[j]
    result[j] = temp

    result = Pair(result, i, gn+1)
    return result


def index_position(array, candy):
    result = []
    for i in range(0, 15):
        if array[i] is candy:
            result.append(i)
    return result


# input is a current state array, heuristic is num of symetric.
def heuristic(array, gn):
    result = gn
    count = 0
    for i in range(5):
        if array[i] == array[i + 10]:
            count += 1
    level = len(set(array))-4
    result += heuristic_matrix[level][count]
    result -= count*30

    if level is 4:
        b_position = index_position(array, 'b')
        w_position = index_position(array, 'w')
        y_position = index_position(array, 'y')
        g_position = index_position(array, 'g')
        p_position = index_position(array, 'p')
        if b_position[0]/5 == b_position[1]/5 and b_position[0]/5 != 1:
            result += 5
        if w_position[0] / 5 == w_position[1] / 5 and w_position[0] / 5 != 1:
            result += 5
        if y_position[0] / 5 == y_position[1] / 5 and y_position[0] / 5 != 1:
            result += 5
        if g_position[0] / 5 == g_position[1] / 5 and g_position[0] / 5 != 1:
            result += 5
        if p_position[0] / 5 == p_position[1] / 5 and p_position[0] / 5 != 1:
            result += 5
    elif level is 3:
        w_position = index_position(array, 'w')
        y_position = index_position(array, 'y')
        g_position = index_position(array, 'g')
        if w_position[0] / 5 == w_position[1] / 5 and w_position[0] / 5 != 1:
            result += 5
        if y_position[0] / 5 == y_position[1] / 5 and y_position[0] / 5 != 1:
            result += 5
        if g_position[0] / 5 == g_position[1] / 5 and g_position[0] / 5 != 1:
            result += 5
    elif level is 2:
        w_position = index_position(array, 'w')
        y_position = index_position(array, 'y')
        if w_position[0] / 5 == w_position[1] / 5 and w_position[0] / 5 != 1:
            result += 5
        if y_position[0] / 5 == y_position[1] / 5 and y_position[0] / 5 != 1:
            result += 5
    elif level is 1:
        w_position = index_position(array, 'w')
        if w_position[0] / 5 == w_position[1] / 5 and w_position[0] / 5 != 1:
            result += 5
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
        self.time_out = False

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
        init = Pair(self.ol, 100, 0)
        openlist = [init]
        closelist = []

        while len(openlist) is not 0 and not self.time_out:
            current_pair = openlist[0]
            if is_symmetric(current_pair.ol):
                break
            else:
                allowed_positions = get_allowed_input(current_pair.ol, current_pair.gn)

                closelist.append(current_pair)
                close_ol = list(map(lambda x: x.ol, closelist))

                openlist.remove(current_pair)
                open_ol = list(map(lambda x: x.ol, openlist))

                # filter those in open-list but gn is less
                for i in allowed_positions:
                    if i.ol in open_ol:
                        for x in openlist:
                            if x.ol is i.ol and x.gn > i.gn:
                                x.pre_e = i.pre_e
                                x.gn = i.gn
                open_add = list(filter(lambda x: x.ol not in close_ol and x.ol not in open_ol, allowed_positions))

                openlist += open_add
                open_ol = list(map(lambda x: x.ol, openlist))

                openlist.sort(key=lambda x: heuristic(x.ol, x.gn), reverse=False)

            if time.time()-self.start_time >= 4:
                self.time_out = True
            # for i in current_pair.ol:
            #     if i is 'e':
            #         print('#', end=' ')
            #     else:
            #         print(i, end=' ')
            # print('\n')

        solution_path = []
        node = openlist[0]
        while node.pre_e is not 100:
            node_e = node.ol.index('e')
            solution_path.append(node_e)
            back_state = swap(node.ol, node.pre_e, 0)
            for i in closelist:
                if back_state.ol == i.ol:
                    node = i
        solution_path = solution_path[::-1]
        result_path = []
        for i in solution_path:
            result_path.append(chr(i+97))
        self.out_order = result_path

        if self.time_out:
            self.out_order = []

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
        # string_o += str(len(self.out_order))
        # string_o += '\tof length\n'
        for i in self.out_order:
            string_o += chr(ord(i)-32)
        string_o += '\n'
        time_consume = self.end_time - self.start_time
        if self.time_out:
            time_consume = 0
        time_consume = str(time_consume*1000.000)
        string_o += time_consume
        string_o += 'ms\n'
        print(string_o, end=' ')
        return string_o
