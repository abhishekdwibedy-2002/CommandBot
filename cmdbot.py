import os
import pyttsx3
import pyfiglet

y="All Executabe programs are listed below\n\t---------Basic Command---------\n\n$time \n$date\n\n\t---------Apps---------\n\n$Notepad\n$Google Chrome\n$VLC\n$Telegram\n$Virtual Box\n$Discord\n$Window Media Player\n$Visual Studio Codes\n$File Explorer\n$Camera\n\n\t---------System---------\n\n$Open Terminal\n$Open Control Panel\n$PC Information\n$Windows Information\n\n\t---------Settings---------\n\n#Action Center\n#Troubleshooting\n#Event Viewer\n#Computer Management\n#Uninstall Programs\n#Internet Properties\n#IP Address\n#System Report\n#Control Monitor\n#Task Manager\n\n\t----------Other Features----------\n\n-- Browse Any Website by giving the url name\n-- Send Message through Whatsapp by giving the number to whome u want to send Message"

#heading
titleheading = pyfiglet.figlet_format("\n\t--Abhishek's Assistant-- ", font = "epic")
print(titleheading)
print("\n\t>>> : An OS Based program into Menu Driven using Python : <<<")
s2 = pyfiglet.figlet_format("                       WELCOME TO ASSISTANT", font = "digital" ) 
print(s2)

#voice
print("Enter Your Name : ",end='')
name=input()
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("welcome to my tool, which is an OS Based program into Menu Driven using Python")
engine.say( " hello {} I'm your Assistant!!! How can i help you ?".format(name) )
engine.runAndWait()  

#Tnformation 
print("Info :-- If you want to know all executable programms type 'help' command ")


while True:
    print()
    print("What You Want me to Do ? :",end='')
    p=input()

#basiccommand
    if (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("time" in p)) :
            os.system("time")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("date" in p)) :
            os.system("date")


#apps
    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("notepad" in p) or ("editor" in p) or ("text editor" in p)) :
            pyttsx3.speak("Please Wait Your Notepad Is Opening")
            os.system("notepad")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("chrome" in p) or ("browser" in p) or ("google chrome" in p) or ("google" in p) or ("chrome browser" in p)) :
            pyttsx3.speak("Please wait your Google Chrome Is Opening")
            os.system("chrome")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p) or ("play" in p)) and (("vlc" in p) or ("VLC" in p) or ("music" in p) or ("video" in p) or ("media player" in p) or ("video player" in p)) :
            pyttsx3.speak("Please Wait your VLC Player is opening")
            os.system("vlc")
        
    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("telegram" in p) or ("Telegram" in p)) :
            pyttsx3.speak("Please Wait your Telegram is opening")
            os.system("telegram")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("virtualbox" in p) or ("oracle" in p) or ("vm" in p)) :
            pyttsx3.speak("Please Wait your virtual box is opening")
            os.system("virtual box")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("discord" in p) or ("Discord" in p)) :
            pyttsx3.speak("Please Wait your discord is opening")
            os.system("discord")

    elif(("run" in p) or ("play" in p) or ("open" in p) or ("launch" in p) or ("execute" in p)) and (("media" in p) or ("window media player" in p) or ("musics" in p) or ("wm player" in p) or ("music player" in p)):
            pyttsx3.speak("please wait your windows media player is opening")
            os.system("wmplayer")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("code" in p) or ("vscode" in p) or ("visualstudiocode" in p)) :
            pyttsx3.speak("Please Wait your VS code is opening")
            os.system("code")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("explorer" in p) or ("file" in p) or ("file manager" in p)) :
            pyttsx3.speak("Please Wait your file explorer is opening")
            os.system("explorer")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show") in p) and ("camera" in p) :
            pyttsx3.speak("please wait your camera is opening")
            os.system("Start microsoft.windows.camera:")


