import os

os.system("")

class HealthBar:
  hp: str = "█"
  missingHp: str = "_"
  barrier: str = "|"
  colours: dict = {"red": "\033[91m",
                    "purple": "\33[95m",
                    "blue": "\33[34m",
                    "blue2": "\33[36m",
                    "blue3": "\33[96m",
                    "green": "\033[92m",
                    "green2": "\033[32m",
                    "brown": "\33[33m",
                    "yellow": "\33[93m",
                    "grey": "\33[37m",
                    "default": "\033[0m"
                    }

  def __init__ (self, entity, length:int = 20, isColoured:bool = True, colour:str = "") -> None:
    self.entity = entity
    self.length = length
    self.max_value = entity.health_max
    self.current_value = entity.health

    self.isColoured = isColoured
    self.colour = self.colours.get(colour) or self.colours["default"]

  def update(self) -> None:
    self.current_value = self.entity.health

  def draw(self) -> None:
    remainingHp = round(self.current_value/self.max_value * self.length)
    lostHp = self.length - remainingHp
    print(f"{self.entity.name}'s HP: {self.entity.health}/{self.entity.health_max}")
    print(f"{self.barrier}"
          f"{remainingHp * self.hp}"
          f"{lostHp * self.missingHp}"
          f"{self.colours["default"] if self.isColoured else ""}"
          f"{self.barrier}")