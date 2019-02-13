from instruction import Instruction
from random import randint
import os.path
import os
import numpy as np

flag = False
while(not flag):
    os.system('cls' if os.name == 'nt' else 'clear') # Clearing console
    directory = input('Name of file in directory "Files": ')
    directory = 'Files\ ' + directory
    directory = directory.replace(" ", "")
    if os.path.exists(directory):
        file = open(directory, 'r')
        flag = True
    else:
        print("File doesn't exist, try again...")

instructionNumber = 0
lineInFile = 0
groupCounter = 0  # Count how many groups of instructions the program have
instructionList = []  # List of all assembly instructions
jumpList = []

# Run all file lines
for line in file:
    line = line.rstrip()
    if not ':' in line:  # Select just the instructions

        instructionNumber = instructionNumber + 1  # Increasing number of instruction aux variable
        instruction = Instruction(-1, -1, -1, -1, -1, False)  # Initialize a instruction

        name = line.split().__getitem__(
            0)  # Separate every word from a unique line, and get '0' position, which is name of instruction

        instruction.setNumber(instructionNumber)  # Setting number of the instruction
        instruction.setName(name)  # Setting name of instruction
        instruction.setLine(lineInFile)  # Setting line number of this instruction in file

        if name == 'jmp' or name == 'je' or name == 'jne' or name == 'jg' or name == 'jge' or name == 'jl' or name == 'jle':  # If name is a deviation Instruction so...
            jumpName = line.split().__getitem__(1)  # Get the second word from this line, and here is the name of a group of instructions
            instruction.setJumpName(jumpName)  # Setting deviation group name in a JUMP instruction

            # Choose if program will real deviate or not
            isDeviate = randint(0, 1)
            if isDeviate == 0:
                isDeviate = False
            else:
                isDeviate= True
            instruction.setIsDeviate(isDeviate)

            # Setting some attributes.
        else:
            operation_1 = line.split().__getitem__(1)
            operation_1 = operation_1.replace(",","")
            operation_2 = line.split().__getitem__(2)
            if not ";" in operation_1:
                instruction.setJumpName(operation_1)  # Setting operator 1. (Second column)
            if not ";" in operation_2:
                instruction.setJumpLine(operation_2)  # Maybe it doesn't exist (Third column)
            if instruction.getName() == "ret" or instruction.getName() == "leave":
                instruction.setJumpLine(-1)
                instruction.setJumpName(-1)
            instruction.setIsDeviate(False) # Means no deviation

        instructionList.append(instruction)  # Appending one element on a list of instructions

        lineInFile = lineInFile + 1

    else:
        if not '_' in line:  # Here is the lines that countains the name of a group of instruction from a deviation
            groupCounter = groupCounter + 1
            jump = Instruction(-1, -1, -1, -1, -1, False)  # Iniatialize the object jump

            name = line.replace(':', "")  # Erasing ":" from this line

            jump.setName(name)  # Setting name in this object
            jump.setLine(lineInFile - groupCounter + 1)  # Setting the instruction number that deviate will jump
            jumpList.append(jump)  # Appending one element on a list of group instruction names

        lineInFile = lineInFile + 1

os.system('cls' if os.name == 'nt' else 'clear') # Clearing console

# Lines from 48 to 57, is to set "JumpLine" in "Jump" instructions,
# JumpLine: Line which the program is going to jump deppending on the instruction.
for i in range(len(instructionList)):
    name = instructionList[i].getName()
    jumpName = ""

    if name == 'jmp' or name == 'je' or name == 'jne' or name == 'jg' or name == 'jge' or name == 'jl' or name == 'jle':
        jumpName = instructionList[i].getJumpName()

        for j in range(len(jumpList)):
            if jumpName == jumpList[j].getName():
                instructionList[i].setJumpLine(jumpList[j].getLine())

    print(instructionList[i].getName(), instructionList[i].getNumber(), instructionList[i].getJumpName(),
          instructionList[i].getJumpLine(), instructionList[i].getIsDeviate())

print("Number of instructions found: ", instructionNumber)
file.close()

flag_aux = 1

def renderPipeline(pipeline, lenght, clock, completedInstructions):

    for i in range(40):
        print("-", end=" ")  # display "------"
    print()  # move cursor down to next line
    print("CLK", clock)  # display variable clock
    print()  # move cursor down to next line

    for i in range(lenght):  # for i to lenght
        print()  # move cursor down to next line
        # print("instruction", pc[0][i], "\t", end=" ")  # display pipeline steps
        for j in range(clock):
            if pipeline[i][j] == 1:
                print(" FI ", end=" ")
            elif pipeline[i][j] == 2:
                print(" DI ", end=" ")
            elif pipeline[i][j] == 3:
                print(" FO ", end=" ")
            elif pipeline[i][j] == 4:
                print(" CO ", end=" ")
            elif pipeline[i][j] == 5:
                print(" EI ", end=" ")
            elif pipeline[i][j] == 6:
                print(" WO ", end=" ")
            else:
                print("    ", end=" ")
        print()
    print()
    print("\nCompleted Instructions :", completedInstructions)
    print()

pc = -1
def buildPipeline(pipeline, lenght, clock, completedInstructions):
    global flag_aux # to modify global variable
    global pc

    pipeline[lenght][clock] = 1  # set 1 on the diagonal of the matrix
    if clock != 0:
        for i in range(lenght):
            if pipeline[i][clock - 1] != 0:
                pipeline[i][clock] = pipeline[i][clock - 1] + 1  # increment value of the last column

            if pipeline[i][clock] == 6:
                completedInstructions += 1
                pc += 1
                # todo: Read instruction

                if instructionList[pc].getJumpLine() != -1: # Means that happens a deviation
                    pc = int(instructionList[pc].getJumpLine()-1)
                    break

    return completedInstructions  # return number of instruction witch had already been read

#  inicialization of variables
clock = 0
lenght = 0
option = '1'
completedInstructions = 0
pipeline = np.zeros((50, 50))
endProgram = 0

# run while input != "0"
print('Type any key to proceed and 0 to exit!')
while option != '0':

    #  call functions to build and render the pipeline
    completedInstructions = buildPipeline(pipeline, lenght, clock, completedInstructions)
    renderPipeline(pipeline, lenght, clock, completedInstructions)
    clock += 1
    #verify if next instruction != NULL
    # if yes:
        #endProgram = 1

    if lenght < 50: #if endProgram != 1:
        lenght += 1

    option = input()
