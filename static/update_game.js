'use strict';

const updateText = () => {

	const textbox = document.querySelector('.text'); 

	const updateGame = async () => {
		try {
			const result = await fetch('/update_game', {
				method: 'put',
				headers: { "Content-Type": "application/json" }
			});
			const texts = await result.json();
			console.log(texts)
			return { status: 'success', data: texts }; 
		} catch (error) {
			console.warn(error); 
			return { status: 'Retrieve error', error: error };
		}
	}

	updateGame()
}


// ({{ url_for('user_input') | tojson }});


updateText();
