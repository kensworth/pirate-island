from random import randint

class PirateIsland():
    def __init__(self, numPirates):
        self.pirateList = []
        colors = ['red', 'blue']
        for i in range(numPirates):
            color = colors[randint(0,1)]
            pirate = Pirate(color) 
            self.pirateList.append(pirate)
    def printPirates(self):
        colors = []
        for pirate in self.pirateList:
            colors.append(pirate.color)
        print 'pirates', colors
    def execute(self):
        self.calledColors = []
        for i in range(len(self.pirateList)):
            self.calledColors.append(self.pirateList[i].survive(len(self.pirateList), self.calledColors, self.pirateList[i + 1:]))
        deadPirates = 0
        for i in range(len(self.pirateList)):
            if self.calledColors[i] != self.pirateList[i].color:
                deadPirates += 1
        print 'called colors', self.calledColors
        print deadPirates, 'pirate(s) dead!', len(self.pirateList) - deadPirates, 'pirate(s) alive!'

class Pirate():
    def __init__(self, color):
        self.color = color
    def survive(self, totalPirates, calledColors, piratesInFront):
        redBlueEnumMap = {
            'red': False,
            'blue': True 
        }
        xorFront = None
        xorBack = None
        for i in range(len(piratesInFront)):
            if xorFront == None:
                xorFront = redBlueEnumMap[piratesInFront[len(piratesInFront) - 1].color]
            else:
                xorFront ^= redBlueEnumMap[piratesInFront[len(piratesInFront) - i - 1].color]
        for i in range(len(calledColors)):
            if xorBack == None:
                xorBack = redBlueEnumMap[calledColors[0]]
            else:
                xorBack ^= redBlueEnumMap[calledColors[i]]
        if len(piratesInFront) == totalPirates - 1:
            return redBlueEnumMap.keys()[redBlueEnumMap.values().index(xorFront)]
        elif len(piratesInFront) == 0:
            return redBlueEnumMap.keys()[redBlueEnumMap.values().index(xorBack)]
        else:
            return redBlueEnumMap.keys()[redBlueEnumMap.values().index(xorFront ^ xorBack)]

pirateIsland = PirateIsland(100)
pirateIsland.printPirates()
pirateIsland.execute()
