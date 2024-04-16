Cohort Day:

# Module: Python

## Subject: Writing Clean Code

### Goal: 
The purpose of the lesson today is to learn how to write clean code.

### Tools
- [pylint](https://eninedev.github.io/developer/pylint)
- [black](https://eninedev.github.io/developer/black)

### Reading
### What is `pylint`

> https://github.com/pylint-dev/pylint

Pylint is a static code analyser. It lyses your code without actually running it. 
It checks for errors, enforces a coding standard, looks for 
[code smell](https://martinfowler.com/bliki/CodeSmell.html), and can 
make suggestions about how the code could be refactored.

_A code smell is a surface indication that usually corresponds to a deeper problem in the system._

### What is `black`

> https://github.com/psf/black

`Black` is an uncompromising Python code formatter. Blackened code looks the same 
regardless of who wrote it and how it was written. Formatting is PEP-8 compliant, 
becomes transparent/invisible after a while, and allows for better focus on the content. 

### Assignment

1. Install `black` and `pylint` in your virtual environment.

2. Run `black` on all your code submitted to-date and commit the updated code.

3. Run `pylint` on all the code. Store the results in a markdown formatted file called
   `pylint_output.md` and upload to the github.

4. ALL future assignments must be blackened and pylint-ed before submission.
