import yaml

class Yaml:

    def __init__(self):
        self.file_name = 'commands.yaml'
        self.data = None

    def load_yaml(self):
        """
        Loads a YAML file and returns a python object.

        Returns:
            Python Dictionary with all the commands as values.
        """

        try:
            with open(self.file_name, 'r') as f:
                self.data = yaml.safe_load(f)
                return self.data

        except yaml.YAMLError as e:
            print(f"Error parsing YAML file: {e}")
