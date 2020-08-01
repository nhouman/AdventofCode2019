def readFile():
    global intcode
    file = open("DayTwoInput.txt", "r")
    intcode = file.read()
    intcode = intcode.split(",")
    intcode = [int(i) for i in intcode]
    file.close

def execute(x):
    op = intcode[x]
    loc_one = intcode[x+1]
    loc_two = intcode[x+2]
    dest = intcode[x+3]

    if intcode[x] != 99:
        if intcode[x] == 1: #add
            intcode[dest] = intcode[loc_one] + intcode[loc_two]
            execute(x+4)
        elif intcode[x] == 2: #multiply
            intcode[dest] = intcode[loc_one] * intcode[loc_two]
            execute(x+4)
    else:
        print("Location 0:",intcode[0])


if __name__ == "__main__":
    readFile()
    intcode[1] = 12
    intcode[2] = 2
    execute(0)
    
