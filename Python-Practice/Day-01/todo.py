def display_menu():
    print("\nMenu:\n")
    print("1.Add task")
    print("2.View tasks")
    print("3.Mark as done/remove")
    print("4.Exit")

def add_task(tasks):
    new_task=input("Enter a new task:")
    tasks.append(new_task)
    print("Task added")

def view(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("Your tasks:")
    for i,task in enumerate(tasks,start=1):
        print(f"{i}.{task}")

def mar(tasks):
    if not tasks:
       print("No tasks available.")
       return
    mark=int(input("Enter the no. of the task completed"))
    if(mark>=1 and mark<=len(tasks)):
        tasks.pop(mark-1)
        print("Task removed successfully!")
    else:
        print("Invalid task number")

def exit():
    print("Exited Succesfully")

tasks = []

while True:
    display_menu()

    c = int(input("Enter your choice: "))

    if c == 1:
        add_task(tasks)

    elif c == 2:
        view(tasks)

    elif c == 3:
        mar(tasks)

    elif c == 4:
        print("Exited Successfully")
        break

    else:
        print("Invalid choice")



