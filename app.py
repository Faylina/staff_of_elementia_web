#---------------------------------------#
#------------ FLASK SERVER -------------#
#---------------------------------------#

#------------ IMPORTS ------------------#

from flask 				import Flask, render_template, request, jsonify, Response
from Cryptodome.Cipher 	import AES
import binascii
import time

from index			import play_game
from texts  		import gameplay_snippets
from keys.key 		import key
from debugging      import debug_functions


#------------ VARIABLES ----------------#

app 						= Flask(__name__)
app.config["SECRET_KEY"] 	= key

texts 						= ['empty']
old_texts 					= ['empty']
player_input 				= []


#------------ FUNCTIONS ----------------#

def check_for_update():
	# debug_functions.debugProcess('Checking for update...')

	index_old = len(old_texts) - 1
	index_new = len(texts) - 1

	if old_texts[index_old] is not texts[index_new]:
		return True
	else:
		return False


#------------ FLASK ROUTES ----------------#

# >>> loads the homepage in its initial state

@app.route('/', methods=['GET'])
def index():

	# Reset variables for a new game

	texts.clear()
	texts.append('empty')

	old_texts.clear()
	old_texts.append('empty')

	player_input.clear()

	intro_texts = []
	intro_texts.append(gameplay_snippets.intro)
	intro_texts.append('Enter your response (y = I want to help! / n = No, thanks...):')

	if request.method == 'GET':
		try:
			debug_functions.debugProcess('Starting the game...')


			play_game(player_input)

			return render_template('index.html', texts=intro_texts)
		except:
			print('Homepage could not be loaded...')


# >>> receives user input and passes it to the game script

@app.route('/input', methods=['POST'])
def input():

	if request.method == 'POST':
		try:
			debug_functions.debugProcess('Processing input...')

			print(player_input)

			# add user input to game
			player_input.append(request.data.decode("utf-8"))
			debug_functions.debugVariable('player_input', player_input)

			print(player_input)

			# play game with the added user input
			play_game(player_input)

			return jsonify({'message': 'User input has been passed to game script.'})
		
		except:
			print('User input could not be passed to the game...')


# >>> receives new text from game script

@app.route('/receive_text', methods=['PUT'])
def receive_text():

	if request.method == 'PUT':
		try:
			# time.sleep(0.2)

			debug_functions.debugProcess('Adding text...')

			texts_string = request.json['texts']
			texts.append(texts_string)

			debug_functions.debugVariable('texts', texts)

			return jsonify({'message': 'New texts received from game script.'})
		
		except:
			print('New text has not been received...')


# >>> pushes game updates via SSE to update the frontend

@app.route('/update_game', methods=['GET'])
def update_game():

	if request.method == 'GET':
		try:

			debug_functions.debugProcess('Updating game...')

			def fetch_texts():
				
				# keep SSE route active
				while True:
					if check_for_update() == True:

						# find the latest text
						index = len(texts) - 1

						# update comparison variable for update checks
						old_texts.append(texts[index])

						# send latest text to frontend
						yield f"event: message\ndata: {texts[index]}\n\n"
					else:
						# debug_functions.debugProcess('No update...')
						placeholder = 1

					# time.sleep(0.1)
			
			return Response(fetch_texts(), mimetype="text/event-stream")
		
		except:
			print('Update could not be sent to frontend...')


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


#------------ START SERVER ----------------#

if __name__ == "__main__":
	app.run(host="127.0.0.1", port=5003, debug=True)

