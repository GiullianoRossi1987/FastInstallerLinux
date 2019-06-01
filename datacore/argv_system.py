# coding = utf=8
# using namespace std
from datacore import Gitter, Installer
from datacore import core as DataBaseActions
from sys import argv


class ArgvData(object):

    __help__ = """"""

    oficial_argvs = (
        "-I", "-G", "--all", "-a", "-d", "-l", "-s", "-i", "-c", "--help", "-o", "-pwd", "--all"
    )

    class InvalidArgv(Exception):
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
                for i in DataBaseActions.Installer.query_package():
                    print("Package: "+i[0]+"| Command: "+i[1], end="\n")
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
                for i in DataBaseActions.Gitter.query_repo():
                    print(f"Git Name: {i[0]} | Host: {i[1]}")
            elif data[2] == "-o":
                # gitter screen options
                Gitter.MainScreen()
            else:
                raise cls.InvalidArgv()
        elif data[1] == "-v":
            print(DataBaseActions.__version__)
        else:
            raise cls.InvalidArgv()

    def __init__(self):
        DataBaseActions.Installer()
        DataBaseActions.Gitter()
        self.action_by_argv(argv)




































