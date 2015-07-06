#!/usr/bin/python

#This script removes all unused pacman packages and cleans the package cache

import os

command_check = 'pacman -Qqtd'							#Command used to check for orphaned packages
command_remove = 'pacman -Rns $(' + command_check + ')'	#Command used to remove orphaned packages
command_cache_1 = 'paccache -rk0'							#Command used to remove the package cache of installed packages
command_cache_2 = 'paccache -ruk0'						#Command used to remove the package cache of uninstalled packages

def main():
	#Check if this script is being run with root privileges
	if os.geteuid() != 0:
		exit("Please run this script with root (sudo) privileges!")

	print("")
	print("")
	print("O R P H A N E D   P A C K A G E S")
	print("---------------------------------")
	os.system(command_check)
	print("")
	if yesno("Proceed to remove the above packages?"):
		print("")
		print("")
		print("R E M O V I N G   P A C K A G E S")
		print("---------------------------------")
		os.system(command_remove)
		print("")
		print("")
		print("C L E A N I N G   P A C K A G E   C A C H E")
		print("-------------------------------------------")
		print("Removing installed package cache...")
		os.system(command_cache_1)
		print("Removing uninstalled package cache...")
		os.system(command_cache_2)
		print("")
		print("")
		print("O P E R A T I O N   C O M P L E T E")
		print("")
	else:
		print("")
		print("")
		print("O P E R A T I O N   C A N C E L L E D")
		print("")



#Prompts the user for a simple yes/no question. Returns "True" if the user responds "Yes"
def yesno(prompt, yesdefault=True):
	if yesdefault:
		yesnoprompt = input(prompt + " [Y/n] ")
		if yesnoprompt == "N" or yesnoprompt == "n":
			return False
		elif yesnoprompt == "Y" or yesnoprompt == "y" or yesnoprompt == "":
			return True
		else:
			print("Invalid input...")
			return yesno(prompt, True)
	else:
		yesnoprompt = input(prompt + " [y/n] ")
		if yesnoprompt == "N" or yesnoprompt == "n":
			return False
		elif yesnoprompt == "Y" or yesnoprompt == "y":
			return True
		else:
			print("Invalid input...")
			return yesno(prompt, False)

	

if __name__ == '__main__':
	main()
