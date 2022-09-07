###############
#   PROBLEM   #
###############
# Each new term in the Fibonacci sequence is
# generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose
# values do not exceed four million, find the sum of the even-valued terms.

# Generator for Fibonacci
def fibGen(num):
    # Initial Case
    i = j = 1
    yield i
    yield j
    while (i + j) < num:
        temp = i + j
        i = j
        j = temp
        yield j


def isEven(num):
    return (num % 2 == 0)


def evenFib(num):
    even = list(filter(isEven, fibGen(num)))
    print(even)
    return sum(even)


if __name__ == "__main__":
    g = fibGen(100)
    for i in range(10):
        print(next(g))
    print(evenFib(4000000))
