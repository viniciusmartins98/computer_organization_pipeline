from instruction import Instruction
from random import randint
import os.path
import os
import numpy as np
import string

#Global variables:
# Registers
ebp = 0
esp = 0
temp = 0
temp2 = 0
eax = 0

# aux for cmpl and jle function
aux_operator = 0

flag_aux = 1

# Store id of instruction
id = np.zeros((1, 500))

# Program counter
pc = 0

#
count = 0

def printRegisters():
    print("EBP: ", ebp)
    print("ESP: ", esp)
    print("TEMP: ", temp)
    print("TEMP2: ", temp2)
    print("EAX: ", eax)

def executeMovl(op1, op2):
    op1 = int(op2)
    return op1

def executeAddl(op1, op2):
    op1 = int(op1) + int(op2)
    return op1

def executeIncl(op1):
    op1 = int(op1) + 1
    return op1

def executeCmpl(op1, op2):
    op1 = int(op1) - int(op2)
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

# This is going to read and execute the assembly instructions. It always the address for the next instruction
def readInstruction(pc, instructionList):
    global ebp, esp, temp, temp2, eax, aux_operator # Registers

    name = instructionList[pc].getName() # Name of instruction

    operator_1 = instructionList[pc].getOP1() # First operator
    operator_2 = instructionList[pc].getOP2() # Second operator


    if name == "ret": # "Execute" instruction ret
        return -2
    elif name == "jmp": # "Execute" function jmp.
        return instructionList[pc].getOP2() - 1

    elif name == "jle": # "Execute" function jle.
        instructionList[pc].setIsDeviate(executeJle(aux_operator))  # Setting if will have deviation or not.
        if instructionList[pc].getIsDeviate():
            return instructionList[pc].getOP2() - 1

    #Veirifyes if the instructions have direct values, for example: "movl temp 0".
    if operator_2 != "ebp" and operator_2 != "esp" and operator_2 != "temp" \
            and operator_2 != "temp2" and operator_2 != "eax" and operator_2 != False:
        if operator_1 == "ebp":
            if name == "movl":
                ebp = executeMovl(ebp, operator_2)
            elif name == "addl":
                ebp = executeAddl(ebp, operator_2)
            elif name == "cmpl":
                aux_operator = executeCmpl(ebp, operator_2)
        elif operator_1 == "esp":
            if name == "movl":
                esp = executeMovl(esp, operator_2)
            elif name == "addl":
                esp = executeAddl(esp, operator_2)
            elif name == "cmpl":
                aux_operator = executeCmpl(esp, operator_2)
        elif operator_1 == "temp":
            if name == "movl":
                temp = executeMovl(temp, operator_2)
            elif name == "addl":
                temp = executeAddl(temp, operator_2)
            elif name == "cmpl":
                aux_operator = executeCmpl(temp, operator_2)
        elif operator_1 == "temp2":
            if name == "movl":
                temp2 = executeMovl(temp2, operator_2)
            elif name == "addl":
                temp2 = executeAddl(temp2, operator_2)
            elif name == "cmpl":
                aux_operator = executeCmpl(temp2, operator_2)
                aux_operator = temp2
        elif operator_1 == "eax":
            if name == "movl":
                eax = executeMovl(eax, operator_2)
            elif name == "addl":
                eax = executeAddl(eax, operator_2)
            elif name == "cmpl":
                aux_operator = executeCmpl(eax, operator_2)

    # Instructions that don't have direct values. This will execute most of instructions.
    elif operator_1 == "ebp":
        if name == "incl":
            ebp = executeIncl(ebp)
        elif operator_2 == "esp":
            if name == "movl":
                ebp = executeMovl(ebp, esp)
            elif name == "addl":
                ebp = executeAddl(ebp, esp)
            elif name == "cmpl":
                aux_operator = executeCmpl(ebp, esp)
        elif operator_2 == "temp":
            if name == "movl":
                ebp = executeMovl(ebp, temp)
            elif name == "addl":
                ebp = executeAddl(ebp, temp)
            elif name == "cmpl":
                aux_operator = executeCmpl(ebp, temp)
        elif operator_2 == "temp2":
            if name == "movl":
                ebp = executeMovl(ebp, temp)
            elif name == "addl":
                ebp = executeAddl(ebp, temp)
            elif name == "cmpl":
                aux_operator = executeCmpl(ebp, temp)
        elif operator_2 == "eax":
            if name == "movl":
                ebp = executeMovl(ebp, eax)
            elif name == "addl":
                ebp = executeAddl(ebp, eax)
            elif name == "cmpl":
                aux_operator = executeCmpl(ebp, eax)

    elif operator_1 == "esp":
        if name == "incl":
            esp = executeIncl(esp)
        elif operator_2 == "ebp":
            if name == "movl":
                esp = executeMovl(esp, ebp)
            elif name == "addl":
                esp = executeAddl(esp, ebp)
            elif name == "cmpl":
                aux_operator = executeCmpl(esp, ebp)
        elif operator_2 == "temp":
            if name == "movl":
                esp = executeMovl(esp, temp)
            elif name == "addl":
                esp = executeAddl(esp, temp)
            elif name == "cmpl":
                aux_operator = executeCmpl(esp, temp)
        elif operator_2 == "temp2":
            if name == "movl":
                esp = executeMovl(esp, temp2)
            elif name == "addl":
                esp = executeAddl(esp, temp2)
            elif name == "cmpl":
                aux_operator = executeCmpl(esx, temp2)
        elif operator_2 == "eax":
            if name == "movl":
                esp = executeMovl(esp, eax)
            elif name == "addl":
                esp = executeAddl(esp, eax)
            elif name == "cmpl":
                aux_operator = executeCmpl(esp, eax)
    elif operator_1== "temp":
        if name == "incl":
            temp = executeIncl(temp)
        elif operator_2 == "esp":
            if name == "movl":
                temp = executeMovl(temp, esp)
            elif name == "addl":
                temp = executeAddl(temp, esp)
            elif name == "cmpl":
                aux_operator = executeCmpl(temp, esp)
        elif operator_2 == "ebp":
            if name == "movl":
                temp = executeMovl(temp, ebp)
            elif name == "addl":
                temp = executeAddl(temp, ebp)
            elif name == "cmpl":
                aux_operator = executeCmpl(temp, ebp)
        elif operator_2 == "temp2":
            if name == "movl":
                temp = executeMovl(temp, temp2)
            elif name == "addl":
                temp = executeAddl(temp, temp2)
            elif name == "cmpl":
                aux_operator = executeCmpl(temp, temp2)
        elif operator_2 == "eax":
            if name == "movl":
                temp = executeMovl(temp, eax)
            elif name == "addl":
                temp = executeAddl(temp, eax)
            elif name == "cmpl":
                aux_operator = executeCmpl(temp, eax)
    elif operator_1 == "temp2":
        if name == "incl":
            temp2 = executeIncl(temp2)
        elif operator_2 == "esp":
            if name == "movl":
                temp2 = executeMovl(temp2, esp)
            elif name == "addl":
                temp2 = executeAddl(temp2, esp)
            elif name == "cmpl":
                aux_operator = executeCmpl(temp2, esp)
        elif operator_2 == "ebp":
            if name == "movl":
                temp2 = executeMovl(temp2, ebp)
            elif name == "addl":
                temp2 = executeAddl(temp2, ebp)
            elif name == "cmpl":
                aux_operator = executeCmpl(temp2, ebp)
        elif operator_2 == "temp":
            if name == "movl":
                temp2 = executeMovl(temp2, temp)
            elif name == "addl":
                temp2 = executeAddl(temp2, temp)
            elif name == "cmpl":
                aux_operator = executeCmpl(temp2, temp)
        elif operator_2 == "eax":
            if name == "movl":
                temp2 = executeMovl(temp2, eax)
            elif name == "addl":
                temp2 = executeAddl(temp2, eax)
            elif name == "cmpl":
                aux_operator = executeCmpl(temp2, eax)
    elif operator_1 == "eax":
        if name == "incl":
            eax = executeIncl(eax)
        elif operator_2 == "esp":
            if name == "movl":
                eax = executeMovl(eax, esp)
            elif name == "addl":
                eax = executeAddl(eax, esp)
            elif name == "cmpl":
                aux_operator = executeCmpl(eax, esp)
        elif operator_2 == "ebp":
            if name == "movl":
                eax = executeMovl(eax, ebp)
            elif name == "addl":
                eax = executeAddl(eax, ebp)
            elif name == "cmpl":
                aux_operator = executeCmpl(eax, ebp)
        elif operator_2 == "temp":
            if name == "movl":
                eax = executeMovl(eax, temp)
            elif name == "addl":
                eax = executeAddl(eax, temp)
            elif name == "cmpl":
                aux_operator = executeCmpl(eax, temp)
        elif operator_2 == "temp2":
            if name == "movl":
                eax = executeMovl(eax, temp2)
            elif name == "addl":
                eax = executeAddl(eax, temp2)
            elif name == "cmpl":
                aux_operator = executeCmpl(eax, temp2)
    return pc + 1

