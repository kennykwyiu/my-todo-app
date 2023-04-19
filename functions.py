FILEPATH = 'to_do_list.txt'

def get_to_do_list(filepath=FILEPATH):
    """ Read a text file and return the list of to-do item."""
    with open(filepath, 'r') as file_local:
        to_do_list_local = file_local.readlines()
    return to_do_list_local

def write_to_do_list(to_do_list_arg, filepath=FILEPATH): ##just a procedure, no need to return any vlaue
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(to_do_list_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_to_do_list())