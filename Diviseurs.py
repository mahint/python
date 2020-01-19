#!/usr/bin/python3
#Given a number the script finds out all the divisors
div = int(input("number:"))
x = range(1, div+1)
for item in x:
    if (div % item) == 0:
        print(str (item) + " is a divisor of " + str(div))