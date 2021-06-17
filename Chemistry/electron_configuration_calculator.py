element = int(input('Give the atomic number of the element you want to find the electron configuration of: '))
eleconfig = ''
prefix = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']

def maxocc (s):
    global maxoccu
    if s[1] == 's':
        maxoccu = 2
    elif s[1] =='p':
        maxoccu = 6
    elif s[1] =='d':
        maxoccu = 10
    elif s[1] =='f':
        maxoccu = 14

for x in range(len(prefix)):
    maxocc(prefix[x])
    if element == 0:
        break
    elif element >= maxoccu:
        eleconfig = eleconfig + prefix[x] + str(maxoccu) +' '
        element = element - maxoccu
    elif element < maxoccu:
        eleconfig = eleconfig + prefix[x] + str(element)
        break
    print(element)
print(eleconfig)