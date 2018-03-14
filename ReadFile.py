import cmd
from Box import Box
from Tools import output_file


class ReadFile(cmd.Cmd):
    prompt = 'Candy '

    @staticmethod
    def do_manual(self):
        input_order = []
        with open('./input.txt', 'rt') as f:
            for line in f:
                line = line.strip('\n')
                c = line.split(' ')
                input_order.append(c)

        output_str = ''

        for line in input_order:
            box = Box(line)
            box.manual_run()
            output_str += box.output_string()
            print('%dth puzzle complete.')
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
        input_order = []
        with open('./input.txt', 'rt') as f:
            for line in f:
                line = line.strip('\n')
                c = line.split(' ')
                input_order.append(c)
        index = 0
        output_str = ''
        for line in input_order:
            box = Box(line)
            box.auto_run()
            output_str += box.output_string()
            index+=1
            print('%dth puzzle complete.' % index)
        counter = 0
        flag_counter = 0
        for i in output_str.splitlines():
            if flag_counter % 2 is 0:
                counter += len(i)
            flag_counter += 1
        counter = str(counter)
        output_str += counter
        output_str += '\n'
        sum_time = 0
        for i in output_str.splitlines():
            if 'ms' in i:
                m_position = i.index('m')
                sum_time += float(i[0:m_position])
        output_str += str(sum_time)
        output_str += 'ms\n'
        output_file(output_str)

    @staticmethod
    def do_exit(self):
        return True


if __name__ == '__main__':
    ReadFile().cmdloop()