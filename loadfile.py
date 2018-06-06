import os
import os.path
import utility


def loadFile(): #open
    with open("theatre.txt", "r") as fileObj:
        prices = []
        rows = fileObj.readline()
        rows = utility.checkNumbers(rows)
        columns = fileObj.readline()
        columns = utility.checkNumbers(columns)
        for i in range(rows):
            price = float(fileObj.readline())
            prices.append(price)
    return(rows, columns, prices)
