# coding = utf-8
# using namespace std
import json
from os import system, chdir
from typing import Any

__git__ = "https://github.com/GiullianoRossi1987/FastInstallerLinux"


class Database(object):
    archive = Any
    document = list

    def __init__(self, file_name="database.json"):
        self.archive = open(file_name, "rw")
        self.document = json.loads(self.archive.read())

    @classmethod
    def update(cls):
        n = json.dumps(cls.document)
        cls.archive.write(n)
        del n
        
    @classmethod
    def union_all(cls, data_part: list, index: int):
        cls.document[index] = data_part
        cls.update()


class Installer(Database):
    doc_installer = list

    @classmethod
    def __init_subclass__(cls): cls.doc_installer = cls.document[0]["Installer"]  # Installer Position

    class PackageNotFound(Exception):
        args: str = "%pack% nao foi encontrado!"

        def __init__(self, ar="esse pacote"): self.args = self.args.replace("%pack%", ar)

    class PackageExistsError(Exception):
        args: str = "%pack% ja existe no sistema"

        def __init__(self, arg="esse pacote"): self.args = self.args.replace("%pack%", arg)
    
    class CampUnfilied(Exception):
        args: str = "%camp% nao eh um campo valido valido"

        def __init__(self, cp="esse campo"): self.args = self.args.replace("%camp%", cp)
    

    @classmethod
    def pack_exists(cls, pack: str):
        for i in cls.doc_installer: 
            if i["Package_nm"] == pack: return True
        return False
    
    @classmethod
    def return_index(cls, pack: str):
        if not cls.pack_exists: raise cls.PackageNotFound(pack)
        ind = 0
        for i in cls.doc_installer:
            if i["Package_nm"] == pack: break
            ind += 1
        return ind
    
    def add_pack(self, data: dict):
        if cls.pack_exists(data["Package_nm"]): raise cls.PackageExistsError(data["Package_nm"])
        self.doc_installer.append(data)
        self.union_all(data_part=self.doc_installer, index=0)
    
    def __delete_pack__(self, pack_name: str):
        if not self.pack_exists(pack_name): raise self.PackageNotFound(pack_name)
        ind = self.return_index(pack_name)
        del self.doc_installer[ind]
        self.union_all(data_part=self.doc_installer, index=0)
    
    def __alt_pack__(self, pack: str, camp: str, vl: str):
        if not self.pack_exists(pack): raise self.PackageNotFound(pack)
        if camp not in ("Package_nm", "Command", "Installed"): raise self.CampUnfilied(camp)
        ind = self.return_index(pack)
        self.doc_installer[ind][camp][vl]
        self.union_all(self.doc_installer, 0)
    
    def __query_pack__(self, param_vl: str, camp_req="--all", param_camp="none")
        results = []
        if param_camp == "none":
            if camp_req == "--all": results = self.doc_installer
            else:
                for i in self.doc_installer: results.append(i[camp_req])
        else:
            if camp_req == "--all":
                for i in self.doc_installer:
                    if i[param_camp] == param_vl: results.append(i)
            else:
                for i in self.doc_installer:
                    if i[param_camp] == param_vl: results.append(i[camp])
        return results
    
    @classmethod
    def install_pack(cls, pack="--all"):
        if pack == "--all":
            for i in cls.doc_installer: 
                system(i["Command"])
                i["Installed"] = "True"
            cls.union_all(cls.doc_installer, 0)
        else:
            ind = cls.return_index(pack)
            system(cls.doc_installer[ind]["Command"])
            cls.doc_installer[ind]["Installed"] = "True"
            cls.union_all(cls.doc_installer, 0)


class Gitter(Database):
    doc_gitter = list

    @classmethod
    def __init_subclass__(cls):self.doc_gitter = self.document[1]["Gitter"]

    class RepositoryNotFound(Exception):
        args = "%repo% nao foi encontrado ou nao existe!"

        def __init__(self, rp="esse repositorio"): self.args = self.args.replace("%repo%", rp)
    
    class RepositoryExistsError(Exception):
        args = "%repo% ja existe no sistema!"

        def __init__(self, rp="esse repositorio"): self.args = self.args.replace("%repo%", rp)
    
    class CampUnfilied(Exception):
        args = "%camp% nao eh um campo valido!"

        def __init__(self, cp="esse campo"): self.args = self.args.replace("%camp%", cp)

    
    @classmethod
    def repo_exists(cls, repo_nm: str):
        for i in cls.doc_gitter:
            if i["Repository_nm"] == repo_nm: return True
        return False
    
    @classmethod
    def return_index(cls, repo: str):
        if not cls.repo_exists(repo): raise cls.RepositoryNotFound(repo)
        ind = 0
        for i in cls.doc_gitter:
            if i["Repository_nm"] == repo: break
            ind += 1
        return ind
    
    @classmethod
    def add_repo(cls, data: dict):
        if cls.repo_exists(data["Repository_nm"]): raise cls.RepositoryExistsError(data["Repository_nm"])
        cls.doc_gitter.append(data)
        cls.union_all(cls.doc_gitter, 1)
    
    @classmethod
    def del_repo(cls, repo_nm: str):
        if not cls.repo_exists(repo_nm): raise cls.RepositoryNotFound(repo_nm)
        ind = cls.return_index(repo_nm)
        del cls.doc_gitter[ind]
        cls.union_all(cls.doc_gitter, 1)
    
    @classmethod
    def alt_repo(cls, repo_nm: str, camp: str, vl: str):
        if not cls.repo_exists(repo_nm): raise cls.RepositoryNotFound(repo_nm)
        if camp not in ("Repository_nm", "RemoteName", "EmailUser", "NameUser")
        ind = cls.return_index(repo_nm)
        cls.doc_gitter[ind][camp] = vl
        cls.union_all(cls.doc_gitter, 1)
    
    @classmethod
    def query_repo(cls, vl: str, camp_req="--all", param="none"):
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
                    if i[param] == vl: rs.append(i[camp])
        return rs
    
    @classmethod
    def configure_repo(cls, repo_nm="--all"):
        if repo_nm == "--all":
            for i in cls.doc_gitter:
                system("git clone "+i["Host"])
                chdir(i["Repository_nm"])
                system("git config --global user.name = "+i["NameUser"])
                system("git config --global user.email = "+i["EmailUser"])
                system("git remote add "+i["RemoteName"]+" "+i["Host"])
                chdir("..")
        else:
            if not cls.repo_exists(repo_nm): raise cls.RepositoryNotFound(repo_nm)
            ind = cls.return_index(repo_nm)
            system("git clone "+cls.doc_gitter[ind]["Host"])
            chdir(cls.doc_gitter[ind]["Repository_nm"])
            system("git config --global user.name = "+cls.doc_gitter[ind]["NameUser"])
            system("git config --global user.email = "+cls.doc_gitter[ind]["EmailUser"])
            system("git remote add "+cls.doc_gitter[ind]["RemoteName"]+" "+cls.doc_gitter[ind]["Host"])
            chdir("..")


class Configurations(Database):
    config_doc = dict


    @classmethod
    def __init_subclass__(cls): 
        cls.config_doc = cls.document[2]["Configuration"]
        if not bool(cls.config_doc["SnapInstalled"]):
            system("sudo apt-get install snapd")
        if not bool(cls.config_doc["GitInstalled"]):
            system("sudo apt-get install git")
        if not bool(cls.config_doc["OriginalDoc"]):
            print("Atencao!\nO documento de banco de dados sendo usado nao eh original!\nCuidado!")
            print("Para conseguir o original va ate esse link:\n"+__git__)


if __name__ == "__main__": pass
    
    

    




            


            
            





















