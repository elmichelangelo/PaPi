from handler.create_workspace import Workspace


class PaPiMain(object):
    def __init__(self, strings):
        self.workspace = Workspace(strings)


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

    print(papi_test.workspace.dict_original_directory)
