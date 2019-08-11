# coding = utf-8
# using namespace std
from datacore import core
from os import system
from datacore import argv_system
from sys import argv
from datacore import annimations_cgi
from datacore.backup_maker import DatabaseToBackup
from sys_screens.Repositories import MainScreen as repositories_screen
from sys_screens.Installer import MainScreen as installer_screen
from sys_screens.Gitter import MainScreen as gitter_screen
from sys_screens.Exporter import MainExporterScreen
from sys_screens.DebPacks import DebPacksScreen


about = """"""


if len(argv) > 1:
    argv_system.ArgvData()
    exit(0)

database = core.Database()
Installer = core.Installer()
Gitter = core.Gitter()
DebPacks = core.DebianPacks()

__doc__ = """
FastInstallerLinux: This is a fast, easy and simple database to save your favorites tools, github repositories,
install and clone it.

At the first screen you have four options: 
1- Installer : It goes to the Installer options.
2- Gitter: It goes to git database options.
3- Help: show this helpful message.
4- Exit: Exit system.

In the Installer options you have seven options:
1 - Install Package: it installs a package from database. THIS PACKAGE NEEDS TO BE IN THE DATABASE!
2 - Install All Packages: it install all packages from database.
3 - Add package: It adds a package to database
    You have to type what's the package name, and him command to install.
4 - Delete package: It delete a package in database
5 - Alter Package: It alter an package in database.
    You have to type what's the package, using him name, the camp and the new value to the camp.
6 - See all the packages: It show's you all the packages and it commands in database.
7 - Exit to the first screen.

In the Gitter options you have also 7 options:
1 - Configure repository: Configure a repository in the database.
2 - Configure all the repositories in the database. 
"""


annimations_cgi.GenericSystem.start_all_system()
back = DatabaseToBackup()
logo = """
 _____         _   ___           _        _ _           _     _             
|  ___|_ _ ___| |_|_ _|_ __  ___| |_ __ _| | | ___ _ __| |   (_)_ __  _   _ _    _
| |_ / _` / __| __|| || '_ \/ __| __/ _` | | |/ _ \ '__| |   | | '_ \| | | |\ \/ /
|  _| (_| \__ \ |_ | || | | \__ \ || (_| | | |  __/ |  | |___| | | | | |_| | >  <
|_|  \__,_|___/\__|___|_| |_|___/\__\__,_|_|_|\___|_|  |_____|_|_| |_|\__,_|/_/\_\\
    
"""

while True:
    while True:  # main menu
        system("clear")
        print(logo)
        print("""
[1] Installer
[2] Gitter
[3] Help
[4] Repositer
[5] Exporter
[6] Debian Packages
[7] About
[8] Format Database
[9] Exit
        """)
        op1 = int(input(">>> "))
        r = int(input("Confirm? [1]y/[2]n \n>>> "))
        if r == 1: break
    if op1 == 1:
        try:
            installer = installer_screen()
        except installer_screen.EndUsage: continue
    elif op1 == 2:
        try:
            gitter = gitter_screen()
        except gitter_screen.EndUsage: continue
    elif op1 == 3:
        print(__doc__)
        input("<<press any button to return to menu>>")
        continue
    elif op1 == 9:
        back.update_backup()
        exit(0)
    elif op1 == 4:
        try:
            respositories = repositories_screen()
        except repositories_screen.EndUsage:
            continue
    elif op1 == 5:
        try: MainExporterScreen().main_screen_exporter()
        except MainExporterScreen.EndOfUsage: continue
    elif op1 == 6:
        try: DebPacksScreen().main_screen()
        except DebPacksScreen.EndUsage: continue
    elif op1 == 7:
        print(__doc__)
        input("<<press any button to return ")
        continue
    elif op1 == 8:
        print("""""")  # warning message
        t = int(input(">>> "))
        if t == 1: core.Database().format_database()
        else: continue
    else:
        print("That's not a valid option!\nTry again")
        input("<<press any button to return>>")
        continue












































