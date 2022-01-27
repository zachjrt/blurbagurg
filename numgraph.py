import matplotlib.pyplot as graph


initial = int(input("Enter initial number: "))
print(initial)

def math(init):
    x = 1
    y = init
    xList = [1]
    yList = [y]
    if init != 1:
        if init % 2 == 0:
            init = init/2
            print(init)
            x = x + 1
            xList.append(x)
            yList.append(init)
            math(init)
        else:
            init = (init*3)+1
            print(init)
            x = x + 1
            xList.append(x)
            yList.append(init)
            math(init)
    graph.plot(xList, yList)
    graph.xlabel('x - axis')
    graph.ylabel('y - axis')
    graph.title('My first graph!')
    graph.show()
    resetAnswer = input("again? y/n: ")
    if resetAnswer.lower() == "y":
        redoNumber = int(input("Enter initial number: "))
        math(redoNumber)
    else:
        print("Done")
math(initial)

