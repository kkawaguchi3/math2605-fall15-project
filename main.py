#!/usr/bin/env python
import cmd
import problem1

class Main(cmd.Cmd):

    intro = "There are 3 parts to the project. Type `1` for part1, `2` for part2, and `3` for part3."
    prompt = '(linalg) '

    print('Welcome to the linalg shell. Type help or ? to list commands.\n')

    def do_1(self, line):
        'Activate part 1 of the project'
        print("\n==================")
        print("Welcome to Part 1.")
        print("==================\n")
        print("Select A, B, C, or D. For parts F and E, please see the written component for part 1.")
        # problem1.print_everything()
        sub_cmd = SubInterpreter_1()
        sub_cmd.cmdloop()

    def do_2(self, line):
        'Activate part 2 of the project'
        print("\n==================")
        print("Welcome to Part 1.")
        print("==================\n")
        import iterativeMethods

    def do_3(self, line):
        'Activate part 3 of the project'
        print("Part 3!")
        import Part_3

    def do_quit(self, line):
        'Quit'
        exit()

    def do_q(self, line):
        'Quit'
        exit()


class SubInterpreter_1(cmd.Cmd):
    prompt = "(linalg->part1) "

    def do_A(self, args):
        problem1.A()

    def do_B(self, args):
        problem1.B()

    def do_C(self, args):
        problem1.C()

    def do_quit(self, args):
        return True
    do_EOF = do_quit


if __name__ == '__main__':
    Main().cmdloop()
