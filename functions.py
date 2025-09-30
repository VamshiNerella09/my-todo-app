FILEPATH= "todos.txt"


def get_todos(filepath=FILEPATH):
    """" Reading the text file and return it to the
    list."""
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos( todos_arg, filepath=FILEPATH):
    """ writing the todos item in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == '__main__':
    print("Hello")
    print(get_todos())

