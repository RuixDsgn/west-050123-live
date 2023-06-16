import { useState, useEffect } from "react"

import Header from "./components/Header"
import ProjectContainer from "./components/ProjectContainer"
import ProjectForm from "./components/ProjectForm"

/* 
	The Component LifeCycle

	- What happens over the course of the component's time on the application

	1. Mounting
		- Everything that happen when the comp in put on the page
		- Common CompMounting functions
			- Fetch all projects and set the state
			- Server Connections

	2. Updating
		- While the comp is mounted (on the page) all the changes that the comp goes through

	3. Unmounting
		- Cleanup
		- What happens when the component leaves the page (un-renders)
		
	ALL CONTAINED IN THE USEEFFECT HOOK

	useEffect(callbackFunc, dependencyArray)


	depArray = Tracks only the changes in the variables (state) listed in the array
	No depArray => Runs callbackFunc on ANY CHANGE IN THE COMPONENT
	depArray with something in it => tracks the listed state(s)
	empty depArray => Only on component mounting!

*/

const App = () => {
	const [projects, setProjects] = useState([])
	const [isDarkMode, setIsDarkMode] = useState(true)

	useEffect(() => {
		console.log("EVERYCHANGE OF STATE ON APP")
	})
	// * COMPONENT DID MOUNT
	useEffect(() => {
		console.log("LOAD PROJECTS")
		fetchAllProjects()

		return () => {
			console.log("cleanup")
			setProjects([])
		}
	}, [])

	const fetchAllProjects = () => {
		fetch("http://localhost:4000/projects")
			.then((res) => res.json())
			.then((projects) => setProjects(projects))
	}

	const dark = isDarkMode ? "App" : "App light"

	return (
		<div className={dark}>
			<Header isDarkMode={isDarkMode} setIsDarkMode={setIsDarkMode} />
			<ProjectForm setProjects={setProjects} />
			<ProjectContainer projects={projects} />
		</div>
	)
}

export default App
