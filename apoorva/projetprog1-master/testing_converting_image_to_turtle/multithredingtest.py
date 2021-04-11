import turtle
from collections import deque


def move1():
    for _ in range(360):
        turtle1.forward(1)
        turtle1.left(1)
        yield


def move2():
    for _ in range(360):
        turtle2.forward(1)
        turtle2.right(2)
        yield


# Create turtles
turtle1 = turtle.Turtle('turtle')
turtle1.speed('fastest')
turtle2 = turtle.Turtle('turtle')
turtle2.speed('fastest')

# Create and populate a task queue

taskqueue = deque()
taskqueue.append(move1())  # Add tasks (generators)
taskqueue.append(move2())

while taskqueue:   # Run all of the tasks
    # Get the next task
    task = taskqueue.pop()
    try:
        # Run it to the next yield and enqueue
        next(task)
        taskqueue.appendleft(task)
    except StopIteration:
        # Task is done
        pass

turtle.done()