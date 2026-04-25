import json

# Function to load data from file
def load_data():
    try:
        f = open("tasks.json", "r")
        data = json.load(f)
        f.close()
        return data["tasks"], data["status"]
    except:
        # Agar file nahi hai to khali lists return karo
        return [], []

# Function to save data to file
def save_data(t_list, s_list):
    # Dono lists ko ek dictionary mein daal kar save karo
    data_to_save = {
        "tasks": t_list,
        "status": s_list
    }
    f = open("tasks.json", "w")
    json.dump(data_to_save, f)
    f.close()

# Main Program Starts Here
my_tasks, my_status = load_data()

while True:
    print("\n********** MY TO-DO LIST **********")
    print("1. Add New Task")
    print("2. Show All Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    
    user_input = input("Choose an option (1-5): ")

    if user_input == "1":
        new_task = input("What is the task? ")
        my_tasks.append(new_task)
        my_status.append("Pending") # Naya task hamesha pending hoga
        save_data(my_tasks, my_status)
        print("Done! Task added to the list.")

    elif user_input == "2":
        print("\n--- YOUR CURRENT TASKS ---")
        if len(my_tasks) == 0:
            print("Your list is empty!")
        else:
            # Simple loop using range instead of enumerate
            for i in range(len(my_tasks)):
                print(str(i) + ". [" + my_status[i] + "] " + my_tasks[i])

    elif user_input == "3":
        task_num = int(input("Enter the task number to mark as done: "))
        if task_num < len(my_tasks):
            my_status[task_num] = "Completed"
            save_data(my_tasks, my_status)
            print("Great job! Task marked as completed.")
        else:
            print("Invalid number! Please check the list again.")

    elif user_input == "4":
        task_num = int(input("Enter the task number to delete: "))
        if task_num < len(my_tasks):
            my_tasks.pop(task_num)
            my_status.pop(task_num)
            save_data(my_tasks, my_status)
            print("Task has been removed.")
        else:
            print("Invalid number!")

    elif user_input == "5":
        print("Exiting... Have a nice day!")
        break
    
    else:
        print("Wrong option! Try again.")