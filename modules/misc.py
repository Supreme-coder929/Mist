import pyminizip
import paramiko
import random
from faker import *

fake = Faker()


class color:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'

class MISC:
	def main():
		def createZIPS():

			fileList = []
			fileQuotes = []

			print(f'''
    -------------- Password Protected ZIP Creator ---------------
		Example of ZIP name - test.zip

		The files you want to zip must be in your current working directory.
				''')
			print("Name of zip file to be created?")
			zipFileName = input("> ")
			print("Name of password for your zip file?")
			passwordFile = input("> ")
			FilesToBeTransfered = input(f"Amount of files to transfer to {zipFileName}: ")

			if int(FilesToBeTransfered.strip()) == 1:
				print("Enter the file path.")
				OneFilePath = input("> ")
				pyminizip.compress(OneFilePath, None, zipFileName, passwordFile, 5)
				print(color.BOLD + color.GREEN + f"ZIP File has been succesfully created." + color.END)
				createZIP()
			else:
				for fileNames in range(int(FilesToBeTransfered)):
					files = input(f"FILE NAME-{fileNames}> ")
					fileList.append(files)

				for quotes in range(int(FilesToBeTransfered)):
					fileQuotes.append("")

				
				print(color.BOLD + color.GREEN + "[+] Created Zip. Now sending files." + color.END)


				pyminizip.compress_multiple(fileList, fileQuotes, zipFileName, passwordFile, 5)
				print(color.BOLD + color.GREEN + "[+] File Transfer Completed. ZIP has been created." + color.END)

		def sftpClient():
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			
			cmd = ['ls', 'chdir', 'pwd', 'get', 'put', 'exit']

			current_directory = "/"

			print(f'''
	COMMANDS 
	ls - List Files
	chdir - Change Directory
	pwd - Get current working directory
	get - Get a file from your remote machine
	put - Transfer a file from your local machine the remote machine
				''')
			ip = input("Specify the IP address: ")
			user = input("Enter the user: ")
			passwd = input("Enter the password: ")
			portnumber = input("Enter the port: ")
			ssh.connect(hostname=ip, username=user, password=passwd, port=portnumber)
			print(f"Succesfully Connected To {color.BOLD + ip + color.END}")
			sftp_client = ssh.open_sftp()
			sftp_client.chdir(current_directory)


			while True:
				commandline = input(f"{color.BOLD + ip + color.END}>")
				for commands in cmd:
					if commandline in commands:
						if commandline == "ls":
							print(sftp_client.listdir())
						elif commandline == "chdir":
							change_directory = input(f"{color.BOLD + 'chdir>' + color.END}")
							try:
								sftp_client.chdir(change_directory)
							except:
								print("No such directory found")
						elif commandline == "pwd":
							print(sftp_client.getcwd())
						elif commandline == "get":
							print("Make sure to enter the full path of")
							get_file = input(f"{color.BOLD + 'get>' + color.END}")
							try:
								sftp_client.get(get_file, get_file)
							except:
								print("File does not exist.")
						elif commandline == "put":
							print("Enter full path to file if its not in your current working directory")
							print("All transfered files go to the /tmp directory")
							put_file = input(f"{color.BOLD + 'put>' + color.END}")
							sftp_client.put(put_file, f"/tmp/{put_file}")
						elif commandline == "exit":
							print(f"{ip} - Session Closed.")
							sftp_client.close()
						else:
							print("Invalid Command")

		def moveFiles():
			global homePath


			filess = ''
			fileList = []
			try:
				print(f'''
				----- Move Multiple Files -----
				Example of Folder Path = home/user/folder
				Note - Do CTRL-C to go back to the menu at any time.
					''')
				while True:
					folderPath = input("Enter path to folder -->  ")
					fileAmount = input(f"How many files would you like to transfer at once to {folderPath}: ")
					if int(fileAmount) < 0:
						break
						print("Enter a valid number")
						manageFiles()
					for i in range(int(fileAmount)):
						filess = input("Enter File Path>")
						fileList.append(filess)

					for files in fileList:
						shutil.move(files, folderPath)

					break
				print(color.BOLD + color.GREEN + f"Transfer of {fileAmount} files has been sent to {folderPath}" + color.END)
			except:
				print("Error has occurred.")

		def fullFakeGen():
			print(f'''

{color.BOLD + color.GREEN}

--------  FULL FAKE PORTFOLIO GENERATOR  ---------
{color.END}
{color.BOLD + color.GREEN}

------- [!] BASIC INFO [!] -------

Name - {fake.name()}
Age - {random.randint(1, 90)}
Gender - {random.choice(["Women", "Man"])}

{color.END}
{color.BOLD + color.YELLOW}

------ [!] FINANCIAL INFORMATION [!] -------

Credit Card Number - {fake.credit_card_number()}
Credit Card Security Number - {fake.credit_card_security_code()}
Credit Card Provider - {fake.credit_card_provider()}
Credit Card Expiry Date - {fake.credit_card_expire()}

{color.END}
{color.BOLD + color.BLUE}

----- [!] MORE INFO [!] ------

Phone Number - {fake.phone_number()}
Personal Email - {fake.ascii_free_email()}
Address -  {fake.address()}
Currently working as - {fake.job()}

{color.END}
{color.BOLD + color.RED}

----- [!] NETWORK INFORMATION [!] -----

Public IPv4 - {fake.ipv4()}
Private IPv4 - {fake.ipv4_private()}
MAC Address - {fake.mac_address()}

{color.END}
				''')

		def fakeInfoGen():
			print('''

	------ Fake Info Generator -------

		[1] Fake Address Generate
		[2] Fake Name Generate
		[3] Full Fake Credentials Generate
		[4] Fake Generate Portfolio (Includes All)


			''')
			while True:
				fakeOption = input("Choose your number: ")
				if fakeOption == "1":
					fakeAddress = fake.address()
					print(f"Fake Address: {color.BOLD + color.GREEN + fakeAddress + color.END}")
				elif fakeOption == "2":
					fakeName = fake.name()
					print(f"Fake Name: {color.BOLD + color.GREEN + fakeName + color.END}")
				elif fakeOption == "3":
					print(f'''

			Credit Card Number - {fake.credit_card_number()}
			Credit Card Security Number - {fake.credit_card_security_code()}
			Credit Card Provider - {fake.credit_card_provider()}
			Credit Card Expiry Date - {fake.credit_card_expire()}


						''')
				elif fakeOption == "4":
					fullFakeGen()

				else:
					print("Invalid Input.")
		while True:
			print(f'''

			
		███╗░░░███╗██╗░██████╗████████╗░░░░██╗███╗░░░███╗██╗░██████╗░█████╗░
		████╗░████║██║██╔════╝╚══██╔══╝░░░██╔╝████╗░████║██║██╔════╝██╔══██╗
		██╔████╔██║██║╚█████╗░░░░██║░░░░░██╔╝░██╔████╔██║██║╚█████╗░██║░░╚═╝
		██║╚██╔╝██║██║░╚═══██╗░░░██║░░░░██╔╝░░██║╚██╔╝██║██║░╚═══██╗██║░░██╗
		██║░╚═╝░██║██║██████╔╝░░░██║░░░██╔╝░░░██║░╚═╝░██║██║██████╔╝╚█████╔╝
		╚═╝░░░░░╚═╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░░░╚═╝░░░░░╚═╝╚═╝╚═════╝░░╚════╝░

			[1] Create Password-Protected ZIPS
			[2] SFTP Client
			[3] Move Files
			[4] Generate Fake Info


				''')
			miscOption = input("Choose your number: ")
			if miscOption == "1":
				createZIPS()
			elif miscOption == "2":
				sftpClient()
			elif miscOption == "3":
				moveFiles()
			elif miscOption == "4":
				fakeInfoGen()