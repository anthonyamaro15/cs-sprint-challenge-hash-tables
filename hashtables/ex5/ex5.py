# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    files_found = []

    directory = {}

    for file in files:

        parts = file.split('/')

        # parts[-1] to get last item
        filename = parts[-1]
        # foo, bar, baz

        if filename not in directory:
            directory[filename] = []

        directory[filename].append(file)

    for query in queries:
        if query in directory:
            files_found.extend(directory[query])

    return files_found


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
