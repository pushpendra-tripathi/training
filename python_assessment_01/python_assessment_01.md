# Assessment

## Instructions

1. Put your Name on every question and answer page
2. You will have 60 minutes to complete this assessment
3. All computers must be turned off while completing this assessment
4. All phones must be turned off and turned in while completing this assessment

## Question 1 - `number_of_matches(n: int)`

Write a Python function, `number_of_matches()` that takes an integer `n` as input, representing the number of teams in a tournament. 

The function should calculate and return the total number of matches that will be played, where each team plays against every other team exactly once.

## Question 2 - `exclude(a, b, c)`

Write a Python function that takes three lists as input and returns the elements that are present in both the first and second lists but not in the third list. The order of elements in the output does not matter.

### Sample

```
In [1]: a = [1, 2, 3, 4, 5]

In [2]: b = [3, 4, 5, 6, 7]

In [3]: c = [5, 6, 7, 8, 9]

In [4]: exclude(a, b, c)
Out[4]: [3, 4]
```

## Question 3 - `mathcalc(e: str)`

Write a Python function `mathcalc()` that takes a mathematical expression as a string, where the expression involves addition ('x+y') or subtraction ('x-y'), and returns the result. x and y will be less than or equal to 1000.

### Sample

```
In [1]: mathcalc("12+34")
Out[1]: 46
```
```
In [2]: mathcalc("500-34")
Out[2]: 466
```

## Question 4 - `dict_transform(data)`

Write a Python function that takes a list of employee dictionaries as input, where each dictionary contains 'name', 'age', and 'department' as keys. The function should convert this list into a dictionary where the keys are department names, and the values are lists of names belonging to each department. If there are no employees in a particular department, the list for that department should be empty

### Sample

```
employee_list = [
    {"name": "Rahul", "age": 30, "department": "Accounts"},
    {"name": "Amit", "age": 25, "department": "HR"},
    {"name": "Priya", "age": 28, "department": "Accounts"},
]
```

```
In [2]: dict_transform(employee_list)
Out[2]: {
    "Accounts": ["Rahul", "Priya"],
    "HR": ["Amit"]
}
```

## Question 5 - `flatten()`

Write a Python function `flatten()` to flatten a nested list. The function should take a nested list as input and return a flattened list. 

### Output

```
In [1]: flatten([2, [4, 3], 5, [6, 7, 8]])
Out[1]: [2, 4, 3, 5, 6, 7, 8]
```

## Question 6 - `cointoss(n)`

Write a Python function `cointoss` that simulates tossing n coins and returns the percentage of heads and tails. 

`n` is an input and represents the number of coin tosses

Return a dictionary with 'heads' and 'tails' as keys and their corresponding percentages as values. Percentages should be rounded to two decimal places

### Sample

```
In [1]: cointoss(32)
Out[1]: {"heads": 48.35, "tails": 51.65}
```

## Question 7 - `wordcount(sentence: str)`

Write a Python function that takes a `sentence` as input and returns a dictionary where 
- key = integer
- value = list of all words whose length is equal to the key

Assume that words are separated by spaces and there is no punctuation

### Sample

```
In [1]: wordcount("This sentence has many four letter words")
Out[1]: {
    3: ["has"], 
    4: ["This", "many", "four"], 
    5: ["words"], 
    6: ["letter"], 
    8: ["sentence"]
}
```

## Question 8 - `nthroot(n, a, b)`

Write a function that returns a dictionary of keys from a to b and values of True/False if the nth root of the key is an integer

### Sample

```
In [1]: nthroot(2, 1, 10)
Out[1]: {
	1: True,
	2: False,
	3: False,
	4: True,
	5: False,
	6: False,
	7: False,
	8: False,
	9: True,
	10: False
}
```
