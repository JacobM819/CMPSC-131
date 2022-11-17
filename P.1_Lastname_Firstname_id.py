def occur_count(word, lst):
    count = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if word == lst[i][j]:
                count += 1
    return count


def create_lst(filename):
    infile = open(filename, "r")
    lst = []
    for line in infile:
        lst += [line.split()]
    infile.close()
    print(lst)
    return lst


def write_cvs(filename, lst):
    outfile = open(filename, "w")
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            word = lst[i][j]
            occur = occur_count(word, lst)
            line_num = i+1
            word_num = j+1
            print(word, occur, line_num, word_num)
    outfile.close()


def main():
    lst = create_lst("project.txt")
    write_cvs("project.cvs", lst)


main()
