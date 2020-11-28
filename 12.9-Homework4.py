# 1630338
# David Leonel Gonzalez

# ZyLabs 12.8.1 had a default template to use parts and name as variables
# the lab had a flaw to correct which the try/ except block needed to assign
# after the given while statement.
parts = input().split()
name = parts[0]
while name != "-1":

    # so as suggested by ZyLabs 12.8.1 to insert a try block to catch the exception
    # using age as variable to assign int to parts + 1 because without adding 1
    # output would be 1 less
    # and as suggested an output of 0 was assigned to age

    try:
        age = int(parts[1]) + 1
    except ValueError as exception:
        age = 0

# to get next line indent had to be removed one to allow for
# print statement to follow next line, thus print is to the left.

    print("{} {}" .format(name, age))

# parts and name variable were used from ZyLabs 12.8.1 as recommended to
# display correct output list of single word first name and age.

    parts = input().split()
    name = parts[0]
