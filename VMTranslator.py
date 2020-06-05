import sys
from Parser import Parser
from CodeWriter import CodeWriter

def createOutputFileName(file):
    currentFileName = file.split(".")[0]
    currentFileName = currentFileName.split("/")[-1]
    outputFileName = currentFileName + ".asm"
    return outputFileName

def main():
    inputName = sys.argv[1]
    inputFile = Parser(inputName)
    outputName = createOutputFileName(inputName)
    outputFile = CodeWriter(outputName)

    while inputFile.hasMoreCommands():
        inputFile.advance()
        command = inputFile.getCommand()
        print("command", command)
        if inputFile.isArithmetic():
            print("outputs add")
            outputFile.writeArithmetic(command)
        elif inputFile.isPush() or inputFile.isPop():
            outputFile.writePushPop(command) 
    
    inputFile.close() 
    outputFile.close()
    print("VMTranslator finished.")

if __name__ == "__main__":
    main()