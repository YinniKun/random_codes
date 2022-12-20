'''
Task Manager tells you the task you should complete today based on the
information stored in a tasks.txt file in the same directory
The tasks.txt file can be modified by calling the function, or be edited manually

To use this program efficiently, break down big tasks into smaller pieces and add
them seperately. For example, if you have an assignment due, set a due date for each
questions and add them seperately to the program.

For tasks without due date, the program will try to squeeze it in whenever possible.
'''

import argparse
import os
import datetime
from dateutil.relativedelta import relativedelta

error_msg = "Your to-do tasks file does not exist! Please make sure you have a tasks.txt in this directory."

def find_file():
    '''
    find_file returns True if task.txt is in the same directory as main.py
    '''
    for root, dir, files in os.walk(os.getcwd()):
      if "tasks.txt" in files:
        return True
    return False


def main():
    if args.display_task:
        if find_file():
            f = open("tasks.txt", "r")
            L = f.readlines()
            f.close()
            print("======Your current to-do tasks are======\n")
            for each in L:
                name = each.split()[0] 
                time = each.split()[1]
                due = each.split()[2]
                msg = name + ", which needs " + time + " hours to complete. It is due on " \
                    + due + ".\n"
                print(msg)
            print("======End of your current to-do tasks======")
        else:
            print(error_msg)
    if args.add_name != False:
        assert (args.add_name != False) and (args.add_time != False), \
            "Please ensure you entered a time requirement (an possibly a due date) for your tasks."
        with open("tasks.txt", "r") as f:
            lines = f.readlines()
        if args.add_due == False:
            due = "someday_in_the_future"
        else:
            due = args.add_due
        task = args.add_name + " " + args.add_time + " " + due + "\n"
        lines.append(task)
        f = open("tasks.txt", "w")
        for each in lines:
            f.write(each)
        print("New task added")
    if args.delete_task != False:
        if find_file():
            with open("tasks.txt", "r") as f:
                lines = f.readlines()
            with open("tasks.txt", "w") as f:
                for line in lines:
                    if line.split()[0] != args.delete_task:
                        f.write(line)
            print("Task deleted")
        else:
            print(error_msg)
    if args.time != False:
        if find_file():
            f = open("tasks.txt","r")
            L = f.readlines()
            f.close()
            availability = float(args.time)
            today = datetime.date.today()
            to_do = []
            urgent = []
            non_urgent = []
            for x in L:
                task = x.split()[0]
                time = float(x.split()[1])
                if x.split()[2] != "someday_in_the_future":
                    due = datetime.datetime.strptime(x.split()[2], '%Y-%m-%d').date()
                else:
                    due = x.split()[2]

                ## Classifying the tasks 
                if (due != "someday_in_the_future") and \
                    (due <= today + relativedelta(days =+ 2)):
                    to_do.append([task,time,due])
                    availability = availability - time
                elif (due != "someday_in_the_future") and \
                    (due <= today + relativedelta(days =+ 5)):
                    urgent.append([task, time, due])
                else:
                    non_urgent.append([task, time, due])
            ## If we still have time, get tasks from urgent
            if availability > 0:
                urgent.sort(key = lambda x: x[2])
                for x in urgent:
                    if availability - x[1] >= 0:
                        to_do.append(x)
                        availability = availability - x[1]
            to_do.sort(key = lambda x: x[2])
            ## If we still have time, get tasks from non-urgent
            if availability > 0:
                for x in non_urgent:
                    if availability - x[1] >= 0:
                        to_do.append(x)
                        availability = availability - x[1]
            ## print to screen
            print("======Your To-Do Tasks for Today======\n")
            if availability < 0:
                message = "****Note: more time dedicated to work today is needed than your availability, " \
                    + "as there are too many tasks due in two days.****\n"
                print(message)
            for each in to_do:
                name = each[0]
                time = each[1]
                due = each[2]
                msg = name + ", which needs " + str(time) + " hours to complete. It is due on " \
                    + str(due) + ".\n"
                print(msg)
            print("======End of Your To-Do Tasks for Today======")
        else:
            print(error_msg)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    description = 'Automatically help you to determine the tasks that you should do today. \
                        You may also add or delete tasks to your to-do list by using this program')
    parser.add_argument("-t", "--time", default = False,
                        help="The amount of time that you have today in hours. \
                            Skip this parameter if you just want to add/delete tasks")
    parser.add_argument("-an", "--add_name", default = False,
                        help="The name of the new tasks you want to add. \
                            Skip this parameter if you just want to delete tasks / see the \
                                tasks you should be doing today")
    parser.add_argument("-at","--add_time", default = False,
                        help="The time required to complete the task in hours. \
                            Skip this parameter if you just want to delete tasks / see the \
                                tasks you should be doing today.")
    parser.add_argument("-ad","--add_due", default = False,
                        help="The due date for the task in yyyy-mm-dd. \
                            Skip this parameter if you just want to delete tasks / see the \
                                tasks you should be doing today. \
                            Skip this parameter if the task does not have a due date.")
    parser.add_argument("-d","--delete_task", default = False,
                        help="The name of the task that you would like to delete. \
                            Skip this parameter if you just want to add tasks / see the \
                                tasks you should be doing today")
    parser.add_argument("-display","--display_task", action=argparse.BooleanOptionalAction,
                        help="Display all the tasks based on due dates. \
                            Skip this flag if you just want to add/delete tasks / see the \
                                tasks you should be doing today")
    
    args = parser.parse_args()
    main()