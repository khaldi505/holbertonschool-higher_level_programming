#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_len = len(sys.argv)
    if argv_len - 1 == 0:
        print("{:d} arguments.".format(argv_len - 1))
    if argv_len - 1 == 1:
        print("{:d} argument:".format(argv_len - 1))
        print("{:d}: {:s}".format(1, sys.argv[1]))
    elif argv_len > 1:
        print("{:d} arguments:".format(argv_len - 1))
        for x in range(1, argv_len):
            print("{:d}: {:s}".format(x, sys.argv[x]))
