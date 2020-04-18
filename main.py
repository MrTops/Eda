"""
Main.py lets you access the IDE. The IDE allows for saving, loading, and running files. You can run code by importing the run.py file under the Eda folder then just loading a file as a array (of lines) and putting it in Eda.execute. Eda is like python in the fact that it is compiled at execution.
"""

import os



def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def new_file(filename, filetype=".txt"):
	open(filename + filetype, "w+").close()

def enter_ide():
	write_mode = False
	current_file = ""
	current_data = []
	current_line = 1
	override_update_line = False
	while True:
		try:
			clear()
			print("""
	===========================|
	Exit|Save|Load|Help|Reload |
	==============================================
	Eda IDE, V0.0.1 | Type "sm Help"
	File: {}         | to learn how to use Eda IDE
	==============================================
			""".format(current_file))
			num = 0
			log = ""
			for line in current_data:
				num += 1
				log += "{}| {}\n".format(num, line.rstrip("\n"))
			print(log)

			if not write_mode:
				command = input()

			if write_mode:
				if not override_update_line:
					current_line = len(current_data)+1
				

				line = input("{}| ".format(current_line))
				
				if line == "write":
					write_mode = False
				elif line.startswith("b"):
					current_line = int(line.split(" ")[1])
					override_update_line = True
				elif line.startswith("p"):
					current_data.pop(int(line.split(" ")[1])-1)
				else:
					if not override_update_line:
						current_data.append(line)
					else:
						current_data[current_line-1] = line
						override_update_line = False

			elif str.startswith(command, "sm"):
				if command.split(" ")[1] == "Help":
					clear()
					print("""
	Eda IDE, Help Page. Hit enter to return
	==============================================
	Eda IDE is console based and must use commands
	The command you used to get here "sm" 
	lets you select from the options at the top of the IDE.

	Here's what they do
	===================
	Exit| Closed Eda IDE and goes to main menu
	Save| Saves the file to your computer
	Load| Loads a save file from your computer
	Help| It got you here!
	Reload| Reloads the file, will reset any non-saved data
	===================

	To write to the IDE you must first create the new file using "nf".
	So with nf you must specify some things
	"nf filename type"
	Upon creating a new file it is automatically sent to the IDE
	============================================================
	To write to the file you need to run the command "write" to enter write mode
	While in write mode you write to the file by typing then hitting enter, to edit a
	previous line type "Eda-line" then the line number you wish to return to.
	For example "Eda-line 10" will go to line 10. If the line doesn't exist then it will
	create that line and any before it

	To exit write mode enter "Eda-exitWrite"
	============================================================
					""")
					input("""	[ENTER]""")
				elif command.split(" ")[1] == "Reload":
					current_data = open(current_file, "r").readlines()
				elif command.split(" ")[1] == "Exit":
					clear()
					main_menu()
					break
				elif command.split(" ")[1] == "Load":
					current_file = command.split(" ")[2]
					current_data = open(current_file, "r").readlines()
				elif command.split(" ")[1] == "Save":
					saving = open(current_file, "w+")
					for line in current_data:
						saving.write(line)
					saving.close()
			elif str.startswith(command, "nf"):
				new_file(command.split(" ")[1], command.split(" ")[2])
				print("""	Created file {}\nHit enter to proceed""".format(command.split(" ")[1] + command.split(" ")[2]))
				current_file = command.split(" ")[1] + command.split(" ")[2]
				current_data = open(current_file, "r").readlines()
				input("")
			elif command == "write":
				write_mode = True
		except:
			pass
		

		


def main_menu():
	print("""
	Eda IDE,
	V 0.0.1
	Developed by @DevTops using repl.it
	===================================
	Please select an option below
	===================================
	1) execute file
	2) load file
	3) enter ide
	""")
	while True:
		try:
			selection = int(input("#: "))
			if selection == 1:
				print("	This feature is not yet added")
			elif selection == 2:
				print("	This feature is not yet added")
			elif selection == 3:
				enter_ide()
			else:
				print("	Not a selection")
		except:
			print("	Please input a number")


main_menu()