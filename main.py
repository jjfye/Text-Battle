from character import Hero, Enemy
import weapon

hero = Hero(name="Hero", health=100)
enemy = Enemy(name="Enemy", health=100, weapon=weapon.spear)

hero.equip(weapon.sword)

while True:
  hero.attack(enemy)
  enemy.attack(hero)

  print(f"{hero.name}'s HP: {hero.health}")
  print(f"{enemy.name}'s HP: {enemy.health}")
  
  input()