#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    for i in range(10):
        print(10-i)
        print("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here!
    int_list = [int**2 for int in int_list]
    return int_list
    pass

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if (i % 15 == 0):
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i += 1
    pass
