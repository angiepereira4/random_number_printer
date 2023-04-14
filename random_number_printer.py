import argparse
import random


parser = argparse.ArgumentParser(description='Print numbers from 1 to 10 in random order.')


parser.add_argument('--seed', type=int, help='Random seed', default=None)


args = parser.parse_args()


if args.seed:
    random.seed(args.seed)


numbers = list(range(1, 11))
random.shuffle(numbers)


print(numbers)
