textToNumber = {
    "one" : '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

# Functions

def readFile(fileName):
    lines = []
    file = open(fileName, "r")
    for line in file:
        lines.append(line)
    file.close()
    return lines

def getDigitList(text):
    numbers = {}
    for textNumber in textToNumber:
        list = [i for i in range(len(text)) if text.startswith(textNumber, i)]
        for index in list:
            numbers[index] = textToNumber[textNumber]
    for i in range(len(text)):
        if text[i].isdigit():
            numbers[i] = text[i]
    numbers = dict(sorted(numbers.items()))
    digits = [i for i in numbers.values()]
    return digits

def getNumberFromList(list):
    number = 0
    if len(list) == 1:
        number = int(list[0] + list[0])
    else:
        number = int(list[0] + list[-1])
    return number;

def main():
    finalCount = 0
    lines = readFile("advent.txt")
    for line in lines:
        digitList = getDigitList(line)
        number = getNumberFromList(digitList)
        finalCount += number
    print(finalCount)
        

# Main

if __name__ == "__main__":
    main();