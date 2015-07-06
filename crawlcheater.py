#!/usr/bin/python

import sys
import os
import shutil

#-----CONFIGURATION------------------------------------------------------------------
savedir = r"/home/harrison/.crawl/saves"	#Location of the dungeon crawl character files
backupdir = r"/home/harrison/.crawlbackups" #Location you would like to store the backup files
#------------------------------------------------------------------------------------

#Main entry point for the script
def main():
	#Check to see if this script was run with root privileges
	if os.geteuid() == 0:
		exit("Please DO NOT run this script with root (sudo) privileges!")

	#Check to see if the dungeon crawl save directory exists
	if not os.path.exists(savedir):
		exit("Could not find valid save directory at \"" + savedir + "\"")

	#Check to see if the backup directory exists (and if it doesn't, prompt the user for its creation)
	if not os.path.exists(backupdir):
		os.system("reset")
		print("Could not find existing backup directory at \"" + backupdir + "\"!")
		yesno = input("Would you like to create a new backup directory here? [Y/n] ")
		if yesno == "Y" or yesno == "y" or yesno == "":
			os.makedirs(backupdir)
			input("Finished! - Press any key to continue...")
			os.system("reset")
		elif yesno == "N" or yesno == "n":
			exit("Okay Then. Bye.")
		else:
			exit('Please type "Y", "y", "N", or "n" only...')

	#Figure out if we have been passed any command line arguments and redirect the script to the appropriate function if necessary
	if len(sys.argv) < 2:
		mainmenu()
	elif "-h" in sys.argv[1]:
		help()
	elif "-b" in sys.argv[1]:
		dobackup(sys.argv[2], False)
	elif "-r" in sys.argv[1]:
		dorestore(sys.argv[2], False)
	else:
		exit("Unkown parameter!")
	
#Main menu for the script (called if the user doesn't pass any command line arguments)
def mainmenu():
	os.system("reset")
	print("Harrison's Dungeon Crawl Character Saver")
	print("----------------------------------------")
	print("1 - Backup a character")
	print("2 - Restore a character")
	print("3 - Backup all characters")
	print("4 - Restore all characters")
	print("5 - Delete a character")
	print("")

	mainchoice = input("Please make a selection: ")

	if mainchoice == "1":
		backup()
	elif mainchoice == "2":
		restore()
	elif mainchoice == "3":
		backupall()
	elif mainchoice == "4":
		restoreall()
	elif mainchoice == "5":
		delete()
	else:
		exit("That wasn't an option, smart-ass...")

#Delete menu
def delete():
	os.system("reset")
	savefiles = os.listdir(savedir)
	characters = []

	for filename in savefiles:
		if ".cs" in filename:
			characters.append(filename.replace(".cs", ""))

	if len(characters) < 1:
		exit("No characters found in save folder!")

	print("Delete Character")
	print("----------------")
	for character in characters:
		print(str(characters.index(character) + 1) + " - " + character)

	print("")
	charselect = input("Please make a selection: ")
	charselectindex = int(charselect) - 1

	print("")
	if charselectindex < len(characters) and charselectindex >= 0:
		dodelete(characters[charselectindex])
		exit()
	else:
		exit("That wasn't an option, smart-ass...")

#Deletes the specified character
def dodelete(charactername):
	charfilename = charactername + ".cs"
	fullsavedir = savedir + "/" + charfilename

	savefiles = os.listdir(savedir)

	if charfilename in savefiles:
		yesnodel = input("Are you sure you want to delete this character? [Y/n] ")
		if yesnodel == "N" or yesnodel == "n":
			exit("Deletion cancelled...")
		elif yesnodel == "Y" or yesnodel == "y" or yesnodel == "":
			print("Processing character: " + charactername)
			os.remove(fullsavedir)
			print('"' + charactername + '" at "' + fullsavedir + '" deleted!')
		else:
			exit("That wasn't an option, smart-ass...")

	print("")

#Restore menu
def restore():
	os.system("reset")
	backupfiles = os.listdir(backupdir)
	characters = []

	for filename in backupfiles:
		if ".cs" in filename:
			characters.append(filename.replace(".cs", ""))

	if len(characters) < 1:
		exit("No characters found in backup folder!")

	print("Restore Character")
	print("-----------------")
	for character in characters:
		print(str(characters.index(character) + 1) + " - " + character)

	print("")
	charselect = input("Please make a selection: ")
	charselectindex = int(charselect) - 1

	print("")
	if charselectindex < len(characters) and charselectindex >= 0:
		dorestore(characters[charselectindex], False)
		exit("Character restore complete!")
	else:
		exit("That wasn't an option, smart-ass...")

