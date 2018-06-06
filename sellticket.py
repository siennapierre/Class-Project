import displaychart
import utility

def displayPrices(prices):
    for price in prices:
        print("$",price)

def checkSeats(theatre, soldRow, soldFirst, soldLast):
        for i in range(soldFirst, soldLast + 1):
            if theatre[soldRow][i] == '#':
                return False
        return True

def sellTickets(theatre, prices):
    displaychart.printChart(theatre, prices)
    
    #ask for row to reserve
    soldRow = input("In which row would you like to to be seated?: ")
    soldRow = utility.checkNumbers(soldRow)
    if soldRow == None or (soldRow < 0 or soldRow >= len(theatre)):
        print("Invalid row.")
        return
    
    #ask for seat to reserve
    soldColumn = input("Which seat(s) do you want?(first-last): ")
    soldList = soldColumn.split("-")
    soldFirst = soldList[0]
    soldFirst = utility.checkNumbers(soldFirst)
    soldLast = soldList[-1]
    soldLast = utility.checkNumbers(soldLast)
    if soldFirst == None or soldFirst < 0 or soldFirst >= len(theatre[soldRow]):
        print("Invalid seat.")
        return
    elif soldLast == None or soldLast < 0 or soldLast >= len(theatre[soldRow]):
        print("Invalid seat.")
        return

    #check for reserved seats
    if checkSeats(theatre, soldRow, soldFirst, soldLast):
        for i in range(soldFirst, soldLast + 1): 
            theatre[soldRow][i] = '#'
        total = (soldLast-soldFirst+1)*prices[soldRow]
        print("Your seat is reserved, and your total is $%.2f." % total,"Enjoy the show!")
    else:
        print("One or more of those seats is taken. Please try again.")
        return   
