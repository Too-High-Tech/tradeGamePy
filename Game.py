from tradeGame import Player, Item, Enemy
import json

class Game:
    '''
    The main game class holds all game objects.
    '''
    def __init__(self):
        self.players = []
        self.items = []
        self.enemies = []

        self.load_resources()

    #ToDo;
    #Create function for loading game prefabs to use in __init__ function.
    def load_resources(self):
        filepath = 'tradeGame/resources/'

        self.players = self.load_players(filepath)
        self.items = self.load_items(filepath)
        self.enemies = self.load_enemies(filepath)

    def load_items(self,filepath):
        try:
            with open(filepath+'items.json','r') as f:
                items = json.load(f)
                iresult = []
                for item in items:
                    lItem = Item(item['id'],item['name'],item['levelreq'],item['rarity'],item['itype'],item['slot'],item['stat_mods'])
                    iresult.append(lItem)
                self.items = iresult
                return iresult
        except(IOError,IndexError):
            print('Failed to load item data.')
        
    def load_players(self,filepath):
        try:
            with open(filepath+'players.json','r') as f:
                players = json.load(f)
                presult = []
                for player in players:
                    ##Going to encounter a problem serializing item objects in the inventory and equipped dicts.
                    ##could just __dict__ the objects and run each one in the inventory and equipped through a load item function
                    lPlayer = Player(player['id'], player['name'], player['password'], player['level'], player['exp'], player['rexp'], player['silver'], player['gold'], player['stats'], player['inventory'], player['equipped'])
                    presult.append(lPlayer)
                return presult
        except(IOError,IndexError):
            print('Failed to load player data.')

    def load_enemies(self,filepath):
        try:
            with open(filepath+'enemies.json','r') as f:
                enemies = json.load(f)
                eresult = []
                for enemy in enemies:
                    ##Going to encounter a problem serializing item objects in the inventory and equipped dicts.
                    ##could just __dict__ the objects and run each one in the inventory and equipped through a load item function
                    lEnemy = Enemy(enemy['id'],enemy['name'],enemy['level'],enemy['rarity'],enemy['type'],enemy['stats'])
                    eresult.append(lEnemy)
                return eresult
        except(IOError,IndexError):
            print('Failed to load enemy data.')
        

    def save_resources(self):
        filepath = 'tradeGame/resources'

        with open(filepath+'/items.json','w') as f:
            nitems = []
            for item in self.items:
                item_dict = item.__dict__
                nitems.append(item_dict)
            json.dump(nitems,f)
        
        with open(filepath+'/players.json','w') as f:
            nplayers = []
            for player in self.players:
                player_dict = player.__dict__
                nplayers.append(player_dict)
            json.dump(nplayers,f)

        with open(filepath+'/enemies.json','w') as f:
            nenemies = []
            for enemy in self.enemies:
                enemy_dict = enemy.__dict__
                nenemies.append(enemy_dict)
            json.dump(nenemies,f)


    #Each of the following will respectivly retrieve the requested object from the provided ID.
    #ToDO; Consistant generation of object IDs.
    def find_item_by_id(self,item_id):
        pass


    def find_enemy_by_id(self,enemy_id):
        pass


    def find_player_by_id(self,player_id):
        pass


    #Events
    def hunt(self,player:Player):
        '''
        Generates a worthy opponent for a player to fight, then pits them against one another.
        '''


