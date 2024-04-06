# Subject: Python
## Topic: Data Structures
## Module: 
<https://docs.python.org/3/tutorial/datastructures.html#data-structures>



### Goal
You should be able to select the appropriate data structure for different tasks, manipulate data within these structures, and leverage built-in functions and methods to efficiently work with collections of data.
### Reading 

### Assignment



# Subject: Python
## Topic: Functions

# Goal: Writing good functions

The purpose of this lesson today is to write as many functions as we can in the best way we can.

## Guidelines

1. All numbers must be formatted in lacs (00,00,000) and crores (00,00,00,000)
2. Precision to two decimal places is required. Round any additional precision to two decimal places.
   

## Worksheet

**1. Simple Interest**

Write a function `simple_interest(principal, term, rate)` that returns the total value of the `principal` that grows simply at the `rate` (per annum) for the given `term` in years.

```python
>>> simple_interest(123456, 23, 0.08)
3,50,615
```

**2. Compound Interest (Basic)**

Write a function `compound_interest(principal, term, rate)` that returns the total value of the `principal` that grows at the compounded `rate` (per annum) for the given `term` in years.

```python
>>> compound_interest(123456, 23, 0.08)
7,24,867
```

**3. Compound Interest (Advanced)**

Write a function `compound_interest_with_payments(principal, payment, term, rate, end_of_period=True)` that returns the total value of the `principal` that grows at the compounded `rate` (per annum) for the given `term` in years assuming that an additional amount of `payment` is added to the amount per term.

`end_of_period` determines whether the additional payment was made at the start or end of the interval and will affect the calcualtion.

Round the result to the nearest paisa.

```python
>>> compound_interest_with_payments(0, 100000, 35, 0.10)
2,36,02,436.85
```

```python
>>> compound_interest_with_payments(0, 368970.52, 35, 0.10)
10,00,00,002.17
```

**4. Savings Calculator**

Write a function `savings_calculator(present_value, future_value, term, rate, end_of_period=True)` which calculates the required payment per interval such that the compounded value given the other parameters will yield a final value equal to `future_value` at the end of `term`.

Round the number up to the nearest paisa.

```python
>>> savings_calculator(0, 1e8, 35, 0.10)
3,68,970.52
```

### Think of a csv file as a two dimensional table and write the following 3 functions

**5. Inner Join**

Given two files, write an inner join function on any number of keys

```python
>>> files_innerjoin(filename1, filename2, **kwargs)
The output file should be named 'results.csv' and should contain the results of the join operation
```

**6. Left Outer Join**

Given two files, write a left outer join function on any number of keys

```python
>>> files_leftouterjoin(filename1, filename2, **kwargs)
The output file should be named 'results.csv' and should contain the results of the join operation
```

**7. Right Outer Join**

Given two files, write a right outer join function on any number of keys

```python
>>> files_leftouterjoin(filename1, filename2, **kwargs)
The output file should be named 'results.csv' and should contain the results of the join operation
```

**8. List of dicts to dict of lists**

Convert a list of dicts to a dict of lists

```python
>>> list_to_dict(data: list)

data = [{"name": "a", "age": 21}, {"name": "b", "age": 43}]
output = {"name": ["a", "b"], "age": [21,43]}
```

**9. Dict of lists to a list of dicts**

Convert a dict of lists to a list of dicts

```python
>>> dict_to_list(data: dict)

data = {"name": ["a", "b"], "age": [21,43]}
output = [{"name": "a", "age": 21}, {"name": "b", "age": 43}]
```

**10. Split a csv file**

Split a large csv file on values of one or more columns into multiple files

```python
>>> split_file(filename, split_cols: list)

example:
if the file has columns name, age, city, is_married
split_cols=["city", "is_married"]

split_file(filename, split_cols)

output: There should two files for each city for married and unmarried

```
## Notes
