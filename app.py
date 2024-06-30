#---------------------------------------#
#------------ FLASK SERVER -------------#
#---------------------------------------#

from flask 	import Flask, render_template, url_for, request, redirect, jsonify
from index	import play_game
from texts  import gameplay_snippets

app 			= Flask(__name__)
texts 			= []
player_input 	= []

texts.append(gameplay_snippets.title)
texts.append(gameplay_snippets.intro)
texts.append('Enter your response (y = I want to help! / n = No, thanks...):')

@app.route('/', methods=['POST', 'GET'])
def index():
	print('indexing...')
	play_game(player_input)
	return render_template('index.html', texts=texts)
	
@app.route('/start_game', methods=['POST'])
def start_game():
	if request.method == 'POST':
		print('Starting game...')
		texts_str = request.json['texts']
		texts = texts_str.split('$')
		print(texts)
		return render_template('index.html', texts=texts)
	
@app.route('/update_game', methods=['PUT'])
def update_game():
	if request.method == 'PUT':
		try:
			print('Updating game...')
			texts_str = request.json['texts']
			texts = texts_str.split('$')
			print(texts)
			return render_template('index.html', texts=texts)
		except:
			print('Updating not possible...')

@app.route('/user_input', methods=['POST'])
def user_input():
	if request.method == 'POST':
		print('Processing input...')
		player_input.append(request.data.decode("utf-8"))
		#print(player_input)
		play_game(player_input) 
		return jsonify(message='success')


if __name__ == "__main__":
	app.run(port=5003, debug=True)

