class File:
    def __init__(self, name, size, content):
        self.name = name
        self.size = size
        self.content = content


class Folder:
    def __init__(self, name, files, subfolders):
        self.name = name
        self.files = files
        self.subfolders = subfolders

    def add_file(self, File):
        return -1

    def add_folder(self, Folder):
        return -1

    def list_conents(self):
        return -1

    def search_file(self, file_name):
        return -1
