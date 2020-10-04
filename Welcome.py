import Robot
import RobotTypes
import Tasks
import time
import sys
# pip install pyobj --user
# pip install playsound
from playsound import playsound

my_robot = Robot.Robot("", 1)
types = RobotTypes.types
# tasks = my_robot.get_tasks()
robots = []
leaderboard = {}


def run_welcome():
    print("Please select a command: ")
    print("1: View robot family")
    print("2: Create a new robot")
    print("3: Complete tasks")
    print("4: View Leaderboard")
    print("5: Have a robot party!")
    print("6: Exit")
    print("Please enter your choice: ")
    # makes sure that the input is valid
    while True:
        try:
            choice = int(input())
            if 0 < choice < 7:
                break
            else:
                print("Please enter a valid choice: ")
        except Exception:
            print("Please enter an integer: ")

    # perform desired task
    if choice == 1:
        view_current_robots()
    elif choice == 2:
        create_robot()
    elif choice == 3:
        assign_tasks()
    elif choice == 4:
        view_leaderboard()
    elif choice == 5:
        robot_party()
    elif choice == 6:
        save_robots()
        print("Bye for now! Hope to see you again soon.")
        print("(ㅅꈍ﹃ꈍ)*gᵒᵒᒄ ᵑⁱgᑋᵗ♡(ꈍ﹃ꈍㅅ)*")
        print(" -- Love, your robot family.")
        sys.exit()


def create_robot():
    name = input("Please choose a name for your robot: ")
    print(name + " has been created successfully!")
    print()
    print("Time to pick what type of robot you want.")
    print("Here are the types of robots you can choose from:")
    # print a list of types of robots the user can choose from
    for i in range(len(types)):
        print(str(i + 1) + ": " + types[i][0] + " " + types[i][1])
    print("Please enter the number of your choice: ")
    # make sure the input is valid
    while True:
        try:
            choice = int(input())
            if 0 < choice < 7:
                # make sure that this robot does not already exist
                for i in range(len(robots)):
                    if robots[i].name == name and robots[i].type == types[choice - 1][0]:
                        print("This robot already exists.")
                        create_robot()
                my_robot.name = name
                my_robot.type = types[choice - 1][0]
                my_robot.emoji = types[choice - 1][1]
                break
            else:
                print("Please enter a valid choice: ")
        except Exception:
            print("Please enter an integer: ")

    print("Congratulations! " + my_robot.name + ", the " + my_robot.type + " has been successfully created!")
    print()
    print(my_robot.emoji)
    my_robot.say_name()
    print()

    # add newly made robot to list of all robots
    robots.append(Robot.Robot(name, types[choice - 1][0]))
    robots[-1].emoji = my_robot.emoji
    robots[-1].finishedTasks = []
    run_welcome()


def view_current_robots():
    # if there are no robots, go back to main menu
    if len(robots) == 0:
        print("There are currently no robots in the robot family.")
        print()
        run_welcome()

    # list the current robot family
    print("Here are the current robots in your family!")
    for i in range(len(robots)):
        print(robots[i].name + ", the " + robots[i].type + " robot")
    print()
    run_welcome()


def assign_tasks():
    print("Here are the current robots:")
    for i in range(len(robots)):
        print(str(i + 1) + ": " + robots[i].name + " " + robots[i].type)
    print("Which robot would you like to assign tasks to? Please enter the number of your choice: ")
    # makes sure input is valid
    while True:
        try:
            choice = int(input())
            if 0 < choice < len(robots) + 1:
                my_robot = robots[choice - 1]
                break
            else:
                print("Please enter a valid choice: ")
        except Exception:
            print("Please enter an integer: ")

    # assign and complete the tasks
    print(my_robot.name + " will now complete the following tasks:")
    my_robot.get_tasks()
    my_robot.report_tasks()
    print()
    print("Now completing tasks...")
    justFinished = my_robot.complete_tasks()
    print()
    # add newly complete tasks to the leaderboard
    for t in justFinished:
        #my_robot.finishedTasks.append(t)
        if t not in leaderboard:
            leaderboard[t] = {}
        if my_robot.name not in leaderboard[t]:
            leaderboard[t][my_robot.name] = 0
        leaderboard[t][my_robot.name] = leaderboard[t].get(my_robot.name) + 1
    run_welcome()

def robot_party():
    print("It's party time! (Turn your volume up)")
    print("Setting the mood...")
    playsound('Robot_Noises.mp3')
    i = 5
    while i > 0:
        if i % 2 == 0:
            print("L=(ಠ_ಠ)=┐   \m/_(>_<)_\m/   ╰( ⁰ ਊ ⁰ )━☆ﾟ.*･｡ﾟ   (>^o^)><(^o^<)   ¯\_( ͡° ͜ʖ ͡°)_/¯")
        else:
            print("┌=(ಠ_ಠ)=┘   /w\_(>_<)_/w\   ﾟ.*･｡ﾟ☆━( ⁰ ਊ ⁰ )｣   <(^o^<)(>^o^)>   _/¯( ͡° ͜ʖ ͡°)¯\_")
        time.sleep(3)
        i -= 1
    run_welcome()

def view_leaderboard():
    if len(leaderboard) == 0:
        print("There are currently no leaders")
        print()
        run_welcome()
    # display the leaderboard
    print("-----CURRENT LEADERBOARD-----")
    for k, v in leaderboard.items():
        print(k.upper())
        # sort each task by the robots who complete the most times
        sorted_task = sorted(leaderboard[k].items(), key=lambda x: x[1], reverse=True)
        # display only the top five robots for each task
        for s in range(min(len(sorted_task), 5)):
            print(str(s + 1) + ": " + sorted_task[s][0] + " -> " + " completed " + str(sorted_task[s][1]) + " times")
    print()
    run_welcome()

def load_robots():
    file = open('robots.txt', 'r')
    lines = file.readlines()
    file.close()

    index = 0
    # go through textfile of saved robots and load them into the list of current robots
    for line in lines:
        t = []
        finished = []
        r = line.split(";")
        my_robot.name = r[0]
        my_robot.type = r[1]
        my_robot.emoji = r[2]
        my_robot.tasks = t
        for i in r[3].strip().split(","):
            if len(i) > 0:
                finished.append(i)
                my_robot.finishedTasks.append(i)
        # add these already finished tasks to the leaderboard
        for t in finished:
            # my_robot.finishedTasks.append(t)
            if t not in leaderboard:
                leaderboard[t] = {}
            if my_robot.name not in leaderboard[t]:
                leaderboard[t][my_robot.name] = 0
            leaderboard[t][my_robot.name] = leaderboard[t].get(my_robot.name) + 1

        # my_robot.finishedTasks = finished
        robots.append(Robot.Robot(r[0], r[1]))
        robots[index].finishedTasks = finished
        robots[index].emoji = my_robot.emoji
        index += 1

def save_robots():
    # before exiting, save all of the current robots into the textfile in the correct format
    file = open('robots.txt', 'w')
    for i in range(len(robots)):
        my_robot = robots[i]
        if len(my_robot.finishedTasks) > 0:
            t = ""
            for j in my_robot.finishedTasks:
                t += j + ","
            t = t[:-1]
        else:
            t = ""
        line = my_robot.name + ";" + my_robot.type + ";" + my_robot.emoji + ";" + t + '\n'
        file.write(line)
    file.close()

if __name__ == '__main__':
    print("Welcome to Bot-O-Mat, home of your favorite robots!")
    print("└[∵┌]└[ ∵ ]┘[┐∵]┘")
    print()
    load_robots()
    run_welcome()
