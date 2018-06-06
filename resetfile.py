import os
import displaychart

def resetFile():
    print("Theatre Program has been reset.")
    rows, columns, prices = displaychart.getRowsAndColumns()
    theatre = displaychart.buildChart(rows, columns)
    return(rows, columns, prices, theatre)


