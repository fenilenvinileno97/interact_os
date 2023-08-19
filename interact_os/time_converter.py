#!/usr/bin/env python3

def to_seconds(hours, minutes, seconds):
    return 3600*hours+60*minutes+seconds

print("Welcome to time converter")

cont = "y"

while (cont.lower() == "y"):
    hours = int(input("Enter a number of hours: "))
    minutes = int(input("Enter a number of minutes: "))
    seconds = int(input("Enter a number of seconds: "))
    print('You have a total of {} seconds'.format(to_seconds(hours, minutes, seconds)))

    cont = input('Do you want to make another conversion? [press y to continue]: ')

print("Goodbye!")

