def readFile():
    global code
    file = open("DayTwoInput.txt", "r")
    code = file.read()
    code = code.split(",")
    file.close

def execute(x):
    if int(code[x]) == 1: #add
        result = int(code[x+1]) + int(code[x+2])
        code[x+3] = result
        execute(x+4)
    elif int(code[x]) == 2: #multiply
        result = int(code[x+1]) * int(code[x+2])
        code[x+3] = result
        execute(x+4)
    elif int(code[x]) == 99: #end
        print(code[0])

    
if __name__ == "__main__":
    readFile()
    code[1] = 12
    code[2] = 2
    location = 0
    execute(0)
