from asyncore import ExitNow
from datetime import datetime


filename=input("Enter Save File Name: ")# I created the filename as the global constant to be used in the functions later on. 
                                        # As so the processes will be recorded in the process of file input and output with user define named file

def uservalidation(prompt, valid_range):
    while True:
        userinput = input(prompt)
        try:
            userinput = int(userinput)
            if userinput not in valid_range:
                print("ERROR! Please enter a valid number.")
            else:
                return userinput
        except ValueError:
            print("ERROR! Please enter a valid number.")#User validation function created to prevent out of bounds or range input from the user

def menu():
    print("*~"*60+"\n\t\t\t\t\tTaskMuse: Your Productive Companion\n")
    print("*~"*60)
    print("\n\t\t\t\t\tPLEASE SELECT THE TYPE OF USER BELOW\n")
    print("\t\t\t1:NEW USER\t\t\t\t\t\t2:EXISTING USER\n")
    print("_"*120)
    typeuser="\nPlease enter the Choice: "
    choice=uservalidation(typeuser,[1,2])
    if choice==1:
        print("\n"+"_"*120)
        print("Thank You For Choosing TaskMuse\nWe Will Brief You On the Steps To Use This App\n")
        print("*~"*60)
        print("ADD TASK: This is the section where you are free to add any type of task with various description of your choice")
        print("Within this section you are able to: \n1. Add due date/remainder\n2. Categorize tasks of your choice\n3. Priotize tasks and display them in order\n4. Search for the tasks\n")
        print("*~"*60)
        print("VIEW TASK: You are able to view the task and: \n1. Check the due dates of the respective tasks\n2. Able to mark the task as you are finished with it \n3. See the different catergories you have added\n")
        print("*~"*60)
        print("EXIT: Use this to quit the app\n")
        print("*~"*60)
        print("\n\nNow That You Are Familiar With The App, LIST ON!\n")
        mainmenu(filename)
    elif choice==2:
       mainmenu(filename)#The menu screen to determine whether the user is new or existing

def mainmenu(filename):
    print("*~"*60)
    main=("\t\t\t\t\t\tTASKMUSE\n\n"+"1: ADD TASK\n2: VIEW TASK\n"+"3: EXIT\n\n"+"*~"*60+"\n"+"What Would You Like To Do Today:"+"\n")
    choice=uservalidation(main,[1,2,3,4])
    while True:
        if choice==1:
            addtask(filename)
        elif choice==2:
            viewtask(filename)
        elif choice==3:
            stop()#the main part to determine which process will the user select as such the processes are:
                          # 1. to add the tasks 2. to view the tasks    3. exit the program


#THIS FUNCTIONS BELOW ARE FOR THE ADDTASKS
def addtask(filename):
    print("*~"*60+"\n")
    print("\t\t+ TASK\t\t\t\t+ CATEGORY"+"\t\t\t+MAIN MENU""\n\n")
    print("*~"*60+"\n")
    main=("PRESS 1: TASK \nPRESS 2: CATEGORY\nPRESS 3: MAIN MENU"+"\nENTER: ")
    choice=uservalidation(main,[1,2,3])
    if choice==1:
            task(filename)
    elif choice==2:
            category(filename)
    elif choice==3:
            mainmenu(filename)

def task(filename):
    print("\n"+"*~"*60+"\n")
    title=input("ENTER TITLE: ")
    print("")
    while True:
        try:
            date_str = input("Set the Due Date In Format Of: DATE/MONTH/YEAR"+"\nExample: 12/12/2021"+"\nDate: " )
            time_str = input("Set the Due Time In Format Of: HOURS:MINUTES AM/PM "+"\nExample: 4:00 PM (Use 12 Hour Clock System)"+"\nTime: ")

            due_datetime = datetime.strptime(date_str + ' ' + time_str, '%d/%m/%Y %I:%M %p')
            formatted_due_datetime = due_datetime.strftime('%d/%m/%Y %I:%M %p')

            break  # Exit the loop if valid date and time are provided

        except ValueError:
            print("Invalid date or time format. Please use the format: DATE/MONTH/YEAR HOURS:MINUTES AM/PM")
    notes=input("Write Here: ")
    file=open(f"{filename}.txt","w")
    file.write(title+"\n")
    file.write(formatted_due_datetime+"\n")
    file.write(notes+"\n")
    file.close()
    print("\n" + "*~" * 60 + "\n")

def category(filename):
    print("\n"+"*~"*60+"\n")
    cat=input("ENTER NAME OF CATEGORY: ")
    print("")
    title=input("ENTER TITLE: ")
    print("")
    while True:
        try:
            date_str = input("Set the Due Date In Format Of: DATE/MONTH/YEAR"+"\nExample: 12/12/2021"+"\nDate: " )
            time_str = input("Set the Due Time In Format Of: HOURS:MINUTES AM/PM "+"\nExample: 4:00 PM (Use 12 Hour Clock System)"+"\nTime: ")

            due_datetime = datetime.strptime(date_str + ' ' + time_str, '%d/%m/%Y %I:%M %p')
            formatted_due_datetime = due_datetime.strftime('%d/%m/%Y %I:%M %p')

            break  # Exit the loop if valid date and time are provided

        except ValueError:
            print("Invalid date or time format. Please use the format: DATE/MONTH/YEAR HOURS:MINUTES AM/PM")
    notes=input("Write Here: ")
    file=open(f"{filename}.txt","w")
    file.write(cat+"\n")
    file.write(title+"\n")
    file.write(formatted_due_datetime+"\n")
    file.write(notes+"\n")
    file.close()
    print("\t\t\t\t\t\tTask Details:"+"\n\n")
    print("Category: ",cat)
    print("Title:", title)
    print("Due Date and Time:", formatted_due_datetime)
    print("Notes:", notes)
    print("\n" + "*~" * 60 + "\n")


#THIS FUNCTIONS BELOW ARE FOR VIEWTAKS
def viewtask(filename):
    print("*~"*60)
    print("\n1.Category\n2.Tasks\n3.Main Menu")
    print("*~"*60)
    v="Enter: "
    choice=uservalidation(v,[1,2,3])
    if choice==1:
        print("\n"+"*~"*60)
        file=open(f"{filename}.txt","r")
        category=file.readline()
        title=file.readline()
        date=file.readline()
        notes=file.readline()
        print("CATEGORY: ",category+"\n"+"Title: ",title+"\n"+"Due Date: ",date+"\n"+"Notes: ",notes)
        file.close()
        print("\n" + "*~" * 60 + "\n")

    elif choice==2:
        print("\n"+"*~"*60)
        file=open(f"{filename}.txt","r")
        title=file.readline()
        date=file.readline()
        notes=file.readline()
        print("Title: ",title+"\n"+"Due Date: ",date+"\n"+"Notes: ",notes)
        file.close()
        print("\n" + "*~" * 60 + "\n")
    elif choice==3:
        mainmenu(filename)


def stop():
    print("Thank You For Using This App. We Wish To See You Again!")
    exit()

menu()