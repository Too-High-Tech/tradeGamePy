from random import randint

class Enemy():
    def __init__(self,id,name,level,rarity=1,e_type='Normal', stats:dict=None):
        self.id = id
        self.name = name
        self.level = level
        self.rarity = rarity
        self.type = e_type
        if stats == None:
            self.stats = stats={'hp':10,'max_hp':10,'atk':1,'defence':1,'crit':1,'lifesteal':0}
        else:
            self.stats = stats

    def take_damage(self,source,damage):
        if source.stats['hp'] >= 1:
            self.stats['hp'] -= damage
            print(self.name+' took '+str(damage) +' damage.  '+str(self.stats['hp'])+' / '+str(self.stats['max_hp']))
            if self.stats['hp'] <= 0:
                self.death(source)
            else:
                self.retaliate(source)

    def retaliate(self,target):
        print(self.name+' attacking '+target.name)
        atk_value = self.stats['atk']
        def_value = target.stats['defence'] / 1000
        #Determine damage value based on atk of source and defense of self
        dmg_value = round(atk_value - def_value)
        target.take_damage(self,dmg_value)
    
    def death(self,source):
        exp_reward = round(self.rarity * self.stats['max_hp'])
        silver_reward = round(self.level * self.rarity * 1.10)
        if self.type == 'Normal':
            source.gain_exp(exp_reward)
            source.change_cash('s',silver_reward)
            dice = randint(1,100)
            if dice in range(60,101): #40% chance to drop loot.
                #Loot dropped.
                silver_reward = round(silver_reward * 1.5)
                source.change_cash('s',silver_reward)
                if dice in range(90,101): #10% chance that two items drop.
                    #Two loot dropped.
                    silver_reward = round(silver_reward * 2)
                    source.change_cash('s',silver_reward)
                    if dice == 100: #1% chance that 3 items drop.
                        #three items dropped
                        #Jackpot for silver
                        silver_reward = round(silver_reward * 10)
                        source.change_cash('s',silver_reward)
            elif self.type == 'Boss':
                pass

            