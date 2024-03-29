#!/usr/bin/python
import getpass
import string
import os

# creatinga lists of users, their PINs and bank statements
users = ['user1', 'user2', 'user3']
pins = ['1234', '2222', '3333']
amounts = [1000, 2000, 3000]
count = 0
# while loop checks existance of the enterd username
print("****************************************************************************")
print("*                                                                          *")
print("*                   Welcome to IT SOURCECODE ATM SYSTEM                    *")
print("*                                                                          *")
print("****************************************************************************")
while True:
	user = input('\nENTER USER NAME: ')
	user = user.lower()
	if user in users:
		if user == users[0]:
			n = 0
		elif user == users[1]:
			n = 1
		else:
			n = 2
		break
	else:
		print('----------------')
		print('****************')
		print('INVALID USERNAME')
		print('****************')
		print('----------------')

# comparing pin
while count < 3:
	print('------------------')
	print('******************')
	pin = input('PLEASE ENTER PIN: ')
	print('******************')
	print('------------------')
	if pin.isdigit():
		if user == 'user1':
			if pin == pins[0]:
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('INVALID PIN')
				print('***********')
				print('-----------')
				print()

		if user == 'user2':
			if pin == pins[1]:
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('INVALID PIN')
				print('***********')
				print('-----------')
				print()
				
		if user == 'user3':
			if pin == pins[2]:
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('INVALID PIN')
				print('***********')
				print('-----------')
				print()
	else:
		print('------------------------')
		print('************************')
		print('PIN CONSISTS OF 4 DIGITS')
		print('************************')
		print('------------------------')
		count += 1
	
# in case of a valid pin- continuing, or exiting
if count == 3:
	print('-----------------------------------')
	print('***********************************')
	print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
	print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
	print('***********************************')
	print('-----------------------------------')
	exit()

print('-------------------------')
print('*************************')
print('LOGIN SUCCESFUL, CONTINUE')
print('*************************')
print('-------------------------')
print()
print('--------------------------')
print('**************************')	
print(str.capitalize(users[n]), 'welcome to ATM')
print('**************************')
print('----------ATM SYSTEM-----------')
# Main menu
while True:
	#os.system('clear')
	print('-------------------------------')
	print('*******************************')
	response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nLodgement__(L)  \nChange PIN_(P)  \nQuit_______(Q) \nType The Letter Of Your Choices: ').lower()
	print('*******************************')
	print('-------------------------------')
	valid_responses = ['s', 'w', 'l', 'p', 'q']
	response = response.lower()
	if response == 's':
		print('---------------------------------------------')
		print('*********************************************')
		print(str.capitalize(users[n]), 'YOU HAVE ', amounts[n],'EURO ON YOUR ACCOUNT.')
		print('*********************************************')
		print('---------------------------------------------')
		
	elif response == 'w':
		print('---------------------------------------------')
		print('*********************************************')
		cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
		print('*********************************************')
		print('---------------------------------------------')
		if cash_out%10 != 0:
			print('------------------------------------------------------')
			print('******************************************************')
			print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 10 EURO NOTES')
			print('******************************************************')
			print('------------------------------------------------------')
		elif cash_out > amounts[n]:
			print('-----------------------------')
			print('*****************************')
			print('YOU HAVE INSUFFICIENT BALANCE')
			print('*****************************')
			print('-----------------------------')
		else:
			amounts[n] = amounts[n] - cash_out
			print('-----------------------------------')
			print('***********************************')
			print('YOUR NEW BALANCE IS: ', amounts[n], 'EURO')
			print('***********************************')
			print('-----------------------------------')
			
	elif response == 'l':
		print()
		print('---------------------------------------------')
		print('*********************************************')
		cash_in = int(input('ENTER AMOUNT YOU WANT TO LODGE: '))
		print('*********************************************')
		print('---------------------------------------------')
		print()
		if cash_in%10 != 0:
			print('----------------------------------------------------')
			print('****************************************************')
			print('AMOUNT YOU WANT TO LODGE MUST TO MATCH 10 EURO NOTES')
			print('****************************************************')
			print('----------------------------------------------------')
		else:
			amounts[n] = amounts[n] + cash_in
			print('----------------------------------------')
			print('****************************************')
			print('YOUR NEW BALANCE IS: ', amounts[n], 'EURO')
			print('****************************************')
			print('----------------------------------------')
	elif response == 'p':
		print('-----------------------------')
		print('*****************************')
		new_pin = str(getpass.getpass('ENTER A NEW PIN: '))
		print('*****************************')
		print('-----------------------------')
		if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
			print('------------------')
			print('******************')
			new_ppin = str(getpass.getpass('CONFIRM NEW PIN: '))
			print('*******************')
			print('-------------------')
			if new_ppin != new_pin:
				print('------------')
				print('************')
				print('PIN MISMATCH')
				print('************')
				print('------------')
			else:
				pins[n] = new_pin
				print('NEW PIN SAVED')
		else:
			print('-------------------------------------')
			print('*************************************')
			print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
			print('*************************************')
			print('-------------------------------------')
	elif response == 'q':
		exit()
	else:
		print('------------------')
		print('******************')
		print('RESPONSE NOT VALID')
		print('******************')
		print('------------------')
By the way, if you are new to  Python programming and don’t have any idea what  Python IDE to use, I have here a list of the Best Python IDE for Windows, Linux, Mac OS for you.

Additionally, I also have here How to Download and Install the Latest Version of Python on Windows.

To start executing an ATM Program In  Python, make sure that you have installed Python on your computer.

Steps On How To Run The Project
Time needed: 5 minutes

These are the steps on how to run an ATM Program In Python With Source Code

Step 1: Download Source Code
First, find the downloadable source code below and click to start downloading the source code file.
Step 2: Extract File
Next, after finished to download the file, go to the file location right-click the file, and click extract.
Step 3: Open Project Path and Open CMD (Command Prompt).
In order for you to run the project, you just need to open the project path and type CMD. The first thing you need to do is type  py atm. py in the command prompt. After that, just wait for a few seconds to load the system.
Download the Source Code below!
Click Here To Download The Source Code!
Summary
This article is a way to enhance and develop our skills and logic ideas which is important in practicing the  Python programming language which is the most well-known and most usable programming language in many companies.


CategoriesPython Projects With Source Code
Pointers in C Program with Source Code
Leave Management System Project In Python With Source Code
Leave a Comment
Comment
Name
Name *
Email
Email *

Save my name, email, and website in this browser for the next time I comment.


Activity Diagram (32)
ASP.net Projects with Source Code (21)
C Projects With Source Code (50)
C Tutorial (15)
C# Projects With Source Code (6)
C++ Projects With Source Code (35)
Class Diagram (37)
CodeIgniter Projects (30)
Components Diagram (21)
Data Flow Diagram (26)
Database Design Projects (23)
Django Projects With Source Code (98)
Final Year Projects (14)
Java Projects With Source Code (86)
JavaScript Projects With Source Code (57)
Laravel Projects (7)
PHP Projects With Source Code (133)
PHP Tutorial (9)
Python OpenCV Projects (44)
Python Projects With Source Code (100)
Python Tutorial (20)
Sequence Diagram (24)
UML Deployment Diagram (16)
Uncategorized (1)
Use Case Diagram (21)
VB.Net Projects With Source Code (16)
About Us
Terms
Disclaimer
Privacy Policy
Contact
Theme By sourcecodehero.com
This site uses Google AdSense ad intent links. AdSense automatically generates these links and they may help creators earn money.
Python