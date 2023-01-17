# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# ASSIGNMENT STRINGS

# PART 1

# Players who scored in UEFA Euro 1988 Final
player_0 = "Ruud Gullit"
player_1 = "Marco van Basten"

# In which minute was scored?
goal_0 = 32
goal_1 = 54

# Scorers Final
scorers = player_0 + " " + str(goal_0) + ", " + player_1 + " " + str(goal_1)
print(scorers)

# report Final
report = f'{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute'
print(report)

# PART 2

# Full name player
player = "Aron Dasayev"

# Isolate first name Player with SLICE and FIND
first_name = player[:player.find(" ")]  # find

print("first name:", first_name)
print(first_name)

# FIND, SLICING and LEN to isolate and store the length of the last name
last_name = player[player.find(" ")+1:]  # find
print("last name:", last_name)

last_name_len = len(last_name)  # len
print("len lastname:", last_name_len)

# Name short
name_short = f'{first_name[0:1]}. {last_name}'
print(name_short)

# Chant optie 1
'''chant = (f'{first_name}! ' * len(first_name))[:-1]'''

# Chant optie 2:
chant = (f'{first_name}! ' * len(first_name)).strip()
print(chant)

# Good chant
good_chant = chant[-1] != ' '
print(good_chant)
