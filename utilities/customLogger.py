import logging

class LogGen:
    @staticmethod
    def loggen():
        # specify the log format and file path to save
        logging.basicConfig(filename=".\\Logs\\automation.log",format='%(asctime)s: %(message)s',datefmt='%m/%d/%Y %H:%M:%S',force=True)
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger