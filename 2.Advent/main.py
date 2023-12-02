class Game:
    def __init__(self, text:str) -> None:
        self.id : int = self.__getid(text)
        self.records : list = self.__getrecords(text)

    def __getid(self, text:str) -> int:
        leftIndex : int = text.index(" ")
        rightIndex : int = text.index(":")
        return int(text[leftIndex:rightIndex])

    def __getrecords(self, text:str) -> list:
        def getRecordStr(text:str):
            leftIndex : int = text.index(":")+2
            return text[leftIndex:]

        def getRecordStrList(text:str):
            recordList : list = []
            semicolonList : list = [i for i, ltr in enumerate(text) if ltr == ";"]

            if len(semicolonList) == 0:
                recordList.append(text.replace("\n", ""))
            else:
                for i in range(len(semicolonList)):
                    if i == 0:
                        recordList.append(text[:semicolonList[i]])
                        if len(semicolonList) == 1:
                            record : str = text[semicolonList[i]+2:]
                            recordList.append(record.replace("\n", ""))
                    elif i == len(semicolonList) - 1:
                        recordList.append(text[semicolonList[i-1]+2:semicolonList[i]])
                        record : str = text[semicolonList[i]+2:]
                        recordList.append(record.replace("\n", ""))
                    else:
                        recordList.append(text[semicolonList[i-1]+2:semicolonList[i]])

            return recordList
        
        def getRecord(text:str) -> dict:
            record : list = {}
            recordList : list = []
            commaList : list = [i for i, ltr in enumerate(text) if ltr == ","]

            if len(commaList) == 0:
                recordList.append(text)
            else:
                for i in range(len(commaList)):
                    if i == 0:
                        recordList.append(text[:commaList[i]])
                        if len(commaList) == 1:
                            recordList.append(text[commaList[i]+2:])
                    elif i == len(commaList) - 1:
                        recordList.append(text[commaList[i-1]+2:commaList[i]]) 
                        recordList.append(text[commaList[i]+2:])
                    else:
                        recordList.append(text[commaList[i-1]+2:commaList[i]])

            for recStr in recordList:
                greenIndex : int = recStr.find("green")
                redIndex : int = recStr.find("red")
                blueIndex : int = recStr.find("blue")

                if greenIndex != -1:
                    record["green"] = int(recStr[:greenIndex-1])
                if redIndex != -1:
                    record["red"] = int(recStr[:redIndex-1])
                if blueIndex != -1:
                    record["blue"] = int(recStr[:blueIndex-1])

            return record

        gameStr : str = getRecordStr(text)
        recordStrList : list = getRecordStrList(gameStr)
        records : list = []

        for recordStr in recordStrList:
            records.append(getRecord(recordStr))

        return records
    
    def ispossible_v1(self, maxRed: int, maxGreen: int, maxBlue: int) -> bool:
        for record in self.records:
            if "green" in record:
                if record["green"] > maxGreen:
                    return False
            if "red" in record:
                if record["red"] > maxRed:
                    return False
            if "blue" in record:
                if record["blue"] > maxBlue:
                    return False
        return True
    
    def getMinimumPower(self) -> int:
        power : int = 1
        cube = {"green": 0, "red": 0, "blue": 0}

        for record in self.records:
            if "green" in record:
                if record["green"] > cube["green"]:
                    cube["green"] = record["green"]
            if "red" in record:
                if record["red"] > cube["red"]:
                    cube["red"] = record["red"]
            if "blue" in record:
                if record["blue"] > cube["blue"]:
                    cube["blue"] = record["blue"]

        for color in cube:
            if(cube[color] != 0):
                power *= cube[color]

        return power
# Functions

def readfile(fileName:str):
    lines : list = []
    file = open(fileName, "r")
    for line in file:
        lines.append(line)
    file.close()
    return lines

def main():
    finalCount : int = 0
    lines : list = readfile("advent.txt")
    for line in lines:
        game : Game = Game(line)
        finalCount += game.getMinimumPower()
    print(finalCount)
        

# Main

if __name__ == "__main__":
    main();