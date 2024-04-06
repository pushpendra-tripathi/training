# Subject: Django
## Topic: Assessment
## Module:
### Goal
This assessment will test your knowledge and application of Django: one-to-one, foreign key, and many-to-many relationships between models to accurately capture the data structure to effectively organize and manage information.
### Reading
### Assignment

### 1. Create a model for Profile containing following fields:
- slug
- username
- email
- phone
- address

### 2. Create a model for Author containing following fields:
- slug
- name
- profile [one to one to Profile]

### 3. Create a model for Publisher containing following fields:
- slug
- name
- website
- email
- address

### 4. Create a model for Book containing following fields:
- slug
- author [foreign key to Author]
- title
- publisher [foreign key to Publisher]
- date_of_pub


### 5. Create a model for Collection containing following fields:
- slug
- name
- book [many to many to Book]


