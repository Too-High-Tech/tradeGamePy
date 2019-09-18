from tradeGame import *#
from time import sleep

player = Player(0,'Swoopy','pass')
while True:
    player.gain_exp(10)
    print(str(player.exp) + ' / ' + str(player.rexp))
    sleep(3)
