import sys
import os
from Parser import Parser
from CodeWriter import CodeWriter

def main():
    try:
        inputName = sys.argv[1]
    except IndexError:
        raise SystemExit("Usage: {} <input filename>".format(sys.argv[0]))
    
    outputFile = inputName.partition(".")[0] + '.asm'
    filename = os.path.basename(inputName).partition(".")[0]

    writer = CodeWriter(filename, outputFile)
    parser = Parser(inputName)

    while parser.hasMoreCommands():
        parser.advance()
        command = parser.getCommand()
        if parser.isArithmetic():
            writer.writeArithmetic(command)
        elif parser.isPush() or parser.isPop():
            writer.writePushPop(command)
        else:
            raise Exception("{} command not supported".format(command))
    
    parser.close() 
    writer.close()
    print("VMTranslator finished.")

if __name__ == "__main__":
    main()
