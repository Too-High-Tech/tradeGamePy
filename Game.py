from tradeGame import Player, Item, Enemy
import json

class Game:
    '''
    The main game class holds all game objects.
    Game.players
    Game.items
    Game.enemies
    '''
    def __init__(self):
        self.players = []
        self.items = []
        self.enemies = []
        self.load_resources()


    def load_resources(self):
        filepath = 'tradeGame/resources/'

        self.items = self.load_items(filepath)
        self.players = self.load_players(filepath)
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
                    
                    lInven = [self.find_item_by_id(el) for el in player['inventory']]
                    lEquip = {'head':None,'body':None,'weapon':None,'shield':None,'legs':None,'feet':None,'pet':None,'amulet':None}
                    for slot in player['equipped']:
                        if player['equipped'][slot] != None:
                            lEquip[slot] = self.find_item_by_id(player['equipped'][slot])
                    lPlayer = Player(player['id'], player['name'], player['password'], player['level'], player['exp'], player['rexp'], player['silver'], player['gold'], player['stats'], lInven, lEquip)
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
        self.save_items(filepath)
        self.save_players(filepath)
        self.save_enemies(filepath)
        return True
    
    
    def add_player(self,username,hashedpass):
        status = True
        for player in self.players:
            if player.name == username:
                status = False
        if status == True:
            nPlayer = Player(len(self.players),username,hashedpass)
            self.players.append(nPlayer)
            self.save_players('tradeGame/resources')
            self.load_players('tradeGame/resources')
            return True
        else:
            return False
    
    def save_players(self,filepath):    
        with open(filepath+'/players.json','w') as f:
            nplayers = []
            for player in self.players:
                player_dict = player.__dict__
                pinven = []
                pequip = {'head':None,'body':None,'weapon':None,'shield':None,'legs':None,'feet':None,'pet':None,'amulet':None}
                for item in player.inventory:
                    ninven = item.id
                    pinven.append(ninven)
                player_dict['inventory'] = pinven
                for slot in player.equipped:
                    if player.equipped[slot] is not None:
                        nequip = player.equipped[slot].id
                        pequip[slot] = nequip
                player_dict['equipped'] = pequip
                nplayers.append(player_dict)
            json.dump(nplayers,f)
            return True


    def save_enemies(self,filepath):
        with open(filepath+'/enemies.json','w') as f:
            nenemies = []
            for enemy in self.enemies:
                enemy_dict = enemy.__dict__
                nenemies.append(enemy_dict)
            json.dump(nenemies,f)
            return True


    def save_items(self,filepath):
        with open(filepath+'/items.json','w') as f:
            nitems = []
            for item in self.items:
                item_dict = item.__dict__
                nitems.append(item_dict)
            json.dump(nitems,f)
            return True


    #Each of the following will respectivly retrieve the requested object from the provided ID.
    #ToDO; Consistant generation of object IDs.
    def find_item_by_id(self,item_id):
        for item in self.items:
            if item.id == item_id:
                return item
        else:
            return False


    def find_enemy_by_id(self,enemy_id):
        for enemy in self.enemies:
            if enemy.id == enemy_id:
                return enemy
        else:
            return False


    def find_player_by_id(self,player_id):
        for player in self.players:
            if player.id == player_id:
                return player
        else:
            return False


