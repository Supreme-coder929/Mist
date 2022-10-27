import sys
import os
import requests
import time
import json
import re
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(".env_var"))




IPformat = re.compile(r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$')
EMAILformat = re.compile(r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$')


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

class OSINT:
	def main():
		def revNumLookup():
			number = input("Enter the local format phone number: ")
			prefix = input("Enter the country prefix: ")

			url2 = f"https://ipqualityscore.com/api/json/phone/{os.getenv('BUNDLE_QUALITY_API_KEY')}/{prefix + number}?strictness=1"
			url = f"https://api.apilayer.com/number_verification/validate?number={prefix + number}"

			payload = {}
			headers= {
			  "apikey": str(os.getenv("NUM_LOOKUP_API_KEY"))
			}

			response = requests.request("GET", url, headers=headers, data=payload)
			response1 = requests.get(url2)

			formatJson1 = json.loads(response1.text)
			formatJson = json.loads(response.text)

			print(f"Advanced Reverse Phone Lookup | Target - {color.BOLD + prefix + number + color.END}")
			time.sleep(1)
			print(f'''

Valid - {color.BOLD + str(formatJson["valid"]) + color.END}
Number - {color.BOLD + formatJson["number"] + color.END}
Local Format - {color.BOLD + formatJson["local_format"] + color.END}
International Format - {color.BOLD + formatJson["international_format"] + color.END}
Country Prefix - {color.BOLD + formatJson["country_prefix"] + color.END}
Country Code - {color.BOLD + formatJson["country_code"] + color.END}
Country Name - {color.BOLD + formatJson["country_name"] + color.END}
Location - {color.BOLD + formatJson["location"] + color.END}
Carrier - {color.BOLD + formatJson["carrier"] + color.END}
Line Type - {color.BOLD + formatJson["line_type"] + color.END}
Region - {color.BOLD + formatJson1["region"] + color.END}
Fraud Score - {color.BOLD + str(formatJson1["fraud_score"]) + color.END}
Recent Abuse - {color.BOLD + str(formatJson1["recent_abuse"]) + color.END}
VOIP - {color.BOLD + str(formatJson1["VOIP"]) + color.END}
Prepaid - {color.BOLD + str(formatJson1["prepaid"]) + color.END}
Risky - {color.BOLD + str(formatJson1["risky"]) + color.END}
Active - {color.BOLD + str(formatJson1["active"]) + color.END}
Name - {color.BOLD + str(formatJson1["name"]) + color.END}
Timezone - {color.BOLD + str(formatJson1["timezone"]) + color.END}
ZIP Code - {color.BOLD + str(formatJson1["zip_code"]) + color.END}
Leaked - {color.BOLD + str(formatJson1["leaked"]) + color.END}
Active Status - {color.BOLD + str(formatJson1["active_status"]) + color.END}

				''')
	



		def emailLookup(): 
			email = input("Enter the full email of the target: ")


			url = f"https://ipqualityscore.com/api/json/email/{str(os.getenv('BUNDLE_QUALITY_API_KEY'))}/{email}"

			response = requests.get(url)

			formatJson = json.loads(response.text)

			print(f"Advanced Reverse Email Lookup | Target - {color.BOLD + str(email) + color.END}")

			time.sleep(1)
			print(f'''

Valid - {color.BOLD + str(formatJson["valid"]) + color.END}
TImed Out - {color.BOLD + str(formatJson["timed_out"]) + color.END}
Disposable - {color.BOLD + str(formatJson["disposable"]) + color.END}
First Name - {color.BOLD + str(formatJson["first_name"]) + color.END}
Deliverability - {color.BOLD + str(formatJson["deliverability"]) + color.END} 
SMTP Score - {color.BOLD + str(formatJson["smtp_score"]) + color.END}
Overall Score - {color.BOLD + str(formatJson["overall_score"]) + color.END}
DNS Valid - {color.BOLD + str(formatJson["dns_valid"]) + color.END}
Honeypot - {color.BOLD + str(formatJson["honeypot"]) + color.END}
Fraud Score - {color.BOLD + str(formatJson["fraud_score"]) + color.END}
First Seen - {color.BOLD + str(formatJson["first_seen"]["human"]) + color.END}



				''')

		def advancedIpLookup():
			ipaddress = input("IP address of target: ")

			url = f"https://api.apilayer.com/ip_to_location/{ipaddress}"

			payload = {}
			headers= {
			  "apikey": str(os.getenv("GEO_IP_API_KEY"))
			}

			response = requests.request("GET", url, headers=headers, data=payload)

			formatJson = json.loads(response.text)
			print(f"Locating Approximate Area of IP - {color.BOLD + ipaddress + color.END}")
			time.sleep(1)

			print(f'''

Longtitude - {color.BOLD + str(formatJson["longitude"]) + color.END}
Latitude - {color.BOLD + str(formatJson["latitude"]) + color.END}
City - {color.BOLD + str(formatJson["city"]) + color.END}
Continent Code - {color.BOLD + str(formatJson["continent_code"]) + color.END}
Continent Name - {color.BOLD + str(formatJson["continent_name"]) + color.END}
Country Name - {color.BOLD + str(formatJson["country_name"]) + color.END}
Country Code - {color.BOLD + str(formatJson["country_code"]) + color.END}
Currencies - {color.BOLD + str(formatJson["currencies"]) + color.END}
Region Name - {color.BOLD + str(formatJson["region_name"]) + color.END}
Type - {color.BOLD + str(formatJson["type"]) + color.END}

				''')

		print(f'''

		
	███╗░░░███╗██╗░██████╗████████╗░░░░██╗░█████╗░░██████╗██╗███╗░░██╗████████╗
	████╗░████║██║██╔════╝╚══██╔══╝░░░██╔╝██╔══██╗██╔════╝██║████╗░██║╚══██╔══╝
	██╔████╔██║██║╚█████╗░░░░██║░░░░░██╔╝░██║░░██║╚█████╗░██║██╔██╗██║░░░██║░░░
	██║╚██╔╝██║██║░╚═══██╗░░░██║░░░░██╔╝░░██║░░██║░╚═══██╗██║██║╚████║░░░██║░░░
	██║░╚═╝░██║██║██████╔╝░░░██║░░░██╔╝░░░╚█████╔╝██████╔╝██║██║░╚███║░░░██║░░░
	╚═╝░░░░░╚═╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░░░░╚════╝░╚═════╝░╚═╝╚═╝░░╚══╝░░░╚═╝░░░

		[1] Reverse Number Lookup
		[2] Email Lookup
		[3] Advanced IP Lookup


			''')
		while True:
			option = input("Choose your number: ")
			if option == "1":
				revNumLookup()
			elif option == "2":
				emailLookup()
			elif option == "3":
				advancedIpLookup()



