from weapon import spear
from health_bar import HealthBar

class Character:
  def __init__ (self, name: str, health: int) -> None:
    self.name = name
    self.health = health
    self.health_max = health

    self.weapon = spear

  def attack(self, target) -> None:
    target.health -= self.weapon.damage
    target.health = max(target.health, 0)
    target.health_bar.update()
    print(f"{self.name} dealt {self.weapon.damage} damage to {target.name} with {self.weapon.name}")


class Hero(Character):
  def __init__(self, name:str, health:int) -> None:
    super().__init__(name=name, health=health)

    self.health_bar = HealthBar(self, colour="green")
    self.default_weapon = self.weapon

  def equip(self, weapon) -> None:
    self.weapon = weapon
    print(f"{self.name} equipped {self.weapon.name}")

  def drop(self) -> None:
    print(f"{self.name} dropped {self.weapon.name}")
    self.weapon = self.default_weapon


class Enemy(Character):
  def __init__(self, name:str, health:int, weapon) -> None:
    super().__init__(name=name, health=health)

    self.health_bar = HealthBar(self, colour="red")
    self.weapon = weapon