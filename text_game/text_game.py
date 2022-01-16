from character_classes import Talker, Walker, Fighter
from enemy_classes import Goblin
from random import random

player = ''
random_encounter = 0

def start_game():
  print("Great. I am so glad you decided to play")
  print("The next thing you will need to do is create a character.")
  print("Would you like to play as a talker, walker, or a fighter")
  class_input = input(">")
  input_interpreter(class_input, "CLASS")
  print(player)
  print(f"Welcome {player.name}. The journey before you is long but meaningful. The world will be better for it")
  while player.health_points > 0:
    print("where whould we go? left, right or forward")
    direction_input = input(">")
    input_interpreter(direction_input, "DIRECTION")

def battle_engage():
  print(" A GOBLIN approaches")
  goblin = Goblin("Gobby", "stabby")
  print(f'I be {goblin.name}. This here in my hand is {goblin.name_of_weapon} and it craves your blood')
  while player.health_points > 0 and goblin.health_points > 0:
    print("What do you do? run, fight, befriend")
    battle_input = input(">")
    input_interpreter(battle_input, "BATTLE", goblin)
  print("you died. Lame")

  print("You won a battle")
  random_encounter = 0

def shop_engage():
  print("You bought all that stuff")

def enter_town():
  print("You talked to all the people")

def move_in_direction(direction_choice):
  global random_encounter
  if random_encounter > 3:
    battle_engage()
    return
  outcome = random()
  if direction_choice == "left":
    if outcome < .40:
      random_encounter += 1
      return print("The path conitinues")
    else:
      battle_engage()
      return
  elif direction_choice == "right":
    if outcome < .40:
      random_encounter += 1
      return print("The path conitinues")
    else:
      shop_engage()
      return
  elif direction_choice == "forward":
    if outcome < .40:
      random_encounter += 1
      return print("The path conitinues")
    else:
      enter_town()
      return

def class_creation(class_chosen):
  print(class_chosen)
  print("What would you like your characters name to be?")
  input_character_name = input(">")
  print("What would you like to name your weapon?")
  input_weapon_name = input('>')
  global player
  player = class_chosen(input_character_name,input_weapon_name)

def start_output(input):
  if input == "yes":
    start_game()
  elif input == "no":
    print('Okay, you lose.')

def class_output(input):
  if input == "talker":
    class_creation(Talker)
  elif input == "walker":
    class_creation(Walker)
  elif input == "fighter":
    class_creation(Fighter)

def direction_output(input):
  if input == "left":
    move_in_direction("left")
  elif input == "right":
    move_in_direction("right")
  elif input == "forward":
    move_in_direction("forward")

def faster_opponent(faster_opponent,slower_opponent):
  print(f"{faster_opponent.name}: Your death is assurred. assureded. a sure d. assured ")
  outcome = random()
  if outcome < .5:
    slower_opponent.health_points = slower_opponent.health_points - faster_opponent.attack_points
    print(f"{slower_opponent.name} now has HP:{slower_opponent.health_points}")
  else:
    print(f"-{faster_opponent.name} missed their attack -")
  if slower_opponent.health_points > 0:
    outcome = random()
    if outcome < .8:
      print(f"{slower_opponent.name}: Its not over that easy")
      faster_opponent.health_points = faster_opponent.health_points - slower_opponent.attack_points
      print(f"{faster_opponent.name} now has HP:{faster_opponent.health_points}")
      return faster_opponent, slower_opponent
    else:
      print(f"-{slower_opponent.name} missed their attack -")
      return slower_opponent
  else:
    print(f"Bummer {slower_opponent.name} died")
    return slower_opponent

def battle_output(battle_input, enemy):
  global player
  if battle_input == "run":
    if enemy.speed > player.speed:
      print(f"You can not run away from {enemy.name}")
      return 
    else:
      print(f"-{player.name} ran away-")
      return

  if battle_input == "befriend":
    outcome = random()
    if outcome < .5:
      print(f"{player.name}: Hey {enemy.name}, Do you think you have time to talk about what has been bothering you at home? ")
      print(f"{enemy.name}: What do you mean 'player.species'?")
      print(f"{player.name}:I just mean, why are we fighting. I don't even know you")
      print(f"{enemy.name}: Well things have been hard lately")
      print(f"Invite {enemy.name} to be part of your party. yes or no")
      befriend_input = input('>')
      input_interpreter(befriend_input, "BEFRIEND", enemy)
      return
    else:
      print(f"{player.name}: Hey {enemy.name}, Do you think you have time to talk about what has been bothering you at home? ")
      print(f"{enemy.name}: What?! I fight you now!")
      player.health_points = player.health_points - enemy.attack_points
      print(f"{player.name} now has HP:{player.health_points}")
      return 

  if battle_input == "fight":
    if enemy.speed > player.speed:
      faster_opponent(enemy,player)
    else:
      faster_opponent(player,enemy)



def befriend_output(input, friend):
  if input == "yes":
    print(f"{player.name}: Why dont you join me on this quest so we can make it better for everyone ")
    outcome = random()
    if outcome < .5:
      print(f"{friend.name}: Okay, {player.name} I will join you")
      player.party.append(friend)
      player.attack_points = player.attack_points + friend.attack_points
    else:
      print(f"{friend.name}: I don't have time for this")
      print(f"-{friend.name} ran away -")
      friend.health_points = 0
      return friend
  elif input == "no":
    print(f"{player.name}: Do you think you can just let me pass at the moment?")
    print(f"{friend.name}: Yeah, I don't even know what I am doing these days")
    print(f"-{friend.name} walked away -")
    friend.health_points = 0
    return friend

def show_inventory():
  return player.view_inventory()

def input_interpreter(input, definition_of_input, other_character = None):
  if input == "inventory":
    return show_inventory()
  if definition_of_input == "START":
    start_output(input)
  if definition_of_input == "CLASS":
    class_output(input)
  if definition_of_input == "DIRECTION":
    direction_output(input)
  if definition_of_input == "BATTLE":
    battle_output(input, other_character)
  if definition_of_input == "BEFRIEND":
    befriend_output(input, other_character)

print("Would you like to play a game? ;)")
first_input = input(">")
input_interpreter(first_input,"START")
