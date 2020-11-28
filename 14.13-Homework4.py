# 1630338
# David Leonel Gonzalez

num_calls = 0

# 14.8.1 participation activity gives a partition example which
# I based upon my code for the def partition section


def partition(user_ids, i, k):
    # 14.13.1 ZyLab suggest to assign middle element to the pivot

    middle = i + (k - i) // 2
    pivot = user_ids[middle]
    # then a comparison was needed to assign l to i and h to k

    id_num = False
    l = i
    h = k
    # initialize the variable to left and right
    # increment of 1
    # decrement of 1
    # in a while loop like example 14.8.1
    while not id_num:
        while user_ids[l] < pivot:
            l = l + 1

        while pivot < user_ids[h]:
            h = h - 1

        if l >= h:
            id_num = True
# determined swap was necessary for user_ids[l] and user_ids[h]
        else:
            num = user_ids[l]
            user_ids[l] = user_ids[h]
            user_ids[h] = num

            l = l + 1
            h = h - 1
# then returned h but added 1 to stay within recursion depth of comparison
    return h + 1

# 14.8.4 participation activity example was used for the section
# of code I used for def quicksort


def quicksort(user_ids, i, k):
    # 14.13 ZyLab suggest to increment global variable num_calls
    # as well as adding 1 to num_calls each time quicksort() gets called

    global num_calls
    num_calls = num_calls + 1

    # used if statement like example 14.8.4 position k greater than i in partition
    if i < k:

        # used variable j like 14.8.4 example for the last element in partition
        j = partition(user_ids, i, k)
        # recursively sorted low and high partition as instructed used 14.8.4 example
        # changed quicksort with variable j -1
        # changed quicksort j without adding 1
        # changes made to allow for correct output
        quicksort(user_ids, i, j - 1)
        quicksort(user_ids, j, k)

# 14.13 ZyLab provided the remaining code for correct layout of code
# placing input corresponding to partition and quicksort


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

# asserted that there is an initial call to quick start
    quicksort(user_ids, 0, len(user_ids) - 1)

# asserted to print num_calls to quicksort
    print(num_calls)

# concluded by stating the printing sorted user_ids
    for user_id in user_ids:
        print(user_id)
