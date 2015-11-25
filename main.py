#!/usr/bin/env python
import cmd
import problem1

class Main(cmd.Cmd):

    intro = 'Welcome to the linalg shell. Type help or ? to list commands.\n'
    prompt = '(linalg) '

    def do_problem1(self, line):
        'Activate problem 1 of the project'
        print("Problem 1!")
        problem1.print_something()

    def do_problem2(self, line):
        'Activate problem 2 of the project'
        print("Problem 2!")

    def do_problem3(self, line):
        'Activate problem 3 of the project'
        print("Problem 3!")

    def do_quit(self, line):
        'Quit'
        exit()

    def do_q(self, line):
        'Quit'
        exit()

if __name__ == '__main__':
    Main().cmdloop()
