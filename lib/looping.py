#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    x = 10
    while    x > 0:
        print (x)
        x-=1
        print ("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    int_list = [number**2 for number in int_list]
    return int_list

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Call the function to print the FizzBuzz sequence
fizzbuzz()



    
