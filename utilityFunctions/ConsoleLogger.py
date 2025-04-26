import logging

class SingletonType(type):
    """ A metaclass for Singleton implementation. """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class ConsoleLogger(metaclass=SingletonType):
    """ Singleton Logger class. """
    def __init__(self):
        self.logger = logging.getLogger("SingletonLogger")
        if not self.logger.hasHandlers():  # Prevent multiple handlers
            self.logger.setLevel(logging.INFO)
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - FileName: %(filename)s -  FunctionName: %(funcName)s - Message: %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger

