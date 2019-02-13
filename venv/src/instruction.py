class Instruction:
    def __init__(self, name, line, number, operator_1, operator_2, isDeviate):
        self.name = name
        self.line = line
        self.number = number
        self.operator_1 = operator_1
        self.operator_2 = operator_2
        self.isDeviate = isDeviate

    def getName(self):
        return self.name

    def getLine(self):
        return self.line

    def getNumber(self):
        return self.number

    def getJumpName(self):
        return self.operator_1

    def getJumpLine(self):
        return self.operator_2

    def getIsDeviate(self):
        return self.isDeviate

    def setName(self, name):
        self.name = name

    def setLine(self, line):
        self.line = line

    def setNumber(self, number):
        self.number = number

    def setJumpName(self, operator_1):
        self.operator_1 = operator_1

    def setJumpLine(self, operator_2):
        self.operator_2 = operator_2

    def setIsDeviate(self, isDeviate):
        self.isDeviate = isDeviate