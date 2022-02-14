from sys import argv

alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

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

        charIndex = alphabet.index(input[i])
        cypherIndex = 0

        if(trueI % 2 == 0):
            cypherIndex = (charIndex + x0) % len(alphabet)
        elif(x0 > charIndex):
            cypherIndex = len(alphabet) - (abs(charIndex - x0) % len(alphabet))
        else:
            cypherIndex = charIndex - x0

        output = output + alphabet[cypherIndex]
        trueI = trueI + 1
    else:
        output = output + ' '

print(output)
        
