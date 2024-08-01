'use strict';

const init = () => {

	/************* VARIABLES *************/
	
	const inputForm 	= document.querySelector('.input');
	const restartButton = document.querySelector('.restart');
	let sse 			= new EventSource("/update_game");

	/************* FUNCTIONS *************/

	/**
	 * 
	 * This function receives the user input, if there is any,
	 * and sends it to the server side. Then it empties the 
	 * form field in the browser from user input. 
	 * 
	 * @param 	{Event}  event - triggered event object
	 * 
	 * @returns {null}
	 * 
	 */

	const sendInput = (event) => {
		event.preventDefault();

		const input = event.target[0].value;
		// console.log(input)

		fetch('/input', {
			method: 'post', 
			headers: { "Content-Type": "application/text" },
			body: input
		}).then(
			resp => resp.json()
		).then(
			data => {
				//console.log(data);
			}
		).catch(
			console.warn
		)

		event.target.reset();

	}


	/**
	 * 
	 * This function updates the game text in the browser as the 
	 * game progresses. It clears the text box and fills it with
	 * with the server-provided updated text. 
	 * 
	 * @param 	{json}  texts - a JSON-object containing an array 
	 * 							of texts sent by the server
	 * 
	 * @returns {null}
	 * 
	 */

	const updateText = (texts) => {

		// console.log('Updating client...');

		// get data from server and transform from string to array
		const textsString = texts.data;
		// console.log(textsString);

		const textsArray = textsString.split('$');
		// console.log(textsArray);

		// target and clear the text box
		const textContainer 	= document.querySelector('.text');
		textContainer.innerHTML = '';

		// loop over texts to display them in the text box
		for(const text of textsArray) {
			let new_paragraph 		= `<p class="text-snippet"> ${text} </p><br>`;
			textContainer.innerHTML += new_paragraph
		}

		// scroll to bottom of text box
		textContainer.scrollTop = textContainer.scrollHeight;

	}

	/**
	 * 
	 * This function closes the SSE connection and refreshes the
	 * page, effectively restarting the game.
	 * 
	 * @param 	{EventSource}  sse - the SSE connection
	 * 
	 * @returns {null}
	 * 
	 */

	const restartGame = (sse) => {

		sse.close();
		location.reload();
	}


	/************* EVENT LISTENERS *************/

	inputForm.addEventListener('submit', sendInput);
	restartButton.addEventListener('click', () => {restartGame(sse)});

	sse.addEventListener('open', () => {console.log('Connected')});
	sse.addEventListener('update', message => {updateText(message)});
	sse.addEventListener('heartbeat', () => {console.log('heartbeat')});
	sse.addEventListener('error', error => {console.log("SSE error:", error)});
	sse.addEventListener('close', () => {
		console.log('Closing connection.');
		sse.close();
	})

}

init();

