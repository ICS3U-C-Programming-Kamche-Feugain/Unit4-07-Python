#!/usr/bin/env python3\
# Created By:Kamche
# Created on: November 21, 2026
# This program asks the user to create
# a program generating five
# integers per a line using a loop
# and if statement


def main():
    for number in range(1000, 2001):
        print(number, end=" ")

        if (number - 999) % 5 == 0:
            print()


if __name__ == "__main__":
    main()
