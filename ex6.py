types_of_people = 10
x = f"there are {types_of_people} types of people." #a string is put inside a string
#Variables
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."#a string is put inside a string
#print variables
print(x)
print(y)
#using vaiables in dialouge
print(f"I said: {x}")
print(f"I also said: '{y}'")
#more vaiables and dialouge with inserted varaiable
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"#a string is put inside a string
print(joke_evaluation.format(hilarious))
#variables
w = "this is the left side of..."
e = "a string with a right side."
#adds variables
print(w + e)