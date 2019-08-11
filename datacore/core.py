# coding = utf-8
# using namespace std
import sqlite3
from os import chdir
from os import system as check_output
from datacore import annimations_cgi
from os import listdir
from typing import AnyStr
from datacore.color_sys import LoadInColor


colorer = LoadInColor()

"""
This is the main database system. You can import this file, or easily start the main file (installer.py)
The database use only two tables on the database: database.db
And it have all the important and used data for configure repositories and download packages.
"""


__version__  = 1.5


class Database(object):
    __doc__ = """
    The all classes core, where's declared the database connection, and it's cursor.
    Without this class the system's nothing.
    :connection: connect to the database
    """
    connection = sqlite3.connect("./datacore/database.db", timeout=10)
    cursor = connection.cursor()

    def __init__(self, file_db: AnyStr = "./datacore/database.db"):
        """Start the connection and declare the cursor.Maybe not useful. But there is it."""
        self.connection = sqlite3.connect(file_db)
        self.cursor = self.connection.cursor()

    def format_database(self):
        """
        Excludes all the data on the database, and return a list with the numbers of the
        lines excluded.
        """
        qr = self.cursor.executescript("""
delete from Packages;
delete from Gits;
delete from Repositories;

update sqlite_sequence set seq=0 where name="Packages";
update sqlite_sequence set seq=0 where name="Gits";
update sqlite_sequence set seq=0 where name="Repositories";
        """)
        del qr

    def restore_database(self):
        """"""
        # droping all the tables
        query_tbs = self.cursor.execute("select name from sqlite_master where type=\"table\";")
        for tb in query_tbs.fetchall(): dell_com = self.cursor.execute("drop table "+tb[0]+";")
        query_recreate = self.cursor.execute(
            """
create table Packages(
    Cd_Pack integer primary key autoincrement not null unique,
    Nm_Pack text not null unique,
    Command text not null unique
);

create table Gits(
    Cd_Git integer primary key autoincrement not null unique,
    Nm_Git text not null unique,
    Host_Git text not null unique,
    Remote_Nm text not null unique,
    EmailUser text not null unique,
    NameUser text not null unique
);

create table Repositories(
    cd_repo integer primary key autoincrement not null unique,
    nm_repo text not null unique,
    host_vl text not null unique,
    is_ppa integer not null check(is_ppa in (0, 1))
);

create table DebPacks(
    cd_pack integer primary key autoincrement not null unique,
    nm_deb text not null unique,
    link_download text not null unique,
    vl_installed integer not null check(vl_installed in (0, 1))
);

            """
        )
        del query_recreate,query_tbs

    @staticmethod
    def restore_external_database(db: AnyStr):
        con = Database(db)
        con.restore_database()

