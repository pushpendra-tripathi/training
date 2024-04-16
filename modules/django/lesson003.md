Cohort Day:

# Module: Django

## Subject: Models

### Subtopics: Database relationships

Many to one 
many to many
one to one

### Goal:
By the end of this lesson, you will be able to use database relationships to solve problems.

### Reading


### Assignment
 ## 1. Create a Django Model named Book with the following fields:

    title: A CharField with a maximum length of 100 characters.
    author: A CharField with a maximum length of 50 characters.
    publication_date: A DateField to store the publication date of the book.
    isbn: A CharField with a fixed length of 13 characters to store the ISBN number of the book.

    Next, create a Django Model Form named BookForm that allows users to input information for a new book. Include form fields for each of the model's fields, with appropriate labels and validation rules. Finally, integrate the BookForm into a Django view named add_book so that users can access a web page to submit information for a new book. Upon successful form submission, save the book details to the database and redirect the user to a confirmation page.


   ## 2. Create a Django Model named Car with the following fields:

    make: A CharField with a maximum length of 50 characters to store the car's make (e.g., Toyota, Honda).
    model: A CharField with a maximum length of 50 characters to store the car's model (e.g., Camry, Civic).
    year: An IntegerField to store the car's manufacturing year.
    transmission: A ChoiceField with options for 'Automatic' and 'Manual' transmission types.

    Design a Django Model Form named CarForm that includes form fields for each of the model's fields, with appropriate labels and validation rules. Additionally, ensure that the transmission field is rendered as a set of radio buttons for user selection.



 ##  3. Create a Django Model named Song with the following fields:

    title: A CharField with a maximum length of 100 characters to store the song's title.
    artist: A CharField with a maximum length of 50 characters to store the artist's name.
    genre: A ChoiceField with options for 'Pop', 'Rock', 'Hip Hop', and 'Electronic' genres.
    duration: A FloatField to store the duration of the song in minutes.

    Develop a Django Model Form named SongForm with form fields for each of the model's fields, including a dropdown menu for selecting the song's genre.



   ## 4. Create a Django Model named Movie with the following fields:

    title: A CharField with a maximum length of 100 characters to store the movie's title.
    director: A CharField with a maximum length of 50 characters to store the director's name.
    release_year: An IntegerField to store the year the movie was released.
    rating: A ChoiceField with options for movie ratings ranging from 'G' to 'R'.

    Implement a Django Model Form named MovieForm with form fields for each of the model's fields, including a dropdown menu for selecting the movie rating.



 ## 5. Create a Django Model named JobPosting with the following fields:

    title: A CharField with a maximum length of 100 characters to store the job title.
    company: A CharField with a maximum length of 100 characters to store the company name.
    location: A CharField with a maximum length of 100 characters to store the job location.
    employment_type: A ChoiceField with options for 'Full-time', 'Part-time', and 'Contract' employment types.

    Design a Django Model Form named JobPostingForm with form fields for each of the model's fields, including a dropdown menu for selecting the employment type.


   ## 6. Create two Django Models named Product and Category with the following fields:

    Product:name: A CharField with a maximum length of 100 characters to store the product name.
    description: A TextField to store the product description.
    category: A ForeignKey relationship with the Category model to assign a category to each product.
    Category:name: A CharField with a maximum length of 50 characters to store the category name.

    Develop a Django Model Form named ProductForm with form fields for the name, description, and a dropdown menu for selecting the category. Ensure that the form correctly saves the selected category for each product.



 ##  7. Create two Django Models named Task and Project with the following fields:

    Task:name: A CharField with a maximum length of 100 characters to store the task name.
    description: A TextField to store the task description.
    project: A ForeignKey relationship with the Project model to assign a project to each task.
    Project:name: A CharField with a maximum length of 50 characters to store the project name.
    description: A TextField to store the project description.

    Design a Django Model Form named TaskForm with form fields for the name, description, and a dropdown menu for selecting the project. Ensure that the form correctly saves the selected project for each task.


##   8. Create two Django Models named Post and Category with the following fields:

    Post:title: A CharField with a maximum length of 100 characters to store the post title.
    content: A TextField to store the post content.
    category: A ForeignKey relationship with the Category model to assign a category to each post.
    Category:name: A CharField with a maximum length of 50 characters to store the category name.

    Design a Django Model Form named PostForm with form fields for the title, content, and a dropdown menu for selecting the category. Ensure that the form correctly saves the selected category for each post.



##    9. Create three Django Models named Student, Course, and Enrollment with the following fields:

    Student:name: A CharField with a maximum length of 100 characters to store the student's name.
    Course:name: A CharField with a maximum length of 100 characters to store the course name.
    Enrollment:student: A ForeignKey relationship with the Student model to link each enrollment to a student.
    course: A ForeignKey relationship with the Course model to link each enrollment to a course.
    grade: A CharField with a maximum length of 2 characters to store the student's grade in the course.

    Design a Django Model Form named EnrollmentForm with form fields for selecting a student and a course from dropdown menus, as well as an input field for entering the grade. Ensure that the form correctly saves the enrollment details, including the associated student and course.

