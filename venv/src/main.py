from instruction import Instruction
from random import randint
import os.path
import os
import numpy as np

# Registers
ebp = 0
esp = 3
temp = 0
temp2 = 0
eax = 0

aux_operator = 0

def printRegisters():
    print("EBP: ", ebp)
    print("ESP: ", esp)
    print("TEMP: ", temp)
    print("TEMP2: ", temp2)
    print("EAX: ", eax)

def executeMvi(op1, op2):
    op1 = op2
    return op1

def executeAddl(op1, op2):
    op1 = int(op1) + int(op2)
    return op1

def executeIncl(op1):
    op1 = int(op1) + 1
    return op1

def executeCmpl(op1, op2):
    op1 = int(op1) - op2
    return op1

def executeJle(op1):
    if op1 <= 0:
        return True
    else:
        return False

def executeLeave():
    return "Preparando para encerrar programa."

def executeRet():
    return "Encerrando programa."

def readInstruction(pc, instructionList):
    global ebp, esp, temp, temp2, eax, aux_operator

    name = instructionList[pc].getName()

    #mvl instruction
    operator_1 = instructionList[pc].getJumpName()
    operator_2 = instructionList[pc].getJumpLine()


    if name == "ret":
        return -5
    elif name == "jmp":
        return instructionList[pc].getJumpLine() - 1

    elif name == "jle":
        instructionList[pc].setIsDeviate(executeJle(aux_operator))  # Setting if will have deviation or not.
        if instructionList[pc].getIsDeviate():
            return instructionList[pc].getJumpLine() - 1

    #Verifies if it's a direct attribution
    if operator_2 != "ebp" and operator_2 != "esp" and operator_2 != "temp" \
            and operator_2 != "temp2" and operator_2 != "eax" and operator_2 != False:
        if operator_1 == "ebp":
            if name == "movl":
                ebp = executeMvi(ebp, operator_2)
            elif name == "addl":
                ebp = executeAddl(ebp, operator_2)
            elif name == "cmpl":
                aux_operator = executeCmpl(ebp, operator_2)
        elif operator_1 == "esp":
            if name == "movl":
                esp = executeMvi(esp, operator_2)
            elif name == "addl":
                esp = executeAddl(esp, operator_2)
            elif name == "cmpl":
                aux_operator = executeCmpl(esp, operator_2)
        elif operator_1 == "temp":
            if name == "movl":
                temp = executeMvi(temp, operator_2)
            elif name == "addl":
                temp = executeAddl(temp, operator_2)
            elif name == "cmpl":
                aux_operator = executeCmpl(temp, operator_2)
        elif operator_1 == "temp2":
            if name == "movl":
                temp2 = executeMvi(temp2, operator_2)
            elif name == "addl":
                temp2 = executeAddl(temp2, operator_2)
            elif name == "cmpl":
                aux_operator = executeCmpl(temp2, operator_2)
                aux_operator = temp2
        elif operator_1 == "eax":
            if name == "movl":
                eax = executeMvi(eax, operator_2)
            elif name == "addl":
                eax = executeAddl(eax, operator_2)
            elif name == "cmpl":
                aux_operator = executeCmpl(eax, operator_2)

    # Attribution made by other register
    elif operator_1 == "ebp":
        if name == "incl":
            ebp = executeIncl(ebp)
        elif operator_2 == "esp":
            if name == "movl":
                ebp = executeMvi(ebp, esp)
            elif name == "addl":
                ebp = executeAddl(ebp, esp)
            elif name == "cmpl":
                aux_operator = executeCmpl(ebp, esp)
        elif operator_2 == "temp":
            if name == "movl":
                ebp = executeMvi(ebp, temp)
            elif name == "addl":
                ebp = executeAddl(ebp, temp)
            elif name == "cmpl":
                aux_operator = executeCmpl(ebp, temp)
        elif operator_2 == "temp2":
            if name == "movl":
                ebp = executeMvi(ebp, temp)
            elif name == "addl":
                ebp = executeAddl(ebp, temp)
            elif name == "cmpl":
                aux_operator = executeCmpl(ebp, temp)
        elif operator_2 == "eax":
            if name == "movl":
                ebp = executeMvi(ebp, eax)
            elif name == "addl":
                ebp = executeAddl(ebp, eax)
            elif name == "cmpl":
                aux_operator = executeCmpl(ebp, eax)

    elif operator_1 == "esp":
        if name == "incl":
            esp = executeIncl(esp)
        elif operator_2 == "ebp":
            if name == "movl":
                esp = executeMvi(esp, ebp)
            elif name == "addl":
                esp = executeAddl(esp, ebp)
            elif name == "cmpl":
                aux_operator = executeCmpl(esp, ebp)
        elif operator_2 == "temp":
            if name == "movl":
                esp = executeMvi(esp, temp)
            elif name == "addl":
                esp = executeAddl(esp, temp)
            elif name == "cmpl":
                aux_operator = executeCmpl(esp, temp)
        elif operator_2 == "temp2":
            if name == "movl":
                esp = executeMvi(esp, temp2)
            elif name == "addl":
                esp = executeAddl(esp, temp2)
            elif name == "cmpl":
                aux_operator = executeCmpl(esx, temp2)
        elif operator_2 == "eax":
            if name == "movl":
                esp = executeMvi(esp, eax)
            elif name == "addl":
                esp = executeAddl(esp, eax)
            elif name == "cmpl":
                aux_operator = executeCmpl(esp, eax)
    elif operator_1== "temp":
        if name == "incl":
            temp = executeIncl(temp)
        elif operator_2 == "esp":
            if name == "movl":
                temp = executeMvi(temp, esp)
            elif name == "addl":
                temp = executeAddl(temp, esp)
            elif name == "cmpl":
                aux_operator = executeCmpl(temp, esp)
        elif operator_2 == "ebp":
            if name == "movl":
                temp = executeMvi(temp, ebp)
            elif name == "addl":
                temp = executeAddl(temp, ebp)
            elif name == "cmpl":
                aux_operator = executeCmpl(temp, ebp)
        elif operator_2 == "temp2":
            if name == "movl":
                temp = executeMvi(temp, temp2)
            elif name == "addl":
                temp = executeAddl(temp, temp2)
            elif name == "cmpl":
                aux_operator = executeCmpl(temp, temp2)
        elif operator_2 == "eax":
            if name == "movl":
                temp = executeMvi(temp, eax)
            elif name == "addl":
                temp = executeAddl(temp, eax)
            elif name == "cmpl":
                aux_operator = executeCmpl(temp, eax)
    elif operator_1 == "temp2":
        if name == "incl":
            temp2 = executeIncl(temp2)
        elif operator_2 == "esp":
            if name == "movl":
                temp2 = executeMvi(temp2, esp)
            elif name == "addl":
                temp2 = executeAddl(temp2, esp)
            elif name == "cmpl":
                aux_operator = executeCmpl(temp2, esp)
        elif operator_2 == "ebp":
            if name == "movl":
                temp2 = executeMvi(temp2, ebp)
            elif name == "addl":
                temp2 = executeAddl(temp2, ebp)
            elif name == "cmpl":
                aux_operator = executeCmpl(temp2, ebp)
        elif operator_2 == "temp":
            if name == "movl":
                temp2 = executeMvi(temp2, temp)
            elif name == "addl":
                temp2 = executeAddl(temp2, temp)
            elif name == "cmpl":
                aux_operator = executeCmpl(temp2, temp)
        elif operator_2 == "eax":
            if name == "movl":
                temp2 = executeMvi(temp2, eax)
            elif name == "addl":
                temp2 = executeAddl(temp2, eax)
            elif name == "cmpl":
                aux_operator = executeCmpl(temp2, eax)
    elif operator_1 == "eax":
        if name == "incl":
            eax = executeIncl(eax)
        elif operator_2 == "esp":
            if name == "movl":
                eax = executeMvi(eax, esp)
            elif name == "addl":
                eax = executeAddl(eax, esp)
            elif name == "cmpl":
                aux_operator = executeCmpl(eax, esp)
        elif operator_2 == "ebp":
            if name == "movl":
                eax = executeMvi(eax, ebp)
            elif name == "addl":
                eax = executeAddl(eax, ebp)
            elif name == "cmpl":
                aux_operator = executeCmpl(eax, ebp)
        elif operator_2 == "temp":
            if name == "movl":
                eax = executeMvi(eax, temp)
            elif name == "addl":
                eax = executeAddl(eax, temp)
            elif name == "cmpl":
                aux_operator = executeCmpl(eax, temp)
        elif operator_2 == "temp2":
            if name == "movl":
                eax = executeMvi(eax, temp2)
            elif name == "addl":
                eax = executeAddl(eax, temp2)
            elif name == "cmpl":
                aux_operator = executeCmpl(eax, temp2)
    return pc

