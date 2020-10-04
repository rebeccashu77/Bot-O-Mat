import RobotTypes
from random import randint
import Tasks
import time

class Robot:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.tasks = []
        self.finishedTasks = []
        self.emoji = ""

    def say_name(self):
        print("Hi! My name is " + self.name)

    def get_tasks(self):
        # get five fandom tasks from the task list
        tasks = Tasks.tasks
        for i in range(0, 5):
            index = randint(0, len(tasks) - 1)
            self.tasks.append(tasks[index])
        return self.tasks

    def report_tasks(self):
        for t in self.tasks:
            print(t[0])

    def report_completed_task(self, task):
        print(self.name + " has just completed the task " + task)

    def complete_tasks(self):
        justFinished = []
        while len(self.tasks) > 0:
            time.sleep(self.tasks[0][1] / 1000)
            self.finishedTasks.append(self.tasks[0][0])
            self.report_completed_task(self.tasks[0][0])
            justFinished.append(self.tasks[0][0])
            self.tasks.pop(0)

        return justFinished
