#test

# FUNCTION FOR ADDING TASKS
def addTask():
    # take input from user
    task = input("Please enter a task")

    # read existing tasks from file
    try:
        file = open("pendingTask.txt", "r")
        tasks = file.readlines()
        file.close()
    except FileNotFoundError:
        tasks = []

    # add new task to existing tasks
    tasks.append(task + "\n")

    # save updated tasks to file
    file = open("pendingTask.txt", "w")
    file.writelines(tasks)
    file.close()

    # print success message
    print("Task added successfully")


# FUNCTION FOR COMPLETED TASKS

def completedTask():
    # take input from user
    taskName = input("Please enter the name of completed task")

   # read existing tasks from pendingTask.txt file
    try:
        file = open("pendingTask.txt", "r")
        tasks = file.readlines()
        file.close()
    except FileNotFoundError:
        return

   # find the index of completed task in pendingTask.txt file
    taskIndex = None
    for index, task in enumerate(tasks):
        if task == taskName + "\n":
            taskIndex = index
            break
    if taskIndex == None:
        print("Task not found")
        return

    # remove completed task from pendingTask.txt file
    completedTask = tasks.pop(taskIndex)

    # read completed tasks from completedTask.txt file
    try:
        file = open("completedTask.txt", "r")
        completedTasks = file.readlines()
        file.close()
    except FileNotFoundError:
        completedTasks = []

    # add completed task to completedTask.txt file
    completedTasks.append(completedTask)

    # save updated completed tasks to completedTask.txt file
    file = open("completedTask.txt", "w")
    file.writelines(completedTasks)
    file.close()

    # save updated pending tasks to pendingTask.txt file
    file = open("pendingTask.txt", "w")
    file.writelines(tasks)
    file.close()

    # print success message
    print("Task marked as completed and moved to complete task text file successfully")


# FUNCTION FOR VIEWING PENDING TASKS

def viewPendingTasks():
    # read pending tasks from pendingTask.txt file
    try:
        file = open("pendingTask.txt", "r")
        tasks = file.readlines()
        file.close()
    except FileNotFoundError:
        print("No pending tasks")
        return

    # Display pending tasks with their indices
    if not tasks:
        print("No pending tasks")
        return
    else:
        print("PENDING TASKS")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task.strip()}")

# FUNCTION FOR VIEWING COMPLETED TASKS


def viewCompletedTasks():
    # read completed tasks from completedTask.txt file
    try:
        file = open("completedTask.txt", "r")
        tasks = file.readlines()
        file.close()
    except FileNotFoundError:
        print("No completed tasks")
        return

    # Display completed tasks with their indices
    if not tasks:
        print("No completed tasks")
        return
    else:
        print("COMPLETED TASKS")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task.strip()}")


# FUNCTION FOR EDITING PENDING TASKS

def editTasks():
    # Enter name of task to be edited
    taskName = input("Please enter the name of task to be edited")

    # read existing tasks from pendingTask.txt file
    try:
        file = open("pendingTask.txt", "r")
        tasks = file.readlines()
        file.close()
    except FileNotFoundError:
        print("No pending tasks to edit")
        return

    # find the index of task to be edited in pendingTask.txt file
    taskIndex = None
    for index, task in enumerate(tasks):
        if task == taskName + "\n":
            taskIndex = index
            break
    if taskIndex == None:
        print("Task not found")
        return

    # Ask the user to enter a new task description
    newTask = input("Please enter a new task description")

    # replace the old task with new task
    tasks[taskIndex] = newTask + "\n"

    # save updated tasks to file
    file = open("pendingTask.txt", "w")
    file.writelines(tasks)
    file.close()

    # print success message
    print("Task edited successfully")
    viewPendingTasks()

# FUNCTION FOR DELETING PENDING TASKS


def deleteAllPendingTasks():
    # read existing tasks from pendingTask.txt file
    question = input(
        "Are you sure you want to delete all pending tasks? (y/n)")
    if question == "y":
        try:
            file = open("pendingTask.txt", "r")
            tasks = file.readlines()
            file.close()
        except FileNotFoundError:
            print("No pending tasks to delete")
            return

        # delete all pending tasks
        tasks.clear()

        # save updated tasks to file
        file = open("pendingTask.txt", "w")
        file.writelines(tasks)
        file.close()

        # print success message
        print("All pending tasks deleted successfully")
    else:
        print("No pending tasks deleted")


# FUNCTION FOR DELETING COMPLETED TASKS

def deleteAllCompletedTasks():
    # read existing tasks from completedTask.txt file
    question = input(
        "Are you sure you want to delete all completed tasks? (y/n)")
    if question == "y":
        try:
            file = open("completedTask.txt", "r")
            tasks = file.readlines()
            file.close()
        except FileNotFoundError:
            print("No completed tasks to delete")
            return

        # delete all completed tasks
        tasks.clear()

        # save updated tasks to file
        file = open("completedTask.txt", "w")
        file.writelines(tasks)
        file.close()

        # print success message
        print("All completed tasks deleted successfully")
    else:
        print("No completed tasks deleted")

addTask()



# All functions for the todo list
# addTask()
# completedTask()
# viewPendingTasks()
# viewCompletedTasks()
# editPendingTasks()
# deleteAllPendingTasks()
# deleteAllCompletedTasks()
