# from __future__ import print_function
import os
import re
import fileinput
def clearscr():
	print "\033[H\033[J"
clearscr()
# def sed(regex1, regex2):
#     #make format
#     for line in fileinput.input(str[3]):
#         print(line.replace(regex1, regex2), end='', flush=True)
#     print()
while True:
	retval = os.getcwd()
	# path = "/home/keshu/Desktop"
	# os.chdir( path )
	# retval = os.getcwd()
	# print "My Current working directory is: %s\n\n" % retval
	# path = "/home/keshu/Desktop"

	# retval = os.getcwd()
	# print "Current working directory is: %s\n\n" % retval

	# os.chdir( path )

	# retval = os.getcwd()

	# print "Directory changed %s\n\n" % retval

	# for x in os.listdir(retval):
 #    	print x
	write_command=raw_input("Current Dir-[+] "+os.getcwd()+"-> <Enter ur command here>[+]: ")
	# write_command=raw_input("-> ")
	terminal_input=write_command.split()
	if(write_command=="ls"):
		files=os.listdir(".")
		for file in files:
			print file+""
			# print ""
	
	elif(write_command=="pwd"):
		print os.getcwd()
	
	elif(terminal_input[0]=="cd"):
		os.chdir(terminal_input[1])
	
	elif(write_command=="clear"):
		clearscr()
	
	elif(terminal_input[0]=="touch"):
		for x in range(1,len(terminal_input)):
			with open(terminal_input[x],"w+") as file:
				pass
	
	elif(terminal_input[0]=="cat"):
		temp=1000000
		with open(terminal_input[1]) as file:
			for x in file:
				if(temp):
					print x,
					temp-=1
				else:
					break
	
	elif(terminal_input[0]=="head"):
		temp=10
		with open(terminal_input[1]) as file:
			for x in file:
				if(temp):
					print x,
					temp-=1
				else:
					break
	
	elif(terminal_input[0]=="tail"):
		temp=10
		arr=[]
		with open(terminal_input[1]) as file:
			for x in file:
				arr.append(x)
			if(len(arr)<temp):
				for item in arr:
					print item,
			else:
				for item in arr[len(arr)-temp:]:
					print item,

	elif(terminal_input[0]=="diff"):
		if(os.path.exists(terminal_input[1]) and os.path.exists(terminal_input[2])):
			with open(terminal_input[1]) as file1:
				with open(terminal_input[2]) as file2:
					common = set(file1).difference(file2)
			common.discard('\n')
			for line in common:
				print line
			print ""


	elif(terminal_input[0]=="sed"):
		for line in fileinput.input(terminal_input[3]):
			print line.replace(terminal_input[1],terminal_input[2])
			print ""

	
	elif(terminal_input[0]=="grep"):
		patt=terminal_input[1][1:-1]
		with open(terminal_input[2]) as file:
			for x in file:
				matchwords=re.findall(patt,x)
				if len(matchwords):
					print x+""

	elif(write_command=="exit"):
		break
	
	
	else:
		print("Please type valid Command...!")
