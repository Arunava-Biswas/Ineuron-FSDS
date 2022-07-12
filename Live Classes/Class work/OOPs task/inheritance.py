# imporing modules
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


# Creating parent class
class Student:
    try:
        # constructor
        def __init__(self, f_name, l_name):
            self.f_name = f_name
            self.l_name = l_name

        try:
            def Fullname(self):
                return self.f_name + " " + self.l_name

        except Exception as e:
            logger.error(e)

        try:
            def Email(self):
                logger.info(f"{self.f_name}_{self.l_name}@ineuron.com")

        except Exception as e:
            logger.error(e)

    except Exception as e:
        logger.error(e)


# Creating child class (single inheritance)
class Internship(Student):
    try:
        def Intern(self):
            logger.info(f"{self.Fullname()} is also applicable for internship.")

    except Exception as e:
        logger.error(e)


# Creating child class (multilevel inheritance)
class Job(Internship):
    try:
        def Job_guarantee(self):
            logger.info(f"{self.f_name} {self.l_name} is also applicable for job guarantee program.")

    except Exception as e:
        logger.error(e)


# Creating another class
class Courses:
    try:
        def __init__(self, course):
            self.course = course
        try:
            def Coursename(self):
                logger.info(f"The student has opted for {self.course}.")

        except Exception as e:
            logger.error(e)

    except Exception as e:
        logger.error(e)


# Creating class for counting students
class Counting:
    # creating class variables
    num_of_students = 0

    # creating private method counting students
    def __countStud(self):
        Counting.num_of_students += 1
        return Counting.num_of_students


# Creating class(multiple inheritance)
class iNeuron(Job, Courses, Counting):
    try:
        # constructor
        def __init__(self, f_name, l_name, course):
            Job.__init__(self, f_name, l_name)      # fetching attributes from Job class
            Courses.__init__(self, course)          # fetching attributes from Courses class

        # calling the private method of the Count class
        def Count(self):
            logger.info(f"Number of students increased to: {self._Counting__countStud()}")

    except Exception as e:
        logger.error(e)


# Initializing
i3 = iNeuron("arunava", "biswas", "FSDS")
i4 = iNeuron("rajeev", "kumar", "Data Analytics")
i3.Email()
i3.Intern()
i3.Coursename()
i3.Count()
i4.Email()
i4.Intern()
i4.Coursename()
i4.Count()

