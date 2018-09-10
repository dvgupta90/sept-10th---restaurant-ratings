"""Restaurant rating lister."""


# put your code here
import sys

filename = sys.argv[1]
my_file = open(filename)

restaurants_dict = {}

for line in my_file:
    words_list = (line.rstrip()).split(':')
    restaurants_dict[words_list[0]] = words_list[1]

while True:
    choice =input("would you like to add your ratings? Y/N ")
    if choice.upper() == "N":
        break

    restaurant = input("Please enter the restaurant name: ")
    rating = input("Please enter it's rating: ")
    restaurants_dict[restaurant.title()] = rating



for restaurant, rating in sorted(restaurants_dict.items()):
    print("{} is rated at {}." .format(restaurant, int(rating)))

