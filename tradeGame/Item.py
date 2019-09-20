class Item:
    def __init__(self, id, name, levelreq, rarity, itype='Use', slot=None, stat_mods = None):
        self.id = id
        self.name = name
        self.rarity = rarity
        self.levelreq = levelreq
        self.itype = itype
        if slot == None:
            self.slot = None
        else:
            self.slot = slot
        if stat_mods == None:
            self.stat_mods = {'max_hp':0,'max_energy':0,'atk':0,'defence':0,'crit':0,'lifesteal':0}
        else:
            self.stat_mods = stat_mods

    def __repr__(self):
        return str(self.name)