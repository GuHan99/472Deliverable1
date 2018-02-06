
move = {0:[1,5],
        1:[0,2,6],
        2:[1,3,7],
        3:[2,4,8],
        4:[3,9],
        5:[0,6,10],
        6:[1,5,7,11],
        7:[2,6,8,12],
        8:[3,7,9,13],
        9:[4,8,14],
        10:[5,11],
        11:[6,10,12],
        12:[7,11,13],
        13:[8,12,14],
        14:[9,13]}

allowed = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']

class Box:

    def __init__(self, array):
        self.ol = array
        self.empty_position = -1
        self.locate_empty()


    def locate_empty(self):
        for i in range(14):
            if self.ol[i] == 'e':
                self.empty_position = i
                break
        if self.empty_position != -1:
            self.start_game()
        else:
            print("error")
            self.exit_game(False)

    def start_game(self):
        counter = 0
        self.print_table()

        while not self.isSymmetric() and counter<50:
            valid_input = False
            while not valid_input:
                print("Enter the move : ( allowed input : ", self.print_allowed_input() , ")")
                read_in = input("Input : ")

                if read_in in allowed:
                    read_in = int(allowed.index(read_in))
                    if read_in in move[self.empty_position]:
                        self.swap(read_in, self.empty_position)
                        valid_input = True
                        self.empty_position = read_in
                        counter += 1
                        self.print_table()
                    else:
                        print("Invalid move")
                else:
                    print("Enter a to o")

    def print_allowed_input(self):
        array = []
        for i in move[self.empty_position]:
            array.append(allowed[i])
        return array

    def swap(self, i, j):
        temp = self.ol[i]
        self.ol[i] = self.ol[j]
        self.ol[j] = temp

    def isSymmetric(self):
        for i in range(5):
            if self.ol[i] != self.ol[i+10]:
                return False

        print("Congratulation")
        return True


    def exit_game(self, fault):
        if fault:
            print()
        else:
            print()

    def print_table(self):
        for i in range(15):
            if i%5 ==4:
                if self.ol[i] == 'e':
                    print('空')
                else:
                    print(self.ol[i])
            else:
                if self.ol[i] == 'e':
                    print('空'+ " ",end='')
                else:
                    print(self.ol[i] + "  " , end='')


