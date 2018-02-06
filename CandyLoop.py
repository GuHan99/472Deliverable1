import cmd
from Tools import isValid
from Tools import present
import Box
import re

class CandyLoop(cmd.Cmd):
    prompt = 'Loop '

    @staticmethod
    def do_manul(self):
        # input_order = input('please type in the candy order in the box: ')
        # while not isValid(input_order):
        #     input_order = input('please type in the candy order in the box: ')
        input_order = ''
        with open('./sample.txt', 'rt') as f:
            for line in f:
                line = line.strip('\n')
                c = line.split(' ')
                for i in c:
                    input_order += i + ' '

        # present(input_order)
        on_going = True
        box = Box.Box(input_order)
        while on_going:
            input_direction = input('type in the candy ')
            while not re.match('[A-M]', input_direction):
                input_direction = input('type in the candy')
            else:
                box = Box.Box()




    @staticmethod
    def do_exit(self):
        return True

if __name__ == '__main__':
    CandyLoop().cmdloop()



