import cmd
from Box import Box
import re

class ReadFile(cmd.Cmd):
    prompt = 'Loop '

    @staticmethod
    def do_manual(self):
        # input_order = input('please type in the candy order in the box: ')
        # while not isValid(input_order):
        #     input_order = input('please type in the candy order in the box: ')
        input_order = []
        with open('./sample.txt', 'rt') as f:
            for line in f:
                line = line.strip('\n')
                c = line.split(' ')
                input_order.append(c)

        # present(input_order)
        on_going = True

        for line in input_order:
            box = Box(line)

    @staticmethod
    def do_auto(self):
        print("To be implemented")

    @staticmethod
    def do_exit(self):
        return True

if __name__ == '__main__':
    ReadFile().cmdloop()



