# coding = utf-8
# using namespace std
import json
from os import system, chdir
from typing import Any, AnyStr

# todo: refazer o sistema com sem documentos especificos


class Database(object):
    document = list()
    file_name = AnyStr

    def __init__(self, file_name="datacore/database.json"):
        self.file_name = file_name
        with open(self.file_name, "r") as dl: self.document = json.loads(dl.read())

    @classmethod
    def update(cls):
        n = json.dumps(cls.document)
        with open(cls.file_name, "w") as fl: fl.write(n)
        del n

    @classmethod
    def union_doc(cls, dc: dict, index: int):
        cls.document[index] = dc
        cls.update()


class Installer(Database):
    doc_installer = list()  # todo: documentos tipo esse

    @classmethod
    def __init_subclass__(cls): cls.doc_installer = cls.document[0]["Installer"]

    @classmethod
    def faster(cls): cls.union_doc(dc={"Installer": cls.doc_installer}, index=0)

    class PackageNotFound(Exception):
        args = "esse pacote nao pode ser encontrado!"

    class PackageExistsError(Exception):
        args = "esse pacote ja existe no banco de dados"

    class UnfiledCamp(Exception):
        args = "esse campo nao eh um campo valido!"

    @classmethod
    def pack_exists(cls, pack: str):
        for i in cls.doc_installer:
            if i["Package_nm"] == pack: return True
        return False

    @classmethod
    def return_index(cls, pack: str):
        if not cls.pack_exists(pack): raise cls.PackageNotFound()
        ind = 0
        for i in cls.doc_installer:
            if i["Package_nm"] == pack: break
            ind += 1
        return ind

    @classmethod
    def add_package(cls, data: dict):
        if cls.pack_exists(data["Package_nm"]): raise cls.PackageExistsError()
        cls.doc_installer.append(data)
        cls.faster()

    @classmethod
    def delete_package(cls, pack: str):
        if not cls.pack_exists(pack): raise cls.PackageNotFound()
        ind = cls.return_index(pack)
        del cls.doc_installer[ind]
        cls.faster()

    @classmethod
    def alt_package(cls, pack: str, camp: str, vl: str):
        if not cls.pack_exists(pack): raise cls.PackageNotFound()
        if camp not in ("Package_nm", "Command"): raise cls.UnfiledCamp()
        ind = cls.return_index(pack)
        cls.doc_installer[ind][camp] = vl
        cls.faster()

    @classmethod
    def query_pack(cls, vl: str, camp_req="--all", param="none"):
        if camp_req not in ("Package_nm", "Command") or param not in ("Package_nm", "Command"): raise cls.UnfiledCamp()
        rs = []
        if param == "none":
            if camp_req == "--all": rs = cls.doc_installer
            else:
                for i in cls.doc_installer: rs.append(i[camp_req])
        else:
            if camp_req == "--all":
                for i in cls.doc_installer:
                    if i[param] == vl: rs.append(i)
            else:
                for i in cls.doc_installer:
                    if i[param] == vl: rs.append(i[camp_req])
        return rs

    @classmethod
    def install_package(cls, pack="--all"):
        if pack == "--all":
            for i in cls.doc_installer:
                system(i["Command"])
        else:
            if not cls.pack_exists(pack): raise cls.PackageNotFound()
            ind = cls.return_index(pack)
            system(cls.doc_installer[ind]["Command"])


class Gitter(Database):
    doc_gitter = list()

    @classmethod
    def __init_subclass__(cls): cls.doc_gitter = cls.document[1]["Gitter"]

    @classmethod
    def faster(cls): cls.union_doc({"Gitter": cls.doc_gitter}, 1)

    class RepositoryNotFound(Exception):
        args = "Esse repositorio nao pode ser encontrado!"

    class RepositoryExistsError(Exception):
        args = "Esse repositorio ja existe"

    class UnfiledCamp(Exception):
        args = "Esse campo nao eh valido"

    @classmethod
    def repo_exists(cls, repo: str):
        for i in cls.doc_gitter:
            if i["Name"] == repo: return True
        return False

    @classmethod
    def return_index(cls, repo: str):
        if not cls.repo_exists(repo): raise cls.RepositoryNotFound()
        ind = 0
        for i in cls.doc_gitter:
            if i["Name"] == repo: break
            ind += 1
        return ind

    @classmethod
    def add_repo(cls, data: dict):
        n = data["Host"].split("/")
        data["Name"] = n[-1]
        if cls.repo_exists(data["Name"]): raise cls.RepositoryExistsError()
        cls.doc_gitter.append(data)
        cls.faster()

    @classmethod
    def delete_repo(cls, repo: str):
        if not cls.repo_exists(repo): raise cls.RepositoryNotFound()
        ind = cls.return_index(repo)
        del cls.doc_gitter[ind]
        cls.faster()

    @classmethod
    def alt_repo(cls, repo: str, camp: str, vl: str):
        if not cls.repo_exists(repo): raise cls.RepositoryNotFound()
        if not camp in ("RemoteName", "Host", "Name", "EmailUser", "NameUser"):
            raise cls.UnfiledCamp()
        ind = cls.return_index(repo)
        cls.doc_gitter[ind][camp] = vl
        cls.faster()

    @classmethod
    def query_repo(cls, vl: str, camp_req="--all", param="none"):
        if camp_req or param not in ("RemoteName", "Host", "Name", "EmailUser", "NameUser", "--all", "none"):
            raise cls.UnfiledCamp()
        rs = []
        if param == "none":
            if camp_req == "--all": rs = cls.doc_gitter
            else:
                for i in cls.doc_gitter: rs.append(i[camp_req])
        else:
            if camp_req == "--all":
                for i in cls.doc_gitter:
                    if i[param] == vl: rs.append(i)
            else:
                for i in cls.doc_gitter:
                    if i[param] == vl: rs.append(i[camp_req])
        return False

    @classmethod
    def configure_repo(cls, repo="--all"):
        if repo == "--all":
            for i in cls.doc_gitter:
                a = system("git clone "+i["Host"])
                del a
                chdir(i["Name"])
                a = system("git remote add "+i["RemoteName"]+" "+i["Host"])
                del a
                a = system("git config --global user.name = "+i["NameUser"])
                del a
                a = system("git config --global user.email = "+i["EmailUser"])
                del a
                chdir("..")
        else:
            if not cls.repo_exists(repo): raise cls.RepositoryNotFound()
            ind = cls.return_index(repo)
            a = system("git clone "+cls.doc_gitter[ind]["Host"])
            del a
            chdir(cls.doc_gitter[ind]["Name"])
            a = system("git remote add "+cls.doc_gitter[ind]["RemoteName"]+" "+cls.doc_gitter[ind]["Host"])
            del a
            a = system("git config --global user.name = "+cls.doc_gitter[ind]["NameUser"])
            del a
            a = system("git config --global user.email = "+cls.doc_gitter[ind]["EmailUser"])
            del a
            chdir("..")


class Configurations(Database):
    doc_config = dict()

    @classmethod
    def __init_subclass__(cls): cls.doc_config = cls.document[2]["Config"]






























