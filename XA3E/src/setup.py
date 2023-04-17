import os

from models.folder import Folder

class Setup:
    def __init__(self):
        self.output = Folder(
            path = "encrypted",
            create = True
        )