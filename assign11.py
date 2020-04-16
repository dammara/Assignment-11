# Markhus Dammar
# 12 April 2020
# This is the exam, it will create a list and ask the user
# how many numbers they want to put into it.
# the list will then be filled with x amount of random numbers
# then the list will be sorted according to the user's preference
# (\033[1m AND \033[0m provide bold text)
# CODE REUSED 16 APRIL 2020 FOR ASSIGNMENT 11 - ADD TIME TO PROG

import random, time
from search_methods import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort

list = []                   # New empty List


def new_list():             # Will print the sorted list when called
    print("Here is the newly sorted list:", list)
    time.sleep(2)
    next()


def invalid():              # If the choice is invalid, this screen will display
    print("\033[1mINAVLID CHOICE, TRY AGAIN \033[0m")
    time.sleep(2)


def welcome():              # Splash Screen
    print("""\033[1m
    ------------LIST SORT VERSION 1.1.0------------ \033[0m
    Welcome. This program will sort random numbers
              from least to greatest.""")
    time.sleep(2)
    choose()


def choose():                   # This is where the user chooses a method
    print("""\n
    Please choose a sorting method. 
    \033[1m ----ENTER 1, 2, 3, 4, or 5.---- \033[0m
    1. Bubble
    2. Selection
    3. Insertion
    4. Merge
    5. Quick 
    """)
    method = int(input(">>>"))          # Method is inputted here

    while method == 1:                  # Bubble Sort
        print("BUBBLE SORT")
        take_numbers()                  # Calls method to ask user how many numbers will be sorted
        start_time = time.time()        # Starts the stopwatch
        bubble_sort(list)               # Sorts list according to the method
        print(f"List bubble sorted! It took {(time.time() - start_time)} seconds")      # Stops the stopwatch and returns total time
        new_list()                      # Prints new list

    while method == 2:                  # Selection Sort
        print("SELECTION SORT")
        take_numbers()
        start_time = time.time()
        selection_sort(list)
        print(f"List selection sorted! It took {(time.time() - start_time)} seconds")
        new_list()

    while method == 3:                  # Insertion Sort
        print("INSERTION SORT")
        take_numbers()
        start_time = time.time()
        insertion_sort(list)
        print(f"List insertion sorted! It took {(time.time() - start_time)} seconds")
        new_list()

    while method == 4:                  # Merge Sort
        print("MERGE SORT")
        take_numbers()
        start_time = time.time()
        merge_sort(list)
        print(f"List merge sorted! It took {(time.time() - start_time)} seconds")
        new_list()

    while method == 5:                  # Quick Sort
        print("QUICK SORT")
        take_numbers()
        start_time = time.time()
        quick_sort(list)
        print(f"List quick sorted! It took {(time.time() - start_time)} seconds")
        new_list()

    while method > 5 or method < 1:     # Checks for invalid input
        invalid()                       # Calls invalid screen
        choose()


def take_numbers():             # This method takes the user input for how many numbers
    user_numbers = int(input("How many numbers do you want to sort? >>>"))
    for num in range(user_numbers):
        list.append(random.randint(1, 100000))          # Appends random numbers to the list
    print(f"""\nHere is your list of \033[1m {user_numbers} \033[0m numbers: """,
          list)
    time.sleep(1)
    print("\033[1mSORTING... \033[0m")
    time.sleep(1)


def next():                     # This is the end screen to determine if the user will continue or not
    print("\nNOW WHAT?")
    choice = int(input("""
    \033[1mTYPE 1 or 2 \033[0m
        1. Restart
        2. Exit
        >>>"""))
    if choice == 1:             # Will clear list and restart program
        list.clear()
        choose()
    elif choice == 2:           # Exits the program
        print("\033[1mGoodbye! \033[0m")
        time.sleep(1)
        exit()
    else:                       # Checks if input is 1 or 2. If not, Invalid.
        invalid()
        next()


# Program Starts Here
welcome()
