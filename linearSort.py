__author__ = 'bQuinn'


def linsort(lst):
    """
    precondition: list contaions only non-negative integer values
    sorts a list in O(n) time. Or more specifically O(2n + 1x) x being the largest element in the list
    best case O(n) if list is already sorted (uses no extra memory)
    worst case O(2n + x), downside: uses a lot of memory for large values of x
    :param lst: unsorted list
    :return: sorted list
    """
    largest = interplst(lst)
    if isinstance(largest, bool):
        return lst
    else:
        return newlst(createBlanket(lst, largest))


def interplst(lst):
    """
    checks if the list is already sorted, if not return the largest value in the list
    :param lst: list
    :return: True is list is sorted, largest value if not
    """
    largest = 0
    n = 0
    for i in range(len(lst)):
        if lst[i] >= largest:
            largest = lst[i]
            n += 1
    if n == len(lst):
        return True
    else:
        return largest


def createBlanket(lst, largest):
    """
    creates a blanket(list of size largest) and inserts elements of list in sorted order
    :param lst: original list
    :param largest: largest value of original list
    :return: blanket
    """
    blanket = []
    for i in range(largest + 1):
        blanket.append(None)
    for i in range(len(lst)):
        val = lst[i]
        if blanket[val] is None:
            blanket[val] = val
        else:
            if blanket[val] == val:
                blanket[val] = [val, 2]
            elif type(blanket[val]) == list:
                blanket[val][1] += 1
    print("Blanket: " + str(blanket))
    return blanket


def newlst(blanket):
    """
    iterprets the blanket and returnst the new sorted list
    :param blanket: blanket
    :return: sorted list
    """
    newlst = []
    for i in range(len(blanket)):
        if blanket[i] == None:
            pass
        elif type(blanket[i]) == list:
            while blanket[i][1] > 0:
                newlst.append(blanket[i][0])
                blanket[i][1] -= 1
        else:
            newlst.append(blanket[i])
    return newlst


"""""""""""""""""""""""""""""""""""""""""
Running the program
"""""""""""""""""""""""""""""""""""""""""


def main():
    data = open(str(input("Enter filename: ")))
    lst = [int(s.strip()) for s in data]
    print("old list: " + str(lst))
    start = timeit.default_timer()
    result = linsort(lst)
    end = timeit.default_timer()
    mytime = end - start
    start = timeit.default_timer()
    lst.sort()
    end = timeit.default_timer()
    pytime = end - start
    print("sorted list: " + str(result))
    print("time it took mysort: ", str(mytime))
    print("time it took pysort: ", str(pytime))

import random
import timeit


def testfunction():
    largest = int(input("Enter largest value: "))
    size = int(input("Enter size of list: "))
    lst = []
    for i in range(size):
        lst.append(random.randint(0, largest))
    print("old list: " + str(lst))
    start = timeit.default_timer()
    result = linsort(lst)
    end = timeit.default_timer()
    mytime = end - start
    start = timeit.default_timer()
    lst.sort()
    end = timeit.default_timer()
    pytime = end - start
    print("sorted list: " + str(result))
    print("time it took mysort: ", str(mytime))
    print("time it took pysort: ", str(pytime))


def choose():
    prompt = input("Do you have a test file (y/n): ")
    if prompt == 'y':
        main()
    elif prompt == 'n':
        testfunction()
    else:
        print("Please enter valid character (y or n)")
        choose()


choose()