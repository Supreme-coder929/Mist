import os 
import time
from cryptography.fernet import Fernet
import rsa


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

class CRYPTOGRAPHY:
	def main():
		def symmetricDecrypt():
			existingFile = input("Would you like to use a existing key file to decrypt(Yes/No): ")
			if existingFile.strip() == "Yes":
				keyfilePath = input("Enter path to key file --> ")
				try:
					with open(keyfilePath, "rb") as c:
						key = c.read()
				except FileNotFoundError:
					print(color.RED + "File Not Found. Try Again." + color.END)
					symmetricDecrypt()
				decryptMsg = Fernet(key)
				encryptedText = input("Encrypted Message --> ")
				decryptedText = decryptMsg.decrypt(encryptedText.encode())
				print(f"Decrypted Text --> {color.BOLD + color.GREEN + decryptedText.decode() + color.END}")
				time.sleep(2)
			elif existingFile.strip() == "No":
				encryptedMessage = input("Encrypted Message --> ")
				supplyKey = input("Supply the Key --> ")
				s = Fernet(supplyKey.encode())
				text = s.decrypt(encryptedMessage.encode())
				print(f"Decrypted Text --> {color.BOLD + color.GREEN + text.decode() + color.END}")
				time.sleep(3)		
			else:
				print("Invalid Input")
			


		def symmetricEncrypt():
			print("Generating Key....")
			time.sleep(0.5)
			key = Fernet.generate_key()
			d = Fernet(key)
			saveKey = input("Would you like to save your key to a file(Yes/No)? ")
			if saveKey.strip() == "Yes":
				with open("key.pem", "wb") as f:
					f.write(key)
			else:
				existingKey = input("Would you like to use a existing key to encrypt(Yes/No)? ")
				if existingKey.strip() == "Yes":
					keyfile = input("Enter path to key file --> ")
					try:
						with open(keyfile, "rb") as e:
							keyf = e.read()
					except FileNotFoundError:
						print(color.RED + "File Not Found. Try Again." + color.END)
						symmetricMenu()
					print("Message to Encrypt")
					message = input("--> ")
					message = message.encode()
					s = Fernet(keyf)
					encrypted_mes = s.encrypt(message)
					print(f"Encrypted Message - {color.BOLD + color.GREEN + encrypted_mes.decode() + color.END}")
				elif existingKey.strip() == "No":
					msg = input("Enter you message: ")
					print(f"Your key is {color.BOLD + color.GREEN + key.decode() + color.END}")
					encrypted_msg = d.encrypt(msg.encode())
					print(f"Encrypted Text - {color.BOLD + color.GREEN + encrypted_msg.decode() + color.END}")
					time.sleep(3)
					symmetricMenu()
				else:
					print("Invalid Input.")
					symmetricMenu()
					
				
		def asymmetricDecrypt():
			encPath = input("Supply the path to the encrypted file --> ")
			privateKeyPath = input("Supply the path to the private key --> ")
			with open(encPath, "rb") as f:
				encrypted_contents = f.read()

			with open(privateKeyPath, "rb") as e:
				loadedPrivateKey = rsa.PrivateKey.load_pkcs1(e.read())

			print("Decrypting Data...")
			time.sleep(1)

			decrypted_content = rsa.decrypt(encrypted_contents, loadedPrivateKey)

			print(f"Decrypted Content - {color.BOLD + color.GREEN + decrypted_content.decode() + color.END}")
			time.sleep(1)
			asymmetricMenu()



		def asymmetricEncrypt():
			keyPair = input("Would you like to generate new key pairs(Yes/No): ")
			if keyPair == "Yes":
				try:
					publicKey, privateKey = rsa.newkeys(1024)
					print("Generating Public Key Pem File...")
					time.sleep(1)
					with open("publickey.pem", "wb") as f:
						f.write(publicKey.save_pkcs1("PEM"))

					print("Generating Private Key Pem File...")
					time.sleep(1)

					with open("privatekey.pem", "wb") as s:
						s.write(privateKey.save_pkcs1("PEM"))
					print("[+] Process Complete.")
					asymmetricMenu()
				except FileExistsError:
					print("Files already exist in your current working directory. Make sure to move them or delete them.")
					asymmetricMenu()
				
			else:
				pemFileExist = input("Would you like to use a existing public key to encrypt(Yes/No)? ")
				if pemFileExist == "Yes":
					print("Supply the path to the public key file")
					pemfilePath = input("\n Public Key File Path --> ")
					try:
						with open(pemfilePath, "rb") as e:
							loadedPublicKey = rsa.PublicKey.load_pkcs1(e.read())
					except FileNotFoundError:
						print("File Not Found. Try Again.")
						asymmetricEncrypt()
					message = input("\n Message to encrypt: ") 
					message = message.encode()
					encrypted_message = rsa.encrypt(message, loadedPublicKey)
					print(f"\n Encrypted Message - {encrypted_message}")
					fileName = input("\n File Name to write the encrypted data too: ")
					with open(fileName, "wb") as q:
						q.write(encrypted_message)
					print(color.BOLD + color.GREEN + "\n [!] Loading encrypted data to a file." + color.END)
					print(color.BOLD + color.GREEN + "\n\t [+] Encrypted File Created." + color.END)
					asymmetricMenu()
				elif pemFileExist == "No":
					print("Bringing back to menu.")
					asymmetricMenu()

											


		def asymmetricMenu():
			while True:
				print(f'''

			---- Asymmetric Encryption/Decryption Menu ---

			- [1] Encrypt
			- [2] Decrypt


					''')
				while True:
					asymChoice = input("Choose your number: ")
					if asymChoice == "1":
						asymmetricEncrypt()
					elif asymChoice == "2":
						asymmetricDecrypt()
					else:
						print("[!] Invalid Input.")
		

		def symmetricMenu():
			while True:
				print(f'''


			---- Symmetric Encryption/Decryption Menu ----

			- [1] Encrypt
			- [2] Decrypt


					''')
				symChoice = input("Choose your number: ")
				if symChoice == "1":
					symmetricEncrypt()
				elif symChoice == "2":
					symmetricDecrypt()
				else:
					print("[!] Invalid Input")


		while True:
			print(f'''	


		███╗░░░███╗██╗░██████╗████████╗░░░░██╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗░█████╗░
		████╗░████║██║██╔════╝╚══██╔══╝░░░██╔╝██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔══██╗
		██╔████╔██║██║╚█████╗░░░░██║░░░░░██╔╝░██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║░░██║
		██║╚██╔╝██║██║░╚═══██╗░░░██║░░░░██╔╝░░██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║░░██║
		██║░╚═╝░██║██║██████╔╝░░░██║░░░██╔╝░░░╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░╚█████╔╝
		╚═╝░░░░░╚═╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░╚════╝░


			[1] Asymmetric Encryption/Decryption
			[2] Symmetric Encryption/Decryption

				''')
			
			cryptType = input("Choose your number: ")
			if cryptType == "1":
				asymmetricMenu()
			elif cryptType == "2":
				symmetricMenu()
			else:
				print("[!] Invalid Input.")

		


