#Restores the specified character
def dorestore(charactername, skipoverwriteprevious):
	charfilename = charactername + ".cs"
	fullsavedir = savedir + "/" + charfilename
	fullbackupdir = backupdir + "/" + charfilename

	savefiles = os.listdir(savedir)

	if not os.path.exists(fullbackupdir):
		exit("ERROR: Backup not found!")

	if charfilename in savefiles:
		if not skipoverwriteprevious:
			yesno3 = input("Current save for character found, are you sure you want to overwrite this saved game? [Y/n] ")
			if yesno3 == "N" or yesno3 == "n":
				print("Skipping " + charactername + "...")
				print("")
				return
			elif yesno3 == "Y" or yesno3 == "y" or yesno3 == "":
				os.remove(fullsavedir)
			else:
				exit("That wasn't an option, smart-ass...")
		else:
			os.remove(fullsavedir)

	print("Processing character: " + charactername)
	print('"' + fullbackupdir + '" -> "' + fullsavedir + '"')

	shutil.copy(fullbackupdir, fullsavedir)

	print("")

#Restores all backup characters
def restoreall():
	os.system("reset")
	
	print("WARNING: This will automatically overwrite all current saved games you have a backup of!")
	yesno4 = input("Are you sure you want to continue? [Y/n] ")
	if yesno4 == "N" or yesno4 == "n":
		exit("Operation cancelled!")
	elif yesno4 == "Y" or yesno4 == "y" or yesno4 == "":
		print("")
	else:
		exit("That wasn't an option, smart-ass...")

	backupfiles = os.listdir(backupdir)
	characters = []

	for filename in backupfiles:
		if ".cs" in filename:
			characters.append(filename.replace(".cs", ""))

	if len(characters) < 1:
		exit("No characters found in save folder!")

	os.system("reset")
	print("Restore All Characters")
	print("----------------------")

	print("Found " + str(len(characters)) + " backups...")
	print("")

	for character in characters:
		dorestore(character, True)

	exit("Character restore complete!")

#Backup menu
def backup():
	os.system("reset")
	savefiles = os.listdir(savedir)
	characters = []

	for filename in savefiles:
		if ".cs" in filename:
			characters.append(filename.replace(".cs", ""))

	if len(characters) < 1:
		exit("No characters found in save folder!")

	print("Backup Character")
	print("----------------")
	for character in characters:
		print(str(characters.index(character) + 1) + " - " + character)

	print("")
	charselect = input("Please make a selection: ")
	charselectindex = int(charselect) - 1

	print("")
	if charselectindex < len(characters) and charselectindex >= 0:
		dobackup(characters[charselectindex], False)
		exit("Character backup complete!")
	else:
		exit("That wasn't an option, smart-ass...")

#Backs-up the specified character
def dobackup(charactername, skipoverwriteprevious):
	charfilename = charactername + ".cs"
	fullsavedir = savedir + "/" + charfilename
	fullbackupdir = backupdir + "/" + charfilename

	backedupfiles = os.listdir(backupdir)

	if not os.path.exists(fullsavedir):
		exit("ERROR: Save not found!")

	if charfilename in backedupfiles:
		if not skipoverwriteprevious:
			yesno3 = input("Previous backup found, are you sure you want to overwrite this backup? [Y/n] ")
			if yesno3 == "N" or yesno3 == "n":
				print("Skipping " + charactername + "...")
				print("")
				return
			elif yesno3 == "Y" or yesno3 == "y" or yesno3 == "":
				os.remove(fullbackupdir)
			else:
				exit("That wasn't an option, smart-ass...")
		else:
			os.remove(fullbackupdir)

	print("Processing character: " + charactername)
	print('"' + fullsavedir + '" -> "' + fullbackupdir + '"')

	shutil.copy(fullsavedir, fullbackupdir)

	print("")

#Backs-up all characters
def backupall():
	os.system("reset")
	
	print("WARNING: This will automatically overwrite all previous backups of your current characters!")
	yesno4 = input("Are you sure you want to continue? [Y/n] ")
	if yesno4 == "N" or yesno4 == "n":
		exit("Operation cancelled!")
	elif yesno4 == "Y" or yesno4 == "y" or yesno4 == "":
		print("")
	else:
		exit("That wasn't an option, smart-ass...")

	savefiles = os.listdir(savedir)
	characters = []

	for filename in savefiles:
		if ".cs" in filename:
			characters.append(filename.replace(".cs", ""))

	if len(characters) < 1:
		exit("No characters found in save folder!")

	os.system("reset")
	print("Backup All Characters")
	print("---------------------")

	print("Found " + str(len(characters)) + " characters...")
	print("")

	for character in characters:
		dobackup(character, True)

	exit("Character backup complete!")

#Displayes help (if the user passes "-h" or "-help" as a command line argument)
def help():
	print("Harrison's Dungeon Crawl Character Saver")
	print("----------------------------------------")
	print("You may run this script either by itself (for an interactive menu) or with command line arguments...")
	print('To change the save location of character backups or the location of the search directory, modify the "savedir" and "backupdir" variables under the "CONFIGURATION" section in the python script...')
	print("")
	print('Usage: ./crawlcheater.py -[b/backup OR r/restore] [Character Name]')
	print("")
	print('Example: ./crawlcheater.py -backup "My Character"')
	print('Example: ./crawlcheater.py -r Bob')
	print("")

#Boilerplate magic :P
if __name__ == '__main__':
	main()
