#---------------------------------------#
#------------ FLASK SERVER -------------#
#---------------------------------------#

#------------ IMPORTS ------------------#

from flask 			import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, join_room, leave_room
from index			import play_game
from texts  		import gameplay_snippets
from keys.key 		import key
from debugging      import debug_functions

#------------ VARIABLES ----------------#
app 						= Flask(__name__)
app.config["SECRET_KEY"] 	= key
socketio 					= SocketIO(app, logger=True, engineio_logger=True)

texts 						= []
player_input 				= []

#------------ INTRODUCTION ----------------#

texts.append(gameplay_snippets.intro)
texts.append('Enter your response (y = I want to help! / n = No, thanks...):')


#------------ FLASK ROUTES ----------------#

# >>> loads the homepage in its initial state

@app.route('/', methods=['GET'])
def index():
	if request.method == 'GET':
		try:
			debug_functions.debugProcess('Starting the game...')

			play_game()

			return render_template('index.html', texts=texts)
		except:
			print('Homepage could not be loaded...')


# >>> pushes game updates to socketio to update the frontend

@app.route('/update_game', methods=['PUT'])
def update_game():
	if request.method == 'PUT':
		try:
			debug_functions.debugProcess('Updating game...')

			texts_str 	= request.json['texts']
			texts 		= texts_str.split('$')

			debug_functions.debugVariable('texts', texts)

			socketio.emit('update', {'texts': texts})

			return jsonify({'message': 'Update was successful.'})
		except:
			print('Updating not possible...')


#------------ SOCKET IO EVENT LISTENERS ----------------#

# receives player input from frontend, processes it and 
# sends it to the game

@socketio.on('input')
def input(data):
	debug_functions.debugProcess('Processing input...')

	# add user input to game
	player_input.append(data['data'])
	debug_functions.debugVariable('player_input', player_input)

	# play game with additional user input
	play_game(player_input)


# Connect to SocketIO
@socketio.on("connect")
def connect(auth):
	join_room(index)
	debug_functions.debugProcess('Connected to SocketIO')


# Disconnect from SocketIO
@socketio.on("disconnect")
def connect():
	leave_room(index)
	debug_functions.debugProcess('Disconnected to SocketIO')

	# prepare the game for restart by clearing player input from game
	player_input = []
	play_game(player_input)


#------------ START SERVER ----------------#

if __name__ == "__main__":
	socketio.run(app, port=5003, debug=True)

