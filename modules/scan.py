import nmap3
import os
import sys
import simplejson as json
import re
import time
import threading
import socket
from queue import Queue


queue = Queue()

with queue.mutex:
    queue.queue.clear()

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

ipFormat = re.compile(r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$')

nmap = nmap3.Nmap()

class SCAN:
	def main():
		def nmapScan():
			global ipFormat
			global nmap

			print(f'''

------- NMAP Scan --------

	> [1] Full Scan
	> [2] Heavy Scan
	> [3] Stealth Scan
	> [4] Light Scan


				''')

			scanType = input("Choose your scan type<1-4>: ")
			ipTarget = input("Enter the target IP: ")
			try:
				validate = ipFormat.search(ipTarget.strip())
				print(f"Valid IP --> {color.BOLD + color.GREEN + str(validate.group()) + color.END}")
			except:
				print(f"Invalid IP --> {color.BOLD + color.RED + ipTarget + color.END}")
				sys.exit("Syntax - 10.10.10.10")

																									
			if scanType.strip() == "1":
				nmapOutput = nmap.nmap_version_detection(str(ipTarget))
				jsonOutput = json.dumps(nmapOutput, indent=4)
				print(jsonOutput)
				print(color.BOLD + color.GREEN + '\n Scan Complete' + color.END)
				print('\033[39m')
				#pprint.pprint(nmapOutput, indent=4)
			elif scanType.strip() == "2":
				nmapOutput = nmap.scan_top_ports(str(ipTarget), args="-p- -A -sV")
				jsonOutput = json.dumps(nmapOutput, indent=4)
				print(jsonOutput)
				print(color.BOLD + color.GREEN + '\n Scan Complete' + color.END)
				print('\033[39m')
				#pprint.pprint(nmapOutput, indent=4)
			elif scanType.strip() == "3":
				nmapOutput = nmap.scan_top_ports(str(ipTarget), args="-sS")
				jsonOutput = json.dumps(nmapOutput, indent=4)
				print(jsonOutput)
				print(color.BOLD + color.GREEN + '\n Scan Complete' + color.END)
				print('\033[39m')
			elif scanType.strip() == "4":
				nmapOutput = nmap.scan_top_ports(str(ipTarget), args="-f")
				jsonOutput = json.dumps(nmapOutput, indent=4)
				print(jsonOutput)
				print(color.BOLD + color.GREEN + '\n Scan Complete' + color.END)
				print('\033[39m')
			else:
				print("Invalid Input.")


		def pythonScan():
			translatePort = {
				20:'ftp',
				21:'ftp',
				22:'ssh',
				25:'smtp',
				53:'dns',
				69:'tftp',
				80:'http',
				88:'Kerberos',
				102:'Iso-tsap',
				110:'POP3',
				123:'ntp',
				135:'Microsoft-EPMAP',
				137:'netBIOS-ns',
				139:'netBIOS-ssn',
				179:'bgp',
				443:'https',
				445:'microsoft-ds',
				512:'exec',
				514:'shell',
				1099:'rmiregistry',
				1524:'ingreslock',
				500:'ISAKMP',
				902:'VMware-Server',
				1725:'steam',
				2049:'nsf',
				2121:'ccproxy-ftp',
				3306:'mySql',
				5432:'postgresql',
				3398:'RDP',
				4664:'Google-Desktop',
				5900:'vnc',
				6000:'X11',
				6667:'irc',
				6681:'BitTorrent',
				6999:'BitTorrent',
				8009:'ajp13',
				8180:'unknown',
				12345:'NetBus',
				18006:'Back Orifice',
				27374:'Sub7'

			}


			def portScan(port):
				try:
					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					s.connect((targetIP, port))
					return True
				except:
					return False

			def portAmountMode(mode):
				portList = []

				if mode == 1:
					print(color.BOLD + color.GREEN + " Scanning 1024 Ports..." + color.END)
					print(color.BOLD + color.RED + "[!] SMB Ports take 1 minute longer to scan" + color.END)
					for i in range(1, 1024+1):
						portList.append(i)

					for port in portList:
						queue.put(port)

				if mode == 2:
					print(color.BOLD + color.GREEN + " Scanning 65535 Ports..." + color.END)
					print(color.BOLD + color.RED + "[!] SMB Ports take 1 minute longer to scan." + color.END)
					for i in range(1, 65535+1):
						portList.append(i)

					for port in portList:
						queue.put(port)

				if mode == 3:
					for i in [80, 443, 21, 22, 110, 143, 3306, 3389, 512]:
						queue.put(i)
				

			def workers():
				while not queue.empty():
					port = queue.get()
					if portScan(port):
						for key, value in translatePort.items():
							if str(key) == str(port):
								print(color.BOLD + color.GREEN + f"Port {port} | OPEN - {value}" + color.END)
								if queue.empty():
									queue.task_done()




			def start_scan(threads, modetype):

				thread_list = []

				portAmountMode(modetype)

				start = time.perf_counter()
				print("=" * 50)

				for i in range(threads):
					thread = threading.Thread(target=workers, daemon=True)
					thread_list.append(thread)

				for thread in thread_list:
					thread.start()

				for thread in thread_list:
					thread.join()

				end = time.perf_counter()

				print("=" * 50)

				print(color.BOLD + f'Scan Complete ---> Finished in {round(end-start, 2)} seconds.' + color.END)

				print("=" * 50)

			print('''

		------ Upgraded Python Multi-Threaded Port Scanner -----


			[1] Light Scan
			[2] Heavy Scan
			[3] Common Ports Scan

				''')
			modeType = input("Choose your number<1-3>: ")
			targetIP = input("Enter the target IP: ")
			threadAmount = input("Amount of threads: ")
			if modeType.strip() == "1":
				start_scan(int(threadAmount), 1)
			elif modeType.strip() == "2":
				start_scan(int(threadAmount), 2)
			elif modeType.strip() == "3":
				start_scan(int(threadAmount), 3)




		print(f'''

		
	███╗░░░███╗██╗░██████╗████████╗░░░░██╗░██████╗░█████╗░░█████╗░███╗░░██╗
	████╗░████║██║██╔════╝╚══██╔══╝░░░██╔╝██╔════╝██╔══██╗██╔══██╗████╗░██║
	██╔████╔██║██║╚█████╗░░░░██║░░░░░██╔╝░╚█████╗░██║░░╚═╝███████║██╔██╗██║
	██║╚██╔╝██║██║░╚═══██╗░░░██║░░░░██╔╝░░░╚═══██╗██║░░██╗██╔══██║██║╚████║
	██║░╚═╝░██║██║██████╔╝░░░██║░░░██╔╝░░░██████╔╝╚█████╔╝██║░░██║██║░╚███║
	╚═╝░░░░░╚═╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝

		[1] NMAP-BASED SCANS
		[2] PYTHON-BASED SCANS


			''')
		scanOption = input("Enter scan type<1-2>: ")
		if scanOption.strip() == "1":
			nmapScan() 
		elif scanOption.strip() == "2":
			pythonScan()
		else:
			print("Invalid Input.")