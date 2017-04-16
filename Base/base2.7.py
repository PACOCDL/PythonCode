
fileName = ['01.py', '02.py', '03.txt', '04.html']
# print (fileName[2])
# tempName=fileName[0]
# position=tempName.rfind('.')
# print(tempName[position:])
for tempName in fileName:
    position = tempName.rfind('.')
    print(tempName[position:])
while tempName < fileName:
    position = tempName.rfind('.')
