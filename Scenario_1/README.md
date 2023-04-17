# Random Number Printer

This CLI application is written in Python programming language,this program generates and prints 10 random numbers between 1 and 10 in random order.

## Installation

To run this program, you need to have Python 3 installed on your system. If you don't have Python 3 installed.
### MacOS
To download python3 on Mac we use Homebrew :  
**brew install python3**   

### Linux/Ubuntu
To download python3 for linux/Ubuntu :  
sudo apt-get update  
**sudo apt-get install python3**  
Check whether Python 3 is correctly installed on your system by typing the following command and pressing Enter:  
**python --version**   

## Usage  

1. Open your terminal or command prompt.  
2. Navigate to the directory where the program is saved.  
3. Run the command **python3 random_number_printer.py**.  
4. The program will generate 10 random numbers between 1 and 10 and print them to the terminal in random order.


## Overview  

The program uses the random module in Python to generate 10 random numbers between 1 and 10. It then shuffles the list of numbers using the shuffle method in the random module, and prints the shuffled list to the terminal.

Note: This program can be useful for generating random inputs for testing algorithms or for generating random sequences in games.

## Break down of Code  
This program uses the **argparse** module to create a parser object that can handle command-line arguments. It defines one optional argument: **seed**, which takes an integer value and has a default value of **None**. This argument is used to set the random seed for reproducible results.The parser object is used to parse the command-line arguments, and the resulting object is stored in **args**.If the **--seed** argument is provided, the *random* seed is set to the value of the seed argument using the **seed()** method of the random module. This ensures that the same sequence of *random* numbers is generated every time the program is run with the same seed.  
A **list of numbers** from 1 to 10 is generated with **range()** and converted to a list with list(). The **shuffle()** method of the random module is used to shuffle the list of numbers in place.The shuffled list of numbers is printed to the terminal using the **print()** function.  

The program can be run from the command line with: **python3 random_number_printer.py** --seed <seed>  
where <seed> is an optional integer value for the random seed. If the --seed argument is not provided, the program will use the default random seed (None). The program will print the shuffled list of numbers from 1 to 10 to the terminal.  
  
When the program is run, the parser object parses the command-line arguments, and the program generates a list of numbers from 1 to 10 in random order using the **shuffle()** function from the random module. Finally, the program prints the list of *random numbers* to the terminal.