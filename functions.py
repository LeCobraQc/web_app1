FILEPATH = "todos.txt"
def opens_file(filepath=FILEPATH):
    """ Read a text file and return a list of todo items"""
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local

def closes_file(todos_local,filepath=FILEPATH):
    """ Write the todo list in todo.txt and close it"""
    with open(filepath, "w") as file:
        file.writelines(todos_local)


