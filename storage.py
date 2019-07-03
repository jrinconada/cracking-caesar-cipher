

def read(location):
    """ Given a file path returns the contents of the file """
    with open(location, 'r') as file:
        return file.read()


def write(location, data):
    """ Given a file path and some data, saves the data to the file.
        Automatically creates the file if it does not exit and overwrites the content if there is something """
    with open(location, 'w') as file:
        file.write(data)
