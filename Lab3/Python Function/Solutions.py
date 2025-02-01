# Task 1: Convert grams to ounces
def grams_to_ounces(grams):
    return 28.3495231 * grams

# Task 2: Convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

# Task 3: Solve chicken and rabbit puzzle
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if chickens * 2 + rabbits * 4 == numlegs:
            return chickens, rabbits
    return None, None

# Task 4: Filter prime numbers from a list
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# Task 5: Print all permutations of a string
from itertools import permutations

def string_permutations(s):
    return [''.join(p) for p in permutations(s)]

# Task 6: Reverse words in a string
def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))

# Task 7: Check if 3 is next to 3
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# Task 8: Check for 007 sequence
def spy_game(nums):
    code = [0, 0, 7]
    code_index = 0
    for num in nums:
        if num == code[code_index]:
            code_index += 1
        if code_index == len(code):
            return True
    return False

# Task 9: Calculate the volume of a sphere
def sphere_volume(radius):
    return (4 / 3) * 3.14159 * (radius**3)

# Task 10: Return a list with unique elements
def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Task 11: Check if a word/phrase is a palindrome
def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

# Task 12: Print a histogram
def histogram(lst):
    for num in lst:
        print('*' * num)

# Task 13: Guess the number game
import random

def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    guesses = 0

    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break

# Task 14: Import and use functions
def main():
    # Task 1 Example
    print(grams_to_ounces(100))

    # Task 2 Example
    print(fahrenheit_to_celsius(100))

    # Task 3 Example
    print(solve(35, 94))

    # Task 4 Example
    print(filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    # Task 5 Example
    print(string_permutations("abc"))

    # Task 6 Example
    print(reverse_words("We are ready"))

    # Task 7 Example
    print(has_33([1, 3, 3, 1]))

    # Task 8 Example
    print(spy_game([1, 0, 2, 4, 0, 5, 7]))

    # Task 9 Example
    print(sphere_volume(3))

    # Task 10 Example
    print(unique_elements([1, 2, 2, 3, 4, 4, 5]))

    # Task 11 Example
    print(is_palindrome("madam"))

    # Task 12 Example
    histogram([4, 9, 7])