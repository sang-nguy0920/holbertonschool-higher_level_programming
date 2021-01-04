#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for x in range(0, x):
        try:
            if isinstance(my_list[x], int):
                print("{:d}".format(my_list[x]), end='')
                count += 1
        except (TypeError, ValueError):
            pass
    print()
    return count
