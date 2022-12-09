"""
Full Name:
Group Names: Bryan Nguyen, Janel Nguyen, Jacob Meyer
ID:
Date: 12-9-22
Filename: P.2_Lastname_Firstname_id
Purpose: Run multiple search operations on the word-information-table previously implemented in Project 1
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
    for i in range(len(info_lst)):
        if info_lst[i][0] == word:
            info_lst[i][1] += 1
            return i
    # If the word is in the list, return its position index
    info_lst += [[word, 1]]
    position = len(info_lst) - 1
    return position


def get_word_info(lst):
    info_lst = []
    # Create 2D list and grab info for each word
    for row in range(len(lst)):
        for word in range(len(lst[row])):
            word_index = position_in_lst(lst[row][word], info_lst)
            info_lst[word_index] += [row + 1]
            info_lst[word_index] += [word + 1]
    return info_lst


def write_to_csv(filename, info_lst):
    outfile = open(filename, "w")
    max_occurrence = 0

    for i in range(len(info_lst)):
        if info_lst[i][1] > max_occurrence:
            max_occurrence = info_lst[i][1]

    info_lst = [["Word", "Occurrences"]] + info_lst
    for i in range(max_occurrence):
        info_lst[0] += ["Line", "Word #"]

    # Iterate linearly through the 2D list and write to the CSV
    for i in range(len(info_lst)):
        for j in range(len(info_lst[i])):
            if j == len(info_lst[i]) - 1:
                outfile.write(str(info_lst[i][j]) + "\n")
            else:
                outfile.write(str(info_lst[i][j]) + ",")
    outfile.close()


# Part 2 #
def entire_map(info_table):
    for i in range(len(info_table)):
        for j in range(len(info_table[i])):
            print(info_table[i][j], end=" ")
        print()


def get_value(key, info_table):
    value_lst = []
    for i in range(len(info_table)):
        for j in range(1, len(info_table[i])):
            if key == info_table[i][0]:
                value_lst += [info_table[i][j]]
    if len(value_lst) != 0:
        return value_lst
    else:
        return -1


def get_location(key, occurrence, info_table):
    location = []
    for i in range(len(info_table)):
        if info_table[i][0] == key and len(info_table[i]) > occurrence*2+1:
            location += [info_table[i][occurrence*2], info_table[i][occurrence*2+1]]
    if len(location) == 0:
        location = [-1, -1]
    return location


def delete_table(info_table):
    empty_lst = [[]]
    return empty_lst


def delete_entry(info_table, key):
    info_copy1 = info_table
    for i in range(len(info_copy1)):
        if info_copy1[i][0] == key:
            info_copy1[i] = [key]
            return info_copy1
    return -1


def delete_location(key, occurrence, info_table):
    info_copy = []
    occurrence_found = -1
    for i in range(len(info_table)):
        if info_table[i][0] == key:
            info_copy += [[]]
            for j in range(len(info_table[i])):
                if j == occurrence*2 or j == occurrence*2+1:
                    occurrence_found = 0
                    pass
                else:
                    info_copy[i] += [info_table[i][j]]
                if j == 1:
                    info_copy[i][1] -= 1
        else:
            info_copy += [info_table[i]]
    if occurrence_found == -1:
        return -1
    return info_copy


# 2D LIST FORMAT: [["Line", "Word#"...], [word, occurrences, line, word#], [word, occurrences, line, word#]...]
def main():
    lst = create_lst("project.txt")
    info_lst = get_word_info(lst)
    write_to_csv("project.cvs", info_lst)

    entire_map(info_lst)
    value_lst = get_value("Mead", info_lst)
    print(value_lst)

    location = get_location("CMPSC131", 2, info_lst)
    print(location)

    info_copy1 = delete_table(info_lst)
    print(info_copy1)

    info_copy2 = delete_entry(info_lst, "course")
    print(info_copy2)

    info_copy3 = delete_location("CMPSC131", 1, info_lst)
    print(info_copy3)


main()
