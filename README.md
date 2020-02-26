# Termux-GUI
Use termux in GUI mode using XFCE environment

#### XFCE running on Termux -
![screenshot](https://user-images.githubusercontent.com/32305505/74161451-f92a2f80-4c44-11ea-8a84-bd1e9e406b42.png)

A simple python script to install xfce environment in Termux

## Installation
1) apt install python3
2) git clone https://github.com/Deadpool2000/Termux-GUI.git
3) cd Termux-GUI
4) pip3 install -r requirements.txt
5) python3 gui.py

## Download
VNC Viewer - [Download](https://play.google.com/store/apps/details?id=com.realvnc.viewer.android&hl=en_IN)

## How to start Termux-GUI

a) Run 'vncserver' command

b) Add new password for vnc

c) You will get IP Address like this -

      localhost:<session_number>

      e.g. localhost:1
   
d) After above step,type following command -

      DISPLAY=:1 startxfce4 &

   Here,1 is a session number.
      
e) Install VNC Viewer on your phone

f) Add IP Address which you got at Step 3

      e.g. localhost:1
    
g) Add name

h) Click on Connect

i) Enter VNC password which you used at Step 2

## Exit GUI

Enter following command before exit -

            vncserver -kill :<session_number>
            e.g. vncserver -kill :1
            
## If you have any issue regarding this,Report [Here](https://github.com/Deadpool2000/Termux-GUI/issues)
