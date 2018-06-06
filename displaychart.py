import utility

def getRowsAndColumns(): #gets rows, columns, and prices
    while True: #ask for/ check rows
        rows = input("Please enter the number of rows (no more than 10) in your theatre: ")
        rows = utility.checkNumbers(rows)
        if rows == None or rows < 1 or rows > 10:
            print("Invalid input. Please try again.")
            continue
        else:
            break
    while True: #ask for/check number of columns
        columns = input("Please enter the number of seats per row (no more than 20) in your theatre: ")
        columns = utility.checkNumbers(columns)
        if columns == None or columns < 1 or columns > 20:
            print("Invalid input. Please try again.")
            continue
        else:
            break
    prices = []
    while True: #ask for price
        for i in range(0, rows):
            prompt = "Please enter the price for row " + str(i) + ": $"
            price = float(input(prompt))
            if price < 0:
                print("Please enter a valid price.")
                continue
            prices.append(price)
        break
    with open("theatre.txt" , "w") as fileObj:
        fileObj.write(str(rows))
        fileObj.write("\n")
        fileObj.write(str(columns))
        fileObj.write("\n")
        for i in range(rows):
            fileObj.write(str(prices[i]))
            fileObj.write("\n")
    return(rows, columns, prices)
    

def buildChart(rows, columns):
    theatre = []
    for i in range (0,rows):
        theatre.append([])
        for j in range (0,columns):
            theatre[i].append('*')
    return theatre

def printChart(theatre, prices):
    rows = len(theatre)
    columns = len(theatre[0])
    print("%8s " % "", end='') #align to the right
    for i in range (rows): #center Seat heading
        print(" ", end='')
    print("Seats")
    if columns > 10: #print 10's places
        print("%8s " % "", end='')
        for i in range (columns):
            if i % 10 == 0:
                print(int(i / 10), end='')
            else:
                print(" ", end='')
        print("")
    print("%8s " % "", end='') #print 1's places
    for i in range(columns):
        print(i % 10, end='')
    print("")
    for i, row in enumerate(theatre): #print row numbers
        print("Row  %3s " % i, end='') 
        for column in row:
            print(column, end='')
        print("    $%.2f" % prices[i])
        
 
    
