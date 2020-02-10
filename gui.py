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
<----------------------------------------->"""+G+"""
           Termux GUI Installer"""+Y+"""
<----------------------------------------->"""+R+"""
        == """+CY+"""By Deadpool2000 """+R+"""==
    
""")
    try:
        urllib.request.urlopen("http://google.com")
        print(Y+"\n==>"+CY+" Installing repositories............"+W)
        os.system("apt install x11-repo")
        os.system("apt install unstable-repo")
        print(Y+"\n==>"+CY+" Installing XFCE Environment..........."+W)
        os.system("apt install xfce xfce4-terminal tigervnc -y")
        print(R+"""\n
----------------------------------------------"""+Y+"""
Installation complete!\n"""+CY+"""
Now follow these steps to run Termux-GUI -->

1) Run 'vncserver' command
2) Add new password for vnc
3) You will get IP Address like this -

   localhost:<session_number>
   e.g. localhost:1
3) After above step,type following command -

    DISPLAY=:1 startxfce4 &

Here,1 is a session number.
4) Install VNC Viewer on your phone
5) Add IP Address which you got at Step 3
    e.g. localhost:1
6) Add name
7) Click on Connect
8) Enter VNC password which you used at Step 2

"""+G+"""
** Important Note - If you want to exit from GUI,type following command before exit -
                    -> vncserver -kill :<session_number>
                    e.g. vncserver -kill :1
""")
    except:
        print(Y+"""
--------------------------------------------------------------"""+R+"""
Failed to connect to internet! Check your internet connection :( """+Y+"""
--------------------------------------------------------------""")
except KeyboardInterrupt:
    print("Interrupted ! Good Bye! :) ")

