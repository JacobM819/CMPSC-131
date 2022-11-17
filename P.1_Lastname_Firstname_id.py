"""
Full Name:
Group Names: Bryan Nguyen, Janel Nguyen, Jacob Meyer
ID:
Date: 11-17-22
Filename: P.1_Lastname_Firstname_id
Purpose: implement all the concepts learned in this course
"""


def create_lst(filename):
    infile = open(filename, "r")
    lst = []
    for line in infile:
        lst += [line.split()]
    infile.close()
    return lst


def in_lst(word, info_lst):
    for i in range(1, len(info_lst)):
        if info_lst[i][0] == word:
            info_lst[i][1] += 1
            return i
    info_lst += [[word, 1]]
    i = len(info_lst) - 1
    return i


def get_word_info(lst):
    info_lst = [["Word", "Occurrences"]]
    max_occur = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            index = in_lst(lst[i][j], info_lst)
            info_lst[index] += [i + 1]
            info_lst[index] += [j + 1]
            if info_lst[index][1] > max_occur and i != 0:
                max_occur += 1
    for i in range(max_occur):
        info_lst[0] += ["Line", "Word #"]
    return info_lst


def write_to_cvs(filename, info):
    outfile = open(filename, "w")
    for i in range(len(info)):
        for j in range(len(info[i])):
            if j == len(info[i]) - 1:
                outfile.write(str(info[i][j]) + "\n")
            else:
                outfile.write(str(info[i][j]) + ",")
    outfile.close()


def main():
    lst = create_lst("project.txt")
    info = get_word_info(lst)
    write_to_cvs("project.cvs", info)


main()
