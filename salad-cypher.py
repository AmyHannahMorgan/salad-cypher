from sys import argv

alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

cypherbet = None

if(argv[1]):
    cypherbet = list(argv[1].upper()) #some funky issues might occur if cypher key has duplicate characters like "salad" but code should handle it fine
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
        cypherIndex = 0

        if(trueI % 2 == 0):
            cypherIndex = (charIndex + x0) % len(cypherbet)
        elif(x0 > charIndex):
            cypherIndex = (len(cypherbet) - 1) - (abs(charIndex - x0) % len(cypherbet))
        else:
            cypherIndex = charIndex - x0

        output = output + cypherbet[cypherIndex]
        trueI = trueI + 1
    else:
        output = output + ' '

outputFile = open('output.txt', 'w')
outputFile.write(output)
outputFile.close()
        
