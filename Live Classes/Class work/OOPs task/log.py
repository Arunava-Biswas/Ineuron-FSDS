
# importing the modules
import logging as lg
import ineuron
import inheritance
import meth_ovrd
import polymorph
import abstract_encap


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