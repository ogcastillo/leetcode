import logging
import os
from datetime import datetime
import sys


class FileLogger:
    """ Singleton Logger class that ensures shared logging instance across scripts. """
    _logger_instance = None

    @staticmethod
    def ensure_log_directory():
        """ Ensures the logs directory exists. """
        script_root = os.path.dirname(os.path.abspath(sys.argv[0]))  # Main script root folder
        log_folder = os.path.join(script_root, "logs")
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)
        return log_folder

    @staticmethod
    def get_log_filename():
        """ Returns the log file path, ensuring the log folder exists first. """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Current timestamp
        log_folder = FileLogger.ensure_log_directory()  # Ensure logs directory exists
        folder_name = os.path.basename(os.getcwd())  # Get current folder name
        return os.path.join(log_folder, f"{folder_name}_{timestamp}.log")

    @staticmethod
    def get_logger():
        """ Returns the singleton logger instance. """
        if FileLogger._logger_instance is None:
            FileLogger._logger_instance = logging.getLogger("SharedLogger")
            FileLogger._logger_instance.setLevel(logging.INFO)

            # Create a file handler (logs will be stored in dynamically generated log file)
            handler = logging.FileHandler(FileLogger.get_log_filename(), mode='w')
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - '
                                          'FileName: %(filename)s - FunctionName: %(funcName)s - Message: %(message)s')
            handler.setFormatter(formatter)

            # Add the handlers to the logger
            FileLogger._logger_instance.addHandler(handler)
            FileLogger._logger_instance.addHandler(logging.StreamHandler())

        return FileLogger._logger_instance
