from Game import Game
import tradeGame
class DevTools:
    def __init__(self):
        self.game = Game()

    def create_enemy(self):
        enemy_id = len(self.game.enemies)
        enemy_name = input('Enemy Name: ')
        enemy_level = int(input('Enemy Level: '))
        enemy_type = input('Enemy Type: ')
        enemy_rarity = int(input('Enemy Rarity: '))
        enemy_stats = {'atk':0,'defence':0,'hp':0,'max_hp':0,'crit':0}

        points = (enemy_level*4)

        print('Enemy level '+ str(enemy_level) + ' defined, so '+str(points)+' total stat points availale for distribution.')
        print('Note that most of these points should be spent on max_hp.')

        while points > 0:
            for stat in enemy_stats:
                if stat is not 'hp':
                    stat_val = int(input(stat+': '))
                    
                    points -= stat_val
                    if stat == 'max_hp':
                        stat_val = stat_val*10
                    enemy_stats[stat] = stat_val
                    print(str(points)+' points remaining.')
                
            if enemy_stats['max_hp'] != 0:
                enemy_stats['hp'] = enemy_stats['max_hp']
            
        new_enemy = tradeGame.Enemy(enemy_id,enemy_name,enemy_level,enemy_rarity,enemy_type,enemy_stats)

        self.game.enemies.append(new_enemy)

        if self.game.save_enemies('tradeGame/resources') is True:
            print('Enemy added successfully!')

    def run_tools(self):
        while True:
            print('Select a choice: ')
            print('1 - Create a new Enemy')
            choice = input('->')
            if choice == '1':
                self.create_enemy()
            else:
                continue

tools = DevTools()

tools.run_tools()