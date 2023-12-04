# Classes

class Card:
    def __init__(self, text:str) -> None:
        self.id = self.__getid(text)
        self.wins = self.__getwins(text)
        self.copies = 0

    def __getid(self, text:str):
        doublePoint : int = text.index(":")
        firstSpace : int = text.index(" ")
        return int(text[firstSpace:doublePoint])

    def __getwins(self, text:str):
        winList : list = []
        winNum : list = getwinnum(text)
        curNum : list = getcurnum(text)
        intersect : list = getintersection(winNum, curNum)
        for i in range(len(intersect)):
            winList.append(self.id+i+1)
        return winList
    
    def getpoints(self):
        return self.copies + 1

# Functions

def getwinnum(text:str):
    doublePoint : int = text.index(":")+2
    slash : int = text.index("|")-1
    return text[doublePoint:slash].split()

def getcurnum(text:str):
    slash : int = text.index("|")+2
    return text[slash:].split()

def readfile(fileName:str):
    lines : list = []
    file = open(fileName, "r")
    for line in file:
        lines.append(line)
    file.close()
    return lines

def calcPoints(intersect: list):
    points : int = 0
    if len(intersect) > 0:
        points += 1
    for _ in range(len(intersect)-1):
        points *= 2
    return points

def getintersection(winNum: list, curNum: list):
    return list(set(winNum) & set(curNum))

def main():
    sum : int = 0

    lines : list = readfile("advent.txt")
    
    cards : dict = {}
    
    for line in lines:
        card : Card = Card(line)
        cards[card.id] = card

    for card in cards.values():
        for _ in range(card.copies+1):
            for win in card.wins:
                if win in cards:
                    cards[win].copies += 1
        
    
    for card in cards.values():
        sum += card.getpoints()
    
    print(sum)

# Main

if __name__ == "__main__":
    main();