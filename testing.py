from tradeGame import Enemy, Player
from time import sleep

player = Player(0,'Swoopy','pass')

def new_enemy():
    nEnemy = Enemy(1,'Wolf',player.level,1,'Normal')
    return nEnemy

target = new_enemy()
while True:
    
    if target is None:
        print('Creating new enemy')
        target = new_enemy()
        #target.stats['hp'] = target.stats['max_hp']
        
    player.attack(target)
    sleep(1)
    if player.stats['hp'] <= 1:
        player.stats['hp'] = player.stats['max_hp']
    if target.stats['hp'] <= 0:
        target.stats.clear()
        target = None
        
    
