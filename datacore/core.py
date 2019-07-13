# coding = utf-8
# using namespace std
import sqlite3
from os import chdir
from os import system as check_output  # gambiarra
from datacore import annimations_cgi

__doc__ = """
This is the main database system. You can import this file, or easily start the main file (installer.py)
The database use only two tables on the database: database.db
And it have all the important and used data for configure repositories and download packages.
"""

__version__  = 0.4


class Database(object):
    __doc__ = """
    The all classes core, where's declared the database connection, and it's cursor.
    Without this class the system's nothing.
    :connection: connect to the database
    """
    connection = sqlite3.connect("./datacore/database.db", timeout=10)
    cursor = connection.cursor()
    closed = bool
    started = bool

    def __init__(self):
        """Start the connection and declare the cursor.Maybe not useful. But there is it."""
        self.closed = False
        self.started = True


    def close(self):
        """Closes the connection and the cursor, also it alerts the system there was a closed connection"""
        self.cursor.close()
        self.connection.close()
        self.closed = True


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
    def query_package(cls) -> list: # todo: retirar sistema de querys e colocar so pra mostrar o banco de dados.
        """"""
        annimations_cgi.InstallerAnimation.show()
        return cls.cursor.execute("select Nm_Pack, Command from Packages;").fetchall()

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
        return cls.cursor.execute("select Nm_Git, Host_Git, Remote_Nm, EmailUser, NameUser from Gits;").fetchall()


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




