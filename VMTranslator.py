import sys
import os
from Parser import Parser
from CodeWriter import CodeWriter

def getInputName():
    try:
        return sys.argv[1]
    except IndexError:
        raise SystemExit("Usage: {} <input filename>".format(sys.argv[0]))

def trimFile(name):
    return os.path.basename(name).partition(".")[0]

def isVMFile(fileName):
    return os.path.basename(fileName).partition(".")[2] == "vm"

def main():
    inputFileName = getInputName()
    isDirectory = os.path.isdir(inputFileName)

    if isDirectory:
        files = os.listdir(inputFileName)
        vmFiles = filter(isVMFile, files)
        listOfFiles = list(map(lambda fileName: inputFileName + "/" + fileName, vmFiles))

        outputFileName = trimFile(inputFileName)
        writer = CodeWriter(inputFileName + "/" + outputFileName)
        if len(listOfFiles) > 1:
           writer.bootstrap()
    else:
        listOfFiles = [inputFileName]
        outputFileName = trimFile(inputFileName)
        writer = CodeWriter(outputFileName)

    for currentFile in listOfFiles:
        print("File to be parsed: {}".format(currentFile))

        writer.setNewInputFile(trimFile(currentFile))
        parser = Parser(currentFile)

        while parser.hasMoreCommands():
            parser.advance()
            command = parser.getCommand()
            if parser.isArithmetic():
                writer.writeArithmetic(command)
            elif parser.isPush() or parser.isPop():
                writer.writePushPop(command)
            elif parser.isLabel():
                writer.writeLabel(command)
            elif parser.isGoto():
                writer.writeGoto(command)
            elif parser.isIf():
                writer.writeIf(command)
            elif parser.isFunction():
                writer.writeFunction(command)
            elif parser.isCall():
                writer.writeCall(command)
            elif parser.isReturn():
                writer.writeReturn(command)
            elif parser.isComment() or parser.isBlankLine():
                continue
            else:
                raise Exception("Command not supported")
    
    parser.close() 
    writer.close()
    print("VMTranslator finished.")

if __name__ == "__main__":
    main()