flag = False
while(not flag):
    os.system('cls' if os.name == 'nt' else 'clear') # Clearing console
    directory = input('Name of file in directory "Files": ')
    directory = 'Files/' + directory
    if os.path.exists(directory):
        file = open(directory, 'r')
        flag = True
    else:
        print("File doesn't exist, try again...")

# Getting sum number
number = 6
while 1 > number > 5:
    number = input('Type number for the sum (1 to 5): ')

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
        instruction = Instruction(False, False, False, False, False, False)  # Initialize a instruction

        name = line.split().__getitem__(
            0)  # Separate every word from a unique line, and get '0' position, which is name of instruction

        instruction.setNumber(instructionNumber)  # Setting number of the instruction
        instruction.setName(name)  # Setting name of instruction
        instruction.setLine(lineInFile)  # Setting line number of this instruction in file

        if name == 'jmp' or name == 'je' or name == 'jne' or name == 'jg' or name == 'jge' or name == 'jl' or name == 'jle':  # If name is a deviation Instruction so...
            jumpName = line.split().__getitem__(1)  # Get the second word from this line, and here is the name of a group of instructions
            instruction.setJumpName(jumpName)  # Setting deviation group name in a JUMP instruction

            # Choose if program will real deviate or not
            # isDeviate = randint(0, 1)
            # if isDeviate == 0:
            #     isDeviate = False
            # else:
            #     isDeviate= True
            if name == "jmp":
                instruction.setIsDeviate(True)
            else:
                instruction.setIsDeviate(False)

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
                instruction.setJumpLine(False)
                instruction.setJumpName(False)
            instruction.setIsDeviate(False) # Means no deviation

        instructionList.append(instruction)  # Appending one element on a list of instructions

        lineInFile = lineInFile + 1

    else:
        if not '_' in line:  # Here is the lines that countains the name of a group of instruction from a deviation
            groupCounter = groupCounter + 1
            jump = Instruction(False, False, False, False, False, False)  # Iniatialize the object jump

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

