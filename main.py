import os
from character import Hero, Enemy
import weapon

hero = Hero(name="Hero", health=100)
enemy = Enemy(name="Enemy", health=100, weapon=weapon.spear)

hero.equip(weapon.sword)

while True:
  os.system("cls")
  
  hero.attack(enemy)
  enemy.attack(hero)

  hero.health_bar.draw()
  enemy.health_bar.draw()
  
  input()