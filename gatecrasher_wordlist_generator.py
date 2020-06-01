import time
import os
from printy import *

file=open("max_length_of_password","r")
file.close()
file=open("clear_terminal_keyword","r")
file.close()
file=open("available_chars","r")
file.close()
file=open("generated_wordlist","r")

file=open("max_length_of_password", "r")
max_length_of_password=int(file.read())
file.close()

if("restore_point" in os.listdir()):
	file=open("restore_point", "r")
	crack_num_list=file.read().splitlines()
	for x in range(0, len(crack_num_list)):
		crack_num_list[x]=int(crack_num_list[x])
	file.close()
else:
	crack_num_list=[]
	for x in range(0,max_length_of_password):
		crack_num_list.append(0)

time_limit=0

file=open("clear_terminal_keyword", "r")
clear_terminal_keyword=file.read() # This must be "cls" on windows, "clear" on linux
file.close()

file=open("available_chars","r")
available_chars=file.read().splitlines()
file.close()
available_chars.insert(0,"")

restore_point_creatable=0
while True:
	current=0
	try:
		while True:
			crack_num_list[current]+=1
			if(crack_num_list[current]==len(available_chars)):
				crack_num_list[current]=1
				current+=1
			else:
				break
	except:
		os.system(clear_terminal_keyword)
		printy("[c]Maximum number of combinations reached@")
		printy("[c](Let me explain it easier: all combinations finished)@")
		print("Gaterasher Wordlist Generator")
		print("Made by Adnmaster")
		while True:
			time.sleep(0)
	passwd=""
	for x in range(0,len(crack_num_list)):
		passwd+=available_chars[crack_num_list[x]]
	printy("[c]Gatecrasher Wordlist Generator@")
	print(crack_num_list)
	print(passwd)
	print("Made by Adnmaster")
	file=open("generated_wordlist", "a")
	file.write(passwd+'\n')
	file.close()
	if(restore_point_creatable==300):
		print("Warning! Do not close!")
		print("Creating restore point!")
		file=open("restore_point", "w")
		file.write("")
		file.close()
		file=open("restore_point", "a")
		for x in range(0,len(crack_num_list)):
			file.write(str(crack_num_list[x])+"\n")
		restore_point_creatable=0
	else:
		restore_point_creatable+=1
	time.sleep(time_limit)
	os.system(clear_terminal_keyword)