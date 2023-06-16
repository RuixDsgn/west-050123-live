import { useState } from "react"

import Header from "./components/Header"
import ProjectContainer from "./components/ProjectContainer"
import ProjectForm from "./components/ProjectForm"
import ProjectForm1 from "./components/ProjectForm1"

/* 
	Review Questions:
	
	1. Define Lifting State?
	- Move the state to the parent(or higher) component
	- Then pass down the necesary state as props back to the child comp
		- Sometimes, you can package the props, to reduce the amount of props passed

	2. What kind of func is the setState func?
	- asynchronous!
		- state = {name: "louis"}
		- console.log(state)
		- setState({name: "ethan"})
		- console.log(state) // THIS WILL ALWAYS DRAG
			- i.e. output 
				=>  {name: "louis"}
				=>  {name: "louis"}

*/

const App = () => {
	const [projects, setProjects] = useState([])
	const [isDarkMode, setIsDarkMode] = useState(true)

	const dark = isDarkMode ? "App" : "App light"

	return (
		<div className={dark}>
			<Header isDarkMode={isDarkMode} setIsDarkMode={setIsDarkMode} />
			{/* <ProjectForm setProjects={setProjects} /> */}
			<ProjectForm1 setProjects={setProjects} />
			<ProjectContainer projects={projects} setProjects={setProjects} />
		</div>
	)
}

export default App
