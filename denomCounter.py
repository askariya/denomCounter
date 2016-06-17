import csv

pennyCount = 0
nickelCount = 0 
dimeCount = 0 
quarterCount = 0 
fiftyCentCount = 0
fiveDollarCount = 0
tenDollarCount = 0
twentyDollarCount = 0
fiftyDollarCount = 0
hundredDollarCount = 0
dollarCount = 0 
twoDollarCount = 0
tokenCount = 0


inputFile = input("Please enter the name of a csv file (don't forget the extension): ");

try:
	csvFile = open(inputFile, 'rt') 
	fileReader = csv.reader(csvFile)
	for row in fileReader:
		if(row[3] == "Penny"):
			pennyCount += 1
		elif (row[3] == "Nickel"):
			nickelCount += 1
		elif (row[3] == "Dime"):
			dimeCount += 1
		elif (row[3] == "Quarter"):
			quarterCount += 1
		elif (row[3] == "Fifty Cent"):
			fiftyCentCount += 1
		elif ((row[3] == "Dollar") or(row[3] == "Dollar Coin")):
			dollarCount += 1
		elif ((row[3] == "Two Dollar Coin") or (row[3] == "Two Dollar")):
			twoDollarCount += 1
		elif (row[3] == "Five Dollar"):
			fiveDollarCount += 1
		elif (row[3] == "Ten Dollar"):
			tenDollarCount += 1
		elif (row[3] == "Twenty Dollar"):
			twentyDollarCount += 1
		elif (row[3] == "Fifty Dollar"):
			fiftyDollarCount += 1
		elif (row[3] == "Hundred Dollar"):
			hundredDollarCount += 1
		elif (row[3] == "Token"):
			tokenCount += 1
	#insert all functionality here

	print("# of Pennies: ", pennyCount)
	print("# of Nickels: ", nickelCount)
	print("# of Dimes: ", dimeCount)
	print("# of Quarters: ", quarterCount)
	print("# of Dollars: ", dollarCount)
	print("# of Two Dollars: ", twoDollarCount)
	print("# of Five Dollar Bills: ", fiveDollarCount)
	print("# of Ten Dollar Bills: ", tenDollarCount)
	print("# of Twenty Dollar Bills: ", twentyDollarCount)
	print("# of Fifty Dollar Bills: ", fiftyDollarCount)
	print("# of Hundred Dollar Bills: ", hundredDollarCount)
	print("# of Tokens: ", tokenCount)

	totalValue = (pennyCount*0.01) + (nickelCount*0.05) + (dimeCount*0.10) + \
				 (quarterCount*0.25) + (dollarCount*1) + (twoDollarCount*2) + \
				 (fiveDollarCount*5) + (tenDollarCount*10) + (twentyDollarCount*20) + \
				 (fiftyDollarCount*50) + (hundredDollarCount*100)
except FileNotFoundError as e:
	print("Could not find the file specified.")
	var = input("Press 'Enter' to close")
finally:
	csvFile.close()
	print("Total value in cash transactions: $", totalValue)

var = input("Press 'Enter' to close")

