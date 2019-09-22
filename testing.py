from Game import Game, Player, Item, Enemy
from time import sleep
from random import randint

game = Game()

def new_enemy():
    nEnemy = game.enemies[randint(0,2)].spawn()
    return nEnemy


##Saveload testing
#player = Player(0,'Swoopy','pass')
#game.players.append(player)
# wolf2 = Enemy(0,'Wolf Alpha',5,2,'Normal',{'atk':2,'def':2,'hp':15,'maxhp':15})
# game.enemies.append(wolf2)
# game.save_resources()

##
#Combat Testing
##

target = new_enemy()

player = game.find_player_by_id(0)


#print(str(item))

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

        
    
