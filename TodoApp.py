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

# main part
print("=========================================\n         Welcome to To-do List\n=========================================")
askChoice()
