from flask import Flask, render_template, redirect, url_for, session, request, flash
from game.game_manager import GameManager

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for session management
app.config['MAX_PLAYERS'] = 6  # Maximum number of players allowed

# Initialize game manager
game_manager = GameManager()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start-game')
def start_game():
    # Initialize a new game session
    game_id = game_manager.create_new_game()
    session['game_id'] = game_id
    return redirect(url_for('game'))

@app.route('/game')
def game():
    if 'game_id' not in session:
        return redirect(url_for('home'))
    
    game_id = session['game_id']
    game_state = game_manager.get_game_state(game_id)
    return render_template('game.html', game_state=game_state)

@app.route('/add-computer-player', methods=['POST'])
def add_computer_player():
    if 'game_id' not in session:
        return redirect(url_for('home'))
    
    game_id = session['game_id']
    player_name = request.form.get('player_name', '').strip()
    
    if not player_name:
        flash('Please enter a player name', 'error')
        return redirect(url_for('game'))
    
    game_state = game_manager.get_game_state(game_id)
    if len(game_state['players']) >= app.config['MAX_PLAYERS']:
        flash('Maximum number of players reached', 'error')
        return redirect(url_for('game'))
    
    if game_manager.add_player(game_id, player_name):
        flash(f'Added computer player: {player_name}', 'success')
    else:
        flash('Failed to add player', 'error')
    
    return redirect(url_for('game'))

@app.route('/start-game-round', methods=['POST'])
def start_game_round():
    if 'game_id' not in session:
        return redirect(url_for('home'))
    
    game_id = session['game_id']
    game_state = game_manager.get_game_state(game_id)
    
    if len(game_state['players']) < 2:
        flash('Need at least 2 players to start the game', 'error')
        return redirect(url_for('game'))
    
    # Update game state to start the game
    game_state['state'] = 'in_progress'
    game_state['current_round'] = 1
    
    # TODO: Initialize game round (deal cards, etc.)
    return redirect(url_for('game'))

if __name__ == '__main__':
    app.run(debug=True) 