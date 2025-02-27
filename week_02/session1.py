def total_treasure(treasure_map):
    sum = 0
    for key in treasure_map.keys():
			sum += treasure_map[key]
    return sum

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasures(treasure_map1)) 
print(total_treasures(treasure_map2))


##
def can_trust_message(message):
    message_set = set()
    counter = 0
    
    stripped = message.replace(" ". "")
    "".join("  hello  apple  ".split())
    for i in stripped:
      
      if i != " ":
        if i in message_set:
          continue
        else:
          message_set.add(i)
          counter += 1

    
    if len(message_set) == 26:
      return True
  	else:
      return False
  

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))



# Question 3 
from collections import Counter
def find_duplicate_chests(chests):
  set_of_chests= Counter(chests) # gives you {4: 1, 3: 2, 2: 2, ...}
  output = []
	for key in set_of_chests.keys():
    if set_of_chests[key] == 2:
      output.append(key)
  return sorted(output)
      
chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))
  
  
# Question 4

# First go through once and count how many of each letter
def is_balanced(code):
  code_dict= Counter(code) # gives you {4: 1, 3: 2, 2: 2, ...}
  val_set = list(set(code_dict.values()))

  if len(val_set) > 2:
    return False
  else:
    if abs(val_set[0] - val_set[-1]) == 1:
        return True
    else:
        return False

  
  
# Second time: go through all the values and count how many of each distinct value



# Checks:
# Size of dictionary for the second iteration is 2


# Larger key is one more than other key


# Larger key has value 1