#sendemail-html-fiend version coding by unknownzerobit

from subprocess import call
from time import sleep
from termcolor import colored

print('''
		        
		███████╗██╗███████╗███╗   ██╗██████╗ 
		██╔════╝██║██╔════╝████╗  ██║██╔══██╗
		█████╗  ██║█████╗  ██╔██╗ ██║██║  ██║
		██╔══╝  ██║██╔══╝  ██║╚██╗██║██║  ██║
		██║     ██║███████╗██║ ╚████║██████╔╝
		╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ 
                                                ''')
startcolor=colored("\n"+"########## Please don't use it as evil purposes :( ########## " ,"blue")
print("{}".format(startcolor) + "\n")

try:
	pathhtmlcolor=colored("[-]Enter the path of html file : ","green")
	pathhtml=input("{}".format(pathhtmlcolor))
	smtpservercolor=colored("[-]Enter the smtp server : ","green")
	smtpserver=input("{}".format(smtpservercolor))
	smtpportcolor=colored("[-] Enter the smtp port : ","green")
	smtpport=int(input("{}".format(smtpportcolor)))
	usercolor=colored("[-]Enter the username of your smtp : ","green")
	user=input("{}".format(usercolor))
	passwordcolor=colored("[-]Enter the password of your smtp : ","green")
	password=input("{}".format(passwordcolor))
	fromaddresscolor=colored("[-]From your email : ","green")
	fromaddress=input("{}".format(fromaddresscolor))
	toaddresscolor=colored("[-]To victim email : ","green")
	toaddress=input("{}".format(toaddresscolor))
	subjectcolor=colored("[-]Subject : ","green")
	Subject=input("{}".format(subjectcolor))
	messageheadercolor=colored("[-] Enter your header (ex: From: service <m.service@info.org> ) : ","green")
	messageheader=input("{}".format(messageheadercolor))
	sleep(5)
	sendemail=call("cat {} | sendemail -s {}:{} -xu {} -xp {} -f '{}' -t '{}' -u '{}' -o message-header='{}' ".format(pathhtml,smtpserver,smtpport,user,password,fromaddress,toaddress,Subject,messageheader),shell=True)
	print("\n"+"Done")
except KeyboardInterrupt :
	errorcolor=colored("\n"+"GOODBYE :)","red","on_blue",["bold","blink"])
	print("{}".format(errorcolor))
	