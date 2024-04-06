 Accounting System
# Subject: 
## Topic: 
## Module:

### Goal
Learn how to implement functions to credit and debit amounts from an account, record transactions with relevant details, store transaction data in a structured format (e.g., CSV), and generate reports based on categories and modes of payment. Gain proficiency in filtering and organizing data for category and payment reports, as well as in presenting reports in a tabular format for easy interpretation. Additionally, generate HTML files for printed reports to enhance presentation options.

### Assignment

### Write a code to develop an accounting system which generates reports based on category, mode of payments and print reports.

**1. Credit your amount**

Write a function `credit(amount)` that credits the amount to your balance.

```python
def credit(amount):
    return balance
```

```python
>>> credit(25000):
75000.00
```

**2. Debit an amount**

Write a function `debit(amount)` that debits the given amount from your account.

```python
def debit(amount):
    return balance
```

```python
>>> debit(10000):
25000.00
```

**3. Transaction**

Write a function `transaction(amount, category, desc, mode_of_payment, credit=False)` to make a transaction.

```python
def transaction(amount, category, desc, mode_of_payment, credit=False):
    return balance
```

**4. Store all data**

Write a function `ledger(date, amount, category, desc, mode_of_payment)` to store all information regarding your account transaction and store in csv file.

```python
def ledger(date, amount, category, desc, mode_of_payment):
    return
```

**5. Generate category report**

Write a function `generate_category_report(filename)` that...
1. Takes a filename containing all data,
2. filter out category such as food, rent, etc, and
3. generate a csv file with the data.
4. Generated file have date, category, desc, amount

```python
def generate_category_report(filename):
    return csv_file
```

```python
>>> generate_category_report(filename)
category.csv
```

**6. Generate payment report**

Write a function `generate_payment_report(filename)` that
1. Takes a filename containing all data,
2. generate a csv file with the data.
3. Generated file have date, mode of payment, amount, desc

```python
def generate_payment_report(filename):
    return csv_file
```

```python
>>> generate_payment_report(filename)
payment.csv
```

**7. Print the report**

Write a function `print_report()` to print data with category as rows and month as columns.

```python
def print_report():
    """
    Print the report
    """
```

```
>>> print_reports()
Category   Month1   Month2
Food       7000     8000
Rent       10000    10000
```

**8. Generate a text file**

Store the printed data in `print_reports()` in txt file.

```python
def generate_txt(data):
    """
    Store the printed data in print_reports() in txt file.
    """
```

**9. Generate random data**

Write a function `generate_random_data()` which generates data to populate ledger file.

```python
def generate_random_data():
    """
    Generate random data for ledger file.
    """
    return
```


--------------
Bonus :-
`Generating HTML File for printed data in print_reports() will be an additional.`
