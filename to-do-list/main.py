# this code implements a simple to do list with small user interference


import json


file_name="python/todo_list.json"



#function to load tasks
def load_tasks():
    try :
        with open(file_name,'r') as f:
            return json.load(f)
    except:
        return {"tasks":[]}


#function to save tasks
def save_tasks(tasks):
    try :
        with open(file_name,'w') as f:
            json.dump(tasks,f)
    except:
        print("failed to save")

#function to view tasks
def view_tasks(tasks):
    task_list=tasks["tasks"]
    if len(task_list) ==0 :
        print("No tasks to display")
    else:
        print("Your to do list ")
        for idx,task in enumerate(task_list):
            status="[Completed]" if task['complete'] else "[Pending]"
            print(f"Item {idx+1}.{task['description']} | {status}")
            


#function to create tasks
def create_task(tasks):
    description=input("Enter the task description ").strip()
    
    if description:
        tasks["tasks"].append({"description":description,"complete":False})

        #save changes
        save_tasks(tasks)
        print("tasks added")
    else:
        print("description can not be empty")


#function to mark tasks if they are competed or no
def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_number=int(input("Enter the task number to complete").strip())
        if 1<=task_number<=len(tasks):
            tasks["tasks"][task_number-1]["complete"]=True
            save_tasks(tasks)
            print("Task completed and saved ")
        else :
            print("Invalid tasks number")
    except :
        print("Enter a valid number")


#main function to run the enitre program 
def main():
    
    #load the tasks 
    tasks=load_tasks()
    print(tasks)


    while True:
        print("\n To-do list manager ")
        print("1. View tasks")
        print("2. Add task")
        print("3. Comlete task")
        print("4. Exit")

        choice=input("Enter your choice :").strip()
        if choice=="1":
            view_tasks(tasks)
        elif choice=="2":
            create_task(tasks)
        elif choice=="3":
            mark_task_complete(tasks)
        elif choice=="4":
            print("Goodbye")
            break
        else:
            print("invalid choice.PLease try another choice")
main()  
