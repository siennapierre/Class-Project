import os
import os.path
import displaychart
import sellticket
import utility
import loadfile
import displaystats
import resetfile

print ("Hello, and welcome to your Movie Theatre Ticketing Program!")
if os.path.exists("theatre.txt"):
    rows, columns, prices = loadfile.loadFile()
else:
    rows, columns, prices = displaychart.getRowsAndColumns()
    
theatre = displaychart.buildChart(rows, columns)

while True:
    print("""Menu
1) Display Seating Chart
2) Sell Tickets
3) Display Stats
4) Reset
5) Exit Program
""")
    choice = input("Please select an option from the menu: ")
    choice = utility.checkNumbers(choice)
    if choice == 1:
        displaychart.printChart(theatre, prices)
    elif choice == 2:
        sellticket.sellTickets(theatre, prices)
        displaychart.printChart(theatre, prices)
    elif choice == 3:
        displaystats.displayStats(theatre, prices)
    elif choice == 4:
        rows, columns, prices, theatre = resetfile.resetFile()
    elif choice == 5:
        print("Have a nice day!")
        quit()
    else:
        print("Invalid choice.")