# This function will read the assembly file and build a list of all instructions, ordered by line, with all their information.
def readFile(file, instructionList):
    instructionNumber = 0 # Instruction number depending on the line that it is.
    lineInFile = 0 # Line that the instruction is in file
    groupCounter = 0  # Count how many groups of instructions the program have
    jumpList = [] # Aux list that will contain all jump instructions.

    for line in file: # Run line by line in file
        line = line.rstrip() # Copies line in file for the variable "line"
        if not ':' in line:  # Select just the instructions, because instructions don't have ":" in their names.

            instructionNumber = instructionNumber + 1  # Increasing number of instruction aux variable
            instruction = Instruction(False, False, False, False, False, False)  # Initialize a instruction object.

            name = line.split().__getitem__(0) # Separate every word from a unique line, and get '0' position, which is the name of instruction

            instruction.setNumber(instructionNumber)  # Setting number of the instruction
            instruction.setName(name)  # Setting name of instruction
            instruction.setLine(lineInFile)  # Setting line number of this instruction in file

            if name == 'jmp' or name == 'je' or name == 'jne' or name == 'jg' or name == 'jge' or name == 'jl' or name == 'jle':  # If name is a deviation Instruction so...
                jumpName = line.split().__getitem__(1)  # Get the second word from this line, and here is the name of a group of instructions
                instruction.setOP1(jumpName)  # Setting deviation group name in a JUMP instruction

                if name == "jmp": # Instruction "jmp" will always deviate.
                    instruction.setIsDeviate(True)
                else:
                    instruction.setIsDeviate(False)

            else: # Is not a deviation instruction.
                operation_1 = line.split().__getitem__(1) # Getting first operator
                operation_1 = operation_1.replace(",","")
                operation_2 = line.split().__getitem__(2) # Getting second operator
                if not ";" in operation_1: # ";" means that is a "comment"
                    instruction.setOP1(operation_1)  # Setting operator 1. (Second column)
                if not ";" in operation_2:
                    instruction.setOP2(operation_2)  # Setting operator 2. Maybe it doesn't exist (Third column)
                if instruction.getName() == "ret" or instruction.getName() == "leave": # Instructions that have no operators.
                    instruction.setOP1(False) # Setting false in OP1 means that have no operator
                    instruction.setOP2(False) # Setting false in OP2 means that have no operator
                instruction.setIsDeviate(False) # Means no deviation

            instructionList.append(instruction)  # Appending one element on a list of instructions.

            lineInFile = lineInFile + 1 # Increment line in file.

        else: # Here will get just de grouo of instructions names.
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
    # JumpLine: Line which the program is going to jump.
    for i in range(len(instructionList)):
        name = instructionList[i].getName()
        jumpName = ""

        if name == 'jmp' or name == 'je' or name == 'jne' or name == 'jg' or name == 'jge' or name == 'jl' or name == 'jle':
            jumpName = instructionList[i].getOP1()

            for j in range(len(jumpList)): # Runs the jumpList list.
                if jumpName == jumpList[j].getName(): # Find the instruction that have to jump.
                    instructionList[i].setOP2(jumpList[j].getLine()) # Setting the number of instruction that the jump instruction have to jump.
    file.close() # Close file
    return instructionList

