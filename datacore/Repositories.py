# coding = utf-8
# using namespace std
from datacore.core import RepositorySystem
from datacore.beauty import RepoBeuaty
from os import system
from datacore.backup_maker import DatabaseToBackup



__help__ = """"""


class MainScreen(object):

    def __init__(self):
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
                print(__help__)
                input("<<press any button to return>>")
                continue
            elif opc1 == 8:
                DatabaseToBackup().update_backup()
                exit(0)
            else:
                print("Invalid Option!\nTry again!")
                continue






































