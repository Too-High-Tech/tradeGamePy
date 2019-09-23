from flask import Flask, request, session, jsonify
from flask_session import Session
import json
from Game import Game
import hashlib, binascii, os

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


@app.route('/login', methods=['POST'])
def login(): 
        #Find the user from the given details.
        user = request.args.get('user')
        for player in game.players:
            if player.name == user:
                #User found now check password.
                if verify_password(player.password,request.args.get('pass')):
                    session['player'] = player
                    print(session)
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

#==========================================

@app.route('/hunt', methods=['POST'])
def hunt(): 
    if session['player'] is not None:
        minlevel = session['player'].level - 3
        maxlevel = session['player'].level + 3
        
        #Check if player has required hp and energy
        #select an enemy to fight (Code should be moved elsewhere)









if __name__ == "__main__":
    
    sess.init_app(app)
    app.debug = True
    app.run()