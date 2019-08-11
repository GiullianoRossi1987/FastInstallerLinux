# coding = utf-8
# using namespace std
from datacore.core import Installer
from os import system
from time import sleep
from datacore.annimations_cgi import GenericSystem
from datacore.beauty import PackagesBeauty
from datacore.backup_maker import DatabaseToBackup
from datacore.color_sys import LoadInColor


class MainScreen(object):

    installer_obj = Installer()
    logo = """
 ___           _        _ _           
|_ _|_ __  ___| |_ __ _| | | ___ _ __ 
 | || '_ \/ __| __/ _` | | |/ _ \ '__|
 | || | | \__ \ || (_| | | |  __/ |   
|___|_| |_|___/\__\__,_|_|_|\___|_|   

    """

    class EndUsage(BaseException):
        args: object = "Ended Use!"

    def __init__(self):
        GenericSystem.start_installer_system()
        color_obj = LoadInColor()
        while True:
            system("clear")
            while True:
                print(color_obj.set_with_color(self.logo, "red", True))
                print("""
[1] Install Package
[2] Install All Packages
[3] Add Package
[4] Delete Package
[5] Alter Package
[6] Show All Packages
[7] Help
[8] Exit
                """)
                opc = int(input(">>> "))
                r = int(input("Confirm?\n[1]Yes\n[2]No\n>>> "))
                if r == 1: break
            del r
            if opc == 1:
                c = True
                while True:
                    pack = str(input("Package name to Install: "))
                    r = int(input("Confirm?\n[1]Yes\n[2]No\n[3]Cancel.\n>>> "))
                    if r == 3:
                        c = False
                        break
                    if r == 1: break
                if c:
                    self.installer_obj.install_package(pack)
                    del pack
                    sleep(2)
                continue
            elif opc == 2:
                self.installer_obj.install_package()
                sleep(2)
                continue
            elif opc == 3:
                c = True
                while True:
                    pack_name = str(input("Package Name to System: "))
                    command = str(input("Command to Install: "))
                    r = int(input("Confirm?\n[1]Yes\n[2]No\n[3]Cancel.\n>>> "))
                    if r == 3:
                        c = False
                        break
                    if r == 1: break
                if c:
                    self.installer_obj.add_package([pack_name, command])
                    del pack_name, command
                    sleep(2)
                continue
            elif opc == 4:
                c = True
                while True:
                    pack = str(input("Package to Remove from Database: "))
                    r = int(input("Confirm?\n[1]Yes\n[2]No\n[3]Cancel.\n>>> "))
                    if r == 3:
                        c = False
                        break
                    if r == 1: break
                if c:
                    self.installer_obj.del_package(pack)
                    del pack
                    sleep(2)
                continue
            elif opc == 5:
                c = True
                while True:
                    pack = str(input("Package to Alter: "))
                    camp = str(input("Data to Alter: "))
                    vl = str(input("New data value: "))
                    r = int(input("Confirm?\n[1]Yes\n[2]No\n[3]Cancel.\n>>> "))
                    if r == 3:
                        c = False
                        break
                    if r == 1: break
                if c:
                    self.installer_obj.alt_packages(pack, camp, vl)
                    del pack, camp, vl, r
                    sleep(2)
                continue
            elif opc == 6:
                print(PackagesBeauty.shows_all_data(self.installer_obj.query_package()))
                input("<<press any button to return>>")
                continue
            elif opc == 7:
                print(self.installer_obj.__doc__)
                input("<<press any button to return>>")
                continue
            elif opc == 8:
                backuper = DatabaseToBackup()
                backuper.update_backup()
                raise self.EndUsage()
            else:
                input("That's not a valid option!\nTry Again!\n<<press any button to try again>>")
                continue


















