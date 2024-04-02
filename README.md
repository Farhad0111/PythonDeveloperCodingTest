# PythonDeveloperCodingTest
 
a.	Mention of the language and the database (if any) used 

Soln: The project is implemented using the Python programming language, incorporating various library functions and object-oriented programming principles. It utilizes JSON as the database format for storing data. The project involves solving problems using object-oriented design and implementing functionalities using Python libraries.


b.	Any setup instructions.
Soln: No setup is required for the project.


c.	Any assumptions you have made
Soln: The project file is named PythonDeveloperCodingTest.py. Upon running the Python file, a page will display "Welcome to the User Login System" with three choices.
The first choice is "Register," which is defined as the `register_user` function within the Python file. This function is connected to the User.json file. Its purpose is to allow users to register their accounts. During registration, the user is prompted to enter their ID, name, phone number, password, and email address. After completing the registration, the system will display "Registration successful!" and return to the home page with the same three options.
The second choice is the "Login" option, defined as the `login` function. This function verifies whether the entered email address and password match the records in the User.json file. If the credentials are correct, the page will display "Login successful! Welcome, [user's name]" and present five additional options.

  
  1.	Option 1, "Add more movies," allows users to input details of a new movie. Upon selecting this option, the page prompts the user to enter the following information: 
    - Movie ID
    - Movie Name
    - Movie Genre
    - Movie Rating
    - Movie Release Date (DD-MM-YYYY)
  Once the user completes entering the details, the data is stored in the 'Movie.json' file, and the message "Movie added successfully!" is displayed. The page then presents the user with the original five options again.


  2.	Option 2, "View all movies," displays the details of all movies saved in the 'Movie.json' file. The information shown includes the Movie ID, Name, Genre, Rating, and Release Date for each movie. The page then presents the user with the original five options again.


  3.	Option 3, "Rate a movie," allows users to provide a rating for a specific movie. Users are prompted to enter the following information:
    - Id 
    - Movie ID
    - User's Rating (0.0 – 5.0)
  After entering the required data, it is stored in the 'Rating.json' file, and the message "Rating added successfully!" is displayed. The page then presents the user with the original five options again.


  4.	Option 4, "Search a movie," enables users to search for a movie from both the 'Movie.json' and 'Rating.json' files. If a user searches for a movie by name, the page displays the following details:
    - Movie Name
    - Genre
    - Rating
    - Release Date
  (Note: The calculation of the average rating for the searched movie is commented out to ensure the code is executable.) After displaying the movie details, the page presents the user with the original five options again.


  5.	Option 5, "Go to home," allows users to return to the home screen, where they are presented with the initial three options:
    1. Register
    2. Login
    3. Exit
  This option enables users to navigate back to the main menu of the User Login System.

  
If a user selects the third choice, "Exit," the page displays "Exiting..." and the user is logged out, terminating their session. This option allows users to gracefully exit the User Login System.


d.	How much of the problem you were able to solve
Soln: Selecting the appropriate database was one of the most challenging aspects of the project. However, after careful consideration and evaluation, a suitable solution was found. The overall system design encompasses various functionalities such as user registration, login and movie rating. This design allows for a comprehensive and user-friendly user login system, facilitating smooth navigation and interaction for users.


e.	Problems faced with incomplete parts (if any)
Soln: The calculation of the average rating is an incomplete part of the system. This feature aims to provide users with valuable insights by displaying the average rating for a particular movie. However, this functionality requires further development and integration into the system to ensure accurate and reliable results.