#system
    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("command prompt" in p) or ("prompt" in p) or ("terminal" in p) or ("console" in p)) :
            pyttsx3.speak("please wait your terminal or command prompt or console is opening")
            os.system("Start")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("control panel" in p) or ("control" in p)) :
            pyttsx3.speak("please wait your control panel is opening")
            os.system("control panel")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("system information" in p) or ("system" in p) or ("pc info" in p)) :
            pyttsx3.speak("please wait your PC Information is opening")
            os.system("msinfo32") 

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("windows" in p) or ("windows details" in p) or ("windows info" in p)) :
            pyttsx3.speak("please wait your windows Information is opening")
            os.system("control.exe system")

#tools   
    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("action" in p) or ("action center" in p)) :
            pyttsx3.speak("please wait your Action Center is opening")
            os.system("wscui.cpl")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("troubleshoot" in p) or ("troubleshooting" in p)) :
            pyttsx3.speak("please wait your Trobuleshooting is opening")
            os.system("control.exe /name Microsoft.Troubleshooting")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("event viewer" in p) or ("event" in p)) :
            pyttsx3.speak("please wait your Event Viewer is opening")
            os.system("eventvwr.exe")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("computer management" in p) or ("pc management" in p)) :
            pyttsx3.speak("please wait your Computer Mangement is opening")
            os.system("compmgmt.ms")

    elif (("delete" in p) or ("uninstall" in p) or ("uninstall programs" in p)) :
            os.system("appwiz.cpl")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("internet" in p) or ("internet properties" in p) or ("internet details" in p)) :
            pyttsx3.speak("please wait your Internet Information is opening")
            os.system("inetcpl.cpl")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("ip" in p) or ("ip address" in p)) :
            os.system("ipconfig.exe")

    elif (("run" in p) or ("open" in p) or ("execute" in p)or ("show" in p)) and (("performance" in p) or ("system report" in p)) :
            pyttsx3.speak("please wait your System Report is opening")
            os.system("perfmon.exe")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("resource" in p) or ("control monitor" in p)) :
            os.system("resmon.exe")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("taskmanager" in p) or ("task" in p) or ("task manager" in p)):
            pyttsx3.speak("please wait your Task Manager is opening")
            os.system("taskmgr.exe /7")

#specialfeatures
    elif (("search" in p) or ("browse" in p) or ("visit" in p)) and (("website" in p)) :
            while True:
                    print()
                    print("Enter the Web App name :-",end='')
                    url=input()
                    os.system("Start /max chrome.exe http://{}.com".format(url))

    elif (("send" in p) or ("browse" in p) or ("visit" in p)) and (("message" in p) or ("messages" in p)) :
            while True:
                    print()
                    print("Enter the mobile number whom you want to send the message:  ",end='')
                    phone=input()
                    os.system("Start /max chrome.exe http://web.whatsapp.com/send?phone=91{}".format(phone))

#thanku
    elif (("thank you" in p) or ("thanku" in p) or ("thank u" in p) or ("thanks" in p)) :
            print("Always Welcome !!!  It's My Job...")
            pyttsx3.speak("Always Welcome !!!  It's My Job... ")
            print("Want something else from me to do ?\n\t + Tell Me[y/n]:-  ",end='')
            pyttsx3.speak("want something else from me to do.")

            inp=input()
            if inp=="Y" or inp=="y" :
                    continue
            elif inp=="N" or inp=="n" :
                    break
            else :
                    pyttsx3.speak("Okay, i'm assuming you want me to do more.")
                    print("\n\t\t > Okay, i'm assuming you want me to do more.")

#helpcmd
    elif (("help" in p) or ("HELP" in p)) :
            print(y)

#Stop or exit of Cmd bot
    elif (("exit" in p) or ("stop" in p) or ("quit" in p) or ("close" in p) or ("terminate" in p) or ("cancel" in p)) :
            break
    else :
            pyttsx3.speak("Sorry Not Available")
            print("Doesn't Support !!! Try Something Else or Type Help")
	
print("\t\t\n  Thank You :)")
pyttsx3.speak("Thank you for using it !!!  Have a good day...")