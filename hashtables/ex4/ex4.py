def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    numbers_seen = {}

    numbers_with_negatives = []
    for number in a:
        numbers_seen[number] = 1

        if number != 0 and -number in numbers_seen:
            numbers_with_negatives.append(abs(number))
            print(numbers_with_negatives)

   #  print('here ', numbers_seen)
    return numbers_with_negatives


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
