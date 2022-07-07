import random as rand
from collections import OrderedDict

maxSum=100
orderImportant = False
listOfVals = [[0,1,2,10,11,20,21,30,31,40,41],[0,1,2,10,11,20,21,30,31,40,41],[0,1,2,10,11,20,21,30,31,40,41],[0,1,2,10,11,20,21,30,31,40,41],[0,1,2,10,11,20,21,30,31,40,41],[0,1,2,10,11,20,21,30,31,40,41],[0,1,2,10,11,20,21,30,31,40,41],[0,1,2,10,11,20,21,30,31,40,41],[0,1,2,10,11,20,21,30,31,40,41],[0,1,2,10,11,20,21,30,31,40,41]]

def generateContender(listOfVals, maxSum):
    # listOfVals is an n variable array of arrays with "common strategy" values
    total=0
    n = len(listOfVals)
    fakeIndex = rand.randint(0,n-1)
    contender = [0] * n
    for i in range(0,n):
        if i == fakeIndex:
            continue
        filteredList = [a for a in listOfVals[i] if a+total<=maxSum]
        if (len(filteredList) == 0):
            return 0
        entry = filteredList[rand.randint(0,len(filteredList)-1)]
        contender[i] = entry
        total += entry
    contender[fakeIndex] = maxSum - total
    return contender

def isPermutation(A, B):
    counts = {}
    if (len(A) != len(B)):
        return False
    for a in A:
        if a in counts:
            counts[a] = counts[a] + 1
        else:
            counts[a] = 1
    for b in B:
        if b in counts:
            if counts[b] == 0:
                return False
            counts[b] = counts[b] - 1
        else:
            return False
    return True

def battle(c1, c2): # returns true if c1 beats c2 [must be edited]
    length = len(c1)
    points = 0
    for i in range(0,length):
        if c1[i] > c2[i]:
            points += 1
        elif c1[i] < c2[i]:
            points -= 1
    if points > 0:
        return 1 # c1 wins
    elif points == 0:
        return 0 # draw
    return -1 # c1 loses
    
def runCompetition(contenders, cutoff): #cutoff is the number of strategies we manually analyse
    numContenders = len(contenders)
    scoreDict = {}
    for i in range(0,numContenders):
        scoreDict[i] = 0
    for i in range(0,numContenders):
        for j in range(i+1, numContenders):
            c1 = contenders[i]
            c2 = contenders[j]
            result = battle(c1,c2)
            if (result == 1):
                scoreDict[i] += 1
                scoreDict[j] -= 1
            if (result == -1):
                scoreDict[i] -= 1
                scoreDict[j] += 1
    results = dict(sorted(scoreDict.items(), key=lambda x: x[1], reverse=True))
    strategies = [0] * cutoff
    total=0
    for key, entry in results.items():
        strategies[total] = contenders[key]
        total+=1
        if (total==cutoff):
            break
    return strategies

def findBlotto():
    numContenders = 1000
    contenders = [[]] * numContenders
    numGenerated=0
    while numGenerated != numContenders:
        contender = generateContender(listOfVals, maxSum)
        if orderImportant and any(isPermutation(contender,x) for x in contenders):
            continue
        contenders[numGenerated]=contender
        numGenerated += 1
    reduced1 = runCompetition(contenders, 50)
    reduced2 = runCompetition(reduced1, 20)
    result = runCompetition(reduced2, 5)
    for s in result:
        print(s)
