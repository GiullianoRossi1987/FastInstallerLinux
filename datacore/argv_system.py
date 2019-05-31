# coding = utf=8
# using namespace std
# from datacore.screens_system import Gitter, Installer
from datacore import core as DataBaseActions
from sys import argv


class ArgvData(object):

    __help__ = """"""

    oficial_argvs = (
        "-I", "-G", "--all", "-a", "-d", "-l", "-s", "-i", "-c", "--help", "-o", "-pwd"
    )

    class InvalidArgv(Exception):
        args = "This is not a valid argv.\nIf you need help type -h"


    @classmethod
    def action_by_argv(cls, data):
        if data[0] == "--help": print(cls.__help__)
        elif data[0] == "-I":
            if data[1] == "--help":
                print(DataBaseActions.Installer.__doc__)
            elif data[1] == "-i":
                DataBaseActions.Installer.install_package(data[2])
            elif data[1] == "-a":
                DataBaseActions.Installer.add_package([data[2], data[3]])
            elif data[1] == "-d":
                DataBaseActions.Installer.del_package(data[2])
            elif data[1] == "-l":
                DataBaseActions.Installer.alt_packages(data[2], data[3], data[4])
            elif data[1] == "-o":
                # installer options
                pass
            elif data[1] == "-s":
                print(DataBaseActions.Installer.query_package())
            else:
                raise cls.InvalidArgv()
        elif data[0] == "-G":
            if data[1] == "--help": print(DataBaseActions.Gitter.__doc__)
            elif data[1] == "-c":
                if data[3] == "--pwd":  DataBaseActions.Gitter.config_repo(data[2])
                else: DataBaseActions.Gitter.config_repo(data[2], data[3])
            elif data[1] == "-a":
                DataBaseActions.Gitter.add_repo([data[2], data[3], data[4], data[5], data[6]])
            elif data[1] == "-d":
                DataBaseActions.Gitter.del_repo(data[2])
            elif data[1] == "-l":
                DataBaseActions.Gitter.alt_repo(data[2], data[3], data[4])
            elif data[1] == "-s":
                print(DataBaseActions.Gitter.query_repo())
            elif data[1] == "-o":
                # gitter screen options
                pass
            else:
                raise cls.InvalidArgv()
        elif data[0] == "-v":
            print(DataBaseActions.__version__)
        else:
            raise cls.InvalidArgv()

    def __init__(self):
        self.action_by_argv(argv)




































