# Class

class Engine:
    def __init__(self, filePath:str) -> None:
        self.lineWidth = 0
        self.lineHeight = 0
        self.schema : list = self.__getschema(filePath)

    def __getschema(self, filePath:str) -> list:
        schema : list = []
        lines: list = readfile(filePath)
        for line in lines:
            schema.append(line)
        self.lineWidth = len(lines[0])
        self.lineHeight = len(lines)
        return schema

    def getsum(self) -> int:
        sum : int = 0
        for y in range(len(self.schema)):
            digits : list = []
            for x in range(len(self.schema[y])):
                if x not in digits:
                    digits = []
                    if self.__isnumber(self.schema[y][x]):
                        nextX: int = x
                        while self.__isnumber(self.schema[y][nextX]):
                            digits.append(nextX)
                            nextX += 1

                        isEnginePart = False
                        for digit in digits:
                            if self.__issymbolnexttonumber(y, digit):
                                isEnginePart = True
                                break

                        if isEnginePart:
                            strNumber : str = ""
                            for digit in digits:
                                strNumber += self.schema[y][digit]
                            sum += int(strNumber)
        return sum
    
    def getratio(self) -> int:
        sum : int = 0
        for y in range(len(self.schema)):
            for x in range(len(self.schema[y])):
                if self.__isstar(self.schema[y][x]):
                    ratio : int = 1
                    numbers : list = self.__getnumbernexttostar(y, x)
                    
                    if len(numbers) != 2:
                        continue

                    for number in numbers:
                        strNumber : str = ""
                        digits : list = []

                        leftX : int = number[1]
                        while leftX >= 0 and self.__isnumber(self.schema[number[0]][leftX]):
                            digits.insert(0, [number[0], leftX])
                            leftX -= 1
                        
                        rightX : int = number[1] + 1
                        while rightX <= self.lineWidth - 1 and self.__isnumber(self.schema[number[0]][rightX]):
                            digits.append([number[0], rightX])
                            rightX += 1
                        
                        for digit in digits:
                            strNumber += self.schema[digit[0]][digit[1]]

                        # print(strNumber)

                        ratio *= int(strNumber)
                    
                    sum += ratio
        
        return sum

    def __isstar(self, c:str) -> bool:
        return c == "*"

    def __issymbol(self, c:str) -> bool:
        return c != "." and not c.isalnum()
    
    def __isnumber(self, c:str) -> bool:
        return c.isnumeric()
    
    def __getnumbernexttostar(self, y:int, x:int) -> list:
        numbers : list = []

        # Top
        if y != 0 and self.__isnumber(self.schema[y-1][x]):
            numbers.append([y-1, x])
        # Bottom
        if y != self.lineHeight - 1 and self.__isnumber(self.schema[y+1][x]):
            numbers.append([y+1, x])
        # Left
        if x != 0 and self.__isnumber(self.schema[y][x-1]):
            numbers.append([y, x-1])
        # Right
        if x != self.lineWidth - 1 and self.__isnumber(self.schema[y][x+1]):
            numbers.append([y, x+1])
        # Top Left
        if x != 0 and y != 0 and self.__isnumber(self.schema[y-1][x-1]):
            numbers.append([y-1, x-1])
        # Top Right
        if x != self.lineWidth - 1 and y != 0 and self.__isnumber(self.schema[y-1][x+1]):
            numbers.append([y-1, x+1])
        # Bottom Left
        if x != 0 and y != self.lineHeight - 1 and self.__isnumber(self.schema[y+1][x-1]):
            numbers.append([y+1, x-1])
        # Bottom Right
        if x != self.lineWidth - 1 and y != self.lineHeight - 1 and self.__isnumber(self.schema[y+1][x+1]):
            numbers.append([y+1, x+1])

        topRow : list = []
        bottomRow : list = []
        sameRow : list = []
        for digit in numbers:
            if digit[0] == y:
                sameRow.append(digit[1])
            elif digit[0] == y-1:
                topRow.append(digit[1])
            elif digit[0] == y+1:
                bottomRow.append(digit[1])
        
        numbers = []
        
        if len(topRow) > 0 and min(topRow)+1 in topRow:
            topRow.remove(min(topRow)+1)
            if min(topRow)+2 in topRow:
                topRow.remove(min(topRow)+2)

        if len(bottomRow) > 0 and min(bottomRow)+1 in bottomRow:
            bottomRow.remove(min(bottomRow)+1)
            if min(bottomRow)+2 in bottomRow:
                bottomRow.remove(min(bottomRow)+2)

        for digit in topRow:
            numbers.append([y-1, digit])
        for digit in bottomRow:
            numbers.append([y+1, digit])
        for digit in sameRow:
            numbers.append([y, digit])

        return numbers

    def __issymbolnexttonumber(self, y:int, x:int) -> bool:
        # Top
        if y != 0 and self.__issymbol(self.schema[y-1][x]):
            return True
        # Bottom
        elif y != self.lineHeight - 1 and self.__issymbol(self.schema[y+1][x]):
            return True
        # Left
        elif x != 0 and self.__issymbol(self.schema[y][x-1]):
            return True
        # Right
        elif x != self.lineWidth - 1 and self.__issymbol(self.schema[y][x+1]):
            return True
        # Top Left
        elif x != 0 and y != 0 and self.__issymbol(self.schema[y-1][x-1]):
            return True
        # Top Right
        elif x != self.lineWidth - 1 and y != 0 and self.__issymbol(self.schema[y-1][x+1]):
            return True
        # Bottom Left
        elif x != 0 and y != self.lineHeight - 1 and self.__issymbol(self.schema[y+1][x-1]):
            return True
        # Bottom Right
        elif x != self.lineWidth - 1 and y != self.lineHeight - 1 and self.__issymbol(self.schema[y+1][x+1]):
            return True
        else:
            return False

# Functions

def readfile(fileName:str):
    lines : list = []
    file = open(fileName, "r")
    for line in file:
        lines.append(line)
    file.close()
    return lines

def main():
    engine = Engine("advent.txt")
    print(engine.getratio())

# Main

if __name__ == "__main__":
    main();