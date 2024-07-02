#---------------------------------------#
#------------ FLASK SERVER -------------#
#---------------------------------------#

#------------ IMPORTS ------------------#

from flask 				import Flask, render_template, request, jsonify, Response
from Cryptodome.Cipher 	import AES
from flask_socketio 	import SocketIO, join_room, leave_room
import binascii

from index			import play_game
from texts  		import gameplay_snippets
from keys.key 		import key
from debugging      import debug_functions


#------------ VARIABLES ----------------#
app 						= Flask(__name__)
app.config["SECRET_KEY"] 	= key
socketio 					= SocketIO(app, logger=True, engineio_logger=True)
socketio.init_app(app, cors_allowed_origins="*")

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


			play_game(player_input)

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


# >>> fetches and decrypts cookie for authentication

@app.route('/getCookieFlask', methods=['GET'])
def get_cookie():
	debug_functions.debugProcess('Getting cookie...')

	cookie_value = request.cookies.get('codingsorceressbridge')
 
	if not cookie_value:
		return "Cookie not found", 404
		
	cookie_data 	= binascii.unhexlify(cookie_value.split('%3A%3A')[0])
	shared_secret 	= binascii.unhexlify(cookie_value.split('%3A%3A')[1])
	
	cipher 			= AES.new(shared_secret, AES.MODE_CBC, iv=cookie_data[:16])
	decrypted_data 	= cipher.decrypt(cookie_data[16:])

	decrypted_cookie = decrypted_data.decode('utf-8').strip()
	 
	return decrypted_cookie


# >>> deletes the cookie if its invalid

@app.route('/deleteCookieFlask', methods=['DELETE'])
def delete_cookie():
	debug_functions.debugProcess('Deleting cookie...')

	cookies = request.headers.get('Cookie')
	
	try:
		cookies = 'codingsorceressbridge=; Max-Age=0; Path=/;'

	except Exception as e:
		print(e)
	
	response = Response()
	response.headers['Set-Cookie'] = cookies
	return response


# >>> fetches the IP of the current user

@app.route('/getIPFlask', methods=['GET'])
def get_ip():
	debug_functions.debugProcess('Getting IP...')

	forwarded = request.headers.getlist("X-Forwarded-For")
	
	if forwarded:
		ip = forwarded[0].split(",")[0]
	
	else:
		ip = request.remote_addr
	
	debug_functions.debugVariable('ip', len(ip))
	
	return str(ip)


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
	print(player_input)
	join_room(index)
	debug_functions.debugProcess('Connecting to SocketIO')


# Disconnect from SocketIO
@socketio.on("disconnect")
def connect():

	leave_room(index)
	debug_functions.debugProcess('Disconnecting from SocketIO')

	# prepare the game for restart by clearing player input from game
	player_input.clear()
	play_game(player_input)

#------------ START SERVER ----------------#

if __name__ == "__main__":
	socketio.run(app, port=5003, debug=True)

