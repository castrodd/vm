class CodeWriter:
    def __init__(self, name):
        self.currentFileName = None
        self.outputFileName = name + ".asm"
        self.file = open(self.outputFileName, 'a+')
        self.labelCounter = 0
        self.functionName = "anon"
        self.standardPointers = {
            "local": "LCL",
            "argument": "ARG",
            "this": "THIS",
            "that": "THAT",
            "temp": None,
            "pointer": None
        }
        
        print("Output: {}".format(self.outputFileName))
    
    def bootstrap(self):
        self.file.write("// bootstrap\n")
        self.file.write("@261\n")
        self.file.write("D=A\n")
        self.file.write("@SP\n")
        self.file.write("M=D\n")
        self.callInit()
    
    def setNewInputFile(self, name):
        self.currentFileName = name
    
    def getCurrentFileName(self):
        return self.currentFileName
    
    def getFunctionName(self):
        return self.functionName
    
    def setFunctionName(self, name):
        self.functionName = name

    def setLabelNumber(self):
        self.labelCounter = self.labelCounter + 1
        return self.labelCounter

    def getSegmentPointer(self, segment):
        return self.standardPointers[segment]

    def writeArithmetic(self, command):
        action = command[0]
        if action == "add":
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
        elif action == "sub":
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
        elif action == "neg":
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
        elif action == "eq":
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
        elif action == "gt":
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
        elif action == "lt":
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
        elif action == "and":
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
        elif action == "or":
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
        elif action == "not":
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
        action = command[0]
        segment = command[1]
        index = command[2]
        if action == "push" and segment == "constant":
            self.file.write("// push constant {}\n".format(index))
            self.file.write("@{}\n".format(index))
            self.file.write("D=A\n")
            self.file.write("@SP\n")
            self.file.write("A=M\n")
            self.file.write("M=D\n")
            self.file.write("@SP\n")
            self.file.write("M=M+1\n")
        elif action == "pop" and segment in self.standardPointers:
            self.file.write("// pop {} {}\n".format(segment, index))
            if segment == "temp":
                segmentPointer = "R{}".format(5+int(index))
                self.file.write("@{}\n".format(segmentPointer))
                self.file.write("D=A\n")
                self.file.write("@R13\n")
                self.file.write("M=D\n")
                self.file.write("@SP\n")
                self.file.write("M=M-1\n")
                self.file.write("A=M\n")
                self.file.write("A=M\n")
                self.file.write("D=A\n")
                self.file.write("@R13\n")
                self.file.write("A=M\n")
                self.file.write("M=D\n")
            elif segment == "pointer":
                segmentPointer = "R{}".format(3+int(index))
                self.file.write("@{}\n".format(segmentPointer))
                self.file.write("D=A\n")
                self.file.write("@R13\n")
                self.file.write("M=D\n")
                self.file.write("@SP\n")
                self.file.write("M=M-1\n")
                self.file.write("A=M\n")
                self.file.write("A=M\n")
                self.file.write("D=A\n")
                self.file.write("@R13\n")
                self.file.write("A=M\n")
                self.file.write("M=D\n")
            else:
                segmentPointer = self.getSegmentPointer(segment)
                self.file.write("@{}\n".format(index))
                self.file.write("D=A\n")
                self.file.write("@{}\n".format(segmentPointer))
                self.file.write("A=M+D\n")
                self.file.write("D=A\n")
                self.file.write("@R13\n")
                self.file.write("M=D\n")
                self.file.write("@SP\n")
                self.file.write("M=M-1\n")
                self.file.write("A=M\n")
                self.file.write("A=M\n")
                self.file.write("D=A\n")
                self.file.write("@R13\n")
                self.file.write("A=M\n")
                self.file.write("M=D\n")
        elif action == "push" and segment in self.standardPointers:
            self.file.write("// push {} {}\n".format(segment, index))
            if segment == "temp":
                segmentPointer = "R{}".format(5+int(index))
                self.file.write("@{}\n".format(segmentPointer))
                self.file.write("D=M\n")
                self.file.write("@SP\n")
                self.file.write("A=M\n")
                self.file.write("M=D\n")
                self.file.write("@SP\n")
                self.file.write("M=M+1\n")
            elif segment == "pointer":
                segmentPointer = "R{}".format(3+int(index))
                self.file.write("@{}\n".format(segmentPointer))
                self.file.write("D=M\n")
                self.file.write("@SP\n")
                self.file.write("A=M\n")
                self.file.write("M=D\n")
                self.file.write("@SP\n")
                self.file.write("M=M+1\n")
            else:
                segmentPointer = self.getSegmentPointer(segment)
                self.file.write("@{}\n".format(index))
                self.file.write("D=A\n")
                self.file.write("@{}\n".format(segmentPointer))
                self.file.write("A=M+D\n")
                self.file.write("D=M\n")
                self.file.write("@SP\n")
                self.file.write("A=M\n")
                self.file.write("M=D\n")
                self.file.write("@SP\n")
                self.file.write("M=M+1\n")
        elif segment == "static":
            fileName = self.getCurrentFileName()
            variableName = "{}{}{}".format(fileName, ".", index)
            if action == "pop":
                self.file.write("// pop {} {}\n".format(segment, index))
                self.file.write("@SP\n")
                self.file.write("M=M-1\n")
                self.file.write("A=M\n")
                self.file.write("A=M\n")
                self.file.write("D=A\n")
                self.file.write("@{}\n".format(variableName))
                self.file.write("M=D\n")
            else:
                self.file.write("// push {} {}\n".format(segment, index))
                self.file.write("@{}\n".format(variableName))
                self.file.write("D=M\n")
                self.file.write("@SP\n")
                self.file.write("A=M\n")
                self.file.write("M=D\n")
                self.file.write("@SP\n")
                self.file.write("M=M+1\n")
        else:
            raise Exception("{} {} is not an implemented command".format(action, segment))
    
    def writeLabel(self, command):
        functionName = self.getFunctionName()
        labelName = command[1]
        self.file.write("// label {}\n".format(labelName))
        self.file.write("({}${})\n".format(functionName, labelName))
    
    def writeGoto(self, command):
        functionName = self.getFunctionName()
        labelName = command[1]        
        self.file.write("// Goto {}\n".format(labelName))
        self.file.write("@{}${}\n".format(functionName, labelName))
        self.file.write("0;JMP\n")
    
    def writeIf(self, command):
        functionName = self.getFunctionName()
        labelName = command[1]
        self.file.write("// If-goto {}\n".format(labelName))
        self.file.write("@SP\n")
        self.file.write("M=M-1\n")
        self.file.write("A=M\n")
        self.file.write("D=M\n")
        self.file.write("@{}${}\n".format(functionName, labelName))
        self.file.write("D;JNE\n")
    
    def writeFunction(self, command):
        functionLabel = command[1]
        numberOfArgs = int(command[2])
        self.setFunctionName(functionLabel)

        self.file.write("// function {}\n".format(functionLabel))
        self.file.write("({})\n".format(functionLabel))
        for i in range(numberOfArgs):
            self.writePushPop(["push", "constant", "0"])
    
    def loadAndPush(self, symbol):
        self.file.write("// Load {}\n".format(symbol))
        self.file.write("@{}\n".format(symbol))
        self.file.write("D=M\n")
        self.file.write("@SP\n")
        self.file.write("A=M\n")
        self.file.write("M=D\n")
        self.file.write("@SP\n")
        self.file.write("M=M+1\n")
    
    def writeCall(self, command):
        functionName = command[1]
        labelNumber = self.setLabelNumber()
        returnLabel = "{}$ret.{}".format(functionName, labelNumber)

        self.file.write("// call {}\n".format(command[1]))
        self.file.write("@{}\n".format(returnLabel))
        self.file.write("D=A\n")
        self.file.write("@SP\n")
        self.file.write("A=M\n")
        self.file.write("M=D\n")
        self.file.write("@SP\n")
        self.file.write("M=M+1\n")

        self.loadAndPush("LCL")
        self.loadAndPush("ARG")
        self.loadAndPush("THIS")
        self.loadAndPush("THAT")
        self.loadAndPush("SP")

        self.writePushPop(["push", "constant", "5"])
        self.writeArithmetic(["sub"])
        self.writePushPop(["push", "constant", command[2]])
        self.writeArithmetic(["sub"])
        self.file.write("@SP\n")
        self.file.write("M=M-1\n")
        self.file.write("A=M\n")
        self.file.write("A=M\n")
        self.file.write("D=A\n")
        self.file.write("@ARG\n")
        self.file.write("M=D\n")

        self.file.write("@SP\n")
        self.file.write("D=M\n")
        self.file.write("@LCL\n")
        self.file.write("M=D\n")

        self.file.write("@{}\n".format(command[1]))
        self.file.write("0;JMP\n")
        self.file.write("({})\n".format(returnLabel))
    
    def callInit(self):
        returnLabel = "Sys.init$ret.0"

        self.file.write("// call Sys.init\n")
        self.loadAndPush(returnLabel)
        self.loadAndPush("LCL")
        self.loadAndPush("ARG")
        self.loadAndPush("THIS")
        self.loadAndPush("THAT")
        self.loadAndPush("SP")
        self.writePushPop(["push", "constant", "5"])
        self.writeArithmetic(["sub"])
        self.writePushPop(["push", "constant", "0"])
        self.writeArithmetic(["sub"])
        self.file.write("@SP\n")
        self.file.write("M=M-1\n")
        self.file.write("A=M\n")
        self.file.write("A=M\n")
        self.file.write("D=A\n")
        self.file.write("@ARG\n")
        self.file.write("A=M\n")
        self.file.write("M=D\n")
        self.file.write("@SP\n")
        self.file.write("D=M\n")
        self.file.write("@LCL\n")
        self.file.write("M=D\n")
        self.file.write("@Sys.init\n")
        self.file.write("0;JMP\n")
        self.file.write("({})\n".format(returnLabel))

    def restoreSegment(self, segment):
        self.file.write("// restore {}\n".format(segment))
        self.file.write("@13\n")
        self.file.write("M=M-1\n")
        self.file.write("A=M\n")
        self.file.write("D=M\n")
        self.file.write("@{}\n".format(segment))
        self.file.write("M=D\n")
    
    def writeReturn(self, command):
        self.file.write("// return\n")
        self.file.write("@LCL\n")
        self.file.write("D=M\n")
        self.file.write("@13\n")
        self.file.write("M=D\n")
        self.file.write("@SP\n")
        self.file.write("A=M\n")
        self.file.write("M=D\n")
        self.file.write("@SP\n")
        self.file.write("M=M+1\n")
        self.writePushPop(["push", "constant", "5"])
        self.writeArithmetic(["sub"])
        self.file.write("@SP\n")
        self.file.write("M=M-1\n")
        self.file.write("A=M\n")
        self.file.write("A=M\n")
        self.file.write("D=M\n")
        self.file.write("@14\n")
        self.file.write("M=D\n")
        self.file.write("@SP\n")
        self.file.write("M=M-1\n")
        self.file.write("A=M\n")
        self.file.write("D=M\n")
        self.file.write("@ARG\n")
        self.file.write("A=M\n")
        self.file.write("M=D\n")
        self.file.write("@ARG\n")
        self.file.write("D=M+1\n")
        self.file.write("@SP\n")
        self.file.write("M=D\n")
        self.restoreSegment("THAT")
        self.restoreSegment("THIS")
        self.restoreSegment("ARG")
        self.restoreSegment("LCL")
        self.file.write("@14\n")
        self.file.write("A=M\n")
        self.file.write("0;JMP\n")

    def close(self):
        self.file.close()