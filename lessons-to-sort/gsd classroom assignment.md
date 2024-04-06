# Voyage

## Mission

Build a web application that allows 
- teachers to track courses, students, and assignments, and
- students to track their assignments, submissions, and grades.

## Data Model

Color coding:<br>
– Gray lines = `on_delete=DO_NOTHING`<br>
– Red lines = `on_delete=CASCADE`

[![Voyage Data Model](voyage.png)](voyage.png)

## Tasks

1. **Set up the project**
   - Clone the project
   - Set up a database
   - Get it running
2. Create Random Data
   - 5 faculty, 
   - 10 students,
   - 3 programs
   - 3 courses, 
   - 28 content,
   - 5 assignments, and
   - some student assignments

3. Populate all model methods that are stubbed but not populated

4. Admin - Faculty
   - Show the number of courses each faculty is teaching
   - Show the number of assignments by each faculty
   - Show the number of assignments graded by each faculty
   - Course and assignments data should be linked to the correctly filtered list of Course and 
     Assignment models.

5. Admin - Students
   - Show the program each student is enrolled in
   - Show the number of courses each student is enrolled in
   - Show the number of assignments assigned to the student
   - Show the number of assignments each student has submitted
   - Show the average grade of each student
   - Program and number of courses, assignments, etc. should be a link to query for the 
     selected params and filter the right model page accordigly.

6. Admin - Content
    - Show the number of courses that use each content
    - Show the number of assignments that use each content

7. Admin - Programs 
   - Show the number of courses in each program
   - Show the number of students in each program

8. Admin - Courses
   - Show the number of assignments in each course
   - Show the number of assignments that are completed and graded 100%

9. Admin - Assignments
   - Show the average grade of each assignment

10. Dashboard - Faculty
    - List all courses
    - Show the number of students in each course
    - Show the number of assignments in each course

11. Dashboard - Student
    - List all courses
    - Show the number of assignments in each course
    - List all assignments
    - Show the average grade of each assignment
    - List all submissions
    - Show the number of submissions for each assignment

12. Create a new Course
    - Add cbv `views/appviews/CreateNewCourse(TemplateView)` to `views/appviews.py`
    - Add url `/course/new/` to `urls/appurls.py`
    - Add form to create a new course
    - Add template to render the form

13. Create a new Assignment
    - Add cbv `views/appviews/CreateNewAssignment(TemplateView)` to `views/appviews.py`
    - Add url `/assignment/new/` to `urls/appurls.py`
    - Add form to create a new assignment
    - Add template to render the form
    - Make a copy of the course repo for each student
