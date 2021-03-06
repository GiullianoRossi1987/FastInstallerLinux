# coding = utf-8
# using namespace std
from datacore.core import Gitter
from time import sleep
from typing import Type
from os import system
from datacore.annimations_cgi import GenericSystem
from datacore.beauty import GitterBeauty
from datacore.backup_maker import DatabaseToBackup
from datacore.color_sys import LoadInColor


class MainScreen(object):

    gitter_obj = Gitter
    logo = """
  ____ _ _   _            
 / ___(_) |_| |_ ___ _ __ 
| |  _| | __| __/ _ \ '__|
| |_| | | |_| ||  __/ |   
 \____|_|\__|\__\___|_|   

    """

    class EndUsage(BaseException):
        args: object = "End of use!"

    def __init__(self):
        self.gitter_obj.__init__(Type[Gitter])
        GenericSystem.start_gitter_system()
        color_loader = LoadInColor()
        while True:
            system("clear")
            while True:
                print(color_loader.set_with_color(self.logo, "green", True))
                print("""
[1] Configure Repository
[2] Configure All Repositories
[3] Add Repository
[4] Delete Repository
[5] Alter a Repository Data
[6] Show All Repositories
[7] Help
[8] Exit
                """)
                op1 = int(input(">>> "))
                r = int(input("Confirm?\n[1]Yes.\n[2]No.\n>>> "))
                if r == 1: break
            del r
            if op1 == 1:
                c = True
                while True:
                    repo = str(input("Repository Name: "))
                    directoy = str(input("Directory to clone '-pwd' to the actual dir: "))
                    r = int(input("Confirm?\n[1]Yes.\n[2]No\n[3]Cancel\n>>> "))
                    if r == 3:
                        c = False
                        break
                    elif r == 1: break
                if c:
                    self.gitter_obj.config_repo(repo, directoy)
                    del directoy, repo, r
                    sleep(2)
                continue
            elif op1 == 2:
                c = True
                while True:
                    directoy = str(input("Directory to clone '-pwd' to the actual dir: "))
                    r = int(input("Confirm?\n[1]Yes.\n[2]No.\n[3]Cancel\n>>> "))
                    if r == 3:
                        c = False
                        break
                    if r == 1: break
                if c:
                    self.gitter_obj.config_repo(dir_to_clone=directoy)
                    del directoy, r
                    sleep(2)
                continue
            elif op1 == 3:
                c = True
                while True:
                    host = str(input("Repository Host: "))
                    name = str(input("Repo Name: "))
                    remote = str(input("Remote Name: "))
                    email = str(input("User Email: "))
                    name_user = str(input("User Name: "))
                    r = int(input("Confirm?\n[1]Yes\n[2]No\n[3]Cancel\n>>> "))
                    if r == 3:
                        c = False
                        break
                    if r == 1: break
                if c:
                    ls_data = [
                        name,
                        host,
                        remote,
                        email,
                        name_user
                    ]
                    self.gitter_obj.add_repo(ls_data)
                    sleep(2)
                    del ls_data, host, name, name_user, remote, email
                continue
            elif op1 == 4:
                c = True
                while True:
                    repo = str(input("Repository name: "))
                    r = int(input("Confirm?\n[1]Yes\n[2]No\n[3]Cancel\n>>> "))
                    if r == 3:
                        c = False
                        break
                    if r == 1: break
                if c:
                    self.gitter_obj.del_repo(repo)
                    del repo, r
                    sleep(2)
                continue
            elif op1 == 5:
                c = True
                while True:
                    repo = str(input("Repository to alter: "))
                    camp = str(input("Data to alter: "))
                    vl = str(input("New data value: "))
                    r = int(input("Confirm\n[1]Yes\n[2]No\n[3]Cancel\n>>> "))
                    if r == 3:
                        c = False
                        break
                    if r == 1: break
                if c:
                    self.gitter_obj.alt_repo(repo, camp, vl)
                    del camp, vl, repo
                    sleep(2)
                continue
            elif op1 == 6:
                rs = GitterBeauty.shows_all_data(self.gitter_obj.query_repo())
                if len(rs) <= 0:
                    print("There's no repositories here!")
                else:
                    print(rs)
                input("<<press any button to return>>")
                continue
            elif op1 == 7:
                print(self.gitter_obj.__doc__)
                input("<<press any button to return>>")
                continue
            elif op1 == 8:
                backuper = DatabaseToBackup()
                backuper.update_backup()
                raise self.EndUsage()
            else:
                print("Invalid Option!")
                input("Try Again!\n<<press any button to try again>>")
                continue



























