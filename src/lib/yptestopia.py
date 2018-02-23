from testopia import Testopia
from testopiaconfigparser import TestopiaConfigParser

class YPTestopia(Testopia):
    def __init__(self, config):
        parser = TestopiaConfigParser(config)
        self.url = parser.get_testopia_config("Testopia","url")
        self.username = parser.get_testopia_config("Testopia","username")
        self.password = parser.get_testopia_config("Testopia","password")
        super(YPTestopia, self).__init__(self.username, self.password, self.url, sslverify=False)
