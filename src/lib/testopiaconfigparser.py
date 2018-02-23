import ConfigParser

class TestopiaConfigParser(object):

    def __init__(self, config):
        self.parser = ConfigParser.SafeConfigParser()
        # Persist content cases (eg. Uppercase & Lowercase)
        self.parser.optionxform = str
        self.parser.read(config)

    def get_testopia_config(self, section, option):
        return self.parser.get(section, option)

    def get_testopia_config_items(self, section):
        items = []
        if self.parser.has_section(section):
            items = self.parser.items(section)
        return items