Cohort Day:

# Module: Python

## Subject: File I/O

### Goal
Understand file input/output (I/O) in Python, as outlined in the provided documentation. Learn how to implement file reading and manipulation tasks, including functions to read and display file contents, count lines and words, search for specific words, manipulate text, and perform character-based formatting.

### Reading

<https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files>


## Assignment 

1. Write a function in python to read the content from a given text file line by line and display the contents of the file on the screen.
    
    > def read_and_print(filename):
    > 

2. Write a function in python to count the number of lines from a given text file which is not starting with an alphabet "T" and print the result. 
    
    > def read_and_count(filename):
    >    ...

3. Write a function in Python to count and display the total number of words in a text file. 
    
    > def count_words(filename):
    >    ...  
    >  

4. Write a function in Python to read lines from a text file. The function should find and print the occurrence of the word "the".
    
    > def count_the(filename):
    > 

5. Write a function in python to read lines from a text file and display those words, which are less than 4 characters.
    > def display_words(filename):


6. Write a function in Python to count the words "this" and "these" in a text file. [Note that the words "this" and "these" are complete words]
    > def count_words(filename):

7. Write a function in Python to count words in a text file those are ending with alphabet "e".
    > def count_ewords(filename):

8. Write a function in Python to count uppercase character in a text file.
    > def count_upper(filename):

9. A text file contains some text, which needs to be displayed such that every next character is separated by a symbol "#". Write a function definition for hash_display() in Python that would display the entire content of the file in the desired format.

    > def hash_display():

    Example :
    If the file has the following content stored in it :
    THE WORLD IS ROUND


    The function hash_display() should display the following content :
    T#H#E# #W#O#R#L#D# #I#S# #R#O#U#N#D#
