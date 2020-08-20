import pyttsx3
import os

pyttsx3.speak("hello welcome in my program")
print("hello guys welcome in my program related to python programming")
print(" ")
print(" ")
print("press 1 for browser ")
print("press 2 for notepad ")
print("press 3 for media player ")

print("enter your choice: ",end="")

p=input()
#new=input("what do you want open to this program i mean like paint,calculator.......")
if int(p)==1 :
	pyttsx3.speak("thank you for choose browsing")
	print("which one do you want to use: 'firefox' or 'chrome'")
	b=input("enter browser name: ")
	#s=input("which site:  ")
	os.system(b)
elif int(p)==2 :
	pyttsx3.speak("thanks for choosing notepad")
	os.system("notepad")
elif int(p)==3 :
	pyttsx3.speak("thank you 	for 	 choose	 media	 player		 so 		please 		write           which      media     player	 want		 to   	 open		 in    between   v  l  c  media		 player	 or	 windows 	media 	player")
	print("please write which one do you want to use 'vlc media player' or 'windows media player'")
	m=input()
	if m=='vlc media player' :
		os.system("vlc")
	elif m=='windows media player':
		os.system("wmplayer")
else:
	pyttsx3.speak("do not support")
	print("not support")


