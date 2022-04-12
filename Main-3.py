FILE_NAME = '/Users/kora/Downloads/monthly_sales.txt'

salesDictionary = {}

def displayCommandMenu():
  print("COMMAND MENU")
  print("view - View sales for specified month ")
  print("edit - Edit sales for specified month ")
  print("totals - View sales Summary for year ")
  print("exit - Exit program ")

def viewSales():
  month = input("Three-letter month: ")
  month = month.upper()
  if len(month) != 3 or month not in salesDictionary.keys():
    print("Invalid three-letter month")
  else: 
    print("Sales amount for {} is {:,.2f}".format(month,salesDictionary[month]))
  return

def editSalesData():
  month = input("Three-letter month: ")
  month = month.upper()
  if len(month) != 3 or month not in salesDictionary.keys():
    print("Invalid three-letter month")
  else:
      amount = float(input("Sales Amount: "))
      salesDictionary[month] = amount
      writeToFile()
      print("Sales amount for {} is {:,.2f}".format(month,salesDictionary[month]))

def writeToFile():
  fileToWrite = open(FILE_NAME,'w')
  for item in salesDictionary.keys():
    fileToWrite.write(item + " " + str(salesDictionary[item]) + "\n")
  fileToWrite.close()

def displayTotals():
  totalSales = sum(salesDictionary.values())
  monthlyAverage = totalSales/len(salesDictionary.values())
  print("Yearly Total: {:,.2f}".format(totalSales))
  print("Monthly Average: {:,.2f}".format(monthlyAverage))

def readFromFile():
  salesData = open(FILE_NAME,'r')
  for sale in salesData:
    salesLine = sale.strip().split()
    salesDictionary[salesLine[0].upper()] = float(salesLine[1])
  salesData.close()
  return(salesDictionary)

def main():
  salesDictionary = readFromFile()
  displayCommandMenu()
  print()
  while True:
    choice = input("Command: ")
    if choice == 'view':
      viewSales()
      print()
    elif choice == 'edit':
      editSalesData()
      print()
    elif choice == 'totals':
      displayTotals()
      print()
    elif choice == 'exit':
        print()
        print("Thank you for using my app")
        break
    else:
        print("Invalid choice")
   
main()

