def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    needed_weights = {}

    for current_weight_index in range(len(weights)):

        current_weight = weights[current_weight_index]

        if current_weight in needed_weights:
            previously_seen_weight_index = needed_weights[current_weight]

            return (current_weight_index, previously_seen_weight_index)
        needed_weights[limit - current_weight] = current_weight_index

    return None


weights_1 = [4, 6, 10, 15, 16]


print(get_indices_of_item_weights(weights_1, 1, 9))
