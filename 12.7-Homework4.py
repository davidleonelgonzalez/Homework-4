# 1630338
# David Leonel Gonzalez

# ZyLabs 12.6.1 urged the use of variable age as an input integer for def get_age
# which an if statement would be needed to assert the input age that needed to be between
# 18 and 75. Then raised a value error if not in the range of the if statement, thus later returning age

def get_age():

    age = int(input())

    if age < 18 or age > 75:

        raise ValueError("Invalid age.")

    return age

# ZyLabs 12.6.1 used heart_rate as variable that needed to be returned which the function
# needed to calculate heart rate from the age input, thus formula used to meet correct age
# and heart rate corresponding output


def fat_burning_heart_rate(age):

    heart_rate = (220 - age) * 0.70

    return heart_rate

# main is used by participation activity 12.6.1 to handle the exception to modify the call of get_age
# and fat_burning_heart_rate def.


if __name__ == "__main__":
    # used same value error statement from class powerpoint to modify the call
    # of def to assign .format for the required output.

    try:
        age = get_age()
        print("Fat burning heart rate for a {} year-old: {} bpm" .format(age, fat_burning_heart_rate(age)))
    except ValueError as error:
        print(error)
        print("Could not calculate heart rate info.")
        print()
        # used .format to call back the output from the def parameters of age
        # as well as fat_burning_heart_rate(age) modified output
        # stackoverflow.com suggested i use this method given the def parameter approach

# Lastly,  used suggested message for print value of value error for corresponding input
# a print value was added because ZyLabs showed a new line was needed after output.
