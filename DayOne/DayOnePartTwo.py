sum = 0
def readFile():
    file = open("DayOneInput.txt", "r")
    massList = file.readlines()
    file.close()
    return massList

def calculate(x):
    global sum
    y = int(x)
    total = y // 3 - 2
    if total > 0 and total < y:
        sum += total
    if total > 0:
        calculate(total)
            
    
if __name__ == "__main__":
    mass = readFile()
    for x in mass:
        calculate(x)
    print("Sum:",sum)
