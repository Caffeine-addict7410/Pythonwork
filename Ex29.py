#variables
people = 20
cats = 30
dogs = 15

# if there is more people then cats or dogs then a text if there are more cats or dogs then people then other text will appear
if people < cats:
    print("to many cats ! The world is doomed!")
    
if people > cats:
    print("Not many cats! the world is saved!")
    
if people < dogs:
    print("The world is drooled on!")
    
if people > dogs:
    print("The world is dry!")
    
 #dogs more or less ten 5   
dogs += 5

if people >= dogs:
    print("people are greater than or equal to dogs.")
    
if people <= dogs:
    print("People are less than or equal to dogs.")
    
    
if people == dogs:
    print("people are dogs")