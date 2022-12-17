This is a python script to periodically change the desktop background on Ubuntu 20.04 LTS.

Dependencies:
  Python3
  
 Installation:
 -Create a folder named "Wallpaper" in the pictures directory and add at least one picture to it.
 -Move the python script to desired location which will be referred as [scriptPath]
 
 Add a new startup program with the following command
 "nohup python3 [scriptPath]/bg.py &"
 
 To change the interval, edit the script. The time is presented in seconds.
