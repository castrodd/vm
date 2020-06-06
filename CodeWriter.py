class CodeWriter:
    def __init__(self, path):
        self.file = open(path, 'a')
        self.labelCounter = 0
        self.standardPointers = ["local", "argument", "this", "that"]

    def setLabelNumber(self):
        self.labelCounter = self.labelCounter + 1
        return self.labelCounter
    
    def setFileName(self, fileName):
        pass

    def writeArithmetic(self, command):
        # print("writes add", command)
        command = command[0]
        if command == "add":
            self.file.write("// add\n")
            self.file.write("@SP\n")
            self.file.write("M=M-1\n")
            self.file.write("A=M\n")
            self.file.write("D=M\n")
            self.file.write("@SP\n")
            self.file.write("M=M-1\n")
            self.file.write("A=M\n")
            self.file.write("A=M\n")
            self.file.write("D=A+D\n")
            self.file.write("@SP\n")
            self.file.write("A=M\n")
            self.file.write("M=D\n")
            self.file.write("@SP\n")
            self.file.write("M=M+1\n")
        elif command == "sub":
            self.file.write("// sub\n")
            self.file.write("@SP\n")
            self.file.write("M=M-1\n")
            self.file.write("A=M\n")
            self.file.write("D=M\n")
            self.file.write("@SP\n")
            self.file.write("M=M-1\n")
            self.file.write("A=M\n")
            self.file.write("A=M\n")
            self.file.write("D=A-D\n")
            self.file.write("@SP\n")
            self.file.write("A=M\n")
            self.file.write("M=D\n")
            self.file.write("@SP\n")
            self.file.write("M=M+1\n")
        elif command == "neg":
            self.file.write("// neg\n")
            self.file.write("@SP\n")
            self.file.write("M=M-1\n")
            self.file.write("A=M\n")
            self.file.write("D=M\n")
            self.file.write("D=-D\n")
            self.file.write("@SP\n")
            self.file.write("A=M\n")
            self.file.write("M=D\n")
            self.file.write("@SP\n")
            self.file.write("M=M+1\n")
        elif command == "eq":
            currentLabel = self.setLabelNumber()
            self.file.write("// eq\n")
            self.file.write("@SP\n")
            self.file.write("M=M-1\n")
            self.file.write("A=M\n")
            self.file.write("D=M\n")
            self.file.write("@SP\n")
            self.file.write("M=M-1\n")
            self.file.write("A=M\n")
            self.file.write("A=M\n")
            self.file.write("D=A-D\n")
            self.file.write("@EQ{}\n".format(currentLabel))
            self.file.write("D;JEQ\n")
            self.file.write("D=0\n")
            self.file.write("@NOTEQ{}\n".format(currentLabel))
            self.file.write("0;JMP\n")
            self.file.write("(EQ{})\n".format(currentLabel))
            self.file.write("D=-1\n")
            self.file.write("(NOTEQ{})\n".format(currentLabel))
            self.file.write("@SP\n")
            self.file.write("A=M\n")
            self.file.write("M=D\n")
            self.file.write("@SP\n")
            self.file.write("M=M+1\n")
        elif command == "gt":
            currentLabel = self.setLabelNumber()
            self.file.write("// gt\n")
            self.file.write("@SP\n")
            self.file.write("M=M-1\n")
            self.file.write("A=M\n")
            self.file.write("D=M\n")
            self.file.write("@SP\n")
            self.file.write("M=M-1\n")
            self.file.write("A=M\n")
            self.file.write("A=M\n")
            self.file.write("D=A-D\n")
            self.file.write("@GT{}\n".format(currentLabel))
            self.file.write("D;JGT\n")
            self.file.write("D=0\n")
            self.file.write("@NOTGT{}\n".format(currentLabel))
            self.file.write("0;JMP\n")
            self.file.write("(GT{})\n".format(currentLabel))
            self.file.write("D=-1\n")
            self.file.write("(NOTGT{})\n".format(currentLabel))
            self.file.write("@SP\n")
            self.file.write("A=M\n")
            self.file.write("M=D\n")
            self.file.write("@SP\n")
            self.file.write("M=M+1\n")
        elif command == "lt":
            currentLabel = self.setLabelNumber()
            self.file.write("// lt\n")
            self.file.write("@SP\n")
            self.file.write("M=M-1\n")
            self.file.write("A=M\n")
            self.file.write("D=M\n")
            self.file.write("@SP\n")
            self.file.write("M=M-1\n")
            self.file.write("A=M\n")
            self.file.write("A=M\n")
            self.file.write("D=A-D\n")
            self.file.write("@LT{}\n".format(currentLabel))
            self.file.write("D;JLT\n")
            self.file.write("D=0\n")
            self.file.write("@NOTLT{}\n".format(currentLabel))
            self.file.write("0;JMP\n")
            self.file.write("(LT{})\n".format(currentLabel))
            self.file.write("D=-1\n")
            self.file.write("(NOTLT{})\n".format(currentLabel))
            self.file.write("@SP\n")
            self.file.write("A=M\n")
            self.file.write("M=D\n")
            self.file.write("@SP\n")
            self.file.write("M=M+1\n")
        elif command == "and":
            self.file.write("// and\n")
            self.file.write("@SP\n")
            self.file.write("M=M-1\n")
            self.file.write("A=M\n")
            self.file.write("D=M\n")
            self.file.write("@SP\n")
            self.file.write("M=M-1\n")
            self.file.write("A=M\n")
            self.file.write("A=M\n")
            self.file.write("D=A&D\n")
            self.file.write("@SP\n")
            self.file.write("A=M\n")
            self.file.write("M=D\n")
            self.file.write("@SP\n")
            self.file.write("M=M+1\n")
        elif command == "or":
            self.file.write("// or\n")
            self.file.write("@SP\n")
            self.file.write("M=M-1\n")
            self.file.write("A=M\n")
            self.file.write("D=M\n")
            self.file.write("@SP\n")
            self.file.write("M=M-1\n")
            self.file.write("A=M\n")
            self.file.write("A=M\n")
            self.file.write("D=A|D\n")
            self.file.write("@SP\n")
            self.file.write("A=M\n")
            self.file.write("M=D\n")
            self.file.write("@SP\n")
            self.file.write("M=M+1\n")
        elif command == "not":
            self.file.write("// neg\n")
            self.file.write("@SP\n")
            self.file.write("M=M-1\n")
            self.file.write("A=M\n")
            self.file.write("D=M\n")
            self.file.write("D=!D\n")
            self.file.write("@SP\n")
            self.file.write("A=M\n")
            self.file.write("M=D\n")
            self.file.write("@SP\n")
            self.file.write("M=M+1\n")
        else:
            raise Exception("Not a valid command")
    
    def writePushPop(self, command):
        parseCommand = command
        action = parseCommand[0]
        segment = parseCommand[1]
        index = parseCommand[2]
        # print("command", action, segment, index)
        if action == "push" and segment == "constant":
            self.file.write("// push constant {}\n".format(index))
            self.file.write("@{}\n".format(index))
            self.file.write("D=A\n")
            self.file.write("@SP\n")
            self.file.write("A=M\n")
            self.file.write("M=D\n")
            self.file.write("@SP\n")
            self.file.write("M=M+1\n")
        elif action == "push" and segment in self.standardPointers:
            pass
        elif action == "pop" and segment in self.standardPointers:
            self.file.write("// pop {} {}\n".format(segment, index))
            self.file.write("@SP\n")
            self.file.write("M=M-1\n")
            self.file.write("A=M\n")
            self.file.write("D=A\n")
            self.file.write("@{}\n".format(segment))
            self.file.write("A=M+{}\n".format(index))
            self.file.write("M=D\n")
        elif action == "push" and segment in self.standardPointers:
            self.file.write("// push {} {}\n".format(segment, index))
            self.file.write("@{}\n".format(segment))
            self.file.write("A=M+{}\n".format(index))
            self.file.write("D=M\n")
            self.file.write("@SP\n")
            self.file.write("A=M\n")
            self.file.write("M=D\n")
            self.file.write("@SP\n")
            self.file.write("M=M+1\n")
        else:
            raise Exception("Not an implemented command")

    def close(self):
        self.file.close()