def printInstructionList(instructionList):
    print("------------------------------------")
    print ("INSTRUCTIONS: ")
    for i in range(len(instructionList)):
        print(instructionList[i].getNumber(), instructionList[i].getName(), instructionList[i].getOP1(),
              instructionList[i].getOP2())
    print("------------------------------------")

def renderPipeline(pipeline, lenght, clock, completedInstructions, instructionList, iNum, printBegin):
    for i in range(40):
        print("-", end=" ")  # display "------"
    print()  # move cursor down to next line
    print("\t\tSUM")
    print("INPUT: ", iNum)
    printInstructionList(instructionList)
    printRegisters()
    print()  # move cursor down to next line
    print("CLK", clock, "\t\t\t", end=" ")  # display variable clock
    for i in range(printBegin, clock+1):
        print(i, "\t", end=" ")
    print()  # move cursor down to next line
    for i in range((printBegin-printBack), lenght + 1):  # for i to lenght
        print()  # move cursor down to next line
        print("{:3d}".format(i + 1), "|", end=" ")
        print("instruction", id[0][i], end=" ")  # display pipeline steps
        for j in range(printBegin, clock + 1):
            if pipeline[i][j] == 1:
                print("\t FI ", end=" ")
            elif pipeline[i][j] == 2:
                print("\t DI ", end=" ")
            elif pipeline[i][j] == 3:
                print("\t FO ", end=" ")
            elif pipeline[i][j] == 4:
                print("\t CO ", end=" ")
            elif pipeline[i][j] == 5:
                print("\t EI ", end=" ")
            elif pipeline[i][j] == 6:
                print("\t WO ", end=" ")
            else:
                print("\t    ", end=" ")
        print()
    print()
    print("\nCompleted Instructions :", completedInstructions)
    print()
    for i in range(40):
        print("-", end=" ")  # display "------"
    print()

