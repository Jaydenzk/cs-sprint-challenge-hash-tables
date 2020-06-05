def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    storage = {}
    result = []
    # loop each num in array
    # abs() is to get absolute value and .get return the value for given key
    for num in a:
        if storage.get(abs(num)):
            if (storage.get(abs(num)) + num) == 0:
                result.append(abs(num))
        # if no value, pass num as key along with it's value
        else:
            storage[abs(num)] = num

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
