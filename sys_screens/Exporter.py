# coding = utf-8
# using namespace std
from datacore.core import DatabaseExporter
from os import system as check_output


class MainExporterScreen(DatabaseExporter):
    """
    Contains the main screen for the exportation system
    """

    def main_screen_exporter(self):
        """
        That's the main screen, for the user export and fork some data on the databases!.
        It works like the all whole screens in the system.
        :raise self.EndOfUsage: To warn the system that the use of the option ended.
        """
        while True:
            check_output("clear")
            while True:
                print(self.exporter_logo + """

    [1] Export to database
    [2] Import from database
    [3] Help
    [4] Exit
                    """)
                opc = int(input(">>> "))
                confirm = int(input("Confirm that option?\n[1] Yes\n[2] No\n>>> "))
                if confirm == 1: break
            if opc == 1:
                c = True
                while True:
                    check_output("clear")
                    path_db_to = str(input("Type the path from the database to export: "))
                    confirm = int(input("Confirm that data?\n[1] Yes\n[2] No\n[3] Cancel\n>>> "))
                    if confirm == 3:
                        c = False
                        break
                    if confirm == 1: break
                if c:
                    self.export_data_to(path_db_to)
                    input("Exported data successfully!\n<<press any button to return>>")
                continue
            elif opc == 2:
                c = True
                while True:
                    check_output("clear")
                    path_db_import = str(input("Type the path to the database to import: "))
                    confirm = int(input("Confirm that data?\n[1] Yes\n[2] No\n[3] Cancel\n>>> "))
                    if confirm == 3:
                        c = False
                        break
                    if confirm == 1: break
                if c:
                    self.import_from(path_db_import)
                    input("Imported successfully!\n<<press any button to return>>")
                continue
            elif opc == 3:
                check_output("clear")
                print(self.help_str)
                input("<<press any button to return>>")
                continue
            elif opc == 4:
                raise self.EndOfUsage()
            else:
                print("That's not a valid option!\nTry it again!")
                input("<<press any button to return>>")
                continue




