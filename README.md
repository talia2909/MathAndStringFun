# MathAndStringFun

## Overview

MathAndStringFun is a Python script consisting of 4 distinct functions, each designed to perform a specific mathematical or string manipulation task:

1. **f1**: This function receives a string as input and prints the number of letters (a-z or A-Z) that aren't lower case vowels (a, e, i, o, u, y). Note that the letter ‘y’ is considered a vowel for this purpose. 

2. **f2**: This function takes two parameters, a float `x` and an integer `n`, in that order. The program then calculates the Taylor approximation (of order `n`) of the expression `ln(1 + x)` around the point `x`. The function performs input validity tests and prints an 'error' message if the input is not in the correct format or there is a computational error. The value of `x` should be a float in the range [-0.7, 0.7].

3. **f3**: This function receives a string of English words as input. It takes every even word (a word that is located in an even position in the string) and makes it uppercase, and takes every odd word and makes it lowercase. The function then prints the uppercase words in ascending lexicographical order, followed by the lowercase words in descending lexicographical order.

4. **f4**: This function receives a number and checks if it's a Lychrel candidate. If the number is a Lychrel candidate (meaning that the number of iterations needed is over 500), the function prints 'True'. If the number isn't a Lychrel candidate, the function prints the number of iterations.

## Installation

Ensure you have Python installed on your system. Python 3.7 or later is recommended. To run the script, simply download it and run it using the Python interpreter:

```sh
python3 MathAndStringFun.py
```

## Usage

When you run the script, you will be prompted to input a number between 1 and 4. This number corresponds to the function you wish to execute. Then, you will be asked to provide further inputs based on the chosen function:

- For function **f1**, input a string. The function will then print the number of non-lowercase vowel characters.
- For function **f2**, first input a float (in the range of -0.7 to 0.7) and then an integer.
- For function **f3**, input a string of English words. The function will then print the sorted words as described in the Overview section.
- For function **f4**, input a number. The function will then print either 'True' or the number of iterations, depending on whether the number is a Lychrel candidate.



