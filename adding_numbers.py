#!/usr/bin/env python3

# Created by Noah McCaskill
# Created May 2022
# This program adds a desired amount of numbers together with user input.


def main():
    # this function asks for the number of times to add numbers
    # then asks for what numbers in specific to add.
    times_added = 0
    total_sum = 0

    # input
    add_loop_string = input("Enter how many numbers you want to add: ")

    #input & process
    try:

        add_loop = int(add_loop_string)

        for times_added in range(add_loop):
            number_to_add_string = input("Enter a number: ")
            number_to_add = int(number_to_add_string)

            if number_to_add < 0:
                continue

            total_sum = total_sum + number_to_add
            times_added += 1

        # output
        print("\nThe sum of your numbers is {0}.".format(total_sum))

    except Exception:
        print("\nYour integer is invalid. Please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
    