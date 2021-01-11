import sys
import pickle
import os
from handler.create_workspace import Workspace


class PaPiMain(object):
    def __init__(self, strings):
        self.workspace = Workspace(strings)

    def run(self):
        while True:
            command = input("Enter cmd: ")
            if command == "undo":
                self.workspace.undo_workspace()
            elif command == "save":
                self.save_analysis()
            elif command == "load":
                self.load_analysis()
            elif command == "new":
                self.workspace.create_workspace()
            elif command == "exit":
                sys.exit()

    def save_analysis(self):
        save_name = input("Save analysis as: ")
        self.workspace.dict_working_directory["path of save files"] = os.path.join(
            self.workspace.dict_working_directory["root path"],
            save_name
        )
        self.workspace.create_folder(self.workspace.dict_working_directory["path of save files"])
        sf_working_directory = open(
            os.path.join(self.workspace.dict_working_directory["path of save files"], "working_directory.dat"),
            'wb'
        )
        pickle.dump(str(self.workspace.dict_working_directory), sf_working_directory)
        sf_working_directory.close()
        sf_origin_directory = open(
            os.path.join(self.workspace.dict_working_directory["path of save files"], "origin_directory.dat"),
            'wb'
        )
        pickle.dump(str(self.workspace.dict_original_directory), sf_origin_directory)
        sf_origin_directory.close()

    def load_analysis(self):
        save_name = input("Path of save file: ")
        save_directory = os.listdir(os.path.join(self.workspace.dict_working_directory["root path"], save_name))
        # TODO hier weiter arbeiten
        for save_file in save_directory:
            save_file = open(
                os.path.join(save_name),
                'rb'
            )
            loaded_file = pickle.load(save_file)
            save_file.close()


def set_language():
    lang = input("Enter language: ")
    lan_string = None
    if lang == "en":
        import strings.eng_strings as lan_string
    elif lang == "de":
        import strings.ger_strings as lan_string
    return lan_string


if __name__ == "__main__":
    # lan_strings = set_language()
    import strings.eng_strings as lan_strings

    papi_test = PaPiMain(lan_strings)
    papi_test.run()
