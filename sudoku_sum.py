import itertools
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--target", required=True, type=int,
	help="target number to sum to")
ap.add_argument("-l", "--length", required=False, type=int,
        help="length of list of numbers summing to target")
ap.add_argument("-r", "--repeat", default=False, action='store_true',
        help="boolean flag to allow numbers to repeat")
ap.add_argument("-i", "--include", required=False, type=int,
        help="specify number to include")
ap.add_argument("-e", "--exclude", required=False, type=int,
        help="specify number to exclude")
args = vars(ap.parse_args())

target  = args["target"]
length  = args["length"] if args["length"] else -1
repeat  = args["repeat"]
include = args["include"] if args["include"] else -1
exclude = args["exclude"] if args["exclude"] else -1

num_set = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Solutions to sums adding to {}:".format(target))

def sudoku_sum_list(t, r, l, inc, e, available, used):

    ### BASE CASE ###

    # stop iteration condition
    if sum(used) >= target or (l != -1 and l <= len(used)) or (e != -1 and e in used):

        # correct result condition
        if sum(used) == target and isAscending(used) and (l == -1 or l == len(used)) and (inc == -1 or inc in used) and (e == -1 or e not in used):
            print(used)

    ### RECURSIVE CASE ###

    else: 
        for i in available:

            a = list(available)
            # if numbers allowed to repeat, number stays in available set
            if not r:
                a.remove(i)

            u = list(used)
            u.append(i)

            sudoku_sum_list(t, r, l, inc, e, a, u)

def isAscending(list):
    previous = list[0]
    for number in list:
        if number < previous:
            return False
        previous = number
    return True



sudoku_sum_list(target, repeat, length, include, exclude, num_set, [])        
