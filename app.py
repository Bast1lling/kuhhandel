from flask import Flask, render_template, redirect, url_for, session, request, jsonify, flash
from game.game_manager import GameManager
from game.player import HumanPlayer, ComputerPlayer
import random
app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for session management
app.config['MAX_PLAYERS'] = 6  # Maximum number of players allowed

# Initialize game manager
game_manager = GameManager()

@app.route('/')
def home():
    # Clear any existing game session
    session.clear()
    # Create a new game for the lobby
    game_id = game_manager.create_new_game()
    game_manager.add_player(game_id)
    game_manager.add_player(game_id)
    session['game_id'] = game_id
    game = game_manager.get_game(game_id)
    return render_template('index.html', game=game)

@app.route('/start-game')
def start_game():
    if 'game_id' not in session:
        return redirect(url_for('home'))
    
    game_id = session['game_id']
    game = game_manager.get_game(game_id)
    
    if len(game.players) < 3:
        flash('Need at least 3 players to start the game', 'error')
        return redirect(url_for('home'))
    
    return redirect(url_for('auction_game'))

@app.route('/add-computer-player', methods=['POST'])
def add_computer_player():
    if 'game_id' not in session:
        return jsonify({'success': False, 'error': 'No game session found'})
    
    game_id = session['game_id']
    game = game_manager.get_game(game_id)
    
    if len(game.players) >= app.config['MAX_PLAYERS']:
        return jsonify({'success': False, 'error': 'Maximum number of players reached'})
    
    game_manager.add_player(game_id)
    
    # Get the updated game state
    game = game_manager.get_game(game_id)
    
    # Return the updated player list along with success status
    return jsonify({
        'success': True,
        'players': [player.name for player in game.players]
    })


@app.route('/auction-game')
def auction_game():
    if 'game_id' not in session:
        return redirect(url_for('home'))
    
    game_id = session['game_id']
    game = game_manager.get_game(game_id)
    
    # Get the human player
    human_player = next(player for player in game.players if player.is_human)
    
    return render_template('auction_game.html', game=game, human_player=human_player)

@app.route('/start-game-round', methods=['POST'])
def start_game_round():
    if 'game_id' not in session:
        return redirect(url_for('home'))
    
    game_id = session['game_id']
    game = game_manager.get_game(game_id)
    
    if len(game.players) < 2:
        flash('Need at least 2 players to start the game', 'error')
        return redirect(url_for('game'))
    
    # Update game state to start the game
    game.current_round = 1
    game.current_player_index = random.randint(0, len(game.players) - 1)
    
    return redirect(url_for('auction_game'))

if __name__ == '__main__':
    app.run(debug=True) 