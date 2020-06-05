def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weight = {}
    dupe_check = False
    duplicates = {} # Check

    # iterate through weights and store them in the dict
    for i in range(0, length):
        current = weights[i]
        weight[current] = i  # set the value to the index
        # we subtract the current value from the limit to find which package
        target = limit - current
        if target in weight:
            if current > target:
                return (i, weight[target])  # tuple of indexes
            elif current < target:
                return (i, weight[target])
            elif target == current:  # if it finds a dupe
                if dupe_check is False:  # and it isnt already clasified as a duplicate
                    dupe_check = True  # change the bool
                    duplicates[current] = i  # set the value to the index
                elif dupe_check is True:
                    return (i, duplicates[current])



    return None
