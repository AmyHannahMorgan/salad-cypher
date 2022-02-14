from sys import argv

def codec(flag, index, length, fibb, fibbCount):
    if(flag == 'e'):
        if(fibbCount % 2 == 0):
            return (index + fibb) % length
        elif(fibb > index):
            return (length - 1) - (abs(index - fibb) % length)
        else :
            return index - fibb
    else: 
        if(fibbCount % 2 == 0):
            if(fibb > index):
                return (length - 1) - (abs(index - fibb + 1) % length)
            else :
                return index - fibb
        else: 
            if(index + fibb > length):
                return (index + fibb + 1) % length
            else:
                return (index + fibb) % length 

alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

cypherbet = None

if(argv[2]):
    cypherbet = list(argv[2].upper()) #some funky issues might occur if cypher key has duplicate characters like "salad" but code should handle it fine
    for char in alphabet:
        if char not in cypherbet:
            cypherbet.append(char)
else:
    cypherbet = alphabet

print(cypherbet)

input = open('input.txt', 'r').read().upper()

x2 = 0
x1 = 0
x0 = 0

trueI = 0

output = ''

for i in range(len(input)):
    if(input[i] != ' '):
        #calculate next step in sequence
        x0 = x1 + x2

        #if x0 is 0 set it to one to begin the sequence
        if(x0 == 0):
            x0 = 1
        
        #swap terms around for next calculation
        x2 = x1
        x1 = x0

        charIndex = cypherbet.index(input[i])
        cypherIndex = codec(argv[1], charIndex, len(cypherbet), x0, trueI)

        # if(trueI % 2 == 0):
        #     cypherIndex = (charIndex + x0) % len(cypherbet)
        # elif(x0 > charIndex):
        #     cypherIndex = (len(cypherbet) - 1) - (abs(charIndex - x0) % len(cypherbet))
        # else:
        #     cypherIndex = charIndex - x0

        output = output + cypherbet[cypherIndex]
        trueI = trueI + 1
    else:
        output = output + ' '

outputFile = open('output.txt', 'w')
outputFile.write(output)
outputFile.close()
        
