from character_classes import PlayerClass

class Goblin(PlayerClass):
  def __init__(self, name, name_of_weapon):
      super().__init__(name, name_of_weapon)
      self.special = "Grapple"
      self.weapon = "Short Sword"
      self.health_points = 20
      self.attack_points = 2
      self.speed = 5