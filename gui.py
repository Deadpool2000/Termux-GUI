import os
import urllib.request

try:
    R='\033[91m' #Red
    Y='\033[93m' #Yellow
    G='\033[92m' #Green
    CY='\033[96m' #Cyan
    W='\033[97m' #White
    B='\033[95m' #Blue

    print(Y+"""
<----------------------------------------------->"""+G+"""
              Termux GUI Installer"""+Y+"""
<----------------------------------------------->"""+R+"""
              == """+CY+"""By Deadpool2000 """+R+"""==
    
""")
    try:
        urllib.request.urlopen("http://google.com")
        print(Y+"\n==>"+CY+" Installing repositories............\n"+W)
        os.system("pkg install x11-repo")
        os.system("pkg install unstable-repo")
        os.system("pkg install root-repo")
        print(Y+"\n==>"+CY+" Installing XFCE Environment...........\n"+W)
        os.system("pkg install xfce xfce4-terminal tigervnc -y")
        print(R+"""\n
----------------------------------------------\n"""+R+"""
      == """+Y+"""Installation complete! """+R+"""=="""+CY+"""\n
Now follow these steps to run Termux-GUI -->

"""+R+"""1)"""+Y+""" Run """+G+"""'vncserver'"""+Y+""" command
"""+R+"""2)"""+Y+""" Add new password for vnc
"""+R+"""3)"""+Y+""" You will get IP Address like this -"""+G+"""

   localhost:<session_number>"""+Y+"""
   e.g. localhost:1
   
"""+R+"""3)"""+Y+""" After above step,type following command -"""+G+"""

    DISPLAY=:1 startxfce4 &"""+Y+"""

Here,1 is a session number.
"""+R+"""4)"""+Y+""" Install VNC Viewer on your phone
"""+R+"""5)"""+Y+""" Add IP Address which you got at Step 3"""+G+"""

    e.g. localhost:1
    
"""+R+"""6)"""+Y+""" Add name
"""+R+"""7)"""+Y+""" Click on Connect
"""+R+"""8)"""+Y+""" Enter VNC password which you used at Step 2

"""+G+"""
** Important Note - If you want to exit from GUI,type following command before exit -

-> vncserver -kill :<session_number>

e.g. vncserver -kill :1
"""+W)
    except:
        print(Y+"""
<------------------------------>"""+R+"""
Failed to connect to internet!\nCheck your internet connection :( """+Y+"""
<-------------------------------->\n"""+W)
except KeyboardInterrupt:
    print("Interrupted ! Good Bye! :) ")

