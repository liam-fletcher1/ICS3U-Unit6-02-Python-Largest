#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Oct 2021
# This gets random numbers then finds the largest using an array

import random


def largest_of_numbers(list_numbers):
    # this functions gets random numbers then finds the largest using an array

    largest_number = list_numbers[0]
    for user_x in list_numbers:
        if user_x > largest_number:
            largest_number = user_x

    return largest_number


def main():
    # this function uses a list

    random_numbers = []

    # input
    print("The random numbers are ")
    print("")
    for loop_counter in range(0, 10):
        a_single_number = random.randint(0, 100 + 1)
        random_numbers.append(a_single_number)
        print("{0}, ".format(a_single_number), end="")
    print("")

    answer = largest_of_numbers(random_numbers)

    print("")
    print("The largest number is: {0} ".format(answer))
    print("")
    print("\nDone.")


if __name__ == "__main__":
    main()
