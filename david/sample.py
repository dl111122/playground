from __future__ import print_function
import sys

def main():
    fname = raw_input('Enter file to print: ')
    with open(fname) as f:
        lineno = 0
        for line in f:
            lineno = lineno + 1
            sline = line.strip()
            print(lineno, ":", sline)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
