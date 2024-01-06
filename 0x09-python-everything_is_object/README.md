# Everything is an Object

## 🔍 **Understanding Objects in Python:**
In Python, an object is a fundamental concept representing a data structure that encapsulates data (attributes) and the methods (functions) that operate on the data. Objects are instances of classes and possess a unique identity, type, and value. For instance, when you create an object of class `Person`, it could have attributes such as `name` and `age`, along with methods like `get_age()`.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an object (instance) of the Person class
john = Person("John", 25)
```

🏗 **Distinguishing Between a Class and an Object:**
A class acts as a blueprint or template for creating objects, defining their structure and behavior. An object, also known as an instance, is a concrete realization of that blueprint. Multiple objects can be created from a single class, each with its unique attributes and methods.

```python
class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

# Creating an object (instance) of the Circle class
circle_instance = Circle(5)
```

🔄 **Immutable vs Mutable Objects:**
Immutable objects cannot be modified once created, while mutable objects can be changed after creation. Examples of immutable objects include strings and tuples, whereas lists and dictionaries are mutable, allowing modifications like adding or removing elements.

```python
# Immutable object (string)
immutable_string = "Hello"

# Mutable object (list)
mutable_list = [1, 2, 3]
```

🔗 **Understanding References in Python:**
In Python, a reference is a way to access the memory location of an object. When you create a variable and assign it an object, the variable holds a reference to that object rather than the object itself.

```python
a = [1, 2, 3]
b = a  # Both 'a' and 'b' reference the same list object
```

📝 **Assignment in Python:**
Assignment is the process of binding a name to an object in Python. For instance, `x = 10` assigns the name `x` to the integer object `10`.

```python
x = 10
```

🔄 **Understanding Aliases:**
An alias occurs when two or more variables refer to the same object. If you change the object through one variable, the change is reflected in the other variable as well.

```python
original_list = [4, 5, 6]
alias_list = original_list  # 'alias_list' is an alias for 'original_list'
```

🔍 **Checking Object Identity and Linkage:**
Use the `is` keyword to check if two variables refer to the exact same object in memory. On the other hand, using `==` checks for equality in terms of object value.

```python
c = [1, 2, 3]
d = c
are_identical = c is d  # 'are_identical' is True

e = [1, 2, 3]
f = [1, 2, 3]
are_linked = e == f  # 'are_linked' is True
```

🔍 **Displaying the Variable Identifier:**
Utilize the `id()` function in Python to obtain the memory address (identifier) of an object.

```python
variable_id = id(x)
```

🔄 **Understanding Mutable and Immutable Objects:**
Mutable objects can be modified after creation, while immutable objects retain the same value throughout their lifetime.

```python
# Immutable object (tuple)
immutable_tuple = (1, 2, 3)

# Mutable object (dictionary)
mutable_dict = {'a': 1, 'b': 2}
```

🧱 **Built-in Mutable Types:**
Common built-in mutable types include lists, dictionaries, and sets. These objects can be modified after creation.

```python
# Mutable list
list_example = [1, 2, 3]

# Mutable dictionary
dict_example = {'name': 'John', 'age': 25}
```

🧱 **Built-in Immutable Types:**
Common built-in immutable types encompass integers, floats, strings, tuples, and frozensets. Once created, these objects cannot be altered.

```python
# Immutable integer
int_example = 42

# Immutable string
str_example = "Hello, World!"
```

🔄 **Passing Variables to Functions in Python:**
Python passes variables to functions by passing references to objects. Modifications to mutable objects persist outside the function, while immutable objects create a new object upon modification.

```python
def modify_list(lst):
    lst.append(4)

mutable_list_example = [1, 2, 3]
modify_list(mutable_list_example)  # 'mutable_list_example' is modified outside the function
```