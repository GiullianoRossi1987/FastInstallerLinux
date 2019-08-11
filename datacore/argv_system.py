# coding = utf-8
# using namespace std
from sys_screens import Gitter, Installer
from datacore import core as DataBaseActions
from sys import argv
from datacore import beauty


class ArgvData(object):

    __help__ = """"""

    oficial_argvs = (
        "-I", "-G", "--all", "-a", "-d", "-l", "-s", "-i", "-c", "--help", "-o", "-pwd", "--all", "-Sl"
    )

    class InvalidArgv(BaseException):
        args = "This is not a valid argv.\nIf you need help type -h"

    @classmethod
    def action_by_argv(cls, data):
        if data[1] == "--help": print(cls.__help__)
        elif data[1] == "-I":
            if data[2] == "--help":
                print(DataBaseActions.Installer.__doc__)
            elif data[2] == "-i":
                DataBaseActions.Installer.install_package(str(data[3]))
            elif data[2] == "-a":
                DataBaseActions.Installer.add_package([data[3], data[4]])
            elif data[2] == "-d":
                DataBaseActions.Installer.del_package(data[3])
            elif data[2] == "-l":
                DataBaseActions.Installer.alt_packages(data[3], data[4], data[5])
            elif data[2] == "-o":
                Installer.MainScreen()
            elif data[2] == "-s":
                rs = beauty.PackagesBeauty.shows_all_data(DataBaseActions.Installer.query_package())
                if len(rs) <= 0:
                    print("There's no packages here!")
                else:
                    print(rs)
            else:
                raise cls.InvalidArgv()
        elif data[1] == "-G":
            if data[2] == "--help": print(DataBaseActions.Gitter.__doc__)
            elif data[2] == "-c":
                if data[3] == "--pwd":  DataBaseActions.Gitter.config_repo(data[3])
                else: DataBaseActions.Gitter.config_repo(data[3], data[4])
            elif data[2] == "-a":
                DataBaseActions.Gitter.add_repo([data[3], data[4], data[5], data[6], data[7]])
            elif data[2] == "-d":
                DataBaseActions.Gitter.del_repo(data[3])
            elif data[2] == "-l":
                DataBaseActions.Gitter.alt_repo(data[3], data[4], data[5])
            elif data[2] == "-s":
                rs = beauty.GitterBeauty.shows_all_data(DataBaseActions.Gitter.query_repo())
                if len(rs) <= 0:
                    print("There's no repositories here!")
                else:
                    print(rs)
            elif data[2] == "-o":
                # gitter screen options
                try:
                    Gitter.MainScreen()
                except Gitter.MainScreen.EndUsage: exit(0)
            else:
                raise cls.InvalidArgv()
        elif data[1] == "-v":
            print(DataBaseActions.__version__)
        elif data[1] == "-R":
            if data[2] == "--help": print(DataBaseActions.RepositorySystem.help_sys)
            elif data[2] == "-c":
                DataBaseActions.RepositorySystem().config_repo(data[3])
            elif data[2] == "-a":
                DataBaseActions.RepositorySystem().add_to_db([data[3], data[4], int(data[5])])
            elif data[2] == "-d":
                DataBaseActions.RepositorySystem().del_repo_db(data[3])
            elif data[2] == "-l":
                DataBaseActions.RepositorySystem().alt_repo_data(data[3], data[4], data[5])
            elif data[2] == "-s":
                if data[3] == "--ppa":
                    repos = beauty.RepoBeuaty().shows_all_data(DataBaseActions.RepositorySystem().get_ppa_repos())
                elif data[3] == "--normal":
                    repos = beauty.RepoBeuaty().shows_all_data(DataBaseActions.RepositorySystem().get_regular_repos())
                else:
                    repos = beauty.RepoBeuaty.shows_all_data(DataBaseActions.RepositorySystem().get_all_repos())
                if len(repos) <= 0:
                    print("There's no repositories!")
                else:
                    print(repos)
        elif data[1] == "-D":
            db = DataBaseActions.DebianPacks()
            if data[2] == "--help" or "-h": print(db.help_txt)
            elif data[2] == "-i" or "--install":
                db.install_deb_pack(data[3])
            elif data[2] == "-a" or "--add":
                db.add_deb_pack([data[3], data[4], int(data[5])])
            elif data[2] == "-d" or "--delete":
                db.del_deb_pack(data[3])
            elif data[2] == "-l" or "--alter":
                db.alt_deb_pack(data[3], data[4], data[5])
            elif data[2] == "-s" or "--show":
                rs = db.get_deb_packs()
                if len(rs) <= 0: print("There's no Debian Packages !")
                else: print(beauty.DebBeauty().show_all_data(rs))
            else: raise cls.InvalidArgv()
        elif data[1] == "--export":
            exp = DataBaseActions.DatabaseExporter()
            exp.export_data_to(data[2])
        elif data[1] == "--import":
            imp = DataBaseActions.DatabaseExporter()
            imp.import_from(data[2])
        else:
            raise cls.InvalidArgv()

    def __init__(self):
        DataBaseActions.Installer()
        DataBaseActions.Gitter()
        self.action_by_argv(argv)




































