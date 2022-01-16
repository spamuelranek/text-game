
from item_classes import Armor, Potion, Weapon

class PlayerClass():
  def __init__(self,name,name_of_weapon):
    self.name = name
    self.name_of_weapon = name_of_weapon
    self.weapon = ''
    self.health_points = 100
    self.attack_points = 10
    self.speed = 1
    self.special = ''
    self.experience = 0
    self.party = []
    self.inventory = []

  def __str__(self):
    player_info = f"""{self.name} weilder of {self.name_of_weapon} a {self.weapon}
{self.name} has HP:{self.health_points} and AP:{self.attack_points}
{self.name} has the speed of {self.speed}
Their special ability is {self.special}"""
    return player_info

  def view_inventory(self):
    for item in self.inventory:
      print(item.name)
      if isinstance(item, Weapon):
        print(f" A |{item.type_of_weapon}| that does: {item.damage}")
      elif isinstance(item, Armor):
        print(f" Armor that adds :{item.protection}")
      elif isinstance(item, Potion):
        print (f" A potion that does :{item.effect}  of {item.kind_of_potion} ")
    return
    

class Talker(PlayerClass):
  def __init__(self, name, name_of_weapon):
      super().__init__(name, name_of_weapon)
      self.special = "Random Chance"
      self.weapon = "Dagger"
      self.inventory.append(Weapon(name_of_weapon, 2, self.weapon))

  def __str__(self):
    return super().__str__()

class Walker(PlayerClass):
  def __init__(self, name, name_of_weapon):
      super().__init__(name, name_of_weapon)
      self.special = "Fury"
      self.weapon = "Staff"
      self.speed = 2
      self.inventory.append(Weapon(name_of_weapon, 2, self.weapon))

  def __str__(self):
    return super().__str__()

class Fighter(PlayerClass):
  def __init__(self, name, name_of_weapon):
      super().__init__(name, name_of_weapon)
      self.special = "Rage"
      self.weapon = "Hammer"
      self.attack_points = 15
      self.inventory.append(Weapon(name_of_weapon, 2, self.weapon))

  def __str__(self):
    return super().__str__()