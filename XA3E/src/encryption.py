import random

class Encryption:
    def __init__(self, key: str = None, key_size: int = 64, progressive: bool = True):
        self.key = key
        self.key_size = key_size if (key_size != None) else 64
        self.progressive = progressive
        self.padding = '-'

        self.__generate_key__()

    def __update__(self, data: str, index: int, replacement: str):
        return ("{}{}{}".format(
            data[:index],
            replacement,
            data[index + 1:]
        ))
    
    def __progressivity__(self, line: str, index: int):
        line_size = len(line)

        if (self.progressive == True):
            self.key = self.__update__(self.key, index, f"{line_size - (10 * (line_size / 10))}")

    def __generate_key__(self):
        characters = []

        if (self.key == None):
            for i in range(0, self.key_size):
                characters.append(chr(random.randint(32, 126)))
            self.key = "".join(characters)

    def __pack__(self, content: str):
        pack = []
        pack_size = 3
        size = len(content)
        i = 0

        while (i < size):
            if (i + pack_size < size):
                pack.append(content[i:i + pack_size])
            else:
                pack.append(content[i:size])
            i += pack_size
        return (pack)

    def __encrypt__(self, content: list):
        result = []
        buffer = []
        align = 0

        for index, line in enumerate(content):
            for i in range(len(line)):
                align = i if (i < len(self.key)) else 0
                buffer.append(chr(ord(line[i]) ^ ord(self.key[align])))
            result.append("".join(buffer))
            buffer.clear()
            self.__progressivity__(line, index)

        return (result)

    def encrypt(self, content: list):
        packs = self.__pack__(content)

        return (self.__encrypt__(packs))
