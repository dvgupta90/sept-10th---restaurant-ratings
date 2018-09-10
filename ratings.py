"""Restaurant rating lister."""


# put your code here
import sys

filename = sys.argv[1]
my_file = open(filename)

restaurants_dict = {}

for line in my_file:
    words_list = (line.rstrip()).split(':')
    restaurants_dict[words_list[0]] = words_list[1]

for restaurant, rating in sorted(restaurants_dict.items()):
    print("{} is rated at {}." .format(restaurant, rating))