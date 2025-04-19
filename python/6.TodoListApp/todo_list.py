"""
6. Todo List App (Console-based)
Add a task to a list
Mark as done / delete a task
Use while loop to manage program flow
"""


def main():
    tasks = [] # task list
    run: bool = True
    options_menu()
    while run:
        picked_task = input("Pick an option: ")
        match picked_task:
            case "1":
                view_tasks(tasks)
                pass
            case "2":
                add_task(tasks)
                pass
            case "3":
                mark_task(tasks)
                pass
            case "4":
                delete_task(tasks)
                pass
            case "5":
                run = False
                return
            case _:
                print("That is not a valid option.")
                pass




def view_tasks(tasks):
    if not tasks:
        print("No tasks in todo list")
        return
    else:
        print("ToDo List:")
        print("==========")
        for i, task in enumerate(tasks, 1):
            status = "[x]" if task["done"] else "[ ]"
            print(f"{i}. {status} {task["taskName"]}")
    return

def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append({"taskName": task, "done": False})
    return

def mark_task(tasks):
    if not tasks:
        print("No tasks in todo list")
        return
    else:
        view_tasks(tasks)
        to_check = int(input("Pick the number of a task to mark: ")) - 1
        tasks[to_check]["done"] = True if not tasks[to_check]["done"] else False
    pass

def delete_task(tasks):
    if not tasks:
        print("No tasks in todo list")
        return
    else:
        view_tasks(tasks)
        to_delete = int(input("Pick the number of a task to delete: "))
        tasks.pop(to_delete - 1)
    pass
def options_menu():
    print("ToDo List Options Menu:")
    print("=======================")
    print("1. View All Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Quit")
    pass


if __name__ == "__main__":
    main()

