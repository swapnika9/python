engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
newVoiceRate=145
engine.setProperty('rate',newVoiceRate)
os.system("cls")
os.system('color 74')
print("#####################################################################################################################")
print("#####################################################################################################################")
print("---------------------------------------------------[ App Assistant]---------------------------------------------------")
print("#####################################################################################################################")
print("#####################################################################################################################")

pyttsx3.speak("Welcome to My App Assistant")
print("Enter your user name to continue...")
pyttsx3.speak("Enter your user name to continue...")
#Input your username
#Storing the Name input in a variable
User_Name = input("Enter your user name:").upper()

#Clearing the screen
os.system("cls")

#Storing Chatbot Name
cb_name = "ALEXA"

#Getting the current Date
print("---------------------------------------------------------------------------------------------------------------------")
today = datetime.now()
print("Username     :", User_Name)
print("Login date   :", today.strftime("%Y-%m-%d %H:%M:%S"))

#Welcome_screen of my chatbot
print("---------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------[ My App Assistant]------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------")
print(">>",cb_name,"    : Hi ",User_Name,"!!! My name is ", cb_name)
pyttsx3.speak(" Hi %s !!!, My name is ALEXA" %(User_Name))
print(">>",cb_name,"    : I am having shortcuts to open administrative tools, system or user installed applications for you")
pyttsx3.speak(" I am having shortcuts to open administrative tools, system or user installed applications for you")
print(">>",cb_name,"    : How may I help you %s?"%(User_Name))
pyttsx3.speak(" How may I help you %s? " %(User_Name))
print("enter open/start/begin/launch then application name to open required application")
pyttsx3.speak("enter open or start or begin or launch then application name to open required application")
while True:
#for getting the reply from end-user
	print(">>",User_Name,"     : " , end='')
	p = input()
	
	if (("Taskmanager" in p) or ("taskmanager" in p) or ("TASKMANAGER" in p) or ("TaskManager" in p))  and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):
		print(">>",cb_name,"    : Jeez!!! Kill the not responding taks it will     consume more memory")
		pyttsx3.speak("	Jeez!!! Kill the not responding tasks it will consume more memory ")
		os.system("taskmgr")
    
	elif (("Systemconfiguration" in p) or ("configuration" in p) or ("System Configuration" in p) or ("system configuration" in p))  and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):		
		print(">>",cb_name,"    : Gonna change system startup configurations.. Go Ahead!! ")
		pyttsx3.speak("	Gonna change system startup configurations.. Go Ahead!! ")
		os.system("msconfig")
    
	elif (("Notepad" in p) or ("notepad" in p) or ("NOTEPAD" in p) or ("NotePad" in p))  and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):
		print(">>",cb_name,"    : Prioritize your everyday tasks with notepad it will be helpful ...")
		pyttsx3.speak(" Prioritize your everyday tasks with notepad  it will be helpful ...")		
		os.system("notepad")

	elif (("Perfomancemonitor" in p) or ("monitor" in p) or ("performance" in p) or ("performance monitor" in p)) and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):
		print(">>",cb_name,"    : Oh no!! Lagging in performance is more irritaning thing.. I will open it for you")
		pyttsx3.speak("	Oh no!! Lagging in performance is more irritaning thing.. I will open it for you")
		os.system("perfmon")

	elif (("Registryeditor" in p) or ("Registry" in p) or ("registry" in p) or ("Registry editor" in p)) and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):
		print(">>",cb_name,"    : Yeah!!! I will open registry settings for you")
		pyttsx3.speak("	Yeah!!! I will open registry settings for you")
		os.system("regedit")

	elif (("systeminformation" in p) or ("systeminfo" in p) or ("System Information" in p) or ("Systeminformation" in p)) and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):
		print(">>",cb_name,"    : Amazing!!! Your system is having powerful specifications.. If you don't believe me i will show you")
		pyttsx3.speak("	Amazing!!! Your system is having powerful specifications.. If you don't believe me i will show you")
		os.system("msinfo32")

	elif (("Windows Firewall" in p) or ("firewall" in p) or ("Windowsfirewall" in p) or ("Firewall" in p)) and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):
		print(">>",cb_name,"    : Need protection from harmful viruses.. I am not saying corona")
		pyttsx3.speak("	Need protection from harmful viruses.. I am not saying corona")
		os.system("WF")		

	elif (("Remote desktop" in p) or ("RDP" in p) or ("rdp" in p) or ("remote desktop" in p)) and (("open" in p) or ("show"in p) or ("start" in p) or ("launch" in p) or ("begin" in p)):
		print(">>",cb_name,"    : Please connect with your friends system.. He needs your help")
		pyttsx3.speak("	Please connect with your friends system.. He needs your help")
		os.system("mstsc")