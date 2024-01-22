def askChoice():
    tasks = []
    while True:
        choice = input("\nSelect a number.(Type 'exit' for quitting)\n1. Show all tasks\n2. Add a task\n3. Delete a task\n4. Complete a done task\n:")

        if (choice == "exit"):
            print("Au revoir!")
            break
        else:
            if(choice == "1"):
                showTasks(tasks)
            if(choice == "2"):
                addTasks(tasks)
            if(choice == "3"):
                deleteTask(tasks)
            if(choice == "4"):
                completeTask(tasks)

# Function for showing all tasks.
def showTasks(tasks):
    if(len(tasks) == 0):
        print("\nThere is no task now.")
    else:
        print("\nTasks are below:")
        for task in tasks:
            print(str(tasks.index(task)) + "[ ] : " + task)

# Function for add tasks.
def addTasks(tasks):
    while True:
        # 사용자 입력 받기
        user_input = input("Add a task(Type 'exit' for quitting): ")

        # 종료 조건 확인
        if user_input.lower() == 'exit':
            break

        # 리스트에 문자열 추가
        tasks.append(user_input)
    
    showTasks(tasks)

# Function for deleting a task
def deleteTask(tasks):
    showTasks(tasks)
    if tasks:
        try:
            task_index = int(input("Enter the index of the task to delete: "))
            if 0 <= task_index < len(tasks):
                del tasks[task_index]
                print("Task deleted successfully.")
            else:
                print("Invalid index. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks to delete.")





def showTasks(tasks):
    if not tasks:
        print("\nThere are no tasks now.")
    else:
        print("\nTasks are below:")
        for index, (task, completed) in enumerate(tasks):
            status = "[x]" if completed else "[ ]"
            print(f"{index} {status} : {task}")


def addTasks(tasks):
    while True:
        user_input = input("Add a task(Type 'exit' for quitting): ")
        if user_input.lower() == 'exit':
            break
        tasks.append((user_input, False))
    showTasks(tasks)



def completeTask(tasks):
    showTasks(tasks)
    if tasks:
        try:
            task_index = int(input("Enter the index of the task to complete: "))
            if 0 <= task_index < len(tasks):
                task, _ = tasks[task_index]
                tasks[task_index] = (task, True)
                print("Task marked as completed.")
            else:
                print("Invalid index. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks to complete.")




# main part
print("=========================================\n         Welcome to To-do List\n=========================================")
askChoice()
