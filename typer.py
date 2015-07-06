#!/usr/bin/python

#This program types out the specified character sequence

import sys
import time

default_time = 0.02
version = 1

def main():
	
	#Check how many parameters we have
	if len(sys.argv) < 2:
		typeit("Harrison's typer script...")
		typeit("-----------------------")
		typeit('Usage: python typer.py [String : Message] [Float : Delay (0.02)] [String : Seperator ("")]')
		print("")
		typeit('Example: python typer.py "This is a test with the minimum arguments!"')
		typeit('This is a test with the minimum arguments!')
		print("")
		typeit('Example: python typer.py "This is also a test, but with a slower typing speed!" 0.06')
		typeit('This is also a test, but with a slower typing speed!', 0.06)
		print("")
		typeit('Example: python typer.py "This is a test with the maximum amount of tweaking!" 0.03 " "')
		typeit('This is a test with the maximum amount of tweaking!', 0.03, " ")
		print("")
	elif len(sys.argv) == 2:
		typeit(str(sys.argv[1]))
	elif len(sys.argv) == 3:
		typeit(str(sys.argv[1]), float(sys.argv[2]))
	elif len(sys.argv) == 4:
		typeit(str(sys.argv[1]), float(sys.argv[2]), str(sys.argv[3]))
	else:
		exit("Unkown parameter!")

def typeit(characters, sleeptime=default_time, seperator=''):
	if len(characters) == 0:
		print("")

	for char in characters:
		print(char, end=seperator, flush=True)
		time.sleep(sleeptime)

	print("")

if __name__ == '__main__':
	main()
