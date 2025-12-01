# Movie Rating Analyzer Program
# Write a Python program that:
# 1. Accepts the number of movies.
# (Example: 5 movies)
# 2. Takes the names of the movies into a list.
# 3. Takes the ratings (0–10) of each movie into another list.
# 4. Write the following functions and use them in your program:
# Function 1: getHighest(ratings)
# Function 2: getAverage(ratings)
# Function 3: moviesAbove(movies, ratings, x)
# Function 4: badMovies(movies, ratings)
'''output should look like:Highest Rating: <value>
Average Rating: <value>
Movies Above 8: <list>
Bad Movies (Rating < 5): <list>
create a menubased program
'''
def getHighest(ratings):
    return max(ratings)
def getAverage(ratings):
    return sum(ratings) / len(ratings)
def moviesAbove(movies, ratings, x):
    result = []
    for i in range(len(ratings)):
        if ratings[i] > x:
            result.append(movies[i])
    return result
def badMovies(movies, ratings):
    result = []
    for i in range(len(ratings)):
        if ratings[i] < 5:
            result.append(movies[i])
    return result
num = int(input("Enter number of movies: "))
movies = []
ratings = []
for i in range(num):
    name = input(f"Enter movie #{i+1} name: ")
    movies.append(name)
    while True:
        try:
            rating = float(input(f"Enter rating for '{name}' (0–10): "))
            if 0 <= rating <= 10:
                ratings.append(rating)
                break
            else:
                print("Rating must be between 0 and 10.")
        except:
            print("Please enter a valid number.")
while True:
    print("Movie Rating Analyzer Programme")
    print("1. Show Highest Rating")
    print("2. Show Average Rating")
    print("3. Show Movies Above a Rating")
    print("4. Show Bad Movies (Rating < 5)")
    print("5. Exit")
    choice = input("Enter choice (1–5): ")
    if choice == "1":
        print("Highest Rating:", getHighest(ratings))
    elif choice == "2":
        print("Average Rating:", round(getAverage(ratings), 2))
    elif choice == "3":
        x = float(input("Enter the minimum rating: "))
        print("Movies Above", x, ":", moviesAbove(movies, ratings, x))
    elif choice == "4":
        print("Bad Movies (Rating < 5):", badMovies(movies, ratings))
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
