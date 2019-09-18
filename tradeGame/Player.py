class Player():

    def __init__(self, id:int, name:str, password:str, level:int=1, exp:int=0, rexp:int=90, silver:int=0, gold:int=0,stats:dict={'hp':10,'max_hp':10,'energy':100,'max_energy':100,'atk':1,'defence':1,'crit':0,'lifesteal':0}, inventory:list=None, equipped:dict={'head':None,'body':None,'weapon':None,'shield':None,'legs':None,'feet':None,'pet':None,'amulet':None,}):
        self.id = id
        self.name = name
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
        print(self.name +' gained '+ str(amount) + ' exp.  ('+str(self.exp)+' / '+str(self.rexp)+')')
        if self.exp >= self.rexp:
            self.level_up()

    
    def level_up(self):
        while self.exp >= self.rexp:
            #Level up!
            self.rexp = round(self.rexp * 1.13)
            self.level += 1
            print(self.name+' just reached level '+str(self.level)+'!')
            #Add +10 to hp and energy, +1 to other stats.
            for stat in self.stats:
                if stat is not 'lifesteal':
                    if stat == 'max_hp' or stat == 'max_energy':
                        self.stats[stat] += 10
                    else:
                        self.stats[stat] += 1
            self.stats['hp'] = self.stats['max_hp']
            self.stats['energy'] = self.stats['max_energy']
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
                print(self.name +' gained '+ str(amount) + ' ' + g_s+'.')
                return True
            elif amount < 0:
                self.gold -= amount
                print(self.name +' lost '+ str(amount) + ' ' + g_s+'.')
                return True
        elif g_s == 's' or g_s == 'S':
            g_s = 'silver'
            if amount > 0:
                self.silver += amount
                print(self.name +' gained '+ str(amount) + ' ' + g_s+'.')
                return True
            elif amount < 0:
                print(self.name +' lost '+ str(amount) + ' ' + g_s+'.')
                self.silver -= amount
                return True
        else:
            return False

    def attack(self,target):
        if target is not None:
            print(self.name+' attacking '+target.name)
            #TODO: Determine critical hit (Critical Roll function)
            atk_value = self.stats['atk']
            def_value = target.stats['defence'] / 1000
            #Determine damage value based on atk of source and defense of self
            dmg_value = round(atk_value - def_value)
            target.take_damage(self,dmg_value)
        else:
            print('Target is none.')
        
    def take_damage(self,source,damage):
        if source.stats['hp'] >= 1:
            self.stats['hp'] -= damage
            print(self.name+' took '+str(damage) +' damage.  '+str(self.stats['hp'])+' / '+str(self.stats['max_hp']))
            if self.stats['hp'] <= 0:
                self.death()
    
    def death(self):
        if self.stats['hp'] <= 0:
            self.stats['hp'] = 0
            self.stats['energy'] = 0
            print(self.name + ' died.')
            pass
