# Termux-GUI (v1.2)
Use termux in GUI mode using XFCE and MATE environment

### XFCE running on Termux -
![Screenshot_20200211-114119](https://user-images.githubusercontent.com/32305505/75316470-74b5ee80-588b-11ea-8454-4fd4c0aceba7.png)

### MATE running on Termux -

![Screenshot_20211011-103504](https://user-images.githubusercontent.com/32305505/136737365-5d7d55d0-9d1e-4e6e-8003-aa116222ec45.png)


A simple python script to install xfce and mate environment in Termux

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
   
d) After above step, to start GUI, use following command -

   A] For XFCE environment -

      DISPLAY=:1 startxfce4 &

   B] For MATE environment -

      DISPLAY=:1 mate-session &

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


# Donate


### Don't buy me a coffee. I HATE COFFEE!


### Just show your support here -


**Bitcoin - 34TbAyKNqpEEA9123FZApkkKZ4AvWjbkom**

**Ethereum - 0x8Efc824b3b3702c3b2421cAE6c47912262185042**

**Litecoin -  M8FodbAuYQsWXb5VXTSx6F3VCbtcXk7skz**

**Ripple(XRP) -  Address [rw2ciyaNshpHe7bCHo4bRWq6pqqynnWKQg]  / Tag [1493819154]**
