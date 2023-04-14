import argparse
import random

# Create a parser object to handle command-line arguments
parser = argparse.ArgumentParser(description='Print numbers from 1 to 10 in random order.')

# Add an optional argument for the random seed
parser.add_argument('--seed', type=int, help='Random seed', default=None)

# Parse the arguments
args = parser.parse_args()

# Set the random seed if provided
if args.seed:
    random.seed(args.seed)

# Generate a list of numbers from 1 to 10 in random order
numbers = list(range(1, 11))
random.shuffle(numbers)

# Print the numbers
print(numbers)
