import displaychart
import sellticket

def displayStats(theatre, prices):
    totalReserved = 0
    totalUnreserved = 0
    totalRevenue = 0
    for row in theatre:
        for column in row:
            if column == '#':
                totalReserved += 1
            elif column == '*':
                totalUnreserved += 1
    for i, row in enumerate(theatre):
        for column in row:
            if column == '#':
                totalRevenue += prices[i]
    print("Total seats sold: ", totalReserved)
    print("Total seats open: ", totalUnreserved)
    print("Total revenue: $%.2f" % totalRevenue)
