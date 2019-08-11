# coding = utf-8
# using namespace std
from datacore.core import DebianPacks
from datacore.color_sys import LoadInColor
from os import system
from time import sleep
from datacore.beauty import DebBeauty


colorer = LoadInColor()


class DebPacksScreen(DebianPacks):
    """"""

    logo = """"""
    help_txt = """"""

    class EndUsage(Exception):
        args = "End of Use"

    def main_screen(self):
        """"""
        while True:
            system("clear")
            while True:
                print("""
[1] Add a Debian Package
[2] Install from a Debian Package
[3] Install all debian packages
[4] Delete a Debian Package
[5] Alterate Debain Package Data
[6] See all the Packages
[7] Help
[8] Exit
                """)
                opc = int(input(">>> "))
                r = int(input("Confirm Choice?\n[1] Yes\n[2] No\n>>> "))
                if r == 1: break
            if opc == 1:
                c = True
                while True:
                    nm_pack = str(input("Type the Debian Package name: "))
                    link_download = str(input("Type the link to download: "))
                    is_downloaded = int(input("The file's already downloaded in the FastInstallerLinux/deb_bins?\n[1] Yes\n[0] No\n>>> "))
                    if is_downloaded not in range(0, 2):
                        print("That's not a valid value\nAnd you know that\nSo type all again you ugly muggly")
                        sleep(1)
                        continue
                    r = int(input("Confirm those data?\n[1] Yes\n[2] No\n[3] Abort\n>>> "))
                    if r == 3:
                        c = False
                        break
                    if r == 1: break
                if c:
                    self.add_deb_pack([nm_pack, link_download, is_downloaded])
                    input("Added successfully!\n<<press any button to return>>")
                continue
            elif opc == 2:
                c = True
                while True:
                    nm_pack = str(input("Type the debian package to install: "))
                    r = int(input("Confirm the name?\n[1] Yes\n[2] No\n[3] Abort\n>>> "))
                    if r == 1: break
                    if r == 3:
                        c = False
                        break
                if c:
                    self.install_deb_pack(nm_pack)
                    input(nm_pack+" installed\n<<press any button to return>>")
                continue
            elif opc == 3:
                self.install_deb_pack()
                input("all packages installed successfully\n<<press any button to return>>")
                continue
            elif opc == 4:
                c = True
                while True:
                    nm_pack = str(input("The package to delete: "))
                    r = int(input("Confirm the name?\n[1] Yes\n[2]No\n[3] Abort\n>>> "))
                    if r == 3:
                        c = False
                        break
                    if r == 1: break
                if c:
                    self.del_deb_pack(nm_pack)
                    input(nm_pack+" deleted successfully\n<<press any button to return>>")
                continue
            elif opc == 5:
                c = True
                camps = ["nm_pack", "link_download", "vl_installed"]
                while True:
                    nm_pack = str(input("The debian package to alter: "))
                    cp = int(input("Select what alter\n[0] The package Name\n[1] The link to Download\n[2] If it's installed\n>>>"))
                    if cp == 2:
                        new_vl = int(input("Type the new value: "))
                    else:
                        new_vl = str(input("Type teh new value: "))

                    r1 = int(input("Confirm those data?\n[1] Yes\n[2] No\n[3] Abort\n>>> "))
                    if r1 == 3:
                        c = False
                        break
                    if r1 == 1: break
                if c:
                    self.alt_deb_pack(camps[cp], new_vl, nm_pack)
                    input(nm_pack+"altered successfully!\n<<press any button to return>>")
                continue
            elif opc == 6:
                print(DebBeauty.show_all_data(self.get_deb_packs()))
                input("<<press any button to return>>")
                continue
            elif opc == 7:
                input(self.help_txt+"\n<<press any button to return>>")
                continue
            elif opc == 8: raise self.EndUsage()
            else:
                print("That's not a valid option!")
                input("Try again!")
                continue