id = np.zeros((1, 50))

def renderPipeline(pipeline, lenght, clock, completedInstructions):

    for i in range(40):
        print("-", end=" ")  # display "------"
    print()  # move cursor down to next line
    print("CLK", clock)  # display variable clock
    print()  # move cursor down to next line

    for i in range(lenght+1):  # for i to lenght
        print()  # move cursor down to next line
        # print("instruction", pc[0][i], "\t", end=" ")  # display pipeline steps
        print(id[0][i], end=" ")
        for j in range(clock+1):
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
    for i in range(40):
        print("-", end=" ")  # display "------"
    print()
    printRegisters()

pc = -1
count = 0
def buildPipeline(pipeline, lenght, clock, completedInstructions):
    global flag_aux # to modify global variable
    global pc
    global count

    id[0][count] = count + 1
    count += 1
    pipeline[lenght][clock] = 1  # set 1 on the diagonal of the matrix
    if clock != 0:
        for i in range(lenght):
            if pipeline[i][clock - 1] != 0:
                pipeline[i][clock] = pipeline[i][clock - 1] + 1  # increment value of the last column

            if pipeline[i][clock] == 6:
                completedInstructions += 1

                pc = pc + 1
                aux = pc
                pc = readInstruction(pc, instructionList)
                print('PC', pc)
                print('AUX', aux)
                if (aux != pc):
                    id[0][count - 1] = pc + 1
                    count = pc + 1
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
    # verify if next instruction != NULL
    if pc == -5:
        endProgram = 1
        break
    renderPipeline(pipeline, lenght, clock, completedInstructions)
    clock += 1

    if lenght < 50: #if endProgram != 1:
        lenght += 1

    option = input()