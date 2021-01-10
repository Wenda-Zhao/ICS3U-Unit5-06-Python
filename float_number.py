#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Jan 2021
# This program for float number


def calculate(number_float, decimal_place_int):
    # This function is calculate

    # process
    number_float_after = number_float * 10 ** decimal_place_int
    number_float_after = number_float_after + 0.5
    number_float_after = int(number_float_after)
    number_float_after = number_float_after/10 ** decimal_place_int

    return number_float_after


def main():
    # This function is for input

    number_final = -1

    # input
    number = input("Enter a decimal number:")
    decimal_place = input("How many decimal place do you want?")

    try:
        number_float = float(number)
        try:
            decimal_place_int = int(decimal_place)
            # call function
            number_final = calculate(number_float, decimal_place_int)
        except Exception:
            print("decimal place is not a integer")
    except Exception:
        print("number is not a decimal")

    # output
    if number_final == -1:
        print("-1")
    else:
        print("{0}".format(number_final))


if __name__ == "__main__":
    main()
