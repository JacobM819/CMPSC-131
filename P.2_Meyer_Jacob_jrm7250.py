"""
Full Name: Jacob Meyer
Group Names: Bryan Nguyen, Janel Nguyen, Jacob Meyer
ID: jrm7250
Date: 11-17-22
Filename: P.1_Meyer_Jacob_jrm7250
Purpose: implement all the concepts learned in this course
"""


def create_lst(filename):
    infile = open(filename, "r")
    lst = []
    for line in infile:
        lst += [line.split()]
    infile.close()
    return lst


def position_in_lst(word, info_lst):
    # If the word is not in the list, append the new word to the end
    for i in range(1, len(info_lst)):
        if info_lst[i][0] == word:
            info_lst[i][1] += 1
            return i
    # If the word is in the list, return its position index
    info_lst += [[word, 1]]
    position = len(info_lst) - 1
    return position


def get_word_info(lst):
    info_lst = [["Word", "Occurrences"]]
    max_occurrences = 0
    # Create 2D list and grab info for each word
    for row in range(len(lst)):
        for word in range(len(lst[row])):
            word_index = position_in_lst(lst[row][word], info_lst)
            info_lst[word_index] += [row + 1]
            info_lst[word_index] += [word + 1]
            if info_lst[word_index][1] > max_occurrences and row != 0:
                max_occurrences += 1
    # The length of the first row depends on the most occurring word
    for i in range(max_occurrences):
        info_lst[0] += ["Line", "Word #"]
    return info_lst


def write_to_csv(filename, info):
    outfile = open(filename, "w")
    # Iterate linearly through the 2D list and write to the CSV
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
    write_to_csv("project.cvs", info)


main()