def buildPipeline(pipeline, lenght, clock, completedInstructions, instructionList):
    global flag_aux  # to modify global variable
    global pc
    global count
    if id[0][count - 1] < len(instructionList)+1:
        id[0][count] = id[0][count - 1] + 1
        pipeline[lenght][clock] = 1  # set 1 on the diagonal of the matrix
        count += 1

    if clock != 0:
        for i in range(lenght):

            if pipeline[i][clock - 1] != 0:
                pipeline[i][clock] = pipeline[i][clock - 1] + 1  # increment value of the last column

            if pipeline[i][clock] == 6:
                completedInstructions += 1

                pc = pc + 1
                aux = pc
                pc = readInstruction(pc - 1, instructionList)
                if (aux != pc):
                    id[0][count - 1] = pc + 1
                    break

    return completedInstructions  # return number of instruction witch had already been read


#------------------------------------------Program starts here----------------------------------------------------------
#  Initializing variables
clock = 0
lenght = 0
option = '1'
completedInstructions = 0
pipeline = np.zeros((500, 500))
printBegin = 0
printBack = 0
endProgram = False
#List of assembly instructions
instructionList = []

#Open assembly file
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
flag = False
while(flag == False):
    iNum = input('Type number for the sum (1 to 5): ')
    if int(iNum) <= 5 and int(iNum) >= 1:
        flag = True
esp = iNum # Initializing a value to the program.

# iNum is the value of the input.

 # This function creates a list of instructions based on assembly file.
instructionList = readFile(file, instructionList)

while pc != -2:
    #  call function to build the pipeline
    completedInstructions = buildPipeline(pipeline, lenght, clock, completedInstructions, instructionList)

    # verify if next instruction == endProgram(ret)
    if pc == -2:
        os.system('cls' if os.name == 'nt' else 'clear')
        pipeline[lenght, :] = np.zeros((1, 500))
        renderPipeline(pipeline, lenght, clock, completedInstructions, instructionList, iNum, printBegin)
        break
    #  call function to render the pipeline
    if id[0][count-1] != len(instructionList)+1:
        os.system('cls' if os.name == 'nt' else 'clear')
        renderPipeline(pipeline, lenght, clock, completedInstructions, instructionList, iNum, printBegin)
    else:
        pipeline[lenght, :] = np.zeros((1, 500))
        pipeline[lenght][clock+1] = 1
        os.system('cls' if os.name == 'nt' else 'clear')
        renderPipeline(pipeline, lenght-1, clock, completedInstructions, instructionList, iNum, printBegin)

    clock += 1
    if id[0][count-1] < len(instructionList)+1:
        lenght += 1
    if (clock % 12 == 0):
        if printBegin == 0:
            printBegin += 10
        else:
            printBegin += 12
        printBack = 2
    option = input()
