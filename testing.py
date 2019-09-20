from Game import Game, Player, Item, Enemy
from time import sleep

game = Game()

def new_enemy():
    nEnemy = game.enemies[0]
    return nEnemy


##Saveload testing
#player = Player(0,'Swoopy','pass')
#game.players.append(player)
# wolf = Enemy(0,'Wolf',1,1,'Normal')
# game.enemies.append(wolf)
# game.save_resources()

##
#Combat Testing
##

target = new_enemy()


while True:
    #Select's an enemy (A wolf with = level to the player) and fight to the death, repeat until Ctrl+C.
    if target is None:
        print('Creating new enemy')
        target = new_enemy()
        #target.stats['hp'] = target.stats['max_hp']
        
    game.players[0].attack(target)

    sleep(2)

    if game.players[0].stats['hp'] <= 1:
        game.players[0].stats['hp'] = game.players[0].stats['max_hp']
    if target.stats['hp'] <= 0:
        target = None

        
    
