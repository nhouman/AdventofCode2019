sum = 0
def readList():
    file = open("DayOneInput.txt", "r")
    massList = file.readlines()
    file.close()
    return massList

def calculate(mass):
    global sum
    for x in mass:
        sum = sum + (int(x) // 3 - 2)
   
if __name__ == "__main__":
    masses = readList()
    calculate(masses)
    print(sum)
