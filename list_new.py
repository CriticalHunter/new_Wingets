import os

if (os.path.exists("fullList.txt")):
    if (os.path.exists("Old_List.txt")):
        os.remove('Old_List.txt')
    if (os.path.exists("newItems.txt")):
        os.remove("newItems.txt")
    os.rename('fullList.txt','Old_List.txt')
commandToRun = 'winget search > fullList.txt'
os.system(commandToRun)

newCount = 0
oldCount = 0
if (os.path.exists("Old_List.txt")):
    newL = [];oldL = []
    with open('Old_List.txt',encoding='UTF-8') as fhand:            
        for line in fhand:
            oldCount += 1
            try:
                for i in range(33,24,-1):
                    if line[i].isalnum():
                        tempLine = line[i:].split(' ')[0]
                        oldL.append(tempLine)
                        break
            except:
                pass
    with open('fullList.txt',encoding='UTF-8') as fhand2:            
        for line in fhand2:
            newCount += 1
            try:
                for i in range(33,24,-1):
                    if line[i].isalnum():
                        tempLine = line[i:].split(' ')[0]
                        newL.append(tempLine)
                        break
            except:
                pass
    
    temp = ((set(newL).difference(set(oldL))))
    with open('fullList.txt',encoding='UTF-8') as fhand2:     
        with open('newItems.txt','a',encoding='UTF-8') as fhand3:       
            for line in fhand2:
                try:
                    for i in range(33,24,-1):
                        if line[i].isalnum():
                            tempLine = line[i:].split(' ')[0]
                            if tempLine in temp:
                                fhand3.write(line)
                            break
                except:
                    pass 

else:
    pass
print("Operation Completed")
print("There are %d items in Updated List and %d items in your old list " % (newCount, oldCount))
temp = newCount - oldCount
print("The %d new items are listed in 'newItems.txt'" % (temp,))

if (os.path.exists("Old_List.txt")):
        os.remove('Old_List.txt')