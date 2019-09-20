class Player():

    def __init__(self, id:int, name:str, password:str, level:int=1, exp:int=0, rexp:int=90, silver:int=0, gold:int=0,stats:dict=None, inventory:list=None, equipped:dict=None):
        self.id = id
        self.name = name
        self.password = password #TODO: crpytofy this in future
        self.level = level
        self.exp = exp
        self.rexp = rexp
        self.silver = silver
        self.gold = gold
        if stats is None:
            self.stats = {'hp':10,'max_hp':10,'energy':100,'max_energy':100,'atk':1,'defence':1,'crit':0,'lifesteal':0}
        else:
            self.stats = stats
        
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
        if equipped is None:
            self.equipped = {'head':None,'body':None,'weapon':None,'shield':None,'legs':None,'feet':None,'pet':None,'amulet':None}
        else:
            self.equipped = equipped
        self.combat_stats = None
        self.update_combat_stats()
            

    
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
                if stat is not 'lifesteal' and stat is not 'crit':
                    if stat == 'max_hp' or stat == 'max_energy':
                        self.stats[stat] += 10
                    else:
                        self.stats[stat] += 1
            self.stats['hp'] = self.stats['max_hp']
            self.stats['energy'] = self.stats['max_energy']
            self.update_combat_stats()
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
            atk_value = self.combat_stats['atk']
            if target is Player:
                def_value = target.combat_stats['defence'] / 100
            else:
                def_value = target.stats['defence'] / 100
            #Determine damage value based on atk of source and defense of self
            dmg_value = round(atk_value - def_value)
            target.take_damage(self,dmg_value)
        else:
            print('Target is none.')
        
    def take_damage(self,source,damage):
        if source.stats['hp'] >= 1:
            self.stats['hp'] -= damage
            print(self.name+' took '+str(damage) +' damage.  '+str(self.stats['hp'])+' / '+str(self.combat_stats['max_hp']))
            if self.stats['hp'] <= 0:
                self.death()
    
    def death(self):
        if self.stats['hp'] <= 0:
            self.stats['hp'] = 0
            self.stats['energy'] = 0
            print(self.name + ' died.')
            pass

#=======Item handling
#Currently there are no 'stacking' items, each item takes one slot.

    def calculate_item_stats(self):
        '''Returns dict of player's stats with equipped item stats added.
        (True stat value for combat)
        '''
        
        player_stats = self.stats.copy()
        item_stats = {'hp':0,'max_hp':0,'energy':0,'max_energy':0,'atk':0,'defence':0,'crit':0,'lifesteal':0}
        
        if self.equipped is not None:
            for slot in self.equipped:
                if self.equipped[slot] is not None:
                    item = self.equipped[slot]
                    for stat in item.stat_mods:
                        item_stats[stat] += item.stat_mods[stat]
            for stat in item_stats:
                player_stats[stat] += item_stats[stat]
            #print(str(player_stats))
            return player_stats
        else:
            return player_stats

    def update_combat_stats(self):
        self.combat_stats = self.calculate_item_stats()
        print('Core Stats: '+str(self.stats))
        print('Total Stats: '+str(self.combat_stats))

    def use_item(self, item):
        '''
        Equips or consumes item based on item.type's property
        '''
        if item in self.inventory:   
            if item.itype == 'Use':
                #Item is equippable
                if self.equipped[item.slot] is not None:
                    #Item already equipped in slot, unequip then equip this item.
                    print(str(self.equipped[item.slot])+' unequipped.')
                    self.inventory.append(self.equipped[item.slot])
                    self.inventory.remove(item)
                    self.equipped[item.slot] = item
                    print(str(item)+' equipped')
                    self.update_combat_stats()
                elif self.equipped[item.slot] is None:
                    #Nothing is equipped in this slot, equip the item.
                    self.inventory.remove(item)
                    self.equipped[item.slot] = item
                    print(str(item)+' equipped')
                    self.update_combat_stats()
            elif item.itype == 'Consume':
                pass
        else:
            print('You cannot equip an item that is not in your inventory')