#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Sept 2021
# This Program calculate 2 number


def main():
    # This function calculate  2 number

    # input
    first_number = int(input("Enter the first number(integer): "))
    second_number = int(input("Enter the second number(integer): "))

    # process
    answer = first_number + second_number

    # output
    print("")
    print(
        "The answer: {0} + {1} = {2}".format(
            first_number, second_number, answer
        )
    )
    print("\nDone")


if __name__ == "__main__":
    main()
