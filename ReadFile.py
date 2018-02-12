import cmd
from Box import Box
import time
from Tools import output_file

class ReadFile(cmd.Cmd):
    prompt = 'Loop '

    @staticmethod
    def do_manual(self):
        # input_order = input('please type in the candy order in the box: ')
        # while not isValid(input_order):
        #     input_order = input('please type in the candy order in the box: ')
        input_order = []
        start_time = time.time()
        with open('./sample.txt', 'rt') as f:
            for line in f:
                line = line.strip('\n')
                c = line.split(' ')
                input_order.append(c)

        # present(input_order)
        on_going = True
        output_str = ''

        for line in input_order:
            box = Box(line)
            box.manual_run()
            output_str += box.output_string()
        counter = 0
        flag_counter = 0
        for i in output_str.splitlines():
            if flag_counter % 2 is 0:
                counter += len(i)
            flag_counter += 1
        counter = str(counter)
        output_str += counter
        output_file(output_str)
    @staticmethod
    def do_auto(self):
        print("To be implemented")

    @staticmethod
    def do_exit(self):
        return True


if __name__ == '__main__':
    ReadFile().cmdloop()



