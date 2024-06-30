'use strict';

const process = () => {

	const form = document.querySelector('.input'); 

	const processForm = (event) => {
		event.preventDefault();

		const input = event.target[0].value;
		// console.log(input)
		
		fetch('/user_input', {
			method: 'post', 
			body: input
		}).then(
			resp => resp.json()
		).then(
			data => {
				console.log(data);
			}
		).catch(
			console.warn
		)
		event.target.reset();
	}

	form.addEventListener('submit', processForm); 
}


// ({{ url_for('user_input') | tojson }});


process();

