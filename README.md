# /scripts
A collection of various little scripts I have written (usually in python). Most of these scripts are just for fun :P


### magic8ball.py
This script acts like a magic 8 ball. When the user asks it a yes/no question (out loud) and presses enter, it will choose a random responce from a "responces.txt" file in the same directory. The user can keep pressing enter for a new responce. (Requires python3, toilet)

### responces.txt
An example set of responces for the "magic8ball.py" script. Each possible responce should have its own line. Repeating a responce increases the likelihood that it will be selected.

### crawlcheater.py
This script allows you to backup and restore characters from Dungeon Crawl (Stone Soup), effectively allowing you to cheat without entering wizard mode :P and supports command line arguments as well. Note that you need to edit the "savedir" and "backupdir" variables before running the script! Run with the "-h" argument for more info. (Requires python3)

### cleanup.py
This script removes all unused (orphaned) pacman packages and cleans the package cache. (Requires python3, pacman, paccache)

### typer.py
This script "types out" the given character sequence as if it were being typed into the terminal. Supports different typing delays and character seperation. (Requires python3)

### till.py and register.py
These scripts were written by me to make one of my summer jobs easier when my register broke. One impliments a register where multiple amounts can be entered, totaled, and then subtracted from a dollar amound given by the customer for the calculation of change. The other script (till.py) was used at the end of the day to calculate a deposit amount (ignoring coins in the deposit). (Requires python3, toilet)
