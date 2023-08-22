#Made and optimized by MrJuly for Dying Light 1 with a better documentation and much more simple and quick script

# Description
This is a python script which automatically extracts every .csb in the Data folder found in DyingLight/DW when browsing local files of the game.

# Apps Required:
QuickBMS can be found here: https://drive.google.com/file/d/1bpT4Slq6szFzzx6wTU2RWtJH7RnCCjjj/view?usp=sharing
Python can be found here: https://www.python.org/downloads/ (I originally made this script with Python v3.11.4 but it may be different over time as Python continues to update)
CMD can be found by typing "command prompt" in your system search bar 
(In case you don't see the CMD please check the FAQ)
Notepad++ can be found here: https://notepad-plus-plus.org/downloads/

# How to setup
1. Change the contents of the settings.ini file in this folder
```
quickbmsdir = Directory with QuickBMS
bmsscript = No need to update this
quickbmsexe = No need to update this
extractdir = Directory from which the .csb files will be extracted
outputdir = Output folder in which every .csb file will extract
```

2. Click save and close Notepad++

#PIP Installs and How to install them

Step 1.

To run this script you need to have "pathlib" & "configparser"

First open up CMD or the Official Terminal app from Microsoft Store, then do cd {The Location Of Your Folder, eg: Desktop}

With that done then do cd {The Name Of Your Folder Goes Here}

And step 1. is done!

Step 2.

To install pathlib please execute "pip install pathlib" in the CMD or the Official Terminal app from Microsoft Store, wait until it downloads and continue to the next step

Step 3.

To install configparser please execute "pip install configparser" in the CMD or the Official Terminal app from Microsoft Store, wait until it downloads and you are basically done!

#Final Step

Now that everything is setup run the python script in the CMD or the Official Terminal app from Microsoft Store using "python main.py" and you should see the output folder full of the extracted files which your requested
in the specified folder location!


#FAQ

1. I can't see CMD, how do I continue?

If you can't find CMD or the Command Prompt then please download the "Terminal App" from the Microsoft Store which can be found here: https://www.microsoft.com/store/productid/9N0DX20HK701?ocid=pdpshare

2. Why do I need QuickBMS?

QuickBMS will need to be used for reimporting the new and fresh sound data you want to add to the game, without it you would not be able to make the sound file work in game. I will provide a quick tutorial on how to use it:
https://youtu.be/Oaxiu_ejY1E
