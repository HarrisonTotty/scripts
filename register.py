#!/usr/bin/python

#This program makes it easier to calculate register amounts

import os

def main():
	#Clear the Screen
	os.system('reset')

	#Main Loop
	while True:
		os.system("clear")
		os.system('toilet -t "REGISTER"')
		print("###############################################################")
		print("")
		totalitems = getitems()
		print("")
		print("TOTAL = $" + str(totalitems))
		print("")
		getchange(totalitems)
		print("")
		print("")
		input("")

		

def getitems():
	totalitems = 0.0
	currentamout = "e"
	while currentamout is not "":
		currentamout = input("+ $")
		if currentamout is not "":
			totalitems += float(currentamout)

	return totalitems

def getchange(totalitems):
	payamount = float(input("Paying: $"))
	change = payamount - totalitems
	print("CHANGE = $" + str(change))




if __name__ == '__main__':
	main()
