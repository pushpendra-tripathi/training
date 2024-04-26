# Assessment

## Instructions

1. Write your name and the date on every page of the question sheet and the answer sheet
2. You will have 60 minutes to complete this assignment
3. You may not use a computer while taking this assessment; all computers must be turned off.
4. You may not use a phone while taking this assessment; all phones must be turned in.

## Assessment

You are going to write an address book application using the os module, file io and emplying dictionaries and lists.

You will hold all data in the session in the variable `address_book`

Format of address_book will always be

```
[
    {
        "name": "bugs bunny",
        "email": "bugs@warnerbros.com",
        "dob": "1940-07-27"
    },
    {
        "name": "bruce wayne",
        "email": "bruce@wayne.com",
        "dob": "1939-03-30"
    }
]
```

## Example

We will run something similar to this sequence of commands

```python
data = read_file("address.json")
list_names(data)
data = delete_name(data, name)
print_names(data)
write_file(data)
```

```python
data = read_file()
list_names(data)
data = add_name(data, name, email, dob)
print_names(data)
write_file(data, "address.json")
```

## Questions

**1. `read_file(filename)`**

Input file is address_file if provided and $HOME/addressbook.json if not provided.

Assume that all data is stored in the input file as JSON.

Return a list of dictionaries where each dictionary is one address record.

```
def read_file(json_file: str = None):
    """
    Read in a json file and return a list of dictionaries in address_book format
    """
    return
```

```python
data = read_file()
```

**2. `write_file(data, filename)`**

Write the contents of address_book to a json file.

Use the file specified in json_file if provided and in $HOME/addressbook.json if not. 

Output format of the file must be JSON.

Return the number of records written if successful. Return None if not successful.

```
def write_file(address_book, json_file):
    return -1
```

```python
number_of_records = write_file(data)
```

```python
number_of_records = write_file(data, "fubar.json")
```

**3. `list_names(data)`**

Retun a list of names in address_book.

```
In [1]: list_names(data)
Out[1]: ["Bugs Bunny", "Bruce Wayne"]
```

**4. `add_name()`**

Add the name to `address_data` if and only if there is no existing record with the same name, email, and dob.

Return a tuple of (data, boolean) where `data` is address_book format of data and boolean is True if record was created and False if record already existed.

```
def add_name(data, name, email, dob):
    return (data, False)
```

```
In [1]: data, created = add_name(data, "Superman", "kal-el@krypton.com", "1938-04-18")
```


**5. Given two lists, a and b [use list comprehension only],** 

* Create a new list by picking the odd numbers from a and even numbers from b 
    - Example: 
        - a = [1, 2, 3, 4, “a”, “b”] 
        - b = [5, 6, 7, 8, “c”, “d”]
        - result = [1, 3, 6, 8] 
* Create a new list by picking from a where the index number is odd and from b where the index number is even 
    - Example: 
        - a = [1, 2, 3, 4, “a”, “b”] 
        - b = [5, 6, 7, 8, “c”, “d”] 
        - result = [1, 3, “a”, 6, 8, “d”] 
* Create a new list by picking from a where the index number is odd and the value is not a string and from b where the index number is even and the value is a string. 
    - Example: 
        - a = [1, 2, 3, 4, “a”, “b”]  
        - b = [5, 6, 7, 8, “c”, “d”] 
        - result = [1, 3, “d”] 

**6. Create a list containing 72165 random items (Ex: list of random numbers) and count the occurrence of each unique element.**

**7. Given a list of natural numbers till 100, write a list comprehension that contains only even numbered values that have odd number indices.**

**8. Write a function prime_numbers(n) that prints all prime numbers between, and including, 1 and n.**
* Example:
    - prime_numbers(31) will return [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] 
    - prime_numbers(32) will return [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] 

