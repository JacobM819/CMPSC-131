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


def write_to_csv(filename, info_lst):
    outfile = open(filename, "w")
    # Iterate linearly through the 2D list and write to the CSV
    for i in range(len(info_lst)):
        for j in range(len(info_lst[i])):
            if j == len(info_lst[i]) - 1:
                outfile.write(str(info_lst[i][j]) + "\n")
            else:
                outfile.write(str(info_lst[i][j]) + ",")
    outfile.close()


def entire_map(info_table):
    for i in range(1, len(info_table)):
        for j in range(len(info_table[i])):
            # print(info_table[i][j], end=" ")
            pass
        print()


def get_value(key, info_table):
    value_lst = []
    for i in range(1, len(info_table)):
        for j in range(1, len(info_table[i])):
            if key == info_table[i][0]:
                value_lst += [info_table[i][j]]
    if len(value_lst) != 0:
        return value_lst
    else:
        return -1


def get_location(key, occurrence, info_table):
    location_lst = []
    for i in range(1, len(info_table)):
        if key == info_table[i][0] and occurrence+3 < len(info_table[i]):
            location_lst += [info_table[i][occurrence+1], info_table[i][occurrence+2]]
    if len(location_lst) != 0:
        return location_lst
    else:
        return -1


# Not finished
def delete_table(info_table):
    empty_lst = [[]]
    return empty_lst


def delete_entry(info_table, key):
    info_copy1 = info_table
    for i in range(len(info_copy1)):
        if info_copy1[i][0] == key and i != 0:
            info_copy1[i] = [key]
    return info_copy1


# Not finished
def delete_location(info_table, key, occurrence):
    info_copy2 = []
    return info_copy2


# 2D LIST FORMAT: [["Line", "Word#"...], [word, occurrences, line, word#], [word, occurrences, line, word#]...]
def main():
    lst = create_lst("project.txt")
    info_lst = get_word_info(lst)
    write_to_csv("project.cvs", info_lst)
    entire_map(info_lst)
    location_lst = get_location("CMPSC131", 2, info_lst)
    print(location_lst)

    value_lst = get_value("CMPSC131", info_lst)
    # print(value_lst)


# Not finished
    empty_lst = delete_table(info_lst)
    # print(empty_lst)

    info_copy1 = delete_entry(info_lst, "course")
    # print("info_copy1:", info_copy1)

# Not finished
    info_copy2 = delete_location(info_lst, "CMPSC131", 1)
    # print(info_copy2)


main()
