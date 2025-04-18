from modules.functions import add,show,edit,complete,all


while True:
    user_input = input("Enter the action : ").strip()
    if user_input.startswith('add'):
        add(user_input)
    elif user_input.startswith('show'):
        show()
    elif user_input.startswith('edit') :
        edit(user_input)
    elif user_input.startswith('complete') :
        complete(user_input)
    elif user_input.startswith('all') :
        all()
    else:
        print("command not found....")

    