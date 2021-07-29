# table_data = [['apples', 'oranges', 'cherries', 'banana'],
#               ['Alice', 'Bob', 'Carol', 'David'],
#               ['dogs', 'cats', 'moose', 'goose']]
#
#
# def print_table(table):
#     col_widths = [0] * len(table)
#     for i, row in enumerate(table):
#         col_widths[i] = max(len(elem) for elem in row)
#
#     for b in range(len(table[0])):
#         print_list = []
#         for a in range(len(table)):
#             print_list.append(table[a][b])
#         for item, width in zip(print_list, col_widths):
#             print(item.rjust(width), end=' ')
#         print('')
#
#
# print_table(table_data)
#
# https://www.reddit.com/r/learnpython/comments/adu1ky/how_did_i_go_with_this_table_printer_project_from/


table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


def print_table(table_data):
    # initialize the list "col_widths" with zeroes equal to the length of the input list
    col_widths = [0] * len(table_data)

    # iterate over the input list to find the longest word in each inner list
    # if its larger than the current value, set it as the new value
    for i in range(len(table_data)):
        for j in range(len(table_data[i])):
            if len(table_data[i][j]) > col_widths[i]:
                col_widths[i] = len(table_data[i][j])

    # assuming each inner list is the same length as the first, iterate over the input list
    # printing the x value from each inner list, right justifed to its corresponding value
    # in col_widths
    for x in range(len(table_data[0])):
        for y in range(len(table_data)):
            print(table_data[y][x].rjust(col_widths[y]), end=' ')
        print('')


print_table(table_data)

# changed input list to table_data
# https://www.reddit.com/r/inventwithpython/comments/455qgj/automate_the_boring_stuff_chapter_6_table_printer/
