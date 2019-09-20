from tradeGame import Enemy, Player, Item
from time import sleep

def new_enemy():
    nEnemy = Enemy(1,'Wolf',player.level,1,'Normal')
    return nEnemy

player = Player(0,'Swoopy','pass')
target = new_enemy()

#Item testing
helm = Item(0,'Bronze Helm',1,1,'Use','head',{'defence':3})
helm2 = Item(1,'Steel Berserker Helm',1,5,'Use','head',{'defence':15,'atk':2,'lifesteal':5})
weapon = Item(2,'Dragon Scimitar',1,5,'Use','weapon',{'atk':20,'defence':5,'lifesteal':10,'crit':10})

#Add test items to inventory
#player.inventory.append(helm)
player.inventory.append(helm2)
#player.inventory.append(weapon)
#Equip first test item(s)
#player.use_item(helm)
#Equip a better helm
player.use_item(helm2)
#Equip the weapon
#player.use_item(weapon)

while True:
    #Select's an enemy (A wolf with = level to the player) and fight to the death, repeat until Ctrl+C.
    if target is None:
        print('Creating new enemy')
        target = new_enemy()
        #target.stats['hp'] = target.stats['max_hp']
        
    player.attack(target)
    sleep(.5)
    if player.stats['hp'] <= 1:
        player.stats['hp'] = player.stats['max_hp']
    if target.stats['hp'] <= 0:
        target = None
        #After first creature is defeated, equip second test item
        
    
