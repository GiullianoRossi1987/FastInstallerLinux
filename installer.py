# coding = utf-8
# using namespace std
from datacore import core
from time import sleep
from os import system
from datacore import argv_system
from sys import argv
from datacore import annimations_cgi
from datacore.backup_maker import DatabaseToBackup
from datacore.beauty import PackagesBeauty
from datacore.beauty import GitterBeauty
from datacore.core import RepositorySystem
from datacore.beauty import RepoBeuaty


if len(argv) > 1:
    argv_system.ArgvData()
    exit(0)

database = core.Database()
Installer = core.Installer()
Gitter = core.Gitter()

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

while True:
    while True:  # main menu
        system("clear")
        system("figlet Installer")
        print("""
[1]Installer
[2] Gitter
[3] Help
[4] Exit
[5] Repositer                             
        """)
        op1 = int(input(">>> "))
        r = int(input("Confirm? [1]y/[2]n \n>>> "))
        if r == 1: break
    if op1 == 1:
        while True:
            while True:
                print("""
[1] Install package.
[2] Install all packages.
[3] Add package to database.
[4] Delete a package.
[5] Alter package.
[6] See all packages.
[7] Cancel.
                """)
                op2 = int(input(">>> "))
                r1 = int(input("Confirm? [1]y/[2]n\n>>> "))
                if r1 == 1: break
            if op2 == 1:
                cn = True
                while True:
                    pack = str(input("Type the package name\n>>> "))
                    r1 = int(input("Confirm? [1]y/[2]n/[3]cancel.\n>>> "))
                    if r1 == 3:
                        cn = False
                        break
                    elif r1 == 1: break
                if cn:
                    Installer.install_package(pack)
                    print(pack+" installed.\nReturning to menu...")
                    sleep(2)
                del pack
                continue
            elif op2 == 2:
                r1 = int(input("[1]Continue. [2]Cancel"))
                if r1 == 1:
                    Installer.install_package()
                    print("All packages installed.\nReturning to menu...")
                    sleep(2)
                continue
            elif op2 == 3:
                cn = True
                while True:
                    nm_package = str(input("Package Name: "))
                    command_package = str(input("Linux command: "))
                    r1 = int(input("Confirm? [1]Y/[2]N/[3]Cancel.\n>>> "))
                    if r1 == 3:
                        cn = False
                        break
                    elif r1 == 1: break
                if cn:
                    Installer.add_package([nm_package, command_package])
                    print("Added to database successfully\nReturning to menu...")
                    sleep(2)
                del nm_package, command_package
                continue
            elif op2 == 4:
                cn = True
                while True:
                    nm_pack = str(input("Package name: "))
                    r1 = int(input("Confirm? [1]y/[2]n/[3]Cancel.\n>>> "))
                    if r1 == 3:
                        cn = False
                        break
                    elif r1 == 1: break
                if cn:
                    Installer.del_package(nm_pack)
                    print("Removed from database sucessfully!\nReturning to menu ...")
                    sleep(2)
                del nm_pack
                continue
            elif op2 == 5:
                cn = True
                while True:
                    nm_pack = str(input("Package name to alter: "))
                    camp = str(input("Camp to alter: "))
                    value = input("Value to alter in camp: ")
                    r1 = int(input("Confirm? [1]y/[2]n/[3]Cancel.\n>>> "))
                    if r1 == 3:
                        cn = False
                        break
                    elif r1 == 1: break
                if cn:
                    Installer.alt_packages(nm_pack, camp, value)
                    print("Updated data sucessfully!\nReturning to menu ... ")
                    sleep(2)
                del nm_pack, camp, value
                continue
            elif op2 == 6:
                data = Installer.query_package()
                rs = PackagesBeauty.shows_all_data(data)
                if len(rs) <= 0:
                    print("There's no packages in the database!")
                else:
                    print(rs)
                input("<<press any button to return to menu>>")
                continue
            elif op2 == 7: break
    elif op1 == 2:
        while True:
            while True:
                print("""
[1] Configure repository.
[2] Configure all repositories.
[3] Add repository.
[4] Delete repository.
[5] Alter repository.
[6] Query.
[7] Cancel.
                """)
                op3 = int(input(">>> "))
                r2 = int(input("Confirm? [1]y/ [2]n.\n>>> "))
                if r2 == 1: break
            if op3 == 1:
                cn = True
                while True:
                    nm_repo = str(input("The repository name: "))
                    dir_to_clone = str(input("The directory where te repository goes(for here type 'pwd'): "))
                    r1 = int(input("Confirm? [1]y/ [2]n/ [3]Cancel.\n>>> "))
                    if r1 == 3:
                        cn = False
                        break
                    if r1 == 1: break
                if cn:
                    Gitter.config_repo(nm_repo)
                    print(nm_repo+" is configurated!\nReturning to menu ...")
                    sleep(2)
                del nm_repo
                continue
            elif op3 == 2:
                cn = True
                while True:
                    dir_to_clone = str(input("The directory where te repository goes(for here type 'pwd'): "))
                    r1 = int(input("Confirm? [1]y/[2]n/[3]Cancel\n>>> "))
                    if r1 == 3:
                        cn = False
                        break
                    if r1 == 1: break
                if cn:
                    Gitter.config_repo(dir_to_clone=dir_to_clone)
                    print("All repositories are configured.\nReturning to menu ...")
                    sleep(2)
                del cn
                continue
            elif op3 == 3:
                cn = True
                while True:
                    nm_repo = str(input("Repository name (original, from github): "))
                    host = str(input("Repository host: "))
                    remote_nm = str(input("A remote name: "))
                    email = str(input("Email for config: "))
                    name = str(input("Name for config: "))
                    r1 = int(input("Confirm? [1]y/[2]n/[3]Cancel.\n>>> "))
                    if r1 == 3:
                        cn = False
                        break
                    elif r1 == 1: break
                if cn:
                    Gitter.add_repo([nm_repo, host, remote_nm, email, name])
                    print("Added to database sucessfuly!\nReturning to menu!")
                    sleep(2)
                del cn
                continue
            elif op3 == 4:
                cn = True
                while True:
                    nm_repo = str(input("Repository name: "))
                    r1 = int(input("Confirm? [1]y/[2]n/[3]Cancel.\n>>> "))
                    if r1 == 3:
                        cn = False
                        break
                    if r1 == 1: break
                if cn:
                    Gitter.del_repo(nm_repo)
                    print("Deleted sucessfully!\nReturning to menu ...")
                    sleep(2)
                continue
            elif op3 == 5:
                cn = True
                while True:
                    repo = str(input("Repository name: "))
                    camp = str(input("Camp to alter: "))
                    vl = input("Value: ")
                    r1 = int(input("Confirm? [1]y/[2]n/[3]Cancel.\n>>> "))
                    if r1 == 3:
                        cn = False
                        break
                    if r1 == 1:break
                if cn:
                    Gitter.alt_repo(repo=repo, camp=camp, vl=vl)
                    print("Altered sucessfully!\nReturning to menu ...")
                    sleep(2)
                del repo, camp, vl
                continue
            elif op3 == 6:
                s = Gitter.query_repo()
                dt = GitterBeauty.shows_all_data(s)
                if len(dt) <= 0:
                    print("There's no repositories in the database!")
                else:
                    print(dt)
                input("<<press any button to go back to menu>>")
                continue
            elif op3 == 7: break
    elif op1 == 3:
        print(__doc__)
        input("<<press any button to return to menu>>")
        continue
    elif op1 == 4:
        back.update_backup()
        exit(0)
    elif op1 == 5:
        db_con = RepositorySystem()
        while True:
            system("clear")
            while True:
                system("figlet Repositorier")
                print("""
        Welcome!
        Would you like:
        [1] Add a Repository
        [2] Delete a Repository
        [3] Alter a Repository
        [4] See PPA Repositories.
        [5] See Non-PPA repositories.
        [6] Config a repository.
        [7] Help
        [8] Exit
                        """)
                opc1 = int(input(">>> "))
                confirm = int(input("Confirm?\n[1]Y\n[2]\n>>> "))
                if confirm == 1: break
            if opc1 == 1:
                c = True
                while True:
                    nm_repo = str(input("Type the repository name: "))
                    host_vl = str(input("Type the host of the repository: "))
                    is_ppa = int(input("Is that a PPA Repository?\n[1]Y\n[0]N\n>>> "))
                    if is_ppa not in (0, 1):
                        print("That's not a valid value!\nTry all again you moron!")
                        continue
                    confirm = int(input("Confirm?\n[1]Y\n[2]N\n[3]Cancel\n>>> "))
                    if confirm == 3:
                        c = False
                        break
                    if confirm == 1: break
                if c:
                    local_repo_data = [nm_repo, host_vl, is_ppa]
                    db_con.add_to_db(local_repo_data)
                    del local_repo_data
                    input("Added Successfully!\n<<press any button to return>>")
                continue
            elif opc1 == 2:
                c = True
                while True:
                    nm_repo = str(input("The repository to remove: "))
                    confirm = int(input("Confirm?\n[1]Y\n[2]N\n[3]Cancel\n>>> "))
                    if confirm == 3:
                        c = False
                        break
                    if confirm == 1: break
                if c:
                    db_con.del_repo_db(nm_repo)
                    input("Removed Successfully!\n<<press any button to return>>")
                continue
            elif opc1 == 3:
                c = True
                while True:
                    nm_repo = str(input("The repository to alter his data: "))
                    camp = str(input("The data to alter: "))
                    if camp == "is_ppa":
                        vl_new = int(input("The new value (In that case 0 from No, 1 for yes): "))
                    else:
                        vl_new = str(input("The new value: "))
                    confirm = int(input("Confirm?\n[1]Y\n[2]N\n[3]Cancel\n>>> "))
                    if confirm == 3:
                        c = False
                        break
                    if confirm == 1: break
                if c:
                    db_con.alt_repo_data(nm_repo, camp, vl_new)
                    input("Updated Successfully!\n<<press any button to return>>")
                continue
            elif opc1 == 4:
                query = db_con.get_ppa_repos()
                print(RepoBeuaty.shows_all_data(query))
                input("<<press any button to return to the database>>")
                continue
            elif opc1 == 5:
                query = db_con.get_regular_repos()
                print(RepoBeuaty.shows_all_data(query))
                input("<<press any button to return to the database>>")
                continue
            elif opc1 == 6:
                c = True
                while True:
                    repo_to = str(input("Type the repository to config (for config all type '--all'): "))
                    confirm = int(input("Confirm?\n[1]Y\n[2]N\n[3]Cancel\n>>> "))
                    if confirm == 3:
                        c = False
                        break
                    if confirm == 1: break
                if c:
                    if repo_to == "--all":
                        db_con.config_repo()
                        input("All the repositories configured successfully!\n<<press any button to return>>")
                    else:
                        db_con.config_repo(repo_to)
                        input("Repository configured successfully!\n<<press any button to return>>")
                continue
            elif opc1 == 7:
                print(__doc__)
                input("<<press any button to return>>")
                continue
            elif opc1 == 8:
                break
            else:
                print("Invalid Option!\nTry again!")
                continue
        continue










































