def __init__(self, image): # Constructor (with parameters).
        """ Create a new post. """

    # Define all the instance variables here
        self.image = image
        self.caption = self.caption

# if __name__ = "__main__":

    xxx.xxx()

# instance method

def set_aef(self)
(setter and getter)

# Mutable

if a type is able to change , then it's said to be mutable

if unchangeable , then it's unmutable

list is mutable

for example x = [1,2,3,8,9]; y = x, y.append(5)------this will also change x

and if x = x.append(5), x will become none

if we want to edit a list by deleting elements:

del x[1]

here comes a question:

del x [1:5], it starts from 2nd  wont delete the 6th number

## replace

for example x = "aaaa"

string is immutable, we can only create a new one(assign another value for it	)

when we use x.replace("a","awww"), nothing changes, because string is immutable

we can only do it by x = x.replace("a","awww")

we can print(a[0})

but we cannot a[0] = 5 , because a is immutable

### replace cannot be use in list

# Week 4 : data

# List mutating

append, sort, reserve ， remove, dont produce a new list. they all returns None.

so mylist = mylist.sort will turn mylist into None

HOW to use: mylist.sort()  will automatically change it into a sorted list![1726744182777](image/python9136_note/1726744182777.png)

The expression `[1] * 4` creates a list of four 1's. But putting that in a list and multiplying by 4 creates a list with 4 *identical* references to the same 4-element list. Watch the arrows in Python Tutor closely. This is why when the number 2 is assigned to the third element of the list, it changes in all rows (all rows are the same!).

## Definition

**alias**
Two variables refer to the same object. Changes made with one alias will affect the other.

**cloning**
The process of making a copy of an object.

**sequence**

 is the generic term for an ordered set.

## Dictionary

A dictionary is an unordered collection of key-value pairs.

iterator

An *iterator* is an object that contains a countable number of values.

![1726743653751](image/python9136_note/1726743653751.png)

## methods for dictionary

keys

values（）

items()

get()

get(key,alt)

![1726740416751](image/python9136_note/1726740416751.png)

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(list(inventory.items()))

for k, v in inventory.items():
    print("Got", k, "that maps to", v)

### if get("aaa",888)couldn't find "aaa" in dict, it will print 888  (888 means otherwise)

when mutating dict, it is the same as list

## sets

A set is a collection of unique, unordered items

no repeating elements

a_set = set([1,2,3])
print(a_set)----------{1,2,3}

instructions:

set.union(*others)  ---return a new set that contain both

set.intersection(*other)----contain all elements in common

set.difference(*other)--- elements that are not in *others

set.symmetry_difference(other)--each element that contains in one or another

set.add（）

set.remove()

**set.discard(item) works the same as remove(but will not raise an Keyerror )**

s = {1,2,3}
a_item = s.pop()
print(a_item)
print(s)

in this case, s will become {2,3}

set.clear()  will clean all thing in set and turns it into set()

![1726742552627](image/python9136_note/1726742552627.png)

## tuple

warning: tuple does not support item assignment

x = (1,2)

x[0] = 1

this will raise an error

# OOP

![1726745254807](image/python9136_note/1726745254807.png)

this will run the q in object p

## Glossary

**attribute**
One of the named data items that makes up an instance.

**class**
A user-defined compound type. A class can also be thought of as a template for the objects that are instances of it.

**constructor**
Every class has a “factory”, called by the same name as the class, for making new instances. If the class has an  *initializer method* , this method is used to get the attributes (i.e. the state) of the new object properly set up.

**initializer method**
A special method in Python (called `__init__`) that is invoked automatically to set a newly created object’s attributes to their initial (factory-default) state.

**instance**
An object whose type is of some class. The words instance and object are used interchangeably.

**instance variable**
A variable that stores a value associated with the instance. The instance variables together store the state of an instance.

**instantiate**
To create an instance of a class, and to run its initializer.

**method**
A function that is defined inside a class definition and is invoked on instances of that class.

**object**
A compound data type that is often used to model a thing or concept in the real world. It bundles together the data and the operations that are relevant for that kind of data. Instance and object are used interchangeably.

**object-oriented programming**
A powerful style of programming in which data and the operations that manipulate it are organized into classes and methods.

**object-oriented language**

Object-oriented programming involves four key ideas: encapsulation, information hiding, inheritance, and polymorphism.

* **Encapsulation** is the idea that a class can package some data together with the methods that manipulate the data. This is a powerful capability, and the chief idea that distinguishes OOP from structured programming.
* **Information Hiding** promotes quality code by allowing objects to protect their state against direct manipulation by code using the object. Python, like many languages, provides mechanisms to achieve information hiding, but we do not cover them in this lesson.
* **Inheritance** and **polymorphism** are mechanisms that help to enable code reuse and contract-based programming, and will be covered next week.
* 

**attribute**
One of the named data items that makes up an instance.

**class**
A user-defined compound type. A class can also be thought of as a template for the objects that are instances of it.

**constructor**
Every class has a “factory”, called by the same name as the class, for making new instances. If the class has an  *initializer method* , this method is used to get the attributes (i.e. the state) of the new object properly set up.

**initializer method**
A special method in Python (called `__init__`) that is invoked automatically to set a newly created object’s attributes to their initial (factory-default) state.

**instance**
An object whose type is of some class. The words instance and object are used interchangeably.

**instance variable**
A variable that stores a value associated with the instance. The instance variables together store the state of an instance.

**instantiate**
To create an instance of a class, and to run its initializer.

**method**
A function that is defined inside a class definition and is invoked on instances of that class.

**object**
A compound data type that is often used to model a thing or concept in the real world. It bundles together the data and the operations that are relevant for that kind of data. Instance and object are used interchangeably.

**object-oriented programming**
A powerful style of programming in which data and the operations that manipulate it are organized into classes and methods.

**object-oriented language**
A language that provides features, such as user-defined classes and inheritance, that facilitate object-oriented programming.

A language that provides features, such as user-defined classes and inheritance, that facilitate object-oriented programming.

## Glossary

**abstract class**
A class that cannot be instantiated on its own and is typically used as a blueprint for other classes. It can contain abstract methods, which must be implemented by its subclasses.

**abstract method**
a method that is declared in an abstract class but does not have an implementation in that class. Subclasses of the abstract class must provide an implementation for the abstract method.

**child class**
A class that inherits from a parent class (superclass). The child class, also known as subclass, inherits the attributes and methods of the parent class and can also add its own.

**decorator**
A special type of function that is used to modify the behavior of another function or method. It is often used for adding functionality in a reusable way.

**getter**
A method that allows you to access an attribute in a given class

**inheritance**
A mechanism in OOP where a new class (child class or subclass) is derived from an existing class (parent class or superclass).

**override**
A mechanism in OOP that allows a subclass to provide a specific implementation for a method that is already defined in its superclass

**parent class**
A class from which other classes inherit attributes and methods.

#### **polymorphism**

A concept in OOP where an object can be treated as a superclass type.

**setter**
A method that allows you to set or update the value of an attribute in a class

#### **subclass**

A class that is derived from another class (the superclass or parent class). It inherits attributes and methods from the superclass but can also have additional attributes and methods or override inherited ones.
