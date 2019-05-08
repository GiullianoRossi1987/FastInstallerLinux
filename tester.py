
from datacore import core


installer = core.Installer(file_name="datacore/database.json")

dt = {"Package_nm": "Pycharm", "Command":"sudo snap install pycharm-commuinity --classic"}
installer.add_package(dt)
