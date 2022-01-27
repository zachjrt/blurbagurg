initial = int(input("Enter initial number: "))
print(initial)

def math(init):
    x = 1
    y = 0
    if init != 1:
        if init % 2 == 0:
            init = init/2
            print(init)
            math(init)
        else:
            init = (init*3)+1
            print(init)
            math(init)
    resetAnswer = input("again? y/n: ")
    if resetAnswer.lower() == "y":
        redoNumber = int(input("Enter initial number: "))
        math(redoNumber)
    else:
        print("Done")
math(initial)

