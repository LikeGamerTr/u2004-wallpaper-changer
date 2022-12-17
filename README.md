This is a python script to periodically change the desktop background on Ubuntu 20.04 LTS.

## Dependencies:

 + Python3
  
  
## Installation:
 
 1. Create a folder named "Wallpaper" in the pictures directory and add at least one picture to it.
 2. Move the python script to desired location which will be referred as [scriptPath]
 3. Add a new startup program with the following command
 
 ```
 nohup python3 [scriptPath]/bg.py &
 ```

 
 4. To change the interval, edit the script. The time is presented in seconds.
 
When the system is restarted, the script will launch without a terminal interface.
