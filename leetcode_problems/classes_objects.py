# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.
# class print:
#     print(5)

# print
# To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

# class details:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     # __str__
#     def __str__(self):
#         return f"the name is {self.name} and age is {self.age}"
        
# Note: The __init__() function is called automatically every time the class is being used to create a new object.
# p1 = details("siddiq",20)
# print(p1)
# print(p1.age)
# ----------------------------------------------------------------
# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.

# code
# class Myclass:
#     def __init__(self,carname,carprice):
#         self.carname = carname
#         self.carprice = carprice
    
#     # method (inserting a function)
#     def my_func(self):
#         print('Hello welcome sir who bought '+self.carname)

# customer = Myclass('B.M.W',250000)
# customer.my_func()
# print(customer.carname)
# print(customer.carprice)
# ----------------------------------

# The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

# code 
# class Student:
#     def __init__(id,name,add):
#         id.name = name
#         id.add = add
# # object s1 creation
# s1 = Student('kishore','bihar')
# print(f"the student name is {s1.name}")
# print(f"the student address is {s1.add}")
# ---------------------------------------------


# Modify Object Properties

# code 
# class Age:
#     def __init__(self,age):
#         self.age = age
# # a1 object creation
# a1 = Age(30)
# print(a1.age)
# # modifying the object properties
# # changing age 30 to 50
# a1.age = 50
# print(a1.age)
# # -----------------------------------------------
# # Delete the age property from the a1 object:
# del a1.age
# # print(a1.age)
# # You can delete objects by using the del keyword:
# del a1
# print(a1.age)
# --------------------------------------------------------------------------------
'''class definitions cannot be empty, but if you for some reason have a class definition with no content,
 put in the pass statement to avoid getting an error.'''

# # code 
# class Simple:
#     pass

# ----------------------------*******************************---------------------------------------

# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.


# parent class 
# class Info:
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
    
#     # create method in class
#     def Printname(self):
#         print(f"first name is {self.fname} and last name is {self.lname}") 
# # creation of object p1
# p1 = Info('shaik','siddiq')
# p1.Printname()

# # child class 
# '''To create a class that inherits the functionality from another class,
#  send the parent class as a parameter when creating the child class:'''
# class Children(Info):
#     pass
# # Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
# p2 = Children('shaik','Hamza')
# p2.Printname()

# # We want to add the __init__() function to the child class (instead of the pass keyword).
# class child2(Info):
#     def __init__(self,fname,lname):
#     # Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
# # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
#         Info.__init__(self,fname,lname)

# p3 = child2('shaik','muhammad')
# p3.Printname()

# # Creating a class and object with class and instance attributes
# class myclass:
#     # class attribute
#     attr1 = 'mammal'
#     # instance attribute 
#     def __init__(self,name):
#         self.name = name 
# # creating object p1
# p1 = myclass('tommy')
# # Accessing class attributes
# print(f"class attribute is {p1.__class__.attr1}")
# # Accessing instance attributes
# print(f"instance attribute is {p1.name}")
# ---------------------------------------------------
# Super key()
'''By using the super() function, you do not have to use the name of the parent element, 
it will automatically inherit the methods and properties from its parent.'''

# parent class 
# class myclass:
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#     def print_name(self):
#         print(f"first name is {self.fname} and last name is {self.lname} ")
# # child class 
# # class mychild (myclass):
# #     def __init__(self,fname,lname):
# #         super().__init__(fname,lname)
# # object creation
# # p1 = mychild('shaik','hamza')
# # p1.print_name()

# # Add Properties
# class mychild (myclass):
#     def __init__(self,fname,lname,year):
#         super().__init__(fname,lname)
#         # self.graduation_year = 2024
#         '''the year 2024 should be a variable, and passed into the Student class when creating student objects.
#         To do so, add another parameter in the __init__() function:'''
#         self.graduation_year = year
#     # def printchild(self):
#     #     print(f"first name is {self.fname} and last name is {self.lname} . the graduation year is {self.graduation_year}")
#     ''' If you add a method in the child class with the same name as a function in the parent class,
#         the inheritance of the parent method will be overridden.'''
#     def print_name(self):
#         print(f"first name is {self.fname} and last name is {self.lname} . the graduation year is {self.graduation_year}")
# p1 = mychild('shaik','hamza',2024)
# p1.print_name()
# ------------------------------------------------------------------------------------------

# Python Iterators
'''Technically, in Python, an iterator is an object which implements the iterator protocol, 
which consist of the methods __iter__() and __next__().'''

# Iterator vs Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

# All these objects have a iter() method which is used to get an iterator:

# mytuple = ('apple','banana','guava')
# myit = iter(mytuple)
# print(myit)
# print(next(myit))

# Even strings are iterable objects, and can return an iterator:
# string  = 'apple'
# myit = iter(string)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

# We can also use a for loop to iterate through an iterable object:
# for i in string:
#     print(i)
# -------------------------------------------------------------------
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

'''As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), 
which allows you to do some initializing when the object is being created.'''

'''The __iter__() method acts similar, you can do operations (initializing etc.), 
but must always return the iterator object itself.'''

'''The __next__() method also allows you to do operations, 
and must return the next item in the sequence.'''
# class myiterator:
#     def __iter__(self):
#         self.a = 1
#         return self
    
#     def __next__(self):
#         # To prevent the iteration to go on forever, we can use the StopIteration statement.

#         '''In the __next__() method, we can add a terminating condition to raise an error
#         if the iteration is done a specified number of times:'''
#         if self.a <= 20:
#             x = self.a
#             self.a +=1
#             return x 
#         else:
#             raise StopIteration
# p1 = myiterator()
# myiter = iter(p1)
# for i in myiter:
#     print(i)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# --------------------------------------------------------------------------------------

# Polymorphism
'''Polymorphism simply means having many forms. For example, we need to determine 
if the given species of birds fly or not, using polymorphism we can do this using a single function.'''
# class Solution():
#     def maxSubArray(self, nums):
#         self.nums = nums
#         fi = 0
#         li = 0
#         for i in nums[0:]:
#             if i >0:
#                 fi +=1
#                 print(fi)
#                 break
#         for j in nums[::-1]:
#             if j >0:
#                 li +=1
#                 break

#         new_num =nums[(fi-1):-((li)+1)]
#         print(new_num)
# nums = [-1,5,3,4]
# p1 = Solution()
# p1.maxSubArray(nums)


        
        
