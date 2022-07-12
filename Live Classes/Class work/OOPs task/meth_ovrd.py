# Using logging
import logging as lg

# creating a logger variable
logger = lg.getLogger(__name__)

# Here we will set the logger to be INFO
logger.setLevel(lg.INFO)

# creating the format
formatter = lg.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s', '%d/%m/%Y %I:%M:%S %p')

# creating the file and setting the path
file_handler = lg.FileHandler('log_files\\OOPs.log')
file_handler.setFormatter(formatter)

# setting up the stream handler, and it's, this will be printed on the console
stream_handler = lg.StreamHandler()
stream_handler.setFormatter(formatter)

# for the printing
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


# creating base class
class Studentclass:
    try:
        def __init__(self, course):
            self.course = course

        # defining method for the base class
        def Course(self):
            logger.info(f"The course attended by the student at the beginning is {self.course}")

    except Exception as e:
        logger.error(e)


# creating child class to override the method
class Changeclass(Studentclass):
    try:
        # constructor
        def __init__(self, course):
            self.course = course

        # defining method for the child class using method overriding
        def Course(self):
            logger.info(f"The course attended by the student after change is {self.course}")

    except Exception as e:
        logger.error(e)


# Initializing
i5 = Studentclass("FSDS")
i5.Course()
# Using the child class to call the same method
i5 = Changeclass("FSDA")
i5.Course()