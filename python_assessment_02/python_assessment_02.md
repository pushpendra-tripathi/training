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

**5. `search_name()`**

Return a list of names that are a superset of the provided name to be searched.

Searches must be case insensitive.

```
def search_name(data, name):
    return List
```

```
In [1]: search_name(data, "vish")
Out[1]: ["Vishal Apte", "Dhruv Vishveshwar", "Avishka Menon"]
```

**6. `update_name(data)`**

Update email and dob for the record for the given name if there is only one record with that name regardless of capitalization.

Return a tuple of (data, boolean) where `data` is address_book format of data boolean is True if record was updated and False if not

```
def update_name(data, name, email, dob):
    return data, True
```

**7. `delete_name(data, name)`**

Delete the dict entry in the list for the record for the given name if there is only one record with that name regardless of capitalization.

Return a tuple of (data, boolean) where `data` is address_book format of data and boolean is True if record was deleted and False if not

```
def delete_name(data, name):
    return data, True
```

**8. `print_names(data)`**

Print a formatted list of all names in `address_data`.

Data should be sorted by DOB in ascending order.

Date should be in the exact format shown.

Column widths must be as specified exactly:
- Name: 24
- Email: 36
- DOB: 12

```
In [1]: print_names(data)
Out[1]:
Name                    Email                              DOB
Superman                kal-el@krypton.com                 1938-04-18
Bruce Wayne             bruce@wayne.com                    1939-03-30
Bugs Bunny              bugs@warnerbros.com                1940-07-27
```
