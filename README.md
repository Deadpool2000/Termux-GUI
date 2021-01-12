# Termux-GUI
Use termux in GUI mode using XFCE environment

#### XFCE running on Termux -
![Screenshot_20200211-114119](https://user-images.githubusercontent.com/32305505/75316470-74b5ee80-588b-11ea-8454-4fd4c0aceba7.png)

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

## For more information,visit this link - [How to install GUI in Termux](https://mrhacker7.blogspot.com/2020/10/install-graphical-user-interface-gui-in.html?m=1)
## If you have any issue regarding this,Report [Here](https://github.com/Deadpool2000/Termux-GUI/issues)


# Show your support

Don't buy me a coffee.I HATE COFFEE!

Just show your support here -

[![Bitcoin Donate Button](https://deadpool2000.github.io/bitcoin-395-920580(1).png)](https://deadpool2000.github.io/btc.html)

[![Ethereum Donate Button](https://deadpool2000.github.io/New%20Project(1).png)](https://deadpool2000.github.io/eth.html)
