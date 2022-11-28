def read_todos(filepath):
    with open(filepath, 'r') as file:
        file_lines = file.readlines()
    return file_lines

def write_todos(todos_arg, filepath):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())