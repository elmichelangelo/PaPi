
class Workspace(object):
    '''
    creates the workspace
    '''
    def __init__(self, root_path, science_path=None, bias_path=None, dark_path=None, flat_path=None,
                 workspace_path=None, workspace_science_path=None, workspace_bias_path=None,
                 workspace_dark_path=None, workspace_flat_path=None, bias_bool=True, dark_bool=True, flat_bool=True):
        super(Workspace, self).__init__()
        self.root_path = os.path.normcase(root_path)
        self.science_path = self.check_if_none(folder_path=science_path, folder_name='light')
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
        self.flat_bool = flat_bool

    def check_if_none(self, folder_path, folder_name):
        '''
        Checks if the folderpath is none.
        :param folder_path: path there the folder is
        :param folder_name: name of the folder
        :return: return the folder
        '''
        if folder_path != None:
            return os.path.normcase(folder_path)
        else:
            return os.path.join(self.root_path, folder_name)

    def run(self):
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
        shutil.rmtree(self.workspace_path)


if __name__ == "__main__":
    import os
    import shutil
    import glob
    workspace_object = Workspace(root_path=r'C:\Users\patri\OneDrive\Uni\Astronomische_Messungen\WR134',
                                 science_path=r'C:\Users\patri\OneDrive\Uni\Astronomische_Messungen\WR134\TestLight\light',
                                 bias_path=r'C:\Users\patri\OneDrive\Uni\Astronomische_Messungen\WR134\TestBiasA\TestBiasB\bias',
                                 dark_path=r'C:\Users\patri\OneDrive\Uni\Astronomische_Messungen\WR134 - Kopie\TestDark\dark',
                                 flat_path=r'C:\Users\patri\OneDrive\Uni\Astronomische_Messungen\WR134\TestFlatA\TestFlatB\TestFlatC\flat',
                                 workspace_path=r'C:\Users\patri\OneDrive\Uni\Astronomische_Messungen\WR134\Ergebnisse',
                                 workspace_science_path=None,
                                 workspace_bias_path=None,
                                 workspace_dark_path=None,
                                 workspace_flat_path=None,
                                 bias_bool=True,
                                 dark_bool=True,
                                 flat_bool=True)
    workspace_object.run()

    workspace_object.undo_workspace()
