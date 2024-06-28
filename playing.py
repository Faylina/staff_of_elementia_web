import streamlit        as st

placeholderText 		= st.empty()
placeholderInput 		= st.empty()
saved_first_decision 	= None

with placeholderText.container():
	st.write('Hi')
	st.write("\nEnter y.")

with placeholderInput.container():
	first_decision = st.text_input(
			"Make your decision:",
			label_visibility	= "visible",
			disabled			= False,
			placeholder			= 'State it here...',
			key 				= 'first'
		)

if first_decision:
	saved_first_decision = first_decision

	if saved_first_decision:
		with placeholderText.container():
			st.write('Hi')
			st.write("\nEnter y.")
			st.write("  \n You made your first decision.")

		with placeholderInput.container():
			second_decision = st.text_input(
					"Make your decision:",
					label_visibility	= "visible",
					disabled			= False,
					placeholder			= 'State it here...',
					key 				= 'second'
				)

