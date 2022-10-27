from modules.osint import *
from modules.scan import *
from modules.misc import *
from modules.createrevshell import *
from modules.crypto import *
import os
import sys
import nmap3



class checkSystem:
    def linuxCheck():
        if sys.platform == "linux":
            return True
        else:
            return False

    def permissionCheck():
        if os.geteuid() != 0:
            return False
        else:
            return True



class MAIN:
    def main():
        try:
            while True:
                print(f"""

            ███╗░░░███╗██╗░██████╗████████╗
            ████╗░████║██║██╔════╝╚══██╔══╝
            ██╔████╔██║██║╚█████╗░░░░██║░░░
            ██║╚██╔╝██║██║░╚═══██╗░░░██║░░░
            ██║░╚═╝░██║██║██████╔╝░░░██║░░░
            ╚═╝░░░░░╚═╝╚═╝╚═════╝░░░░╚═╝░░░


        ----- Available Modes -----

        - [1] OSINT
        - [2] ENCRYPT/DECRYPT
        - [3] REVERSE SHELL CREATOR
        - [4] SCAN
        - [5] MISC


                """)
                print("Choose your mode.")
                mode = input("Mode Number ---> ")
                if mode.strip() == "1":
                    OSINT.main()
                elif mode.strip() == "2":
                    CRYPTOGRAPHY.main()
                elif mode.strip() == "3":
                    SHELL.main()
                elif mode.strip() == "4":
                    SCAN.main()
                elif mode.strip() == "5":
                    MISC.main()
                else:
                    print("Invalid Input.")
        except KeyboardInterrupt:
            sys.exit("\n Exited Program...")


if checkSystem.permissionCheck() is False:
    sys.exit(color.BOLD + color.RED + "[!] Must have root privs to run this script. " + color.END)

if checkSystem.permissionCheck() is True:
    print(color.BOLD + color.GREEN + "\n\t PERMISSIONS - [+] Root Permissions Detected \n" + color.END)

if checkSystem.linuxCheck() is False:
    sys.exit(color.BOLD + color.RED + "[!] Mist only supports Linux Distrubutions." + color.END)

if checkSystem.linuxCheck() is True:
    print(color.BOLD + color.GREEN + "\t OPERATING SYSTEM - [+] Detected LINUX \n" + color.END)
    time.sleep(1)


os.system("clear")

if __name__ == "__main__":
    MAIN.main()