class Installer(Database):

    __logs = []

    __doc__ = """
    This class works only with the Packages table. It have functions and procedures for the packages management
    """

    class PackageNotFound(Exception):
        __doc__ = "If the typed package was not found in the database. Similar to FileNotFound"
        args = "Esse pacote nao existe no banco de dados!"

    class PackageExistsError(Exception):
        __doc__ = "If the typed package already exists, to prevent duplicate data in the database"
        args = "Esse pacote ja existe no sistema!"

    @classmethod
    def package_exists(cls, pack: str) -> bool:
        """Verify if the typed package exists in the database"""
        a = cls.cursor.execute("select Nm_Pack from Packages;")  # have all the names of the all packages
        for i in a:
            if i[0] == pack: return True  # i is type tuple
        del a
        return False

    @classmethod
    def add_package(cls, data: list):
        """
        Add a package to the database system, also the user needs to type the command to system execute in installation
        :param data: [Nm_Package, Command]
        :return: :None:
        """
        if cls.package_exists(data[0]): raise cls.PackageExistsError()
        a = cls.cursor.execute(f"insert into Packages(Nm_Pack, Command) values ('{data[0]}', '{data[1]}');")
        cls.connection.commit()
        del a # to not use many memory part
        annimations_cgi.InstallerAnimation.add_pack(data[0])

    @classmethod
    def del_package(cls, package: str):
        """Delete a package from the database. It don't uses the primary key to select."""
        if not cls.package_exists(package): raise cls.PackageNotFound()
        a = cls.cursor.execute(f"delete from Packages where Nm_Pack = '{package}';")
        cls.connection.commit()
        del a
        annimations_cgi.InstallerAnimation.del_pack(package)

    @classmethod
    def alt_packages(cls, package: str, camp: str, vl: str):
        """Alter a package data, or name or command used"""
        if not cls.package_exists(package): raise cls.PackageNotFound()
        a = cls.cursor.execute(f"update  Packages set {camp} = '{vl}' where Nm_Pack = '{package}';")
        del a
        cls.connection.commit()
        annimations_cgi.InstallerAnimation.alt_pack(package)

    @classmethod
    def query_package(cls) -> list:
        """"""
        annimations_cgi.InstallerAnimation.show()
        return cls.cursor.execute("select * from Packages;").fetchall()

    @classmethod
    def install_package(cls, package="--all"):
        """Install the typed package, if it's not defined, install all packages in database"""
        if package == "--all":
            a = cls.cursor.execute("select Command from Packages;")
            for i in a.fetchall():
                pack = cls.cursor.execute(f"select Nm_Pack from Packages where Command = '{i[0]}';").fetchall()[0][0]
                annimations_cgi.InstallerAnimation.install_pack(pack)
                b = check_output(i[0])
                del b
            del a
        else:
            if not cls.package_exists(package): raise cls.PackageNotFound()
            a = cls.cursor.execute(f"select Command from Packages where Nm_Pack = '{package}';")
            annimations_cgi.InstallerAnimation.install_pack(package)
            b = check_output(a.fetchall()[0][0])
            print(b)
            del a,b

class Gitter(Database):

    __doc__ = """
    This class works with the git repositories in the database.
    """
    # doc_data_config = git_config_data.configurations

    class RepositoryNotFound(Exception):
        """If the typed repository was not found"""
        args = "Esse repositorio nao esta no banco de dados!"

    class RepositoryExistsError(Exception):
        """If the typed repository already exists to not have duplicate data"""
        args = "Esse repositorio ja existe no banco de dados!"

    @classmethod
    def repo_exists(cls, repo: str) -> bool:
        """
        Verify if repository exists in database.
        :param: repo is not optional.
        :var: s is deleted after the query
        """
        s = cls.cursor.execute(f"select Nm_Git from Gits;")
        for i in s:
            if i[0] == repo: return True
        del s
        return False

    @classmethod
    def add_repo(cls, data: list):
        """
        Add a repository in the database.
        :param: data = [Git name, Host, Remote name, Email user, Name user]
        """
        if cls.repo_exists(data[0]): raise cls.RepositoryExistsError()
        b = cls.cursor.execute("insert into Gits (Nm_Git, Host_Git, Remote_Nm, EmailUser, NameUser) values (?,?,?,?,?);"
                               , data)
        del b
        cls.connection.commit()
        annimations_cgi.GitterAnimations.add_repo(data[0])

    @classmethod
    def del_repo(cls, repo: str):
        """Delete a repository from the database"""
        if not cls.repo_exists(repo): raise cls.RepositoryNotFound()
        a = cls.cursor.execute(f"delete from Gits where Nm_Git = '{repo}';")
        del a
        cls.connection.commit()
        annimations_cgi.GitterAnimations.del_repo(repo)

    @classmethod
    def alt_repo(cls, repo: str, camp: str, vl: str):
        """Alter a database repo"""
        if not cls.repo_exists(repo): raise cls.RepositoryNotFound()
        b = cls.cursor.execute(f"update Gits set {camp} = '{vl}' where Nm_Git = '{repo}';")
        del b
        cls.connection.commit()
        annimations_cgi.GitterAnimations.alt_repo(repo)

    @classmethod
    def query_repo(cls) -> list:
        """
        It takes all the data in the database, raising only the repository name, the host, the remote name
        """
        annimations_cgi.GitterAnimations.show()
        return cls.cursor.execute("select * from Gits;").fetchall()

    @classmethod
    def config_repo(cls, repo="--all", dir_to_clone="--pwd"):
        """Configure the repositories"""
        if dir_to_clone != "--pwd": chdir(dir_to_clone)
        if repo == "--all":
            all_ = cls.cursor.execute("select * from Gits;")
            for i in all_.fetchall():
                a = check_output("git clone "+i[2])
                annimations_cgi.GitterAnimations.clone_repo(i[1])
                del a
                chdir(i[1])
                a = check_output("git remote add "+i[3]+" "+i[2])
                del a
                a = check_output("git config --global user.name = "+i[5])
                del a
                a = check_output("git config --global user.email = "+i[4])
                annimations_cgi.GitterAnimations.config_repo(i[1])
                chdir("..")
                del a
        else:
            if not cls.repo_exists(repo): raise cls.RepositoryNotFound()
            all_ = cls.cursor.execute(f"select * from Gits where Nm_Git = '{repo}';").fetchall()[0]
            a = check_output("git clone "+all_[2])
            del a
            chdir(all_[1])
            a = check_output("git remote add "+all_[3]+" "+all_[2])
            del a
            a = check_output("git config --global user.name = "+all_[5])
            del a
            a = check_output("git config --global user.email = "+all_[4])
            chdir("..")
            del a
        annimations_cgi.GitterAnimations.clone_repo(repo)


