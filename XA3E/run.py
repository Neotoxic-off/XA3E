#!/bin/env python3

import os

from src.arguments import Arguments
from src.setup import Setup
from src.encryption import Encryption

class XPE:
    def __init__(self):
        self.arguments = Arguments()
        self.Setup = Setup()
        self.Encryption = Encryption(
            key = self.arguments.args.key,
            key_size = self.arguments.args.key_size,
            progressive = self.arguments.args.progressive_key
        )

        self.__encrypt__()

    def __open__(self, file: str):
        lines = []

        if (os.path.exists(file) == True):
            with open(file, 'r', encoding = "utf-8") as f:
                lines = f.read()

        return (lines)

    def __save__(self, file: str, content: str):
        splitted = file.split('/')
        file_name = splitted[len(splitted) - 1]

        with open(f"{self.Setup.output.path}/{file_name}", "w+", encoding = "utf-8") as f:
            f.write(content)

    def __encrypt__(self):
        encrypted = None
    
        for file in self.arguments.args.file:
            print(file)
            encrypted = self.Encryption.encrypt(self.__open__(file))
            self.__save__(file, "".join(encrypted))

if (__name__ == "__main__"):
    XPE()
