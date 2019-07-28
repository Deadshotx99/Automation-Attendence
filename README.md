# Automation-Attendence
For > G I T A M  S t u d e n t s   O n l y

Hello fellow G I T A M I T E S 

Im one of you guys who always thought that there should be an alternate way to get Attendence ,omiting the boring procedure of 
logging in to the your G L E A R N ACCOUNTS 

So by using Selenium-Automation + Python3_Script I Created this .. 

From now on to look cool you can just run this python file in your Terminal or Command_line to Get your

# T O T A L A T T E N D E N C E as well as  A T T E N D E N C E BY S U B J E C T 


# INSTALLATION PROCEDURE

# NOTE ~ MAKE SURE THAT YOU HAVE PYTHON_3 OR HIGHER

# 1.Download or clone the REPO

>> In TERMINAL OR CMD
# $ git clone https://github.com/Deadshotx99/Automation-Attendence
# 2.Copy the files into a folder of your choice 

# CREATING VIRTUAL ENVIRONMENT

>> Change the directory to the directory which contains the REPO files using TERMINAL OR CMD
  ( Type this command in terminal or CMD )
  
# FOR MAC AND LINUX (MAY ASLO WORK WITH WINDOWS IF NOT THEN >>> )

# 3. $ python3 -m venv ./venv
>> you will now see a folder named venv containing directorys like lib , bin , include
# ACTIVATING THE VIRTUAL ENVIRONMENT 
{ .  Type this Command in terminal  or CMD ) 
# $ source ./venv/bin/activate


# >> For deactivation $ deactivate


# CREATING VIRTUAL ENVIRONMENT FOR WINDOWS 

# First - $ pip install virtualenv
# second - $ cd "to_the_directory_containing_files"
# third - $ virtualenv venv
# fourth - $ venv\scripts\activate (( ACTIVATION )) 

>>> TO DEACTIVATE ... In the same Directory enter $ deactivate

# If you have any further queries regarding the VIRTUAL ENVIRONMENT VISIT 
 >> https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/
 
# INSTALLING THE PACKAGES
# 4.Now from the files copy the requirements.txt into the lib\python3.7\site-packages and paste it there
# 5.Make sure that you activated the VIRTUAL_ENVIRONMENT which can be verified by
>> normal terminal >> (base)username $ >> virtual_Environment terminal >> (venv)username $
# 6.Now change the directory from 
  1. venv $cd lib
  2. lib  $cd python3.7
  3. python3.7 $cd site-packages 
# 7.Type the following command 

# $ pip install -r requirements.txt 

( This should install the required packages )

# Checking the version of your chromeBrowser
1.open chrome > click on three vertical dots > click help > About GoogleChrome
# If chromeBrowser verision is >> 75.xxx << 
# THEN COPY AND PASTE THE PROVIDED CHROMEBROWSER FILE INTO >> bin << 


# if the version is not >> 75.xxx << 
#  visit this page  -- http://chromedriver.chromium.org/downloads
# NOTE -- DOWNLOAD ONLY THE VERSION WHICH CORRESPONDS TO THE VERION OF "YOUR CHROME BROWSER" 

# >>>>> MOST IMPORTANT <<<< 

# 8.COPY the file "logindetails.txt" and PASTE it INSIDE THE "VENV" DIRECTORY
# NOW OPEN FILE << 
# 1. Delete the content that file has Initially 
>> #userid
>> #password 

# 2. Enter the USERID(REGISTRATION NUMBER) AND PASSWORD in NEWLINES
# TYPE AS FOLLOWS 
>> INSIDE FILE << 

121992391230     >>> Example_id
password@123     >>> Example_password

# SAVE AND CLOSE 



# EXECUTION 

# Now in order to execute 

# 0.Change the directory to  the REPO Directory ( USING $cd )

# 1.activate the Virtual Environment

>> Enter the command

# 2. $ python automate.py

# NOTE:- MAKE SURE THAT YOU ARE IN THE VIRTUAL ENVIRONMENT SO THAT THE PACKAGES ARE ACCESSED FOR THE PROGRAM TO RUN
# NOTE:- YOU CAN ALSO RUN THIS CODE USING AN IDE 
# >>> PROGRAM WILL BE EXECUTED <<<<








