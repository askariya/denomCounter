import csv
# with open('event_transaction_109_2.csv', newline='') as csvFile:
# 	fileReader = csv.reader(csvFile, delimiter=' ', quotechar='|')

pennyCount = 0
nickelCount = 0 
dimeCount = 0 
quarterCount = 0 
dollarCount = 0 
twoDollarCount = 0

inputFile = input("Please enter the name of a csv file (don't forget the extension): ");

csvFile = open(inputFile, 'rt') 
try:
	fileReader = csv.reader(csvFile)
	for row in fileReader:
		if(row[3] == "Penny"):
			pennyCount = pennyCount + 1
		elif (row[3] == "Nickel"):
			nickelCount = nickelCount + 1
		elif (row[3] == "Dime"):
			dimeCount = dimeCount + 1
		elif (row[3] == "Quarter"):
			quarterCount = quarterCount + 1
		elif ((row[3] == "Dollar") or(row[3] == "Dollar Coin")):
			dollarCount = dollarCount + 1
		elif ((row[3] == "Two Dollar Coin") or (row[3] == "Two Dollar")):
			twoDollarCount = twoDollarCount + 1
		else:
			print(row[3])
	#insert all functionality here

	print("# of Pennies: ", pennyCount)
	print("# of Nickels: ", nickelCount)
	print("# of Dimes: ", dimeCount)
	print("# of Quarters: ", quarterCount)
	print("# of Dollars: ", dollarCount)
	print("# of Two Dollar Coins: ", twoDollarCount)

	totalValue = (pennyCount*0.01) + (nickelCount*0.05) + (dimeCount*0.10) + \
				 (quarterCount*0.25) + (dollarCount*1) + (twoDollarCount*2)
finally:
	csvFile.close()

print("Total value in cash transactions: $", totalValue)
var = input("Press 'Enter' to close")

