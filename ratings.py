"""Restaurant rating lister."""


# put your code here
import sys
import random 

filename = sys.argv[1]
my_file = open(filename)

restaurants_dict = {}

for line in my_file:
    words_list = (line.rstrip()).split(':')
    restaurants_dict[words_list[0]] = int(words_list[1])

while True:
    
    print("Please select one of these:\n\
        See all the ratings (S)\n\
        Add a new restaurant (A)\n\
        Update ratings of an existing restaurant (U)\n\
        Quit (Q)")
    choice =input("S, A, U or Q:  ")
   
    if choice.upper() == "Q":
        break
   
    elif choice.upper() == 'A':
        restaurant = input("Please enter the restaurant name: ")
        rating = int(input("Please enter it's rating: "))

        while rating < 1 or rating > 5:
            print("Please enter a rating between 1 and 5.")
            rating = int(input("Please enter it's rating: ")) 

        restaurants_dict[restaurant.title()] = rating

    elif choice.upper() == 'S':
        for restaurant, rating in sorted(restaurants_dict.items()):
            print("{} is rated at {}." .format(restaurant, rating))

    elif choice.upper() == 'U':
        selection = input("Do you want to choose the restaurant to update? Y/N ")
        
        if selection.upper() == "Y":
            print("Here is the list of restaurants: ")
            for restaurant in restaurants_dict.keys():
                print(restaurant)
            new_rating_for_rest = input("Please enter your choice: ").title()
        else:
            restaurants_list = list(restaurants_dict.keys())
            new_rating_for_rest = random.choice(restaurants_list)
        
        print("Here is the restaurant to change the rating.")
        print(new_rating_for_rest, restaurants_dict[new_rating_for_rest])
        
        new_rating = int(input("Please enter new rating "))

        while new_rating < 1 or new_rating > 5:
            print("Please enter a rating between 1 and 5.")
            new_rating = int(input("Please enter it's rating: ")) 
        
        restaurants_dict[new_rating_for_rest] = new_rating





