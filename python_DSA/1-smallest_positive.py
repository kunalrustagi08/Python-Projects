def smallest_positive(in_list):
    small = None
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    for num in in_list:
        if num > 0:
            if small is None or small > num:
                small = num
    return small


# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2
