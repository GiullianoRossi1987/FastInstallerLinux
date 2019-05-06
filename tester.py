
from datacore import core


installer = core.Installer(file_name="datacore/database.json")

pc1 = {"Package_nm": "Pycharm", "Command": "sudo snap install pycharm-community --classic", "Installed": "True"}

installer.install_pack(pc1)
print("Tudo certo!")
