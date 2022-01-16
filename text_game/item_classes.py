class Items:
  def __init__(self, name) -> None:
      self.name = name

class Weapon(Items):
  def __init__(self, name, damage, type_of_weapon) -> None:
      super().__init__(name)
      self.damage = damage
      self.type_of_weapon = type_of_weapon

class Armor(Items):
  def __init__(self, name, protection) -> None:
      super().__init__(name)
      self.protection = protection

class Potion(Items):
  def __init__(self, name, kind_of_potion, effect) -> None:
      super().__init__(name)
      self.kind_of_potion = kind_of_potion
      self.effect = effect
