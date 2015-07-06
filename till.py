#!/usr/bin/python

#This program makes it easier to calculate till amounts

import os

def main():
	#Clear the Screen
	os.system('reset')

	os.system('toilet -t "Till Calculator"')
	print("##########################################################################################################")

	print('\nCHANGE')
	print('-------')
	quarters = int(input('Input the number of quarters: '))
	dimes = int(input('Input the number of dimes: '))
	nickles = int(input('Input the number of nickles: '))
	pennies = int(input('Input the number of pennies: '))
	totalchange = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
	print('TOTAL CHANGE: $' + str(totalchange))

	print('\nCASH')
	print('-----')
	c100 = int(input("Input the number of 100's: "))
	c50 = int(input("Input the number of 50's: "))
	c20 = int(input("Input the number of 20's: "))
	c10 = int(input("Input the number of 10's: "))
	c5 = int(input("Input the number of 5's: "))
	c1 = int(input("Input the number of 1's: "))
	totalcash = (c100 * 100) + (c50 * 50) + (c20 * 20) + (c10 * 10) + (c5 * 5) + c1
	print('TOTAL CASH: $' + str(totalcash))


	drawertotal = totalcash + totalchange
	print('\n-----------------------')
	print('DRAWER TOTAL: $' + str(drawertotal))
	print('-----------------------')

	print('\nDEPOSIT CALCULATION')
	print('--------------------')
	leave = int(input("Input the amout of cash to leave in the drawer: $"))
	depositamount = int(drawertotal) - leave
	print('DEPOSIT: $' + str(depositamount))

	print('\n\nCaclulations complete...')


if __name__ == '__main__':
	main()
