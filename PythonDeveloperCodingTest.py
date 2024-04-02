import json

def register_user(users, new_user, file_path):
    #Append the new user to the list of exisiting users
    users.append(new_user)
    #open the write mode
    with open(file_path, 'w') as file:
        #write the users list to the file in JSON format
        json.dump(users, file)

def login(email, password, file_path):
    #Open the file in read mode
    with open(file_path, 'r') as file:
        #Load the JSON data from the file into the users list
        users = json.load(file)
        #Iterate through each user in the list
        for user in users:
            #Check if email and password match
            if user['email'] == email and user['password'] == password:
                return user
    return None

def add_movie(movies, new_movie, file_path):
    #Append the new movie to the list of existing movies
    movies.append(new_movie)
    #Open the file in write mode
    with open(file_path, 'w') as file:
        #Write the movies list to the file in JSON format
        json.dump(movies, file)

def add_rating(ratings, new_rating, file_path):
    #Append the new rating to the list of existing ratings
    ratings.append(new_rating)
    #Open the file in write mode
    with open(file_path, 'w') as file:
        #Write the ratings list to the file in JSON format
        json.dump(ratings, file)

def view_all_movies(movies):
    #Iterate through each movie in the list
    for movie in movies:
        print("ID:", movie['id'])
        print("Name:", movie['name'])
        print("Genre:", movie['genre'])
        print("Rating:", movie['rating'])
        print("Release Date:", movie['release_date'])
        print()


def search_movie(movie_name, movies):
    for movie in movies:
        if movie['name'].lower() == movie_name.lower():
            print("\nMovie Details:")
            print("Name:", movie['name'])
            print("Genre:", movie['genre'])
            #print(" avrage Rating:", len(movie['rating'])/sum(movie['rating']+rating_file_path['rating']))
            print("Rating:", movie['rating'])
            print("Release Date:", movie['release_date'])
            return True
    print("Movie not found.")
    return False

'''def search_movie(movies, ratings):
    ## Iterate through each movie in the list
    for movie in movies:
        print("ID:", movie['id'])
        print("Name:", movie['name'])
        print("Genre:", movie['genre'])
        print("Release Date:", movie['release_date'])
        print("Rating: ",movie['rating'])
        #Check if the movie has ratings
        if movie['id'] in ratings:
            #Calculate the total rating for the movie
            total_rating = sum(ratings[movie['id']])
            #Calculate the average rating
            average_rating = total_rating / len(ratings[movie['id']])
            print("Average Rating:", average_rating)
        else:
            print("Average Rating: No ratings yet")
        print()'''

def main():
    user_file_path = 'User.json'
    movie_file_path = 'Movie.json'
    rating_file_path = 'Rating.json'

    #Dictionary to store movie ratings
    '''ratings = {}
    #Open the rating file in read mode
    with open(rating_file_path, 'r') as file:
        #Load the JSON data from the file
        rating_data = json.load(file)
        for rating in rating_data:
            #Get the movie ID from the rating
            movie_id = rating['movie_id']
            #Check if the movie ID already exists in the ratings dictionary
            if movie_id in ratings:
                #If exists, append the rating to the existing list
                ratings[movie_id].append(rating['rating'])
            else:
                #If not exists, create a new list with the rating
                ratings[movie_id] = [rating['rating']]'''

    #Run an infinite loop for the menu
    while True:
        print("\nWelcome to User Login System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        # Prompt the user to enter their choice
        choice = input("Enter your choice: ")

        #If the user chooses to register
        if choice == '1':
            id    = input("Enter the id: ")
            name  = input("Enter your name: ")
            phone = input("Enter your phone number: ")
            password = input("Enter your password: ")
            email = input("Enter your email: ")

            #Create a dictionary for the new user
            new_user = {'id': id, 'name': name, 'phone': phone, 'email': email, 'password': password}
            with open(user_file_path, 'r') as file:
                users = json.load(file)
            #Register the new user
            register_user(users, new_user, user_file_path)
            print("Registration successful!")

        #If the user chooses to login
        elif choice == '2':
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            # Attempt to login with provided credentials
            user = login(email, password, user_file_path)
            # If login is successful
            if user:
                print("Login successful! Welcome,", user['name'])

                #Run an infinite loop for user options after login
                while True:
                    print("\nOptions:")
                    print("1. Add more movies")
                    print("2. View all movies")
                    print("3. Rate a movie")
                    print("4. Search a movie")
                    print("5. Go to home")

                    #Prompt for user option
                    option = input("Enter your option: ")
                    #If the user chooses to add more movies
                    if option == '1':
                        # Allow user to add another movie
                        id=input("Enter id: ")
                        name = input("Enter the movie name: ")
                        genre = input("Enter the movie genre: ")
                        rating = input("Enter the movie rating: ")
                        release_date = input("Enter the movie release date (DD-MM-YYYY): ")

                        #Create a dictionary for the new movie
                        new_movie = {'id': id, 'name': name, 'genre': genre, 'rating': rating, 'release_date': release_date}
                        with open(movie_file_path, 'r') as file:
                            movies = json.load(file)
                        #Add the new movie
                        add_movie(movies, new_movie, movie_file_path)
                        print("Movie added successfully!")

                    #If the user chooses to view all movies
                    elif option == '2':
                        # View all movies
                        with open(movie_file_path, 'r') as file:
                            movies = json.load(file)
                        print("\nAll Movies:")
                        #Call the function to display all movies
                        view_all_movies(movies)

                    #If the user chooses to rate a movie
                    elif option == '3':
                        # Rate a movie
                        id=input('Enter id: ')
                        user_id=user['id']
                        movie_id = input("Enter movie_id: ")
                        rating_value = float(input("Enter your rating (0.0 - 5.0): "))

                        #Create a dictionary for the new rating
                        new_rating = {'id': id, 'user_id': user_id, 'movie_id': int(movie_id), 'rating': rating_value}
                        with open(rating_file_path, 'r') as file:
                            ratings = json.load(file)
                        #Add the new rating
                        add_rating(ratings, new_rating, rating_file_path)
                        print("Rating added successfully!")

                    #If the user chooses to search for a movie
                    elif option == '4':
                        # Search a movie
                        movie_name = input("Enter the name of the movie: ")
                        with open(movie_file_path, 'r') as file:
                            movies = json.load(file)
                        #Call the function to search for the movie
                        #search_movie(movies,ratings)
                        search_movie(movie_name, movies)

                    #If the user chooses to go back to home
                    elif option == '5':
                        break

                    #Print a message for invalid option
                    else:
                        print("Invalid option. Please enter a valid option.")

            #Print a message for invalid login attempt
            else:
                print("Invalid email or password. Please try again.")

        #If the user chooses to exit
        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

#If the script is executed directly
if __name__ == "__main__":
#Call the main function to start the program
    main()