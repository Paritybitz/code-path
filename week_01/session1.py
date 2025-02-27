def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")
    
#greeting("Kevin")
def print_catchphrase(character):
    variable = character.lower()
    if variable == "pooh":
        print("Oh brother!")
    elif variable == "tigger":
        print("TTFN: Ta-ta for now!")
    elif variable == "eeyore":
        print("Thanks for noticing me.")
    elif variable == "christopher robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")
        
#print_catchphrase("Pooh")
#print_catchphrase("Poohh")
items = ["piglet", "pooh", "roo", "rabbit"]
def get_item(items, x):
    if x in range(len(items)):
        print(items[x])
    else:
        print("None")
    #if x < 0 or x > len(items)-1: 
       # print("None")
    #else:
      #  print(items[x])
#get_item(items,2)
#get_item(items,3)
#get_item(items,4)

def sum_honey(hunny_jars):
    sum_honey = 0
    
    for vals in hunny_jars:
        sum_honey += vals
    
    print(sum_honey)

sum_honey([2,3,4,5])

