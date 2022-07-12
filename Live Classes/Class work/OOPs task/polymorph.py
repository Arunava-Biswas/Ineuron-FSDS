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


# base class
class Ineuron:
    try:
        def Intro(self):
            logger.info("All the students of Ineuron belong to different courses.")

        def Courses(self):
            logger.info("Some belong to FSDS course and some to FSDA.")

    except Exception as e:
        logger.error(e)


# child class 1
class CourseFSDS(Ineuron):
    try:
        # using the same method of base class differently using polymorphism
        def Courses(self):
            logger.info("These students belong to FSDS course and not FSDA.")

    except Exception as e:
        logger.error(e)


# child class 2
class CourseFSDA(Ineuron):
    try:
        def Courses(self):
            # using the same method of base class differently using polymorphism
            logger.info("These students belong to FSDA course and not FSDS.")

    except Exception as e:
        logger.error(e)


# this function behaves like a bridge between all the classes as per the object
def ineuron_external(a):
    a.Intro()
    a.Courses()


# Initializing
i6 = Ineuron()
i7 = CourseFSDS()
i8 = CourseFSDA()

ineuron_external(i6)             # This is for the parent class
ineuron_external(i7)             # This is for child class 1
ineuron_external(i8)             # This is for child class 2


