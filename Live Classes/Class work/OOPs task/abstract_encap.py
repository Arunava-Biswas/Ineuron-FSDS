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


# Abstraction part
class Courses:
    # Creating attributes
    course1 = "Data Science"        # public
    _course2 = "Web Development"    # protected
    __course3 = "Data Analytics"    # private


class Course1(Courses):
    try:
        def Coursename(self):
            logger.info(f"The first course is: {Courses.course1}")

    except Exception as e:
        logger.error(e)


class Course2(Courses):
    try:
        def __init__(self):
            Courses.__init__(self)

        try:
            def Coursename1(self):
                logger.info(f"The second course is: {self.course2}")

        except Exception as e:
            logger.error(e)

        try:
            def Coursename2(self):
                logger.info(f"The second course is: {self._course2}")

        except Exception as e:
            logger.error(e)

    except Exception as e:
        logger.error(e)


class Course3(Courses):
    try:
        def __init__(self):
            Courses.__init__(self)

        try:
            def Coursename1(self):
                logger.info(f"The third course is: {self.course3}")

        except Exception as e:
            logger.error(e)

        try:
            def Coursename2(self):
                logger.info(f"The third course is: {self._Courses__course3}")

        except Exception as e:
            logger.error(e)

    except Exception as e:
        logger.error(e)


# Encapsulation part
class Blog:
    # Constructor
    def __init__(self):
        self.__blog1 = "Python"

    try:
        def Blogname(self):
            logger.info(f"The blog is about {self.__blog1}")

    except Exception as e:
        logger.error(e)

    # Creating a method to change the value of the attribute
    try:
        def Newblogname(self, new_value):
            self.__blog1 = new_value
            logger.info(f"Now the blog is changed")

    except Exception as e:
        logger.error(e)


# Initializing
c1 = Course1()
c2 = Course2()
c3 = Course3()
b1 = Blog()

c1.Coursename()
try:
    c2.Coursename1()    # this will throw an error as we try to call a protected attribute of the parent class
except Exception as e:
    logger.error(e)

c2.Coursename2()    # here we will be able to print the value of the protected attribute

try:
    c3.Coursename1()  # this will throw an error as we try to call a private attribute of the parent class
except Exception as e:
    logger.error(e)

c3.Coursename2()  # here we will be able to print the value of the private attribute

b1.Blogname()

# Now try to change the value of the attribute of the class
try:
    b1.__blog1 = "Java"
    b1.Blogname()           # here the value will remain same due to encapsulation
except Exception as e:
    logger.error(e)

# Now try to do the same using the class method
try:
    b1.Newblogname("Java")
    b1.Blogname()           # here the value will change
except Exception as e:
    logger.error(e)





