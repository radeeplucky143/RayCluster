import yaml
from logger_util import Logger

class Yaml:

    def __init__(self):
        self.file_name = 'commands.yaml'
        self.data = None
        self.logger = Logger(__name__).create_log_file()

    def load_yaml(self):
        try:
            with open(self.file_name, 'r') as f:
                self.logger.info(f'Loading the {self.file_name} file')
                self.data = yaml.safe_load(f)
                return self.data

        except yaml.YAMLError as e:
            self.logger.error(f"Error parsing YAML file: {e}")
