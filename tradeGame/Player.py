class Player:

    def __init__(self, id:int, username:str, password:str, level:int=1, exp:int=0, rexp:int=90, silver:int=0, gold:int=0, stats:dict={'hp':10,'max_hp':10,'energy':100,'max_energy':100,'atk':1,'def':1,'crit':0,'lifesteal':0}, inventory:list=None, equipped:dict={'head':None,'body':None,'weapon':None,'shield':None,'legs':None,'feet':None,'pet':None,'amulet':None,}):
        self.id = id
        self.username = username
        self.password = password #TODO: crpytofy this in future
        self.level = level
        self.exp = exp
        self.rexp = rexp
        self.silver = silver
        self.gold = gold
        self.stats = stats
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
        if equipped is None:
            self.equipped = []
        else:
            self.equipped = equipped

    
    def gain_exp(self,amount):
        self.exp += amount
        if self.exp >= self.rexp:
            self.level_up()

    
    def level_up(self):
        while self.exp >= self.rexp:
            #Level up!
            self.rexp = round(self.rexp * 1.13)
            self.level += 1
            print(self.username+' just reached level '+str(self.level)+'!')
            #Add +10 to hp and energy, +1 to other stats.
            for stat in self.stats:
                if stat is not 'lifesteal':
                    if stat == 'max_hp' or stat == 'max_energy':
                        self.stats[stat] += 10
                    if stat == 'hp' or stat == 'energy':
                        self.stats[stat] = self.stats['max_'+stat]
                    else:
                        self.stats[stat] += 1
            print(self.stats)
        self.exp = 0

    def change_cash(self,g_s:str,amount:int=0):
        '''
        Gain amount of gold or silver given
        args:
            g_s: 'g' for gold, 's' for silver
            amount: amount of gold or silver to gain/lose.
        '''
        if g_s == 'g' or g_s == 'G' and amount != 0:
            g_s = 'gold'
            if amount > 0:
                self.gold += amount
                return True
            elif amount < 0:
                self.gold -= amount
                return True
        elif g_s == 's' or g_s == 'S':
            g_s = 'silver'
            if amount > 0:
                self.silver += amount
                return True
            elif amount < 0:
                self.silver -= amount
                return True
        else:
            return False

    
        
    
    def die(self):
        if self.stats['hp'] <= 0:
            #Player dies
            pass

