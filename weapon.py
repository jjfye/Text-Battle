class Weapon:
  def __init__ (self, name:str, damage:int, weapon_type:str, value:int) -> None:
    self.name = name
    self.damage = damage
    self.weapon_type = weapon_type
    self.value = value

sword = Weapon("Sword", 7, "Melee", 10)
bow = Weapon("Bow", 10, "Ranged", 12)
spear = Weapon("Spear", 8, "Melee", 5)