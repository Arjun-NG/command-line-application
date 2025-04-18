FILE_PATH='new-todo.txt'
def get_todo(filepath='FILE_PATH') :
    with open(filepath, 'r') as file:
        local_todo = file.readlines()
        file.close()
    return local_todo

def write_todo(todos,file_path=FILE_PATH):
    with open(file_path, 'w') as file:
        file.writelines(todos)
        file.close()
    return todos



def show() :
    with open(FILE_PATH ,'r') as e:
        for index, i in enumerate(e):
            print(f"{index + 1}-{i.strip()}")
        e.close()

def add(user_input):
    if user_input.startswith('add'):
        try:
            task = user_input[4:].strip()
            todos=get_todo()
            todos.append(task + "\n")
            write_todo(todos)
        except ValueError:
            print("give correct format...")

def edit(user_input):
        number = int(user_input[5:])
        number = number - 1
        todos=get_todo()
        print(f"selected {todos[number].strip()}")
        todo = input("Enter the task : ")
        todos[number] = todo + "\n"
        write_todo(todos)
        show()
def complete(user_input):
    try:
        task = int(user_input[9:])
        task = task - 1
        todos = get_todo()
        index = task
        item = todos[index].strip("\n")
        todos.pop(index)
        write_todo(todos)
        print(f"{item} is removed....")
        show()
    except IndexError:
        print("There's no item in a bucket")

def all():
    todos = get_todo()
    todos.clear()
    write_todo(todos)
    print("All data deleted...")
    show()