class RepositorySystem(Database):
    """

    """
    local_camps = ("nm_repo", "host_vl", "is_ppa")
    help_sys = """"""

    class RepositoryExistsError(BaseException):
        """

        """
        args: object = "That repository already exists in the database!"

    class RepositoryNotFoundError(BaseException):
        args: object = "That repository can't be found!"

    class OutOfIndexBool(BaseException):
        args: object = "That number's out of the bool range!"

    class InvalidCamp(IndexError):
        args: object = "That camp's not valid!"

    class InvalidValue(ValueError):
        args: object = "That value's not valid for this camp!"

    class RepositoryAlreadyInstalled(BaseException):
        args: object = "That repository's already in the sources.list!"

    class InvalidHostValue(BaseException):
        args: object = "That host's not valid!"

    class InvalidListStructure(BaseException):
        args: object = "That data list it's out of range"

    @classmethod
    def check_repo_exists(cls, repo: str) -> bool:
        """
        Query for a repository, and checks if that repository exists in the database
        :param repo: The repository to query.
        :type repo : str
        :return: if the repository exists.
        :rtype: bool
        """
        query_find = cls.cursor.execute("select nm_repo from Repositories;")
        for item in query_find.fetchall():
            if item[0] == repo: return True
        return False

    @classmethod
    def get_bool_index(cls, index: int) -> bool:
        """
        Transfer the value of the camp 'is_ppa', from int [0, 1] to bool [True, False]
        :param index: The is_ppa value
        :type index: int
        :return: The bool value of the index. If index = 0 then is False, if index = 1 then is True
        :raise cls.OutOfIndexBool: if the index is not 0 or 1.
        """
        if index == 1: return True
        elif index == 0: return False
        else: raise cls.OutOfIndexBool()

    @staticmethod
    def check_host_vl(host: str) -> bool:
        """
        Checks if that host's valid, it check if the host uses port 80 or port 443, another port's not valid!
        :param host: The host to analize.
        :type host: str
        :return: If the host's valid.
        :rtype: bool
        """
        if "https://" or "http://" in host: return True
        else: return False

    @staticmethod
    def add_repo_ppa(repo: str):
        """
        Configure a ppa repository, using command 'sudo add-apt-repository ppa: %repository$/ppa'
        :param repo: The repository to add, it's need to have '/ppa', else it'll raise a error, of course by the
                    shell.
        :type repo: str
        """
        if "/ppa" not in repo:
            repo += "/ppa"
        command = check_output("sudo add-apt-repository ppa:"+repo)
        del command

    @staticmethod
    def add_repo_regular(repo: str):
        """
        Configures a non-ppa repository, writing it on /etc/apt/sources.list.
        The system'll comment 'Added By FIL' in the repository line, after the repository, of course.
        :param repo: The repository host to add in /etc/apt/sources.list
        """
        command = check_output(f"sudo -sh -c \"{repo} # Added By The FIL\" >> /etc/apt/sources.list")
        del command

    def add_to_db(self, repo_data: list):
        """
        Add a repository to the database.
        :param repo_data: The repository data beeing:
                            index[0] => The repository name [str].
                            index[1] => The repository host [str].
                            index[2] => If is a PPA repository [int]
        :raise self.InvalidListStructure: If the data list is not valid!
        :raise self.RepositoryExistsError: If the repository already exists in the database.
        :raise self.InvalidHostValue: If the host value (index[1]) is not valid!
        """
        if len(repo_data) != 3: raise self.InvalidListStructure()
        if self.check_repo_exists(repo_data[0]): raise self.RepositoryExistsError()
        if not self.check_host_vl(repo_data[1]): raise self.InvalidHostValue()
        annimations_cgi.RepositoryAnime().adding_to_db(repo_data[0])
        add_q = self.cursor.execute("insert into Repositories (nm_repo, host_vl, is_ppa) values (?,?,?)", repo_data)
        self.connection.commit()
        del add_q

    def del_repo_db(self, repo: str):
        """
        Remove a repository from the database
        :param repo: The repository to remove
        :type repo: str
        :raise self.RepositoryNotFoundError: If the repository don't exists in the database.
        """
        if not self.check_repo_exists(repo): raise self.RepositoryNotFoundError()
        annimations_cgi.RepositoryAnime().removing_from_db(repo)
        del_q = self.cursor.execute(f"delete from Repositories where nm_repo='{repo}';")
        self.connection.commit()
        del del_q

    def alt_repo_data(self, repo_to: str, camp: str, new_vl):
        """
        Alter some repository data on the database.
        :param repo_to: The repository to alter.
        :param camp: The camp, or data value type to alter on the database.
                     It can be only:
                        nm_repo = The repository name, [str]
                        host_vl = The host to the repository, [str]
                        is_ppa = If it's a PPA repository. [int]
        :param new_vl: The new value to the data value type (camp). [str|int]
        """
        if not self.check_repo_exists(repo_to): raise self.RepositoryNotFoundError()
        if not camp in self.local_camps: raise self.InvalidCamp()
        if new_vl is not str or int: raise TypeError()
        if camp == "is_ppa":
            query_alt = self.cursor.execute(f"update Repositories set {camp}={new_vl} where nm_repo='{repo_to}';")
        else:
            query_alt = self.cursor.execute(f"update Repositories set {camp}='{new_vl}' where nm_repo='{repo_to};'")
        annimations_cgi.RepositoryAnime().altering_db(repo_to)
        self.connection.commit()
        del query_alt

    def get_ppa_repos(self) -> list:
        """
        Get all the PPA repositories in the database
        :return: a list with all the PPA repositories in the database, all their data on tuples.
        """
        query_ppa = self.cursor.execute("select * from Repositories where is_ppa=1;")
        return query_ppa.fetchall()

    def get_regular_repos(self) -> list:
        """
        Get all the Non-PPA repositories in the database.
        :return: a list with their data, on tuples. Ex: [(data)]
        """
        query_ppa = self.cursor.execute("select * from Repositories where is_ppa=0;")
        return query_ppa.fetchall()

    def get_all_repos(self) -> list:
        """
        Get all the repositories, without separation.
        :return: A list with the repositories data
                data = (id: PK (int), nm_repo (str), host_vl (str), is_ppa (int => bool)
        """
        query = self.cursor.execute("select * from Repositories;")
        annimations_cgi.RepositoryAnime().reading_db()
        return query.fetchall()

    def config_repo(self, repo_nm: str = "*"):
        """
        Configure a repository, setting if it's a ppa or not
        :param repo_nm: The repository to configure. default = '*'
                        if '*', then configure all repositories, ppa or not ppa
        """
        if repo_nm == "*":
            all_ppa_repos = self.get_ppa_repos()
            all_reg_repos = self.get_regular_repos()
            for ppa_repo in all_ppa_repos:
                self.add_repo_ppa(ppa_repo[2])
            for reg_repo in all_reg_repos:
                self.add_repo_regular(reg_repo[2])
            del all_reg_repos, all_ppa_repos
        else:
            if not self.check_repo_exists(repo_nm): raise self.RepositoryNotFoundError()
            query_repo_data = self.cursor.execute(f"select * from Repositories where nm_repo='{repo_nm}';").fetchone()
            if self.get_bool_index(query_repo_data[3]):
                self.add_repo_ppa(query_repo_data[2])
            else:
                self.add_repo_regular(query_repo_data[2])
            del query_repo_data
        command_update = check_output("sudo apt-get update")  # update the list of the linux.
        del command_update


