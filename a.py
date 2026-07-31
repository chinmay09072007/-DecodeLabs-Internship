tasks=[]
while True:
    ch=int(input("Enter your choice:\n1. Add task\n2. View tasks\n3. Delete task\n4. Exit\n"))

    if ch==1:
        print("Enter the task to be added:")
        task=input()
        tasks.append(task)
        print(" task added successfully\n1")
    elif ch==2:    
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}\n") 
                   
    elif ch==3:
        print ("Enter task to be deleted")
        del_task=input()
        if del_task in tasks:
            tasks.remove(del_task)
            print("Task deleted successfully")
        else:
            print("Task not found.")
    elif ch==4:

        print("Exiting the program.")
        break        




