# Tokenizing and Parsing - Part I

## Introduction [^1]

A _tokenizer_ breaks a stream of text into tokens, usually by looking for whitespace (tabs, spaces, new lines).

A _lexer_ is basically a tokenizer, but it usually attaches extra context to the tokens -- this token is a number, that token is a string literal, this other token is an equality operator.

A _parser_ takes the stream of tokens from the lexer and turns it into an abstract syntax tree representing the (usually) program represented by the original text.

The best book on the subject for many decades was [Compilers: Principles, Techniques, and Tools](https://www.amazon.in/dp/0321486811/), aka "The Dragon Book".

## Worksheet

**1. Tokenizer**

Write a function that takes a string `target` and returns all tokens that start with `prefix` and end with `suffix`, inclusive, and returns a list of
items that match.

Add `tokenizer.py` and add the function as stubbed.

```python
tokenizer(target, prefix, suffix):
    return list_of_tokens_that_match
```

**2. Better Tokenization**

Can you describe three limitations of the function described, which if addressed, could allow this code to be more useful and reuseable?

Write your answer in `tokenizer.md`

**3. Scraping a webpage**

Write a function that takes a url and returns a list of all urls that are only referenced as ahrefs in the response text. Make sure to use the tokenizer function you wrote in Part 1.

```python
get_url_list(url):
    # do something
    url_list = tokenizer(webpage_source, prefix, suffix)
    # do something else
    return url_list
```

**4. Infix to postfix**

Take an infix expression `(a + b) ^ c - d / q` and render it as a postfix expression. 

The output must be a list that can be processed as postfix.

Make no assumptions about spacing or other delimiters.

Add your function to the file `tokenizer.py`.

```python
infix_to_postfix(infix_expression: str):
    # do stuff
    return postfix_result
```

*Example*

```python
>>> infix_to_postfix("a+b*c+d")
["a", "b", "c", "*", "+", "d", "+"]
```

## Notes

