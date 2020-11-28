# 1630338
# David Leonel Gonzalez

# ZyLabs 14.6.1 indicates of finding descending index
def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        index_descend = i
        for integer in range(i + 1, len(numbers)):
            if numbers[index_descend] < numbers[integer]:
                index_descend = integer


# 14.6.1 participation activity suggest to swap between numbers[i] and numbers[index_descend]
        num = numbers[i]
        numbers[i] = numbers[index_descend]
        numbers[index_descend] = num
# then a for loop will concede num in numbers to then space with end='' like example in 14.6.1

        for num in numbers:
            print(int(num), end=' ')
        print()

    return numbers

# 14.6.1 asserts to read in a list of integer into numbers
# quora.com suggest the process of input.split() to typecast the inputs into int
# thus int(num) for num which multiple inputs are split for correct output space


if __name__ == "__main__":
    numbers = [int(num) for num in input("").split()]
    selection_sort_descend_trace(numbers)
# then calling numbers into the selection_sort_descend_trace() to give output
