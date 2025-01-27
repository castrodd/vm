class Parser:
    def __init__(self, path):
        self.file = open(path, 'r')
        self.originalCommands = self.file.readlines()
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
        elif mostSignificantPart == "//":
            return "C_COMMENT"
        elif mostSignificantPart == "":
            return ""
        else:
            print("Command cannot be parsed: {}".format(self.getCommand()))
            return None
    
    def getCommand(self):
        return self.currentCommand.strip().split(' ')

    def isArithmetic(self):
        return self.commandType() == "C_ARITHMETIC"
    
    def isPush(self):
        return self.commandType() == "C_PUSH"
    
    def isPop(self):
        return self.commandType() == "C_POP"
    
    def isReturn(self):
        return self.commandType() == "C_RETURN"
    
    def isLabel(self):
        return self.commandType() == "C_LABEL"
    
    def isGoto(self):
        return self.commandType() == "C_GOTO"
    
    def isIf(self):
        return self.commandType() == "C_IF"

    def isFunction(self):
        return self.commandType() == "C_FUNCTION"
    
    def isCall(self):
        return self.commandType() == "C_CALL"
    
    def isComment(self):
        return self.commandType() == "C_COMMENT"
    
    def isBlankLine(self):
        return self.commandType() == ""

    def close(self):
        if self.file:
            self.file.close()