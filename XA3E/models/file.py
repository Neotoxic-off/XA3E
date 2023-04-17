import os

class File:
    def __init__(self, path: str, create: bool = False):
        self.path = path
        self.exists = os.path.exists(path)
        self.create = create

        self.__load__()

    def __load__(self):
        if (self.create == True and self.exists == False):
            os.touch(self.path)
    