class DatabaseExporter(Database):
    """
That class have a important new feature to the system, that's will export local data to other database.
It works hearing the Database class, and the main features are export_data_to() and the main_screen_exporter().

:exception EndOfUsage: The system need't to alert the file installer.py on .. to return the loop in the screens!
    """
    exporter_logo = """
 _____                       _            
| ____|_  ___ __   ___  _ __| |_ ___ _ __ 
|  _| \ \/ / '_ \ / _ \| '__| __/ _ \ '__|
| |___ >  <| |_) | (_) | |  | ||  __/ |   
|_____/_/\_\ .__/ \___/|_|   \__\___|_|   
           |_| 
    """

    help_str = """
    """
    animation = annimations_cgi.ExporterAnimations()

    class EndOfUsage(Exception):
        args = "Final Use"

    def export_data_to(self, to_db: str):
        """
        It inserts the local data from the Packages system, Gitter System and Repositorier System.
        In another words, it forks the database to insert the local data to the database to export.
        :param to_db: The database to send the information. It'll be open by the connection_to_db.
        """
        connection_to_db = sqlite3.connect(to_db)
        cursor_to = connection_to_db.cursor()
        self.animation.export_data_to(to_db)
        # sends to the Packages system
        for dt in self.cursor.execute("select Nm_Pack, Command from Packages;").fetchall():
            try:
                cursor_to.execute("insert into Packages (Nm_Pack, Command) values (?,?);", dt)
            except sqlite3.DatabaseError or sqlite3.ProgrammingError:  # if the data already exists in the database to
                pass
            connection_to_db.commit()
        # sends to the Gitter System
        for git_data in self.cursor.execute("select Nm_Git, Host_Git, Remote_Nm, EmailUser, NameUser from Gits;").fetchall():
            try:
                cursor_to.execute("insert into Gits (Nm_Git, Host_Git, Remote_Nm, EmailUser, NameUser) values (?,?,?,?,?);", git_data)
            except sqlite3.DatabaseError or sqlite3.ProgrammingError:
                pass
            connection_to_db.commit()
        # sends to the Repositorier System
        for repo_data in self.cursor.execute("select nm_repo, host_vl, is_ppa from Repositories;").fetchall():
            try:
                cursor_to.execute("insert into Repositories (nm_repo, host_vl, is_ppa) values (?,?,?);", repo_data)
            except sqlite3.DatabaseError or sqlite3.ProgrammingError: pass
            connection_to_db.commit()
        connection_to_db.commit()
        cursor_to.close()
        connection_to_db.close()

    def import_from(self, db_from: str):
        """
        Imports the main data from other database, like the export_data_to, but it gets the data from.
        :param db_from: The database to get the data
        """
        connection_from = sqlite3.connect(db_from)
        cursor_from = connection_from.cursor()
        self.animation.import_data_from(db_from)
        # gets Packages data
        for dt in cursor_from.execute("select Nm_Pack, Command from Packages;").fetchall():
            try:
                self.cursor.execute("insert into Packages (Nm_Pack, Command) values (?,?);", dt)
            except sqlite3.ProgrammingError or sqlite3.DatabaseError: pass
        # gets Gitter data
        for gitter in cursor_from.execute("select Nm_Git, Host_Git, Remote_Nm, EmailUser, NameUser from Gits;").fetchall():
            try:
                self.cursor.execute("insert into Gits (Nm_Git, Host_Git, Remote_Nm, EmailUser, NameUser) values (?,?,?,?,?);", gitter)
            except sqlite3.DatabaseError or sqlite3.ProgrammingError: pass
        # gets Repositorier data
        for repo_data in cursor_from.execute("select nm_repo, host_vl, is_ppa from Repositories;").fetchall():
            try:
                self.cursor.execute("insert into Repositories (nm_repo, host_vl, is_ppa) values (?,?,?);", repo_data)
            except sqlite3.ProgrammingError or sqlite3.DatabaseError: pass
        self.connection.commit()


