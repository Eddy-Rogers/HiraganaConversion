import sys
import HiraganaLib

if __name__ == '__main__':
    # Program expects one argument (first argument is the name of the script)
    #if len(sys.argv) != 2:
        #print("Unexpected Number of Arguments: " + str(len(sys.argv)))
    #inputfilearg = str(sys.argv[1])
    HiraganaLib.convert_hiragana('N2.txt')
