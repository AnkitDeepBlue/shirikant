import logging

class loggingClass:

    @staticmethod
    def logGen():
        logger = logging.getLogger()

        # Creating Path
        FileHandler = logging.FileHandler("GenratedFile.log")
        # CreateFileFormat
        Formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        FileHandler.setFormatter(Formatter)

        # Passing path to logger
        logger.addHandler(FileHandler)

        # SetLevel
        logger.setLevel(logging.INFO)                        

        return logger


