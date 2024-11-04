#!/usr/bin/env python3

# The first subgoal is to explore all numbers from 1 to k in all possible ways in which it can be done.
# That's actually just all orderings, so k!, k faculty, implying it grows astronomically.
# For example, if k is 100 that is already 3 628 800, rounded to 4 million.
# Ok that's too many possibilities. I'll change the task to writing python functions
# for ways of structured counting that I can think of, hopefully fun ways :) .
# We are not interested in different programming language techniques of counting,
# but rather in the mathematical structures of counting.
# Each way shall be representend in a separate generator function.
# The functions shall be tested with the same input, to see if they give the same result, i.e. the numbers from 1 to k, after sorting the output.
# Each generator function invocation takes a number k and yields the numbers between 1 and k in a certain order.

def count1(k):
    for i in range(1, k + 1):
        yield i

def count2(k):
    for i in range(k, 0, -1):
        yield i

def count3(k):
    for i in range(1, k + 1):
        if i % 2 == 0:
            yield i
    for i in range(1, k + 1):
        if i % 2 == 1:
            yield i

if __name__ == "__main__":
    # Create a list of all functions starting with count based on the globals() dictionary.
    count_functions = [f for f in globals() if f.startswith('count')]

    # Test the functions.
    k = 10
    for f in count_functions:
        ret = sorted(list(globals()[f](k)))
        success = ret == list(range(1, k + 1))
        print(f, success)
        if not success:
            print(ret)

