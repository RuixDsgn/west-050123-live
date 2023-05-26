import React, { useState } from "react"

const Header = ({isDarkMode, setIsDarkMode}) => {

// const [isDarkMode, setIsDarkMode] = useState(true)

const toggleDarkMode = e => {
	// console.log(isDarkMode)
	setIsDarkMode(!isDarkMode)
   // setterFunction((prev State) => {new state})
}

const whichMode = () => {
	if (isDarkMode) {
		return "Dark"
	} else {
		return "Light"
	}
}
	return (
		<header>
			<h1>
				<span className="logo">{"//"}</span>
				Project Showcase
			</h1>
			<button onClick={toggleDarkMode}>{isDarkMode ? "Dark" : "Light"} Mode</button>
		</header>
	)
}

export default Header


/* Creating Light/Dark Mode Using State and Events
	Event
	- Create an event on the targetted button (i.e Button on line 12)
	State
	- Define state variable
	- Define setter function
	- DO NOT modify the state variable directly
	- Use the setter function to set the new value of the state variable
	- React will only see the change in the state variable if the setter function is used
	- Setter functions are asynchrounous 
	- Use useState hook to define the initial state
	   - State Variable
	    - Use a ternary expression on the button with the event (i.e. line 22)
		- Set the state variable to the ternary expression
	   - Setter Function
	    - Use the setter function to create a new state (i.e. line 9)
		- Define the new state as the opposite of the previous state (line 10)
	- Lift state into App by passing the state as a prop by copying and pasting line 5 into line 10 (src/App.js line 14)
	- Set the value of the props in the App, i.e. isDarkMode={isDarkMode} setIsDarkMode={setIsDarkMode}
	- To apply the css class that will actually change the page into light or dark mode, target the area where we need to add the said class
	  - in this case in the App.js in line 13, there is a class called 'App'
	  - Interpolate 'App' with 'Light', which is the css class that turns the page into light mode (i.e. line 13 example)
*/