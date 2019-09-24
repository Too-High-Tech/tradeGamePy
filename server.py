from flask import Flask, request, session, jsonify
from flask_session import Session
import json
import tradeGame
from Game import Game
import hashlib, binascii, os
from random import randint

app = Flask(__name__)
SESSION_TYPE = 'redis'
SECRET_KEY = 'secretkey'
app.config.from_object(__name__)
app.secret_key = 'SecretKey' 
sess = Session()
game = Game()

def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')
 
def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


@app.route('/login',methods=['POST'])
def login(): 
        if 'player' in session:
            session.pop('player', None)
        if 'enemy' in session:
            session.pop('enemy', None)
        #Find the user from the given details.
        user = request.args.get('user')
        for player in game.players:
            if player.name == user:
                #User found now check password.
                if verify_password(player.password,request.args.get('pass')):
                    session['player'] = player.id
                    return jsonify(player.stats_dump()), 200
                else:
                    return 'Password is incorrect.', 400
        else:
            return 'Username not found', 400
        

@app.route('/register', methods=['POST'])
def register(): 
    user = request.args.get('user')
    passhash = hash_password(request.args.get('pass'))
    if game.add_player(user,passhash) is True:
        return 'Registered successfully.', 201
    else:
        return 'Failed to register.', 400

@app.route('/dropsession')
def dropsession(): 
    session.pop('player', None)
    return 'Logged out!', 200
#==========================================

#Majority of this code can be moved to a more appropriate class (Events or Hunting or smthn.)
@app.route('/hunt',methods=['POST'])
def hunt(): 
    #Check if player has required hp and energy
    #select an enemy to fight 
    if 'player' in session:
        player = game.find_player_by_id(session['player'])
        if player.stats['hp'] <= 0:
            player.stats['hp'] = player.combat_stats['max_hp']
        enemy = session.get('enemy')
        if 'enemy' not in session:
            #Select an enemy to fight.
            minlevel = player.level - 2
            maxlevel = player.level + 2         
            #Roll the rarity dice.
            #1 = common, 2 = uncommon, 3 = rare, 4 = epic, 5 = legend
            #    100%        20%         10%         5%       1%      
            rarity_dice = randint(1,100)
            poss_rarity = 1
            if rarity_dice >= 50:
                poss_rarity = 1 
            if rarity_dice in range(51,82):
                poss_rarity = 2
            if rarity_dice in range(83,93):
                poss_rarity = 3
            if rarity_dice in range(94,99):
                poss_rarity = 4
            if rarity_dice == 100:
                poss_rarity = 5
            #grab all enemies within level & rarity range
            poss_enemies = [enemy for enemy in game.enemies if enemy.level in range(minlevel,maxlevel) and enemy.rarity <= poss_rarity]
            #Randomly select an enemy from the lits of potential enemies
            max = len(poss_enemies) - 1
            enemy = poss_enemies[randint(0,max)]
            session['enemy'] = enemy.spawn()
        
        player.attack(session['enemy'])
        
        playerstats = player.stats_dump()
        response = {
            "player":playerstats,
            "enemy":session['enemy'].__dict__
        }
        if session['enemy'].stats['hp'] <= 0:
            session.pop('enemy')
        game.save_players()
        return jsonify(response), 200
        
        
        
        
    else:
        return 'You must be logged in to do this.', 400









if __name__ == "__main__":
    
    sess.init_app(app)
    #app.debug = True
    app.run()