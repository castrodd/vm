class Parser:
    def __init__(self, path):
        self.file = open(path, 'r')
        self.originalCommands = self.file.readlines()
        # print("commands", self.originalCommands)
        self.commands = self.originalCommands[:]
        self.currentCommand = None
        self.arithmeticalLogicalCommands = {
            "add": True,
            "sub": True,
            "neg": True,
            "eq": True,
            "gt": True,
            "lt": True,
            "and": True,
            "or": True,
            "not": True
        }

    def resetCommands(self):
        self.commands = self.originalCommands.copy()
        self.currentCommand = None
    
    def hasMoreCommands(self):
        return len(self.commands) > 0
    
    def advance(self):
        if self.hasMoreCommands():
            self.currentCommand = self.commands.pop(0)
            return True
        return False

    def commandType(self):
        try:
            mostSignificantPart = self.getCommand()[0]
        except:
            return None
        # print(mostSignificantPart)
        if mostSignificantPart in self.arithmeticalLogicalCommands:
            return "C_ARITHMETIC"
        elif mostSignificantPart == "push":
            return "C_PUSH"
        elif mostSignificantPart == "pop":
            return "C_POP"
        elif mostSignificantPart == "label":
            return "C_LABEL"
        elif mostSignificantPart == "goto":
            return "C_GOTO"
        elif mostSignificantPart == "if-goto":
            return "C_IF"
        elif mostSignificantPart == "function":
            return "C_FUNCTION"
        elif mostSignificantPart == "return":
            return "C_RETURN"
        elif mostSignificantPart == "call":
            return "C_CALL"
        else:
            return None
    
    def getCommand(self):
        return self.currentCommand.strip().split(' ')

    def isArithmetic(self):
        print("isArith?", self.commandType())
        return self.commandType() == "C_ARITHMETIC"
    
    def isPush(self):
        return self.commandType() == "C_PUSH"
    
    def isPop(self):
        return self.commandType() == "C_POP"
    
    def isReturn(self):
        return self.commandType() == "C_RETURN"

    def arg1(self):
        if self.isArithmetic():
            return self.getCommand()[0]
        elif self.isReturn():
            return None
        else:
            return self.getCommand()[1]

    def arg2(self):
        currentCommand = self.commandType()
        if currentCommand in ["C_PUSH", "C_POP", "C_FUNCTION", "C_CALL"]:
            return self.getCommand()[2]
        else:
            return None 

    def close(self):
        if self.file:
            self.file.close()