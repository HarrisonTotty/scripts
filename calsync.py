#!/usr/bin/python
#This script will sync calcurse with a google calendar

import os

ics_link = r"YOUR PRIVATE GOOGLE CALENDAR ICS LINK HERE"
ics_savefile = r"calsync.ics"

def main():
	#Download the ICS file from google calendar
	print("Downloading Google Calendar Data...")
	os.system("wget " + ics_link + " -O " + ics_savefile)

	#Clear all previously stored data
	print("Clearing Old Data...")
	os.system(r"rm ~/.calcurse/apts")

	#Import the new data
	print("Importing Google Calendar Data...")
	os.system("calcurse -i " + ics_savefile)

	#We are done
	print("DONE")

if __name__ == '__main__':
	main()
