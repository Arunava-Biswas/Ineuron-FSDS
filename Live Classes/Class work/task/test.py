import logging as lg

lg.basicConfig(filename="logfile.log", level=lg.DEBUG, format='%(asctime)s : %(levelname)s : %(name)s : %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')


class List:
    def __init__(self, lst):
        self.lst = lst

    try:

        def extract_list(self):
            for i in self.lst:
                if type(i) == list:
                    print(i)
            print("\n")

        def extract_dict(self):
            for i in self.lst:
                if type(i) == dict:
                    print(i)
            print("\n")

        def extract_tuple(self):
            for i in self.lst:
                if type(i) == tuple:
                    print(i)
            print("\n")

        def num_key_values(self):
            for i in self.lst:
                if type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int or type(v) == int:
                            print(k, v)
            print("\n")

        def sum_num_data(self):
            summation = 0
            for i in self.lst:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            summation += j

                if type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int or type(v) == int:
                            summation += k
                            summation += v
            print(summation)
            print("\n")

        def odd_values(self):
            l1 = []
            for i in self.lst:
                if type(i) == list:
                    for j in i:
                        if type(j) == int:
                            if j % 2 == 1:
                                l1.append(j)
            print(l1)
            print("\n")

        def find_text(self):
            for i in self.lst:
                if type(i) == list:
                    for j in i:
                        if j == "ineuron":
                            print(i.index(j), j)
                if type(i) == dict:
                    for k, v in i.items():
                        if v == "ineuron":
                            print(k, v)
            print("\n")

        def num_of_occur(self):
            lst1 = []
            for i in self.lst:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        lst1.append(j)
                if type(i) == dict:
                    for k, v in i.items():
                        lst1.append(k)
                        lst1.append(v)

            for i in set(lst1):
                print(i, ":", lst1.count(i))
            print("\n")

        def num_of_keys(self):
            d = {}
            for i in self.lst:
                if type(i) == dict:
                    d.update(i)

            print("\nNumber of keys: ", len(d))

        def string_data(self):
            l1 = []
            for i in self.lst:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == str:
                            l1.append(j)
                if type(i) == dict:
                    for k, v in i.items():
                        if type(k) == str or type(v) == str:
                            l1.append(k)
                            l1.append(v)

            print("\nAll the strings are: ")
            for i in l1:
                print(i)
            print("\n")

        def alpha_num(self):
            d = {}
            for i in self.lst:
                if type(i) == dict:
                    d.update(i)

            for i in list(d.keys()):
                n = str(i)
                if n.isalnum() == True:
                    print(n)
            print("\n")

        def multi(self):
            lst = 1
            tup = 1
            s = 1
            d = 1
            res = 1

            for i in self.lst:
                if type(i) == list:
                    for j in i:
                        if type(j) == int:
                            lst = lst * j
            print("The multiplication result for all list elements is: ", lst)

            for i in self.lst:
                if type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            tup = tup * j
            print("The multiplication result for all tuple elements is: ", tup)

            for i in self.lst:
                if type(i) == set:
                    for j in i:
                        if type(j) == int:
                            s = s * j
            print("The multiplication result for all set elements is: ", s)

            for i in self.lst:
                if type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int or type(v) == int:
                            d = d * k
                            d = d * v
            print("The multiplication result for all dict elements is: ", d)

            res = res * lst * tup * s * d
            print("The multiplication result for all int elements is: ", res)
            print("\n")

        def unwrap(self):
            lst1 = []
            for i in self.lst:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        lst1.append(j)
                if type(i) == dict:
                    for k, v in i.items():
                        lst1.append(k)
                        lst1.append(v)
            print(lst1)

    except Exception as e:
        lg.exception(e)

    else:
        lg.info("All the list functions worked perfectly.")


# class Tuple:
#
# class Dictionary:
#
# class Set:

class String:
    def __init__(self, str):
        self.str = str

    try:
        def slice(self):
            return self.str[1:300:3]

        def rev(self):
            return self.str[-1:0:-1]

        def convert_split(self):
            upper_str = self.str.upper()
            return upper_str.split()

        def low(self):
            return self.str.lower()

        def cap(self):
            return self.str.capitalize()

    except Exception as e:
        lg.exception(e)

    else:
        lg.info("All the string functions worked perfectly.")


s = String("this is My First Python programming class and i am learNING python string and its function")
# Try to extract data from index one to index 300 with a jump of 3
print(s.slice())
# Try to reverse a string without using reverse function
print(s.rev())
# Try to split a string after conversion of entire string in uppercase
print(s.convert_split())
# Try to convert the whole string into lower case
print(s.low())
# Try to Capitalize the whole string.
print(s.cap())

l = List([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) ,
     {'k1' : "sudh", 'k2' : "ineuron", 'k3' : "kumar", 3:6, 7:8} , ['ineuron', 'data science']])

# Try to extract all the list entity
l.extract_list()
# Try to extract all the dictionary entity
l.extract_dict()
# Try to extract all the tuples entity
l.extract_tuple()
# Try to extract all the numeric data which may be part of dict key and values
l.num_key_values()
# Try to give summation of all the numeric data.
l.sum_num_data()
# Try to filter out all the odd values out of all numeric data which is a part of a list
l.odd_values()
# Try to extract "ineuron" out of the data
l.find_text()
# Try to find out a number of occurrences of all the data
l.num_of_occur()
# Try to find out number of keys in dict element
l.num_of_keys()
# Try to filter out all the string data
l.string_data()
# Try to find out alphanum in data
l.alpha_num()
# Try to find out multiplication of all numeric values in the individual collection inside dataset
l.multi()
# Try to unwrap all the collection inside collection and create a flat list
l.unwrap()