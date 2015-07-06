#!/usr/bin/python

import os
from random import randint

#The text file to search for possible responces, seperated by new lines
responcesfile = r"responces.txt"

def main():
	#Reset the terminal
	os.system("reset")

	#Make sure the responces file exists
	if not os.path.exists(responcesfile):
		exit('Unable to locate "' + responcesfile + '"! Exiting...')

	#Extract each responce and place it in an array
	with open(responcesfile) as f:
		responces = f.readlines()

	
	os.system('toilet -t "Magic 8 Ball!"')
	print("##########################################################################################")
	print("\nAsk me anything and then press ENTER!")


	while True:
		#Wait for the user to return an input
		x = input("")

		#Clear the screen
		os.system("clear")

		#Select a random responce
		res = randint(0, len(responces) - 1)
		resp = responces[res]

		#Display the responce
		os.system('toilet -t "' + resp + '"')


if __name__ == '__main__':
	main()
