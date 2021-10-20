import socket
#################
print("\033[1;38m>>>>>>>>>>>>>>>>>\033[2;32m Ahmed Khalaf \033[1;39m<<<<<<<<<<<<<<<<<")
print("\033[1;37m>>>>>>>>>>\033[2;33m \033[1;36m Can \033[1;36 You \033[1;33m Follow  \033[1;36mMe In \033[1;36m Facebook \033[1;37m<<<<<<<<")
print("\033[1;31m>>>>>>>>\033[2;32m https://www.facebook.com/ahmedkhkh477 \033[1;31m<<<<<<<<")
#################
host =input ("\033[1;31m Entert Host Name  : " +"\033[1;33m ")
hostip=socket.gethostbyname(host)
print ("\033[1;36m"+hostip)
try:
	for port in range (1,653):
			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.settimeout(0.5)
			d=s.connect_ex((hostip,port))
			if d==0 :
				print( "\033[1;32m Open {}".format(port))
			else:
				print(" \033[1;35mClosed {}" .format(port))
			
except:
	 pass