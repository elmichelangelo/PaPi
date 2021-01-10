import os


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

            self.dict_original_paths = {
                "root path": str_root_path,
                "folder of bias images": str_folder_bias_images,
                "folder of dark images": str_folder_dark_images
            }
            for idx, filter_type in enumerate(lst_filter_types):
                self.dict_original_paths["folder of light images with filter type %s" % filter_type] = \
                    lst_path_light_images[idx]
                self.dict_original_paths["folder of flat images with filter type %s" % filter_type] = \
                    lst_path_flat_images[idx]

        self.create_folder(self.dict_original_paths["root path"], "original_data")

        """self.science_path = self.check_if_none(folder_path=science_path, folder_name='light')
        self.bias_path = self.check_if_none(folder_path=bias_path, folder_name='bias')
        self.dark_path = self.check_if_none(folder_path=dark_path, folder_name='dark')
        self.flat_path = self.check_if_none(folder_path=flat_path, folder_name='flat')
        self.original_path = os.path.join(self.root_path, 'original')
        self.original_science_path = self.check_if_none(folder_path=science_path, folder_name=r'original\light')
        self.original_bias_path = self.check_if_none(folder_path=bias_path, folder_name=r'original\bias')
        self.original_dark_path = self.check_if_none(folder_path=dark_path, folder_name=r'original\dark')
        self.original_flat_path = self.check_if_none(folder_path=flat_path, folder_name=r'original\flat')
        self.workspace_path = self.check_if_none(folder_path=workspace_path, folder_name=r'workspace')
        self.workspace_science_path = self.check_if_none(folder_path=workspace_science_path,
                                                         folder_name=r'workspace\light')
        self.workspace_bias_path = self.check_if_none(folder_path=workspace_bias_path,
                                                      folder_name=r'workspace\bias')
        self.workspace_dark_path = self.check_if_none(folder_path=workspace_dark_path,
                                                      folder_name=r'workspace\dark')
        self.workspace_flat_path = self.check_if_none(folder_path=workspace_flat_path,
                                                      folder_name=r'workspace\flat')
        self.bias_bool = bias_bool
        self.dark_bool = dark_bool
        self.flat_bool = flat_bool"""

    @staticmethod
    def create_folder(path, folder_name):
        try:
            os.makedirs(os.path.join(path, folder_name))
        except FileExistsError:
            print("The folder '%s' already exist. Pass" % folder_name)

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
        if folder_name:
            if filter_type:
                while not os.path.exists(os.path.join(root_path, folder_name)):
                    folder_name = input(string % (folder_name, root_path, filter_type))
                return folder_name
            else:
                while not os.path.exists(os.path.join(root_path, folder_name)):
                    folder_name = input(string % (folder_name, root_path))
                return folder_name
        else:
            while not os.path.exists(root_path):
                root_path = input(string % root_path)
            return os.path.join(root_path)


    """def run(self):
        '''
        runs the class
        :return:
        '''
        self.__create_folder__(self.original_path, 'Original path')
        self.__create_folder__(self.workspace_path, 'Workspace path')
        self.__create_folder__(self.workspace_science_path, 'Workspace science path')
        self.move_files(self.science_path, self.original_science_path)
        self.copy_files(self.original_science_path, self.workspace_science_path)
        if self.bias_bool:
            self.__create_folder__(self.workspace_bias_path, 'Workspace bias path')
            self.move_files(self.bias_path, self.original_bias_path)
            self.copy_files(self.original_bias_path, self.workspace_bias_path)
        if self.dark_bool:
            self.__create_folder__(self.workspace_dark_path, 'Workspace dark path')
            self.move_files(self.dark_path, self.original_dark_path)
            self.copy_files(self.original_dark_path, self.workspace_dark_path)
        if self.flat_bool:
            self.__create_folder__(self.workspace_flat_path, 'Workspace flat path')
            self.move_files(self.flat_path, self.original_flat_path)
            self.copy_files(self.original_flat_path, self.workspace_flat_path)
        self.verify()

    def verify(self):
        '''
        verify if the folder are created
        :return:
        '''
        pass

    @staticmethod
    def __create_folder__(path, variable_name):
        try:
            os.makedirs(path)
        except FileExistsError:
            print("%s already exist. Pass" % variable_name)

    def move_files(self, source_path, destiny_path):
        shutil.move(source_path, destiny_path)

    def copy_files(self, source_path, destiny_path):
        file_list = glob.glob(os.path.join(source_path, '*.fits'))
        for idx, file in enumerate(file_list):
            print((idx + 1) / len(file_list) * 100)
            shutil.copyfile(file, os.path.join(destiny_path, os.path.basename(file)))

    def undo_workspace(self):
        self.move_files(self.original_science_path, self.science_path)
        if self.bias_bool:
            self.move_files(self.original_bias_path, self.bias_path)
        if self.dark_bool:
            self.move_files(self.original_dark_path, self.dark_path)
        if self.flat_bool:
            self.move_files(self.original_flat_path, self.flat_path)
        shutil.rmtree(self.original_path)
        shutil.rmtree(self.workspace_path)"""


if __name__ == "__main__":
    pass
