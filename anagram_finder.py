print('This program will check if the two lines typed in are anagrams!\n')

print('Type "help" if you need more information about anagrams,\n\nand "No, thanks" to start!\n')

answer=input()

if(answer=='help'):
    print('\nOk, let me tell you about what anagram is.\n')
    input()
    print('If you say the two lines are anagram,\nyou can make the first one by reassembling the second one. \n')
    input()
    print("For example, the word 'desserts' and 'stressed' are anagrams.\n")
    input()
    print("But it doesn't have to be the exact opposite.\n")
    input()
    print("The word 'Elvis' and 'lives' are also anagrams.\n")
    input()
    print('Did you get it? (Y/N)\n')

    answer=input()
    if(answer=='Y'):
        print("\nOk, then. Let's start!")

    if(answer=='N'):
        print("\nWell, you'll have to learn by doing it. Let's start anyway!")

if(answer=='No, thanks'):
    print("\nOk, then. Let's start!")

print('\n')
p=input('Type in the first: ')

q=input('Type in the second: ')

letter=list(p)
letters=list(q)

a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
a[0]=letter.count('a')+letter.count('A')
a[1]=letter.count('b')+letter.count('B')
a[2]=letter.count('c')+letter.count('C')
a[3]=letter.count('d')+letter.count('D')
a[4]=letter.count('e')+letter.count('E')
a[5]=letter.count('f')+letter.count('F')
a[6]=letter.count('g')+letter.count('G')
a[7]=letter.count('h')+letter.count('H')
a[8]=letter.count('i')+letter.count('I')
a[9]=letter.count('j')+letter.count('J')
a[10]=letter.count('k')+letter.count('K')
a[11]=letter.count('l')+letter.count('L')
a[12]=letter.count('m')+letter.count('M')
a[13]=letter.count('n')+letter.count('N')
a[14]=letter.count('o')+letter.count('O')
a[15]=letter.count('p')+letter.count('P')
a[16]=letter.count('q')+letter.count('Q')
a[17]=letter.count('r')+letter.count('R')
a[18]=letter.count('s')+letter.count('S')
a[19]=letter.count('t')+letter.count('T')
a[20]=letter.count('u')+letter.count('U')
a[21]=letter.count('v')+letter.count('V')
a[22]=letter.count('w')+letter.count('W')
a[23]=letter.count('x')+letter.count('X')
a[24]=letter.count('y')+letter.count('Y')
a[25]=letter.count('z')+letter.count('Z')

b=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
b[0]=letters.count('a')+letters.count('A')
b[1]=letters.count('b')+letters.count('B')
b[2]=letters.count('c')+letters.count('C')
b[3]=letters.count('d')+letters.count('D')
b[4]=letters.count('e')+letters.count('E')
b[5]=letters.count('f')+letters.count('F')
b[6]=letters.count('g')+letters.count('G')
b[7]=letters.count('h')+letters.count('H')
b[8]=letters.count('i')+letters.count('I')
b[9]=letters.count('j')+letters.count('J')
b[10]=letters.count('k')+letters.count('K')
b[11]=letters.count('l')+letters.count('L')
b[12]=letters.count('m')+letters.count('M')
b[13]=letters.count('n')+letters.count('N')
b[14]=letters.count('o')+letters.count('O')
b[15]=letters.count('p')+letters.count('P')
b[16]=letters.count('q')+letters.count('Q')
b[17]=letters.count('r')+letters.count('R')
b[18]=letters.count('s')+letters.count('S')
b[19]=letters.count('t')+letters.count('T')
b[20]=letters.count('u')+letters.count('U')
b[21]=letters.count('v')+letters.count('V')
b[22]=letters.count('w')+letters.count('W')
b[23]=letters.count('x')+letters.count('X')
b[24]=letters.count('y')+letters.count('Y')
b[25]=letters.count('z')+letters.count('Z')

A=a.count(0)
B=b.count(0)
if A==26:
    if B==26:
        print('\nThey should be typed in english...')

elif p==q:
    print('\nThey are the same one!')

else:

    if a==b:
        print('\nAnagram!')

    else:
        print('\nNot anagram...')

input('\nPress Enter to continue...')
exit()
