import os
import shutil
import glob


class Workspace(object):
    """
    creates the workspace
    """
    def __init__(self, strings, use_graphical_user_interface=False, root_path=None, science_path=None, bias_path=None, dark_path=None, flat_path=None,
                 workspace_path=None, workspace_science_path=None, workspace_bias_path=None,
                 workspace_dark_path=None, workspace_flat_path=None, bias_bool=True, dark_bool=True, flat_bool=True):
        super(Workspace, self).__init__()

        if use_graphical_user_interface:
            pass
        else:
            # Enter root path and check if path exist
            str_root_path = input(strings.TXT_ENTER_ROOT_PATH)
            str_root_path = self.check_if_path_exist(
                root_path=str_root_path,
                string=strings.TXT_ROOT_PATH_NOT_FOUND
            )

            # Enter filter types
            lst_filter_types = input(strings.TXT_FILTER_TYPES).split(",")

            # Enter folder name of light images dependent of given filter type and check if folder exist
            lst_path_light_images = []
            for filter_type in lst_filter_types:
                str_folder_light_images = input(strings.TXT_ENTER_FOLDER_NAME_OF_LIGHT_IMAGES_WITH_FILTER %
                                                filter_type)
                str_folder_light_images = self.check_if_path_exist(
                    root_path=str_root_path,
                    string=strings.TXT_FOLDER_NAME_OF_LIGHT_IMAGES_WITH_FILTER_NOT_FOUND,
                    folder_name=str_folder_light_images,
                    filter_type=filter_type
                )
                lst_path_light_images.append(str_folder_light_images)

            # Enter folder name of bias images an check if folder exist
            str_folder_bias_images = input(strings.TXT_ENTER_FOLDER_NAME_OF_BIAS_IMAGES)
            str_folder_bias_images = self.check_if_path_exist(
                root_path=str_root_path,
                string=strings.TXT_FOLDER_NAME_OF_BIAS_IMAGES_NOT_FOUND,
                folder_name=str_folder_bias_images
            )

            # Enter folder name of dark images an check if folder exist
            str_folder_dark_images = input(strings.TXT_ENTER_FOLDER_NAME_OF_DARK_IMAGES)
            str_folder_dark_images = self.check_if_path_exist(
                root_path=str_root_path,
                string=strings.TXT_FOLDER_NAME_OF_DARK_IMAGES_NOT_FOUND,
                folder_name=str_folder_dark_images
            )

            # Enter folder name of flat images dependent of given filter type and check if folder exist
            lst_path_flat_images = []
            for filter_type in lst_filter_types:
                str_folder_flat_images = input(strings.TXT_ENTER_FOLDER_NAME_OF_FLAT_IMAGES_WITH_FILTER %
                                               filter_type)
                str_folder_flat_images = self.check_if_path_exist(
                    root_path=str_root_path,
                    string=strings.TXT_FOLDER_NAME_OF_FLAT_IMAGES_WITH_FILTER_NOT_FOUND,
                    folder_name=str_folder_flat_images,
                    filter_type=filter_type
                )
                lst_path_flat_images.append(str_folder_flat_images)

            self.dict_original_directory = {
                "root path": str_root_path,
                "folder of bias images": str_folder_bias_images,
                "folder of dark images": str_folder_dark_images,
                "filter types": lst_filter_types
            }
            for idx, filter_type in enumerate(lst_filter_types):
                self.dict_original_directory["folder of light images with filter type %s" % filter_type] = \
                    lst_path_light_images[idx]
                self.dict_original_directory["folder of flat images with filter type %s" % filter_type] = \
                    lst_path_flat_images[idx]

            self.dict_working_directory = {
                "root path": os.path.join(str_root_path, "working_directory"),
                "folder of bias images": "bias",
                "folder of dark images": "dark",
                "filter types": lst_filter_types
            }
            for idx, filter_type in enumerate(lst_filter_types):
                self.dict_working_directory["folder of light images with filter type %s" % filter_type] = \
                    lst_path_light_images[idx]
                self.dict_working_directory["folder of flat images with filter type %s" % filter_type] = \
                    lst_path_flat_images[idx]

        self.move_original_data()
        self.create_working_directory()

    def move_original_data(self):
        self.create_folder(self.dict_original_directory["root path"], "original_data")
        shutil.move(
            os.path.join(
                self.dict_original_directory["root path"],
                self.dict_original_directory["folder of bias images"]
            ),
            os.path.join(
                self.dict_original_directory["root path"],
                "original_data",
                self.dict_original_directory["folder of bias images"]
            )
        )
        shutil.move(
            os.path.join(
                self.dict_original_directory["root path"],
                self.dict_original_directory["folder of dark images"]
            ),
            os.path.join(
                self.dict_original_directory["root path"],
                "original_data",
                self.dict_original_directory["folder of dark images"]
            )
        )

        for filter_type in self.dict_original_directory["filter types"]:
            shutil.move(
                os.path.join(
                    self.dict_original_directory["root path"],
                    self.dict_original_directory["folder of light images with filter type %s" % filter_type]
                ),
                os.path.join(
                    self.dict_original_directory["root path"],
                    "original_data",
                    self.dict_original_directory["folder of light images with filter type %s" % filter_type]
                )
            )
            shutil.move(
                os.path.join(
                    self.dict_original_directory["root path"],
                    self.dict_original_directory["folder of flat images with filter type %s" % filter_type]
                ),
                os.path.join(
                    self.dict_original_directory["root path"],
                    "original_data",
                    self.dict_original_directory["folder of flat images with filter type %s" % filter_type]
                )
            )

        for folder in os.listdir(self.dict_original_directory["root path"]):
            if not os.listdir(os.path.join(self.dict_original_directory["root path"], folder)):
                os.rmdir(os.path.join(self.dict_original_directory["root path"], folder))

    @staticmethod
    def copy_data(source_path, target_path):
        file_list = glob.glob(os.path.join(source_path, '*.fits'))
        for idx, file in enumerate(file_list):
            print((idx + 1) / len(file_list) * 100)
            shutil.copyfile(file, os.path.join(target_path, os.path.basename(file)))

    @staticmethod
    def create_folder(path, folder_name=None):
        if folder_name:
            try:
                os.makedirs(os.path.join(path, folder_name))
            except FileExistsError:
                print("The folder '%s' already exist. Pass" % folder_name)
        else:
            try:
                os.makedirs(os.path.join(path))
            except FileExistsError:
                print("The path '%s' already exist. Pass" % path)

    def create_working_directory(self):
        self.create_folder(self.dict_working_directory["root path"])
        self.create_folder(self.dict_working_directory["root path"], "bias")
        self.copy_data(
            os.path.join(
                self.dict_original_directory["root path"],
                "original_data",
                self.dict_original_directory["folder of bias images"]
            ),
            os.path.join(
                self.dict_working_directory["root path"],
                self.dict_working_directory["folder of bias images"]
            )
        )

        self.create_folder(self.dict_working_directory["root path"], "dark")
        self.copy_data(
            os.path.join(
                self.dict_original_directory["root path"],
                "original_data",
                self.dict_original_directory["folder of dark images"]
            ),
            os.path.join(
                self.dict_working_directory["root path"],
                self.dict_working_directory["folder of dark images"]
            )
        )

        for filter_type in self.dict_working_directory["filter types"]:
            self.create_folder(
                self.dict_working_directory["root path"],
                self.dict_working_directory["folder of light images with filter type %s" % filter_type]
            )
            self.copy_data(
                os.path.join(
                    self.dict_original_directory["root path"],
                    "original_data",
                    self.dict_original_directory["folder of light images with filter type %s" % filter_type]
                ),
                os.path.join(
                    self.dict_working_directory["root path"],
                    self.dict_working_directory["folder of light images with filter type %s" % filter_type]
                )
            )

            self.create_folder(
                self.dict_working_directory["root path"],
                self.dict_working_directory["folder of flat images with filter type %s" % filter_type]
            )
            self.copy_data(
                os.path.join(
                    self.dict_original_directory["root path"],
                    "original_data",
                    self.dict_original_directory["folder of flat images with filter type %s" % filter_type]
                ),
                os.path.join(
                    self.dict_working_directory["root path"],
                    self.dict_working_directory["folder of flat images with filter type %s" % filter_type]
                )
            )

    @staticmethod
    def check_if_path_exist(root_path, string, folder_name=None, filter_type=None):
        """
        Checks if the folder path is none.
        :param root_path: path there the folder is
        :param string: path there the folder is
        :param folder_name: name of the folder
        :param filter_type: name of the folder
        :return: return the folder
        """
        fits_in_file = False
        if folder_name:
            if filter_type:
                while not os.path.exists(os.path.join(root_path, folder_name)):
                    folder_name = input(string % (folder_name, root_path, filter_type))

                for fits_image in os.listdir(os.path.join(root_path, folder_name)):
                    if ".fits" in str(fits_image):
                        print(fits_image)
                        fits_in_file = True
                if fits_in_file:
                    return folder_name
                else:
                    raise Exception("No fits image in given folder '%s' found" % os.path.join(root_path, folder_name))
            else:
                while not os.path.exists(os.path.join(root_path, folder_name)):
                    folder_name = input(string % (folder_name, root_path))
                for fits_image in os.listdir(os.path.join(root_path, folder_name)):
                    if ".fits" in str(fits_image):
                        print(fits_image)
                        fits_in_file = True
                if fits_in_file:
                    return folder_name
        else:
            while not os.path.exists(root_path):
                root_path = input(string % root_path)
            return os.path.join(root_path)

    def undo_workspace(self):
        shutil.move(
            os.path.join(
                self.dict_original_directory["root path"],
                "original_data",
                self.dict_original_directory["folder of dark images"]
            ),
            os.path.join(
                self.dict_original_directory["root path"],
                self.dict_original_directory["folder of dark images"]
            )
        )
        shutil.move(
            os.path.join(
                self.dict_original_directory["root path"],
                "original_data",
                self.dict_original_directory["folder of bias images"]
            ),
            os.path.join(
                self.dict_original_directory["root path"],
                self.dict_original_directory["folder of bias images"]
            )
        )
        for filter_type in self.dict_original_directory["filter types"]:
            shutil.move(
                os.path.join(
                    self.dict_original_directory["root path"],
                    "original_data",
                    self.dict_original_directory["folder of light images with filter type %s" % filter_type]
                ),
                os.path.join(
                    self.dict_original_directory["root path"],
                    self.dict_original_directory["folder of light images with filter type %s" % filter_type]
                )
            )
            shutil.move(
                os.path.join(
                    self.dict_original_directory["root path"],
                    "original_data",
                    self.dict_original_directory["folder of flat images with filter type %s" % filter_type]
                ),
                os.path.join(
                    self.dict_original_directory["root path"],
                    self.dict_original_directory["folder of flat images with filter type %s" % filter_type]
                )
            )
        shutil.rmtree(os.path.join(self.dict_original_directory["root path"], "original_data"))
        shutil.rmtree(os.path.join(self.dict_working_directory["root path"]))


if __name__ == "__main__":
    pass
