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


class Box:

    def __init__(self, array):
        self.ol = array
        self.empty_position = -1
        self.start_time = time.time()
        self.end_time = 0
        self.out_order = []

    def manual_run(self):
        self._locate_empty()

    def _locate_empty(self):
        for i in range(14):
            if self.ol[i] == 'e':
                self.empty_position = i
                break
        if self.empty_position != -1:
            self._start_game()
        else:
            print("There should be empty space in the input.")
            self.exit_game(False)
            self.end_time = time.time()

    def _start_game(self):
        counter = 0
        self._print_table()

        while not self._is_symmetric() and counter<50:
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

    def _is_symmetric(self):
        for i in range(5):
            if self.ol[i] != self.ol[i+10]:
                return False

        print("Congratulation")
        return True

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
        time_cosume = self.end_time - self.start_time
        time_cosume = str(int(time_cosume))
        string_o += time_cosume
        string_o += 'ms\n'
        return string_o



