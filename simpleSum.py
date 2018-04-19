import argparse


# parses the arguments and calls appropriate sum function
def main():
    par = argparse.ArgumentParser()
    par.add_argument('-f', '--floor', help='rounds the number down before summing', action='store_true')
    par.add_argument('nums', nargs='+', help='enter a list of numbers here to sum them', type=float)
    args = par.parse_args()

    sList = []
    for num in args.nums:
        sList.append(num)

    if args.floor:
        floorSum(sList)
    else:
        sum(sList)


# floors each value sums them and prints the result
def floorSum(args):
    sum = 0
    for num in args:
        args[args.index(num)] = num // 1
    for num in args:
        sum += num
    print sum
    return sum

# sums each argument and prints the result
def sum(args):
    sum = 0
    for num in args:
        sum += num
    print sum
    return sum

if __name__ == '__main__':
    main()