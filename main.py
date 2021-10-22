import re

genome = input('enter a string of characters:')
genome1= genome.upper()

#the algorithm below works only for genes that begin with ATG and end with TAG.

if ( re.findall('ATG(.+?)TAG', genome1)) :
    all_matches=re.findall('ATG(.+?)TAG', genome1)
    print(all_matches)
    for match in all_matches:
        length = len(match)
        if int(length) % 3 == 0:
          print(match)

else:
    print('gene not found')




