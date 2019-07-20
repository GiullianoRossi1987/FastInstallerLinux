# coding = utf-8
# using namespace std
import os
from typing import AnyStr
from datacore.annimations_cgi import BackupAnime


class DatabaseToBackup(object):

    database_file_path = AnyStr
    database_file = AnyStr

    def __init__(self, path_db:str = "./datacore/database.db"):
        self.database_file_path = path_db
        self.database_file = path_db.split("/")[-1]

    def create_backup(self, dir_to:AnyStr = "./public_backup"):
        animation = BackupAnime()
        animation.creating_database()
        os.system("cp "+self.database_file_path+dir_to)
        del animation

    def update_backup(self, dir_to: AnyStr = "./public_backup"):
        animation = BackupAnime()
        animation.sending_to_backup()
        os.system("rm "+dir_to+"/"+self.database_file)
        os.system("cp "+self.database_file_path+" "+dir_to)
        del animation


class BackupConfig(object):

    config = []
    config_file = AnyStr

    def __init__(self, database_path="./datacore/backup_config.dat"):
        with open(database_path, "r") as config_file:
            self.config = config_file.readlines()
        self.config_file = database_path

    def __need_create__(self) -> bool: return self.config[0] == "Not Create Database"


















