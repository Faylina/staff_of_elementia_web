'use strict';

const init = () => {

	/************* VARIABLES *************/
	
	let socketio 	= io();
	const inputForm = document.querySelector('.input');


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

		// extract the user input
		const userInput = event.target[0].value;

		// check whether it has content, if not abort
		if(userInput == '') return;

		// send user input to the server side
		socketio.emit('input', {data: userInput});

		// clear the field in the form
		const inputField = document.querySelector('#player-input');
		inputField.value = '';
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

		// target and clear the text box
		const textContainer 	= document.querySelector('.text');
		textContainer.innerHTML = '';

		// loop over texts to display them in the text box
		for(const text of texts['texts']) {
			let new_paragraph 		= `<p class="text-snippet"> ${text} </p><br>`;
			textContainer.innerHTML += new_paragraph
		}
	}


	/************* EVENT LISTENERS *************/

	inputForm.addEventListener('submit', sendInput);

	socketio.on('update', (texts) => {
		updateText(texts);
	});
}

init();

