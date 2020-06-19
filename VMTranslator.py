import sys
import os
from Parser import Parser
from CodeWriter import CodeWriter

def getInputName():
    try:
        return sys.argv[1]
    except IndexError:
        raise SystemExit("Usage: {} <input filename>".format(sys.argv[0]))

def main():
    inputName = getInputName()
    
    outputFileName = inputName.partition(".")[0] + '.asm'
    filename = os.path.basename(inputName).partition(".")[0]

    writer = CodeWriter(filename, outputFileName)
    parser = Parser(inputName)

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
        elif parser.isComment() or parser.isBlankLine():
            continue
        else:
            raise Exception("{} command not supported".format(command))
    
    parser.close() 
    writer.close()
    print("VMTranslator finished.")

if __name__ == "__main__":
    main()
