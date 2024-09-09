import logging
import datetime
import time

class Logger:

    def __init__(self, file_name):
        self.logger = None
        self.file_name = file_name
        self.date_format = '%Y-%m-%d %H:%M:%S'
        self.formatter = '%(asctime)s - %(levelname)s - %(filename)s - %(message)s'
        self.now = datetime.datetime.now()
        self.log_file_name = f"ray_cluster_{self.now.strftime('%Y-%m-%d_%H')}.log"


    def create_log_file(self):
        logging.basicConfig(
            filename=self.log_file_name,
            level=logging.DEBUG,
            format=self.formatter,
            datefmt=self.date_format
        )
        self.logger = logging.getLogger(self.file_name)
        return self.logger
