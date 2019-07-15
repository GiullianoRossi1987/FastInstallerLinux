# coding = utf-8
# using namespace std
from progressbar import *
# from datacore.core import *


class GitterAnimations(object):

    @classmethod
    def clone_repo(cls, repo: str):
        bar = ProgressBar(widgets=[
            "[Preparing to Clone Repository "+repo+" ", widgets.Percentage(), " ] ", Bar(marker="/")
        ], maxval=100)
        bar.start()
        for i in bar(range(100)):
            time.sleep(0.1)
            bar.update(i)
        bar.finish()
        del bar


    @classmethod
    def config_repo(cls, repo):
        bar = ProgressBar(widgets=[
            "[Preparing to Configure Repository "+repo+" ", Percentage(), "]", Bar(marker="/")
        ], maxval=100)
        bar.start()
        for i in bar(range(100)):
            time.sleep(0.2)
            bar.update(i)
        bar.finish()

    @classmethod
    def add_repo(cls, repo: str):
        bar = ProgressBar(widgets=[
            "[Adding Repository "+repo+" ", Percentage(), "]", Bar(marker="/")
        ], maxval=100)
        bar.start()
        for i in bar(range(100)):
            time.sleep(0.01)
            bar.update(i)
        bar.finish()

    @classmethod
    def del_repo(cls, repo: str):
        bar = ProgressBar(widgets=[
            "[Removing Repository " + repo + " ", Percentage(), "]", Bar(marker="/")
        ], maxval=100)
        bar.start()
        for i in bar(range(100)):
            time.sleep(0.01)
            bar.update(i)
        bar.finish()

    @classmethod
    def alt_repo(cls, repo: str):
        bar = ProgressBar(widgets=[
            "[Altering Repository " + repo + " Data ", Percentage(), "]", Bar(marker="/")
        ], maxval=100)
        bar.start()
        for i in bar(range(100)):
            time.sleep(0.01)
            bar.update(i)
        bar.finish()

    @classmethod
    def show(cls):
        bar = ProgressBar(widgets=[
            "[Reading the Database ", Percentage(), "]", Bar(marker="/")
        ], maxval=100)
        bar.start()
        for i in bar(range(100)):
            time.sleep(0.1)
            bar.update(i)
        bar.finish()


class InstallerAnimation(object):

    @classmethod
    def install_pack(cls, pack: str):
        bar = ProgressBar(widgets=[
            "[Preparing to Install " + pack + " ", Percentage(), "]", Bar(marker="/")
        ], maxval=100)
        bar.start()
        for i in bar(range(100)):
            time.sleep(1)
            bar.update(i)
        bar.finish()

    @classmethod
    def add_pack(cls, pack: str):
        bar = ProgressBar(widgets=[
            "[Adding " + pack + " to Database", Percentage(), "]", Bar(marker="/")
        ], maxval=100)
        bar.start()
        for i in bar(range(100)):
            time.sleep(0.1)
            bar.update(i)
        bar.finish()

    @classmethod
    def del_pack(cls, pack: str):
        bar = ProgressBar(widgets=[
            "[Removing " + pack + " ", Percentage(), "]", Bar(marker="/")
        ], maxval=100)
        bar.start()
        for i in bar(range(100)):
            time.sleep(0.1)
            bar.update(i)
        bar.finish()

    @classmethod
    def alt_pack(cls, pack: str):
        bar = ProgressBar(widgets=[
            "[Altering" + pack + " Data ", Percentage(), "]", Bar(marker="/")
        ], maxval=100)
        bar.start()
        for i in bar(range(100)):
            time.sleep(0.2)
            bar.update(i)
        bar.finish()

    @classmethod
    def show(cls):
        bar = ProgressBar(widgets=[
            "[Reading Database", Percentage(), "]", Bar(marker="/")
        ], maxval=100)
        bar.start()
        for i in bar(range(100)):
            time.sleep(0.1)
            bar.update(i)
        bar.finish()


class GenericSystem(object):

    @classmethod
    def start_all_system(cls):
        bar = ProgressBar(widgets=[
            "[Initializing System With Interface ", Percentage(), "]", Bar(marker="/")
        ], maxval=10)
        bar.start()
        for i in bar(range(10)):
            time.sleep(0.02)
            bar.update(i)
        bar.finish()

    @classmethod
    def start_installer_system(cls):
        bar = ProgressBar(widgets=[
            "[Initializing Installer With Interface ", Percentage(), "]", Bar(marker="/")
        ], maxval=10)
        bar.start()
        for i in bar(range(10)):
            time.sleep(0.02)
            bar.update(i)
        bar.finish()

    @classmethod
    def start_gitter_system(cls):
        bar = ProgressBar(widgets=[
            "[Initializing Gitter With Interface ", Percentage(), "]", Bar(marker="/")
        ], maxval=10)
        bar.start()
        for i in bar(range(10)):
            time.sleep(0.02)
            bar.update(i)
        bar.finish()


class BackupAnime(object):

    def sending_to_backup(self):
        bar = ProgressBar(widgets=[
            "[Setting Database Backup as Default", Percentage(), "]", Bar(marker="/")
        ], maxval=100)
        bar.start()
        for i in bar(range(100)):
            time.sleep(0.2)
            bar.update(i)
        bar.finish()

    def creating_database(self):
        bar = ProgressBar(widgets=[
            "[Setting Database Backup as Default", Percentage(), "]", Bar(marker="/")
        ], maxval=100)
        bar.start()
        for i in bar(range(100)):
            time.sleep(0.2)
            bar.update(i)
        bar.finish()


class RepositoryAnime(object):

    def adding_to_db(self, repo: str):
        bar = ProgressBar(widgets=[
            "[Adding "+repo+"To the database ", Percentage(), "]", Bar(marker="/")
        ], maxval=100)
        bar.start()
        for i in bar(range(100)):
            time.sleep(0.1)
            bar.update(i)
        bar.finish()

    def removing_from_db(self, repo: str):
        bar = ProgressBar(widgets=[
            "[Removing" + repo + "from the database ", Percentage(), "]", Bar(marker="/")
        ], maxval=100)
        bar.start()
        for i in bar(range(100)):
            time.sleep(0.1)
            bar.update(i)
        bar.finish()

    def altering_db(self, repo: str):
        bar = ProgressBar(widgets=[
            "[Updating Data From  " + repo, Percentage(), "]", Bar(marker="/")
        ], maxval=100)
        bar.start()
        for i in bar(range(100)):
            time.sleep(0.1)
            bar.update(i)
        bar.finish()

    def reading_db(self):
        bar = ProgressBar(widgets=[
            "[Reading the database", Percentage(), "]", Bar(marker="/")
        ], maxval=100)
        bar.start()
        for i in bar(range(100)):
            time.sleep(0.1)
            bar.update(i)
        bar.finish()

    def config_repo(self, repo: str):
        bar = ProgressBar(widgets=[
            "[Configuring "+repo, Percentage(), "]", Bar(marker="/")
        ], maxval=100)
        bar.start()
        for i in bar(range(100)):
            time.sleep(0.1)
            bar.update(i)
        bar.finish()





























