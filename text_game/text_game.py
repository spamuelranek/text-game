from character_classes import Talker, Walker, Fighter
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
    input_direction = input(">")
    input_interpreter(input_direction, "DIRECTION")

def battle_engage():
  global random_encounter
  if random_encounter > 2:
    player.health_points = 0
    print("you died. Lame")
  else:
    print("You won a battle")
    random_encounter += 1

def shop_engage():
  print("You bought all that stuff")

def enter_town():
  print("You talked to all the people")

def move_in_direction(direction_choice):
    outcome = random()
    if direction_choice == "left":
      if outcome < .40:
        return print("The path conitinues")
      else:
        battle_engage()
        return
    elif direction_choice == "right":
      if outcome < .40:
        return print("The path conitinues")
      else:
        shop_engage()
        return
    elif direction_choice == "forward":
      if outcome < .40:
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

def input_interpreter(input, definition_of_input):
  if definition_of_input == "START":
    if input == "yes":
      start_game()
    elif input == "no":
      print('Okay, you lose.')
  if definition_of_input == "CLASS":
    if input == "talker":
      class_creation(Talker)
    elif input == "walker":
      class_creation(Walker)
    elif input == "fighter":
      class_creation(Fighter)
  if definition_of_input == "DIRECTION":
    if input == "left":
      move_in_direction("left")
    elif input == "right":
      move_in_direction("right")
    elif input == "forward":
      move_in_direction("forward")
      
print("Would you like to play a game? ;)")
first_input = input(">")
input_interpreter(first_input,"START")
