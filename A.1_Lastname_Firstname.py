"""
Full Name: Jacob Meyer
Group Names: Jacob Meyer, Bryan Nguyen, Janel Nguyen
ID: jrm7250
Date: 9-28-22
Filename: A1_Jacob_Meyer_jrm7250
Purpose: compare elements in a list using two for loops
"""


def count(lst, num):
    counter = 0
    for i in range(len(lst)):
        if lst[i] == num:
            counter = counter + 1
    return counter


def max_min(lst):
    max_count = 0
    min_count = 0
    output = [0, 0]
    for i in range(len(lst)):
        counter = count(lst, lst[i])
        if counter > max_count:
            max_count = counter
            output[0] = lst[i]
        if counter < min_count or i == 0:
            min_count = counter
            output[1] = lst[i]
    return output


def window(lst, w, start):
    biggest = lst[start]
    for i in range(start, start+w):
        if lst[i] > biggest:
            biggest = lst[i]
    return biggest


def shift_lst(lst, w):
    new_lst = []
    for i in range(len(lst)-w+1):
        biggest = window(lst, w, i)
        new_lst = new_lst + [biggest]
    return new_lst


def main():
    lst1 = [10, 30, 60, 88, 10, 30, 10, 60, 3, 88]
    output = max_min(lst1)
    print(output)

    lst2 = [2, 5, 12, 3, 4]
    w = 2
    result1 = shift_lst(lst2, w)
    print(result1)

    lst2 = [1, 3, 5, 1, 2, 4, 7, 8]
    w = 4
    result2 = shift_lst(lst2, w)
    print(result2)

    lst2 = [-2, -9, -1, -4, 33, 11, 65, -4, 99]
    w = 3
    result3 = shift_lst(lst2, w)
    print(result3)



main()
