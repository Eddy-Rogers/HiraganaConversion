import sys
import codecs

inputFileArg = str(sys.argv[1])

#Program Expects one argument (first argument is the name of the script)
if(len(sys.argv) != 2):
    print("Unexpected Number of Arguments: " + len(sys.argv))

inputFile = codecs.open(inputFileArg, encoding='utf-8')
outputFile = codecs.open("conversion.txt", mode="w", encoding="utf-8")

hiraganaConversion = False

for line in inputFile:
    #Start from the end index, continue until we have processed index 0
    index = len(line)
    while(index >= 0):
        if(!hiraganaConversion):
            if(line[index] == ')'):
                hiraganaConversion = true;
                outputFile.

            index--;
        else:
            if(line[index] == '('):

                break;

def replaceHiragana():
    return '';

#while True:
    #try:
        #char = unicode(inputFile.read(1))
        #if not char:
            #break
        #print(char)
    #except:
        #continue
