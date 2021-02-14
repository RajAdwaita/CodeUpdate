from sys import maxsize


def newStack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def pushITEM(stack, item):
    if (len(stack) > 10):
        print("Overflow")

    else:
        stack.append(item)
        print(stack)


def pop_ele(stack):
    if(isEmpty(stack)):
        return ("Underflow")
    (stack.pop())
    return stack


print("\\1.push.\\2.pop.\\-1.Exit")
stack = newStack()
i = 0
while(i != -1):
    i = int(input())

    if i == 1:
        pushITEM(stack, ((input())))
    elif i == 2:
        print(pop_ele(stack))

    elif i == -1:
        exit()

    else:
        print("Invalid Choice")
