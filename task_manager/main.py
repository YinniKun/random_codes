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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    description = 'Automatically help you to determine the tasks that you should do today. \
                        You may also add or delete tasks to your to-do list by using this program')
    parser.add_argument("-t", "--time", default = False
                        help="The amount of time that you have today in hours. \
                            Skip this parameter if you just want to add/delete tasks")
    parser.add_argument("-an", "--add_name", default = False
                        help="The name of the new tasks you want to add. \
                            Skip this parameter if you just want to delete tasks / see the \
                                tasks you should be doing today")
    parser.add_argument("-at","--add_time", default = False
                        help="The time required to complete the task in hours. \
                            Skip this parameter if you just want to delete tasks / see the \
                                tasks you should be doing today.")
    parser.add_argument("-ad","--add_due", default = False
                        help="The due date for the task in yyyy-mm-dd. \
                            Skip this parameter if you just want to delete tasks / see the \
                                tasks you should be doing today. \
                            Skip this parameter if the task does not have a due date.")
    parser.add_argument("-d","--delete_task", default = False
                        help="The name of the task that you would like to delete. \
                            Skip this parameter if you just want to add tasks / see the \
                                tasks you should be doing today")
    parser.add_argument("-t","--display_task", default = False
                        help="Display all the tasks based on due dates. \
                            Skip this parameter if you just want to add/delete tasks / see the \
                                tasks you should be doing today")
    args = parser.parse_args()