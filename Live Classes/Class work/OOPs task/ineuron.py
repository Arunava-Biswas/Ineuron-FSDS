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


# creating class
class Students:
    try:
        # creating class variables
        num_of_students = 0

        # creating constructor
        def __init__(self, f_name, l_name, bt_year):
            self.f_name = f_name
            self.l_name = l_name
            self.bt_year = bt_year

        # creating private method counting students
        def __countStudents(self):
            Students.num_of_students += 1
            return Students.num_of_students

    except Exception as e:
        logger.error(e)


# creating another class
class Batch:
    try:
        def __init__(self, batch_month):
            self.batch_month = batch_month

        # creating a protected method
        def _batchof(self):
            return self.batch_month

    except Exception as e:
        logger.error(e)


# class for multiple inheritance
class Ineuron(Students, Batch):
    try:
        # constructor
        def __init__(self, first, last, year, batch):
            Students.__init__(self, first, last, year)   # fetching attributes from Student class
            Batch.__init__(self, batch)                 # fetching attributes from Batch class

        # creating a public method
        def fullDetails(self):
            logger.info(f"The fullname of the student is: {self.f_name} {self.l_name}")
            logger.info(f"The student belongs to {self._batchof()} batch")

        # calling the private method of the Student class
        def count_student(self):
            logger.info(f"Number of students increased to: {self._Students__countStudents()}")

    except Exception as e:
        logger.error(e)


# creating objects
i1 = Ineuron("Arunava", "Biswas", 1987, "FSDS-May")
i2 = Ineuron("New", "User", 1997, "FSDS-May")
i1.fullDetails()
i1.count_student()
i2.fullDetails()
i2.count_student()


