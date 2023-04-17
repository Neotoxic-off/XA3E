import argparse

class Arguments:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.args = None
        
        self.__load__()

    def __load__(self):
        required = self.parser.add_argument_group("required")
        required.add_argument(
            "-f",
            "--file",
            action = "append",
            required = True,
            help = "File to encrypt"
        )

        options = self.parser.add_argument_group("optionnal")
        options.add_argument(
            "-k",
            "--key",
            action = "store",
            type = str,
            help = "Use a custom encryption key."
        )
        options.add_argument(
            "-ks",
            "--key-size",
            action = "store",
            type = int,
            help = "Use a custom encryption key length."
        )
        options.add_argument(
            "-p",
            "--progressive-key",
            action = "store_true",
            help = "Use progressive key. The key will evoluate during the encryption."
        )

        self.args = self.parser.parse_args()
