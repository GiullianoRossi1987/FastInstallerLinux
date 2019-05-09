# FastInstallerLinux
### A fast configurable installer tools and github repositories on linux

This system makes all your need easy then enough, you can add your tools to download using the linux terminal.
Can add yours GitHub Repositories, alter data from your tools and repository. It's for developers,
but can also used for simple linux users. The only thing recommended for both users, is a little experience with 
the linux terminal, and CLI interface. But it's very easy and useful for all linux users.  

# System requirements  
- ####Snap Installed:  
    It can be installed going to terminal and typing:   
        ``
        sudo apt-get install snapd
        ``  
- ####Git package installed:
    It also can be installed going to terminal and typing:  
        ``
        sudo apt-get install git
        ``  
- ####Python:
    The version used in the system is **__3.6.5__**, but for older version like **__2.7.2__**,   
    we recommend you to install the sqlite3 library if it is not in your python libs.  
    But it can be installed using  
    For Python 3.*:  
    ``
    sudo apt-get install python3-sqlite3
    ``  
    For Python 2.*:  
    ``
    sudo apt-get install python-sqlite3
    ``  
- ####A Linux System:  
    The linux family used for the system is the Debian, but maybe for others versions of the system,
    RedHat and Arch Linux can be supported. But for now, use the Debian based linux.


#Technical Data
The system was wrote in Python language, and the database use sql (Sqlite3 for be more specific).  
The datacore directory have the most important and used part of the system For see more just see the documentation 
in the python file core.py

#SystemTips
1. ####The system have a configure shell script  
    This shell script have all the needed configurations.  
    Also it installs all the requirements, and  it installs the library sqlite3 for python2.* and
    python3.*
    

 