class DebianPacks(Database):
    """

    """
    
    help_txt = """"""

    class PackageExistsError(Exception):
        args: object = "That package already exists!"

    class PackageNotFound(Exception):
        args: object = "That package can't be find in the database"

    class InvalidDownloadLink(Exception):
        args = "That's not a valid download link!"

    class InvalidCamp(Exception):
        args = "That's not a valid camp from the database!"

    @staticmethod
    def check_file_downloaded(link_file: str) -> bool:
        """

        :param link_file:
        :return:
        """
        sep_link = link_file.split("/")
        return sep_link[-1] in listdir("./deb_bins")


    @staticmethod
    def check_link_download(link: str) -> bool:
        """

        :param link:
        :return:
        """
        return "http://" in link and ".deb" in link and "/" in link


    @classmethod
    def check_debpack_exists(cls, deb_pack_name: str) -> bool:
        """

        :param deb_pack_name:
        :return:
        """
        query_all = cls.cursor.execute("select nm_pack from DebPacks;").fetchall()
        for item in query_all:
            if deb_pack_name == item[0]: return True
        return False

    def add_deb_pack(self, pack_data: list):
        """

        :param pack_data:
        """
        if self.check_debpack_exists(pack_data[0]): raise self.PackageExistsError()
        if not self.check_link_download(pack_data[1]): raise self.InvalidDownloadLink()
        command_insert = self.cursor.execute("insert into DebPacks (nm_pack, link_download, vl_installed) values (?,?,?);", pack_data)
        self.connection.commit()
        del command_insert

    def del_deb_pack(self, deb_pack: str):
        """

        :param deb_pack:
        """
        if not self.check_debpack_exists(deb_pack): raise self.PackageNotFound()
        del_com = self.cursor.execute(f"delete from DebPacks where nm_pack = \"{deb_pack}\";")
        self.connection.commit()
        del del_com

    def alt_deb_pack(self, camp: str, new_vl, deb_pack: str):
        """

        :param camp:
        :param new_vl:
        :param deb_pack:
        """
        if not self.check_debpack_exists(deb_pack): raise self.PackageNotFound()
        if camp not in ["nm_pack", "link_download", "vl_installed"]: raise self.InvalidCamp()
        if camp == "vl_installed":
            query_alt = self.cursor.execute(f"update DebPacks set vl_installed={new_vl} where nm_pack=\"{deb_pack}\";")
        else:
            query_alt = self.cursor.execute(f"update DebPacks set {camp}=\"{new_vl}\" where nm_pack=\"{deb_pack}\";")
        self.connection.commit()
        del query_alt

    def get_deb_packs(self) -> list:
        """

        :return:
        """
        query_db = self.cursor.execute("select * from DebPacks;")
        return query_db.fetchall()

    def install_deb_pack(self, pack="*"):
        """

        :param pack:
        :return:
        """
        if pack == "*":
            data = self.get_deb_packs()
            for deb_item in data:
                sep = str(deb_item[2]).split("/")
                file = sep[-1]
                annimations_cgi.DebPacks.installing_package(deb_item[1])
                if not self.check_file_downloaded(deb_item[2]):
                    check_output(f"cd ./deb_bins && wget {deb_item[2]} && cd ..")
                check_output("sudo apt install ./deb_packs/"+file)
        else:
            if not self.check_debpack_exists(pack): raise self.PackageNotFound()
            data_pack = self.cursor.execute("select nm_pack, link_download, vl_installed from DebPacks;").fetchone()
            sep = str(data_pack[1]).split('/')
            if not self.check_file_downloaded(data_pack[1]):
                check_output(f"cd ./deb_bins && wget {data_pack[1]}")
                if int(data_pack[2]) != 1:
                    self.alt_deb_pack("vl_installed", 1, data_pack[0])
            annimations_cgi.DebPacks.installing_package(data_pack[0])
            check_output(f"sudo apt install ./{sep[-1]} && cd ..")





























