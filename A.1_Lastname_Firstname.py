print("joe mother")
print("bryan is joe mother")
print("que te gusta hacer?")
print("Donda esta el milk")
print("Jake gets no bitches")
print("Donde esta el leche")

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


def main():
    lst = [10, 30, 60, 88, 10, 30, 10, 60, 3, 88]
    output = max_min(lst)
    print(output)


main()
