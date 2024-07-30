'use strict';

const checkLogin = () => {

	const fetchingCookie = async () => {
		try {
			const result 	= await fetch('/getCookieFlask');
			const data 		= await result.text();
			return { status: 'success', data: data }; 
		} catch (error) {
			console.warn(error); 
			return { status: 'Retrieve error', error: error };
		}
	}

	const deletingCookie = async () => {
		try {
			const result = await fetch('/deleteCookieFlask', {
				method: 'delete',
				headers: { "Content-Type": "application/json" }
			});
			return { status: 'success', data: result }; 
		} catch (error) {
			console.warn(error); 
			return { status: 'Retrieve error', error: error };
		}
	}

	const gettingIP = async () => {
		try {
			const result 	= await fetch('/getIPFlask');
			const data 		= await result.text();
			return { status: 'success', data: data }; 
		} catch (error) {
			console.warn(error); 
			return { status: 'Retrieve error', error: error };
		}
	}

	Promise.all([ fetchingCookie(), gettingIP() ])
	.then(([bridgeCookie, IP]) => { 

		if (bridgeCookie.data !== "Cookie not found") {
			
			if(bridgeCookie.data === IP.data) { 
				console.log('User is logged in.'); 
			} else { 
				console.log('User is not logged in.'); 
		
				deletingCookie()
				.then(response => {
					location.href = '../../index.php';
				})
				.catch(console.warn)
			}
		} else {
			location.href = '../../index.php';
		}
	}).catch(error => { console.error('Error fetching data:', error); });
}

checkLogin();